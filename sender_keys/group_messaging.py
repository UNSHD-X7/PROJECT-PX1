import hmac
import hashlib
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidSignature

def decrypt_group_message(record: SenderKeyRecord, msg: dict):
    target_index = msg["message_index"]
    chain_key = record.sender_chain_key
    for i in range(record.message_index, target_index):
        _, chain_key = derive_message_key(chain_key)
    message_key, next_chain_key = derive_message_key(chain_key)
    ciphertext = base64.b64decode(msg["ciphertext"])
    nonce = base64.b64decode(msg["nonce"])
    signature = base64.b64decode(msg["signature"])
    # verify signature
    record.public_key().verify(signature, ciphertext)
    # decrypt
    aesgcm = AESGCM(message_key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    # update record
    record.sender_chain_key = next_chain_key
    record.message_index = target_index + 1
    return plaintext
