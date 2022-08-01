from near_functions import query_near_testnet

query = """SELECT emitted_for_receipt_id, emitted_at_block_timestamp, 
        emitted_in_shard_id, emitted_index_of_event_entry_in_shard,
        emitted_index_of_event_entry_in_shard, emitted_by_contract_account_id,
        token_id, event_kind, token_old_owner_account_id, token_new_owner_account_id,
        token_authorized_account_id, event_memo
        FROM assets__non_fungible_token_events
        LIMIT 1000;"""

results = query_near_testnet(query)
print(results)
