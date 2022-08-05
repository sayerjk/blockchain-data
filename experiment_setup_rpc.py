from near_api.providers import JsonProvider

near_provider = JsonProvider("https://rpc.testnet.near.org")
print(near_provider.json_rpc("tx", [
    "BkPbqf4jR9BYpSYAy47ZsYPNA9vjc6CmHJLqRKz4zHac",
    "priceoracle.nhtera.testnet"]))
