from solcx import compile_standard, install_solc
import json
from web3 import Web3

# Connect to ganache
w3 = Web3(Web3.HTTPProvider("http://0.0.0.0:8545"))
chain_id = 1337
my_address = "0x3a15E757b305981111673fF06A410B04Ae7216A4"
private_key = "0xc4a748b56159fc035f43951eedab4119988446f368084891892ec13cb3e0da36"

# Read the contents of the SimpleToken.sol contract file
with open("./SimpleToken.sol", "r") as file:
    simple_token_file = file.read()

# Compile the Solidity contract using the solcx package
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleToken.sol": {"content": simple_token_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode"]}
            }
        },
    },
    solc_version="0.8.17",
)

# Extract the bytecode and ABI from the compiled contract
# bytecode
bytecode = compiled_sol["contracts"]["SimpleToken.sol"]["SimpleToken"]["evm"]["bytecode"]["object"]

# abi
abi = compiled_sol["contracts"]["SimpleToken.sol"]["SimpleToken"]["abi"]

# Create the contract in python
SimpleToken = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get the nonce
nonce = w3.eth.getTransactionCount(my_address)

# Build a transaction to deploy the contract
transaction = SimpleToken.constructor("Simple Token", "SIM", 1000000).buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce}
)

# Sign the transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# Send the signed transaction to deploy the contract
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Wait for the transaction to be mined and get the contract address
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract_address = tx_receipt.contractAddress

# Create an instance of the contract using the contract address
simple_token = w3.eth.contract(address=contract_address, abi=abi)

# Get the balance of the contract owner
owner_balance = simple_token.functions.balanceOf(my_address).call()
print(f"Owner balance: {owner_balance}")

# Transfer tokens to another address
recipient_address = "0xE409c9bBaa6b8CB6e0a0dEa223D11aeFF5c5B5B5"
transfer_value = 100
transfer_transaction = simple_token.functions.transfer(recipient_address, transfer_value).buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce + 1}
)
signed_transfer_txn = w3.eth.account.sign_transaction(transfer_transaction, private_key=private_key)
send_transfer_tx = w3.eth.send_raw_transaction(signed_transfer_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_transfer_tx)

# Get the updated balance of the contract owner and recipient
owner_balance = simple_token.functions.balanceOf(my_address).call()
recipient_balance = simple_token.functions.balanceOf(recipient_address).call()
print(f"Owner balance: {owner_balance}")
print(f"Recipient balance: {recipient_balance}")
