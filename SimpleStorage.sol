// SimpleStorage.sol
// This is a simple smart contract that allows storing and retrieving a single piece of data.

pragma solidity ^0.8.0;

contract SimpleStorage {
    // State variable to store the data
    uint256 public data;

    // Function to set the data
    function setData(uint256 _data) public {
        data = _data;
    }

    // Function to get the stored data
    function getData() public view returns (uint256) {
        return data;
    }
}
