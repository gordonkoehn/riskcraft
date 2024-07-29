"""Ocean module for RiskCraft."""

import json

env = json.load(open(".env.json"))


# TODO: remove this test function
def foo(x: int, y: int) -> int:
    """Add two numbers together."""
    return x + y


# main
def main():
    """Main function."""
    print(foo(1, 2))

    print(env.get("INFURA_NODE_ENDPOINT"))


if __name__ == "__main__":
    main()
