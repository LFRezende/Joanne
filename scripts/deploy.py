from brownie import Joanne, network
from scripts.utils import get_account

LOCAL_CHAINS = ['development', 'ganache-local', 'ganache-local2', 'ganache-local3']
SUPPLY = 1*10**24

def fly():
    # Our only desire is testing this on a real blockchain (testnet)
    account = get_account()
    if network.show_active() in LOCAL_CHAINS:
        return 0
    joanne = Joanne.deploy(SUPPLY, {"from": account})
    return joanne

def main():
    fly()