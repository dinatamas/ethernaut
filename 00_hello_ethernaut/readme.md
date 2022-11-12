0. Hello Ethernaut
------------------
* `await contract.info()`
* `await contract.info1()`
* `await contract.info2('hello')`
* `infoNum` is not a property, it is a function.
* `await contract.info42()`
* `await contract.theMethodName()`
* `await contract.method7123949()`
* To get the password: `await contract.password()`
* `await contract.authenticate('ethernaut0')`
  * The solution was to set the `cleared` attributed to true.
  * This is what the `authenticate` method has done.
