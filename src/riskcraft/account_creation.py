"""Ocean module for RiskCraft.

   creates a new account and writes the private key to .env.json
   """

import json
from eth_account.account import Account


# TODO: remove this test function
def foo(x: int, y: int) -> int:
    """Add two numbers together."""
    return x + y


# main
def main():
    """Main function."""
    print(foo(1, 2))

    env = json.load(open(".env.json"))

    print(env.get("INFURA_NODE_ENDPOINT"))

    account1 = Account.create()
    account2 = Account.create()

    print(
        f"""
    REMOTE_TEST_PRIVATE_KEY1={account1.key.hex()}, ADDRESS1={account1.address}
    REMOTE_TEST_PRIVATE_KEY2={account2.key.hex()}, ADDRESS2={account2.address}
    """
    )

    # write to .env.json as REMOTE_TEST_PRIVATE_KEY1 and 2
    env["REMOTE_TEST_PRIVATE_KEY1"] = account1.key.hex()
    env["REMOTE_TEST_PRIVATE_KEY2"] = account2.key.hex()
    env["ADDRESS1"] = account1.address
    env["ADDRESS2"] = account2.address

    with open(".env.json", "w") as f:
        json.dump(env, f, indent=4)


if __name__ == "__main__":
    main()
