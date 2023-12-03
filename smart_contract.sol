// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract ForestSmartContract {
    // State variables
    address public elder;
    mapping(address => uint256) public balances;
// Events
    event Sent(address from, address to, uint256 amount);

    // Modifiers
    modifier onlyElder() {
        require(msg.sender == elder, "Only the Elder can invoke this");
        _;
    }
