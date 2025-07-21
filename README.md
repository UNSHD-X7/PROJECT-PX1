# PROJECT-PX1

**pypxcryptokit** is a Python cryptographic library providing modern secure messaging primitives, including [Double Ratchet](https://signal.org/docs/specifications/doubleratchet/) and [X3DH (Extended Triple Diffie-Hellman)](https://signal.org/docs/specifications/x3dh/). The library is designed to support end-to-end encryption, forward secrecy, and deniability for secure communication.

## Features

- Double Ratchet protocol for message encryption with forward secrecy and post-compromise security.
- X3DH protocol for initial key agreement and authentication.
- Easy serialization and deserialization for session state management.
- Pluggable cryptographic primitives using Python's `cryptography` and custom implementations.
- Designed for extensibility and integration with secure messaging apps.

## Installation

```bash
pip install pypxcryptokit
```

## Usage

### Double Ratchet

```python
from pypxcryptokit.double_ratchet import DRSession, DHKeyPair, DHPublicKey

# Generate DH key pairs
alice_dh = DHKeyPair.generate_dh()
bob_dh = DHKeyPair.generate_dh()

# Setup Alice as sender
alice_session = DRSession()
alice_session.setup_sender(sk=b"shared_secret_bytes", dh_pk_r=bob_dh.public_key)

# Setup Bob as receiver
bob_session = DRSession()
bob_session.setup_receiver(sk=b"shared_secret_bytes", dh_pair=bob_dh)

# Encrypt a message
msg = alice_session.encrypt_message("Hello Bob!", b"associated_data")

# Decrypt the message
plaintext = bob_session.decrypt_message(msg, b"associated_data")
print(plaintext)  # "Hello Bob!"
```

### X3DH

```python
from pypxcryptokit.x3dh import State, IdentityKeyPairSeed, IdentityKeyFormat, HashFunction

# Create a state (user's key bundle)
state = State.create(
    identity_key_format=IdentityKeyFormat.CURVE_25519,
    hash_function=HashFunction.SHA_256,
    info=b"application info"
)

# Generate a bundle to publish to the server
bundle = state.bundle

# Perform key agreement (active)
shared_secret, associated_data, header = await state.get_shared_secret_active(bundle)
```

## API Reference

For full API details, see the documentation and source files:

- [`double_ratchet.py`](https://github.com/UNSHD-X7/PROJECT-PX1/blob/main/double_ratchet.py)
- [`x3dh.py`](https://github.com/UNSHD-X7/PROJECT-PX1/blob/main/x3dh.py)

## Example Test File

Below is a sample test file demonstrating usage of the Double Ratchet and X3DH APIs.

```python name=tests/test_pypxcryptokit.py
import pytest

from pypxcryptokit.double_ratchet import DRSession, DHKeyPair, DHPublicKey
from pypxcryptokit.x3dh import State, IdentityKeyFormat, HashFunction

def test_double_ratchet_encrypt_decrypt():
    # Setup Alice and Bob sessions
    alice_dh = DHKeyPair.generate_dh()
    bob_dh = DHKeyPair.generate_dh()
    shared_secret = b"supersecretkey12345678901234567890"  # 32 bytes

    alice = DRSession()
    bob = DRSession()

    alice.setup_sender(sk=shared_secret, dh_pk_r=bob_dh.public_key)
    bob.setup_receiver(sk=shared_secret, dh_pair=bob_dh)

    msg = alice.encrypt_message("Hello Bob!", b"header_data")
    pt = bob.decrypt_message(msg, b"header_data")
    assert pt == "Hello Bob!"

def test_x3dh_key_agreement():
    state = State.create(
        identity_key_format=IdentityKeyFormat.CURVE_25519,
        hash_function=HashFunction.SHA_256,
        info=b"app info"
    )
    bundle = state.bundle

    import asyncio
    shared_secret, associated_data, header = asyncio.run(
        state.get_shared_secret_active(bundle)
    )
    assert isinstance(shared_secret, bytes)
    assert isinstance(associated_data, bytes)
    assert header is not None
```

## License

MIT

## Authors

- [UNSHD-X7](https://github.com/UNSHD-X7)

## Source Files

- [`double_ratchet.py`](https://github.com/UNSHD-X7/PROJECT-PX1/blob/main/double_ratchet.py)
- [`x3dh.py`](https://github.com/UNSHD-X7/PROJECT-PX1/blob/main/x3dh.py)

---

**Note**: This library is for educational and research purposes. Do not use in production without thorough security review.
