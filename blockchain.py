# Required libraries and modules
import datetime
import hashlib
import json
import flask
import flask_ngrok


# Creation of Blockchain class. It should allow:
#   Create new blocks and generate their hashes
#   Validating protocol based on a PoW algorithm
#   Verify & validate the chain

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = "0")   # Genesis Block
    
    def create_block(self, proof, previous_hash):
        block = {
            "index"         : len(self.chain) + 1,              # current block number
            "timestamp"     : str(datetime.datetime.now()),     # creation timestamp
            "proof"         : proof,                            # current block nounce
            "previous_hash" : previous_hash                     # previous block hash to link
        }   
        self.chain.append(block)
        return block
    
    def get_previous_block(self, previous_proof):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof = 1   # nounce
        check_proof = False
        
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest() # Hash generated from a non symetric operation
            if hash_operation[:4] == "0000": # First 4 positions of the hash must be zero. If more zeros are required, the difficulty increases.
                check_proof = True
            else:
                new_proof += 1
                
        return new_proof
    