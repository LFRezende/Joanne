# Joanne
A simple smart contract deployment whose structure follows the ERC-20 standard for Fungible Tokens in the Ethereum blockchains.
Joanne, in honor of Joana, is a simple ERC-20 Token deployed in Python using Brownie.

---

- Features and Acknowledgements:

1. The Smart Contract "Joanne.sol" is virtually identical to the avaiable contract of Open Zeppelin, with mild changes, inheriting the ERC20.sol contract.
2. The deployment contract is simple, focusing solely on deploying Joanne into a real blockchain (or at least into a testnet, such as goerli), so coding for local-chain deployment was not a concern.
3. The brownie-config file maps the Open Zeppelin repository in version 4.8.0, as well as the private key for the deployment account via .env (not pushed to github, for trivial reasons).

  > The total supply estipulated was of one million Joanne (JOE).
