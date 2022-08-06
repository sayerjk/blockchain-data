from near_api.providers import JsonProvider

near_provider = JsonProvider("https://rpc.testnet.near.org")
print(near_provider.json_rpc("query", {"request_type": "view_state",
                                       "finality": "final",
                                       "account_id": "node1",
                                       "prefix_base64": ""}))

print("Block Query: ")

block = near_provider.get_block(
    "HYJXpq9SmHg4SskZaXdNQkzjnYpD9wmrmNX2ZH87ZFJk"
)
print(block)

s = 'HszoeEzYx8R5WaFcfSFVeK353TNtrWNibvJ2sMaiytC'

vals = near_provider.get_validators()
print(vals)