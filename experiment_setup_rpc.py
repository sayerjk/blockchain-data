from near_api.providers import JsonProvider

near = JsonProvider("https://rpc.mainnet.near.org")

print(
    f"{'**' * 40}\n",
    f"{near.rpc_addr() = }\n",
    f"{near.json_rpc('status', params=[]) = }\n",
    f"{near.get_status() = }\n",
    f"{near.get_validators() = }\n",
    # f"{near.query('masternode24.poolv1.near') = }",
    f"{near.get_account(account_id='masternode24.poolv1.near') = }\n",
    # `epoch_id` returns from `get_block()`
    f"{near.get_block(block_id='6jJbQ8A99gAotHKnVbv9D7P5oVzwSzj8xuFFxgD5CLL4') = }\n",
    f"{near.get_changes_in_block(block_id='6jJbQ8A99gAotHKnVbv9D7P5oVzwSzj8xuFFxgD5CLL4') = }\n",
    # "stake" field in `get_validators_ordered()`
    f"{near.get_validators_ordered('6jJbQ8A99gAotHKnVbv9D7P5oVzwSzj8xuFFxgD5CLL4') = }\n",
    # f"{near.get_light_client_proof('3x1rcwf9mwepSEHBkCjexHNPzEXvNBF1HEdGCDS1PuG2')}",
    f"{near.get_receipt('HBu8sZuVjMiwNjx9WdjztECMAbije2CUEetNvjA3PqfS') = }\n"
)


"""Reference this link for functions: https://github.com/near/near-api-py/blob/master/near_api/providers.py
    I had to copy/paste the github url code into my local installation of this near-rpc-py library, 
    because the pip install version does not have the most current code in it. """

"""Grab test data from https://explorer.near.org/blocks"""
