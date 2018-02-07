# Heavily inspired by https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b
# Credit to Gerald Nash

import hashlib as hasher
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()


def create_genesis_block():
    return Block(0, date.datetime.now(), "This is an excursion into the unknown", "0")


def mine_block(prev_block, data):
    block = Block(prev_block.index + 1, date.datetime.now(), data, prev_block.hash_block())
    return block



def mine_blocks():
    data = ["this", "blockchain", "is", "not", "the", "greatest", "blockchain", "merely", "a", "tribute"]
    increment = 0
    global current_block
    while True:
        print(current_block.timestamp, current_block.data)
        current_block = mine_block(current_block, data[increment % len(data)])
        blockchain.append(current_block)
        increment += 1


current_block = create_genesis_block()
blockchain = [current_block]

print(current_block)

mine_blocks()

