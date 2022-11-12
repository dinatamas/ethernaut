4 - Telephone
=============

New Stuff
---------
* `msg.sender`, `tx.origin`

Idea: If `tx.origin` is not the same as `msg.sender`, then we can change the owner.
* We must create a transaction that calls this function.
* [1](https://ethereum.stackexchange.com/a/1892)
* [2](https://swcregistry.io/docs/SWC-115)
  * The SWC (Smart Contract Weakness Classification) is very useful!
Exploit: deploy intermediate contract.

```bash
virtualenv venv
source venv/bin/activate.fish
sudo pacman -Sy solidity # solc compiler
pip install web3 py-solc-x
```
Note: I actually should use a venv/ at the root.

SafeMath (older version) also had to be placed here.

Install MetaMask Firefox.
* Export the private key for the Rinkeby testnet.
Use infura.io as web3 endpoint.
* Create `ethernaut_04_telephone` project.
* Copy Infura project ID.
Connect Ethernaut to MetaMask.
* Copy player address.

More reading:
[3](
    https://blog.ethereum.org/2016/06/24/security-alert-smart-contract
    -wallets-created-in-frontier-are-vulnerable-to-phishing-attacks/
)

Solution Explanation
--------------------

Confusing `tx.origin` with `msg.sender` can lead to phishing-style attacks:

1. Use tx.origin to determine whose tokens to transfer, e.g.
```
function transfer(address _to, uint _value) {
  tokens[tx.origin] -= _value;
  tokens[_to] += _value;
}
```
2. Attacker gets victim to send funds to a malicious contract that calls the
   transfer function of the token contract, e.g.
```
function () payable {
  token.transfer(attackerAddress, 10000);
}
```
3. In this scenario, tx.origin will be the victim's address (while msg.sender
   will be the malicious contract's address), resulting in the funds being
   transferred from the victim to the attacker.
