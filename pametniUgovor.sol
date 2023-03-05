// SPDX-License-Identifier: MIT

pragma solidity ^0.8.17;

contract SimpleToken {
    
    // Token details
    string public name;
    string public symbol;
    uint256 public totalSupply;
    
    // Mapping from address to token balance
    mapping(address => uint256) public balances;
    
    // Event emitted when tokens are transferred
    event Transfer(address indexed _from, address indexed _to, uint256 _value);
    
    // Contract owner
    address public owner;
    
    // Modifier that only allows the owner to call a function
    modifier onlyOwner {
        require(msg.sender == owner, "Only contract owner can call this function.");
        _;
    }
    
    // Constructor function that initializes the token details and sets the contract owner
    constructor(string memory _name, string memory _symbol, uint256 _totalSupply) {
        name = _name;
        symbol = _symbol;
        totalSupply = _totalSupply;
        owner = msg.sender;
        balances[owner] = _totalSupply;
    }
    
    // Function to transfer tokens from one address to another
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(balances[msg.sender] >= _value, "Insufficient balance.");
        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }
    
    // Function to check the balance of tokens for a given address
    function balanceOf(address _address) public view returns (uint256) {
        return balances[_address];
    }
    
    // Function to increase the total supply of tokens
    function mint(uint256 _value) public onlyOwner {
        totalSupply += _value;
        balances[owner] += _value;
    }
    
    // Function to decrease the total supply of tokens
    function burn(uint256 _value) public onlyOwner {
        require(balances[owner] >= _value, "Insufficient balance.");
        totalSupply -= _value;
        balances[owner] -= _value;
    }
}
