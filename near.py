from near_functions import query_near_testnet

query = """SELECT emitted_by_contract_account_id, token_id
        FROM assets__non_fungible_token_events
        LIMIT 1;"""

results = query_near_testnet(query)
print(results)
