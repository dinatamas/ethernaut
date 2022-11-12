3. Coin Flip - Attempt #1
-------------------------
* `sudo pacman -Sy nodejs npm`
* `mkdir coin_flip && cd coin_flip`
* `npm install truffle`
* `./node_modules/.bin/truffle init`
* Use the contract to simulate the flips.
* [OpenZeppelin repo](https://github.com/OpenZeppelin/openzeppelin-contracts/)
  * `/blob/v3.4.0/contracts/math/SafeMath.sol`
  * Import from path `./SafeMath.sol`
* Change compiler version in `truffle-config.js`
* `./node_modules/.bin/truffle compile`
* Register an account on [Infura](https://infura.io).
* Create a new Rinkeby project (`ethernaut_coin_flip`).
* `npm install truffle-hdwallet-provider`
* Add the Infura project URL to `truffle-config.js`.
* Add the MetaMask mnemonic to `truffle-config.js`.
* Deploy using `migrations/2_deploy_contracts.js`
* `./node_modules/.bin/truffle migrate --network rinkeby`
* Had to run multiple times, it failed all the time due to network errors...
  * Adding `skipDryRun: true` could help a little.
* Get the contract address from the deployment messages.
  * Check it on `etherscan.io` (select the Rinkeby network)
  * Visit the contract address > Contract > Decompile ByteCode
  * How to decompile offline? (Panoramix decompiler)
* To update: rebuild or remove the `build/` dir and migrate again.
  * The contract will be deployed to a new address.
  * On Etherscan: Verify & Publish the contract! (Multifile)
    * This will generate the ABI for the contract!
    * How else can we retrieve this?
    * For example with the [solc](https://ethereum.stackexchange.com/a/47413)
* `virtualenv venv`
* `source venv/bin/activate.fish`
* `pip install web3`
* `./solve.py`
