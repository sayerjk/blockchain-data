from near_functions import query_near_testnet, create_dictionary
import datetime


keys = ['emitted_for_receipt_id', 'emitted_at_block_timestamp',
        'emitted_in_shard_id', 'emitted_index_of_event_entry_in_shard',
        'emitted_index_of_event_entry_in_shard', 'emitted_by_contract_account_id',
        'token_id', 'event_kind', 'token_old_owner_account_id', 'token_new_owner_account_id',
        'token_authorized_account_id', 'event_memo']

query = """SELECT emitted_for_receipt_id, emitted_at_block_timestamp, 
        emitted_in_shard_id, emitted_index_of_event_entry_in_shard,
        emitted_index_of_event_entry_in_shard, emitted_by_contract_account_id,
        token_id, event_kind, token_old_owner_account_id, token_new_owner_account_id,
        token_authorized_account_id, event_memo
        FROM assets__non_fungible_token_events
        LIMIT 1000;"""

result = query_near_testnet(query)
all_results = []

for item in result:
    record = create_dictionary(keys, list(item))
    all_results.append(record)

for item in all_results:
    if 'emitted_at_block_timestamp' in item.keys():
        # converting epoch time to datetime string
        x = str(item['emitted_at_block_timestamp'])
        mod_string = x[:10]
        datetime_string = datetime.datetime.fromtimestamp(int(mod_string)).strftime('%Y-%m-%d %H:%M:%S')
        item['emitted_at_block_timestamp'] = datetime_string

print(all_results)
