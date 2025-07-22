import os
import struct
from nacl.signing import SigningKey

class SenderKeyBundle:
    def __init__(self):
        self.sender_key_id = struct.unpack("I", os.urandom(4))[0]  # 32bit ID
        self.sender_chain_key = os.urandom(32)  # Chain key (random)
        self.signing_key = SigningKey.generate()
        self.message_index = 0

    def get_public_bundle(self):
        return {
            "sender_key_id": self.sender_key_id,
            "sender_chain_key": self.sender_chain_key,
            "sender_signing_pub": self.signing_key.verify_key.encode()
        }

    def sign(self, message: bytes) -> bytes:
        return self.signing_key.sign(message).signature

