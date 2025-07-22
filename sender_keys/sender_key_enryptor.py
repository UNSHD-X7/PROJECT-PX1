import hmac
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class SenderKeyEncryptor:
    @staticmethod
    def derive_message_key(chain_key):
        message_key = hmac.new(chain_key, b"message", hashlib.sha256).digest()
        next_chain_key = hmac.new(chain_key, b"chain", hashlib.sha256).digest()
        return message_key, next_chain_key

    @staticmethod
    def encrypt(message_key: bytes, plaintext: bytes, associated_data: bytes = b"") -> bytes:
        aesgcm = AESGCM(message_key[:16])  # Use first 16 bytes for AES-128
        nonce = os.urandom(12)
        ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data)
        return nonce + ciphertext

    @staticmethod
    def decrypt(message_key: bytes, ciphertext: bytes, associated_data: bytes = b"") -> bytes:
        aesgcm = AESGCM(message_key[:16])
        nonce = ciphertext[:12]
        return aesgcm.decrypt(nonce, ciphertext[12:], associated_data)
