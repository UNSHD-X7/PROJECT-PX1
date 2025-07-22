from sender_key_encryptor import SenderKeyEncryptor

class GroupMessenger:
    def __init__(self, bundle):
        self.bundle = bundle

    def encrypt_group_message(self, plaintext: bytes) -> dict:
        message_key, next_chain_key = SenderKeyEncryptor.derive_message_key(self.bundle.sender_chain_key)
        self.bundle.sender_chain_key = next_chain_key
        self.bundle.message_index += 1

        ciphertext = SenderKeyEncryptor.encrypt(message_key, plaintext)
        signature = self.bundle.sign(ciphertext)

        return {
            "sender_key_id": self.bundle.sender_key_id,
            "message_index": self.bundle.message_index,
            "ciphertext": ciphertext,
            "signature": signature
        }
