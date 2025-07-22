from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
import os
import struct

class SenderKeyBundle:
    def __init__(self, sender_key_id: int, sender_chain_key: bytes, sender_signing_key: Ed25519PrivateKey, message_index: int = 0):
        self.sender_key_id = sender_key_id
        self.sender_chain_key = sender_chain_key
        self.sender_signing_key = sender_signing_key
        self.message_index = message_index

    @classmethod
    def generate(cls):
        sender_key_id = int.from_bytes(os.urandom(4), 'big')
        sender_chain_key = os.urandom(32)
        sender_signing_key = Ed25519PrivateKey.generate()
        return cls(sender_key_id, sender_chain_key, sender_signing_key)

    def get_public_bundle(self):
        return {
            "sender_key_id": self.sender_key_id,
            "sender_chain_key": self.sender_chain_key,
            "sender_signing_pub": self.sender_signing_key.public_key().public_bytes(
                encoding = serialization.Encoding.Raw,
                format = serialization.PublicFormat.Raw
            ),
        }
