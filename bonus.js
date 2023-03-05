// Import the web3 library
import Web3 from 'web3';

// Connect to the Ethereum network
const web3 = new Web3('http://localhost:8545');

// Set the address of the deployed contract
const contractAddress = '0x3a15E757b305981111673fF06A410B04Ae7216A4';

// Set the ABI of the contract
const contractABI = [
  {
    "inputs": [
      {
        "internalType": "string",
        "name": "_name",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "_symbol",
        "type": "string"
      },
      {
        "internalType": "uint256",
        "name": "_totalSupply",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_to",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "transfer",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "balances",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];

// Create an instance of the contract object
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Call the 'balanceOf' function to get the balance of an address
contract.methods.balanceOf('0xabc...').call((error, balance) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`Balance: ${balance}`);
  }
});

// Send a transaction to transfer tokens from one address to another
const fromAddress = '0x3a15E757b305981111673fF06A410B04Ae7216A4';
const toAddress = '0x2b946920f55BB0506ab64272f0260562d8777151';
const value = 50;
contract.methods.transfer(toAddress, value).send({ from: fromAddress }, (error, transactionHash) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`Transaction hash: ${transactionHash}`);
  }
});
