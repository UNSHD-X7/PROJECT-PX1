import base64
import json

def sender_key_distribution_message(bundle: SenderKeyBundle):
    pub_bundle = bundle.get_public_bundle()
    return json.dumps({
        "sender_key_id": pub_bundle["sender_key_id"],
        "sender_chain_key": base64.b64encode(pub_bundle["sender_chain_key"]).decode(),
        "sender_signing_pub": base64.b64encode(pub_bundle["sender_signing_pub"]).decode(),
    })
# Zprávu zašifrovat Double Ratchet session pro každého člena skupiny.
