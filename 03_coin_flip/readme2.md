3. Coin Flip - Attempt #2
-------------------------
* [Solution](https://www.youtube.com/watch?v=VJZuLb1r1nQ)
  * I will be following this, but with an Infura + Web3.py based solution.
* Plain Web3.py script: compile, deploy and interact with the contract!
* Copy-paste the origin CoinFlip contract to deploy my own version.
* Include SafeMath as a local file.
  * Find the last `0.6.0` version from OpenZeppelin.
* `virtualenv venv`
* `source venv/bin/activate.fish`
* `pip install py-solc-x web3`
* To avoid `which: no solc in (<path>)` warning: `pacman -Sy solidity`
  * The compilation worked without this though...
* Concept: We'll calculate the same value (based on block data) before
  passing it to the victim contract. Since the contract calls will be
  included in the same block, it will receive the same result.
  * Using blocks is not a safe source of randomness!
  * Alternatively, a clone contract could be deployed and queried. If
   the victim tries to involve any non-oracle randomness, the clone
   could be extended with any required view functions.
  * Even "private" variables are visible in the blockchain, because the
   blockchain is storing the contract's state.
  * Miners also have control over things like blockhashes, timestamps,
   and whether to include certain transactions - which allows them to
   bias these values in their favor.
* Solution: `./solve.py`
  * Input the level instance's address.
  * No need to get a new instance if the contract reverts.
