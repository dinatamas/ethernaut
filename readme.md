Ethernaut
=========

https://ethernaut.openzeppelin.com/

* Inspect everything: [Etherscan](https://etherscan.io/)
* I would love to replace MetaMask, but not sure how...
  * Create new wallet.
  * Use Rinkeby test network.
  * Connect the Ethernaut site.
  * `web3js` could be substituted with `web3py`.
    * MetaMask can be replaced with manual signing.
* Get test ether: [Rinkeby faucet](https://faucets.chain.link/rinkeby)
* [Remix Solidity IDE](remix.ethereum.org)
  * Include OpenZeppelin's own Solidity files.
* [Solidity Course](https://www.youtube.com/watch?v=M576WGiDBdQ)
  * [Source](https://github.com/smartcontractkit/full-blockchain-solidity-course-py)
  * [Solidity AST explorer](https://github.com/iamdefinitelyahuman/py-solc-ast)
* [OpenZeppelin tutorial](https://docs.openzeppelin.com/learn/developing-smart-contracts)

Console commands:
* `help()`
  * Get function signature: `sendTransaction.toString()`
* `player`
* `await getBalance(player)`
* `ethernaut`
  * `await ethernaut.owner`
  * Ethernaut.sol contract
* `contract`
  * `instance` is `contract.address`
* `toWei()`, `fromWei()`

Things I learned:
* ABI: Contract Application Binary Interface
  * [ABI Spec](https://docs.soliditylang.org/en/develop/abi-spec.html)
  * [Web3JS](https://web3js.readthedocs.io/en/v1.7.0/)
* [Truffle Contact](https://www.npmjs.com/package/@truffle/contract)
  * [Truffle Suite](https://trufflesuite.com/docs/truffle/)
  * [Truffle Tool](https://github.com/trufflesuite/truffle)

Solidity language:
* `pragma solidity ^0.6.0;`
* `contract <name> {}`
* Types: `bool`, `string`, `uint8`, `address`
  * `memory` modifier
  * `payable` modifier
  * `external` modifier
  * `mapping(address => uint)`
* Math:
  * `.add()`
* Access modifiers: `public`, `private`
  * `<type> <modifiers> public <name>`
  * `view` modifier
* Methods: `constructor`, `function`
  * `msg`: `msg.sender`, `msg.value`
  * `constructor` vs `function <contract name>`
* `modifier <name> {}`
  * `require(<predicate>, <error message>);`
  * `_;`: When the modified function is executed in a modifier.
* `receive() external payable {}`
* Builtin functions:
  * `keccak256`
  * `abi.encodePacked`
  * `address`, `address(this).balance`
  * `transfer`
  * `require`
  * `revert`
  * `blockhash`
  * `block.number`
* Currency: `0.001 ether`
* `import '@openzeppelin/.../SafeMath.sol';`
  * `using SafeMath for uin256;`
  * [Solidity import](https://remix-ide.readthedocs.io/en/latest/import.html)
* Functions that modify the contract state (and thus the blockchain)
 have to be called via transactions. External addresses (like Web3
 clients) cannot see their return values.
  * To get the value: check attributes / `view` functions / events.
  * This or other contracts can get the return value.

The following can be used instead of `await`:
```
function printCallback(error, result) {
  if(!error) { console.log(result); }
  else { console.log(error); }}
```
