from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

class SenderKeyRecord:
    def __init__(self, sender_key_id: int, sender_chain_key: bytes, sender_signing_pub: bytes, message_index: int):
        self.sender_key_id = sender_key_id
        self.sender_chain_key = sender_chain_key
        self.sender_signing_pub = sender_signing_pub  # raw bytes representation
        self.message_index = message_index

    def public_key(self):
        return Ed25519PublicKey.from_public_bytes(self.sender_signing_pub)
