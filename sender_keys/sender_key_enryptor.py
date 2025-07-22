import hmac
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

def derive_message_key(chain_key: bytes):
    message_key = hmac.new(chain_key, b"message", hashlib.sha256).digest()
    next_chain_key = hmac.new(chain_key, b"chain", hashlib.sha256).digest()
    return message_key, next_chain_key

def encrypt_and_sign(plaintext: bytes, bundle: SenderKeyBundle):
    message_key, next_chain_key = derive_message_key(bundle.sender_chain_key)
    aesgcm = AESGCM(message_key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    signature = bundle.sender_signing_key.sign(ciphertext)
    bundle.sender_chain_key = next_chain_key
    bundle.message_index += 1
    return {
        "sender_key_id": bundle.sender_key_id,
        "message_index": bundle.message_index,
        "nonce": base64.b64encode(nonce).decode(),
        "ciphertext": base64.b64encode(ciphertext).decode(),
        "signature": base64.b64encode(signature).decode()
    }
