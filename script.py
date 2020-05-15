# Import web3
from web3 import Web3
infura_url = 'https://mainnet.infura.io/v3/cf6f6ce7ea254774bf0ddf9183bdc6b1'

# Instantiate web3 connection
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())

# Get the latest block on etherium
block = web3.eth.blockNumber
print(block)

# Get the account balance
balance = web3.eth.getBalance('0x39C7BC5496f4eaaa1fF75d88E079C22f0519E7b9')
print(balance)

# Convert Wei currency to Ether
wei_to_ether = web3.fromWei(balance, 'ether')
print(wei_to_ether)
