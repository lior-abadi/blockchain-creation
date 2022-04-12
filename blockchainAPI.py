from flask import Flask, jsonify
from flask_ngrok import run_with_ngrok
from blockchain import Blockchain

app = Flask(__name__)
# run_with_ngrok(app)

app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

blockchain = Blockchain()

@app.route("/mine_block", methods=["GET"])
def mine_block():
    
    previous_block = blockchain.get_previous_block()    
    previous_proof = previous_block["proof"]
    
    
    
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.blockHash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    
    response = {
        
        "message"               : "Successfully mined a new block.",
        "index"                 : block["index"],
        "timestamp"             : block["timestamp"],
        "proof"                 : block["proof"],
        "previous_hash"         : block["previous_hash"] 
        
    }
    
    return jsonify(response), 200    
    
    
@app.route("/get_chain", methods=["GET"])
def get_chain():
    response = {
        "chain"     : blockchain.chain,
        "length"    : len(blockchain.chain)   
    }    
    return jsonify(response), 200

    
@app.route("/is_valid", methods=["GET"])
def is_valid():
    is_valid = blockchain.isChainValid(blockchain.chain)
    
    if is_valid:
        response = {"message"   :  "The blockchain is valid."}
    else:
        response = {"message" : "The blockchain is not valid."}
    
    return jsonify(response), 200


app.run(host = "localhost", port = 3001) # (need to coment flask_ngrok also)
# app.run()