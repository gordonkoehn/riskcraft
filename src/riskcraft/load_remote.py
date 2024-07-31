"""Testing RPC calls to a testnet, to setup the remote environment."""

# Create Ocean instance
import json
from ocean_lib.example_config import get_config_dict
from ocean_lib.ocean.ocean import Ocean
from eth_account import Account
from web3 import Web3
from ocean_lib.web3_internal.http_provider import get_web3_connection_provider

# Load environment variables
env = json.load(open(".env.json"))

# Create Ocean instance
rpc = env.get("PUBLIC_NODE_POLYGON_MUMBAI")
print(f"Connecting to {rpc}")

provider = get_web3_connection_provider(rpc)
web3 = Web3(provider)
# get chain ID from the RPC
chain_id = web3.eth.chain_id
print(f"Chain ID: {chain_id}")

config = get_config_dict(rpc)  # you can also input the string directly
ocean = Ocean(config)

# Create OCEAN object. ocean_lib knows where OCEAN is on all remote networks
OCEAN = ocean.OCEAN_token

# Create Alice's wallet

alice_private_key = env.get("REMOTE_TEST_PRIVATE_KEY1")
alice = Account.from_key(private_key=alice_private_key)

try:
    assert ocean.wallet_balance(alice) > 0, "Alice needs MATIC"
    assert OCEAN.balanceOf(alice) > 0, "Alice needs OCEAN"  # type: ignore
except AssertionError as e:
    print(str(e))
    # Handle the exception here

# Create Bob's wallet. While some flows just use Alice wallet,
#  it's simpler to do all here.
bob_private_key = env.get("REMOTE_TEST_PRIVATE_KEY1")
bob = Account.from_key(private_key=bob_private_key)
try:
    assert ocean.wallet_balance(bob) > 0, "Bob needs MATIC"
    assert OCEAN.balanceOf(bob) > 0, "Bob needs OCEAN"  # type: ignore
except AssertionError as e:
    print(str(e))
    # Handle the exception here

# Compact wei <> eth conversion
