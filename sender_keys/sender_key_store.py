import json
import base64

class SenderKeyRecord:
    def __init__(self, sender_key_id, sender_chain_key, sender_signing_pub, message_index=0):
        self.sender_key_id = sender_key_id
        self.sender_chain_key = sender_chain_key
        self.sender_signing_pub = sender_signing_pub
        self.message_index = message_index

    def to_json(self):
        return json.dumps({
            "sender_key_id": self.sender_key_id,
            "sender_chain_key": base64.b64encode(self.sender_chain_key).decode(),
            "sender_signing_pub": base64.b64encode(self.sender_signing_pub).decode(),
            "message_index": self.message_index
        })

    @staticmethod
    def from_json(data):
        obj = json.loads(data)
        return SenderKeyRecord(
            obj["sender_key_id"],
            base64.b64decode(obj["sender_chain_key"]),
            base64.b64decode(obj["sender_signing_pub"]),
            obj["message_index"]
        )

