import base64
import json

def create_distribution_message(bundle):
    return json.dumps({
        "sender_key_id": bundle.sender_key_id,
        "sender_chain_key": base64.b64encode(bundle.sender_chain_key).decode(),
        "sender_signing_pub": base64.b64encode(bundle.signing_key.verify_key.encode()).decode()
    })

def parse_distribution_message(data):
    obj = json.loads(data)
    return {
        "sender_key_id": obj["sender_key_id"],
        "sender_chain_key": base64.b64decode(obj["sender_chain_key"]),
        "sender_signing_pub": base64.b64decode(obj["sender_signing_pub"])
    }
