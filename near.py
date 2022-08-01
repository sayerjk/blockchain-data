import psycopg2
from enc import DecimalEncoder
import json
import datetime
from datetime import date


def create_dictionary(labels, vals):
    results = {}
    for key, value in zip(labels, vals):
        results[key] = value
    return results


def query_near(sql_query: str) -> dict:
    """Query NEAR blockchain based on sql_query() string input"""
    # test NEAR Indexer database info
    conn = psycopg2.connect(host="35.184.214.98",
                            database="testnet_explorer",
                            user="public_readonly",
                            password="nearprotocol")
    cur = conn.cursor()
    cur.execute(sql_query)
    return cur.fetchall()


# below only for testing the above function. Sample sql query
query = """select *
            FROM assets__non_fungible_token_events
            LIMIT 500;"""

result = query_near(query)
# print(result[0])
# for i in result:
#     print(i[0])

keys = ['emitted_for_receipt_id', 'emitted_at_block_timestamp',
        'emitted_in_shard_id', 'emitted_index_of_event_entry_in_shard',
        'emitted_index_of_event_entry_in_shard', 'emitted_by_contract_account_id',
        'token_id', 'event_kind', 'token_old_owner_account_id', 'token_new_owner_account_id',
        'token_authorized_account_id', 'event_memo']

all_results = []

for item in result:
    rec = create_dictionary(keys, list(item))
    all_results.append(rec)

for item in all_results:
    if 'emitted_at_block_timestamp' in item.keys():
        x = str(item['emitted_at_block_timestamp'])
        item['emitted_at_block_timestamp'] = date.fromtimestamp(int(x) // 1000000000)
        item['emitted_at_block_timestamp'] = item['emitted_at_block_timestamp'].strftime('%Y-%m-%d %H:%M:%S')

now = datetime.datetime.now()
timestamp = datetime.datetime.timestamp(now)
with open(f'data/NEAR_{timestamp}.json', 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=4, cls=DecimalEncoder)

print(all_results)
