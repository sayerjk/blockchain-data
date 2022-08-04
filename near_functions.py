import json
from decimal import Decimal
import datetime
import psycopg2

KEYS = ['emitted_for_receipt_id', 'emitted_at_block_timestamp',
        'emitted_in_shard_id', 'emitted_index_of_event_entry_in_shard',
        'emitted_index_of_event_entry_in_shard', 'emitted_by_contract_account_id',
        'token_id', 'event_kind', 'token_old_owner_account_id', 'token_new_owner_account_id',
        'token_authorized_account_id', 'event_memo']

NEW_KEYS = ['emitted_by_contract_account_id', 'token_id']


class DecimalEncoder(json.JSONEncoder):
    """Converts Decimal() objects to string, allowing JSON storage"""
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def create_dictionary(labels, vals):
    results = {}
    for key, value in zip(labels, vals):
        results[key] = value
    return results


def query_near_testnet(sql_query: str) -> list[dict]:
    """Query NEAR blockchain based on sql_query() string input"""
    # test NEAR Indexer database info
    conn = psycopg2.connect(host="35.184.214.98",
                            database="testnet_explorer",
                            user="public_readonly",
                            password="nearprotocol")
    cur = conn.cursor()
    cur.execute(sql_query)
    result_tuples = cur.fetchall()
    all_results = []

    for item in result_tuples:
        record = create_dictionary(NEW_KEYS, list(item))
        all_results.append(record)

    for item in all_results:
        if 'emitted_at_block_timestamp' in item.keys() and 'emitted_at_block_timestamp' in sql_query:
            # converting epoch time to datetime string
            x = str(item['emitted_at_block_timestamp'])
            mod_string = x[:10]
            datetime_string = datetime.datetime.fromtimestamp(int(mod_string)).strftime('%Y-%m-%d %H:%M:%S')
            item['emitted_at_block_timestamp'] = datetime_string

    return all_results


def export_json(data: list[dict]):
    now = datetime.datetime.now()
    timestamp = datetime.datetime.timestamp(now)
    with open(f'data/NEAR_{timestamp}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4, cls=DecimalEncoder)


def bulk_query(r):
    """Grabs output from NEAR CLI filters for media links"""
    compiled_search_queries = []
    bulk_results = []
    for i in r:
        contract = i['emitted_by_contract_account_id']
        token = i['token_id']
        contract = r'\"{}"'.format(contract)
        token = """{{\"token_id\":\"{}\"}}""".format(token)
        #         print(contract, token)
        x = subprocess.run(
            ["near", "view", contract[1:], "nft_token", token],
            capture_output=True, text=True
        ).stdout.strip('\n').lstrip("View call: ")

        new = x.split("\n")
        new = [i.strip() for i in new]

        found_media = ''
        for item in new:
            if 'View call' in item:
                new.remove(item)
                continue
            if 'media:' in item:
                found_media = item
            if len(item) < 5:
                new.remove(item)

        #         print(new)
        #         print(found_media)

        if len(found_media) > 1 and "null" not in found_media:
            found_media = found_media.lstrip("media: '")
            found_media = found_media.rstrip("',")
            #             print()
            print(found_media)
            bulk_results.append(found_media)

    return bulk_results



