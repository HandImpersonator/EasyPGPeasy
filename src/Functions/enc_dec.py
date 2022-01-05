# enc_dec.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports


# key marker classes for convenience
class Key(object):
    pass


class Public(Key):
    pass


class Private(Key):
    pass


def pgpy_decrypt(enc_data, key):
    """Decrypt a plaintext message with a given encrypted message and private key.
    Public keys will return an error, incorrect private keys will return an error, empty key will return an error.
    Return plaintext message or error if something went wrong."""
    privkey, _ = all_imports.pgpy.PGPKey.from_file(key)
    if not is_public(privkey):
        return privkey.decrypt(all_imports.pgpy.PGPMessage.from_blob(enc_data)).message.decode("utf-8")
    if is_public(privkey):
        return "Public", False


def pgpy_encrypt(data, key):
    """Encrypt a message with a given plaintext message and public key.
    Private keys will return an error, incorrect public keys will return an error, empty key will return an error.
    Return encrypted message or error if something went wrong."""
    pubkey, _ = all_imports.pgpy.PGPKey.from_file(key)
    if is_public(pubkey):
        mes = all_imports.pgpy.PGPMessage.new(data)
        enc_data = (pubkey.pubkey.encrypt(mes, cipher = all_imports.SymmetricKeyAlgorithm.AES256,
                                          hash = all_imports.HashAlgorithm.SHA512))
        return enc_data
    elif not is_public(pubkey):
        return "Private"


def is_public(key):
    """Checks whether the given key is a public or a private key, using magic property."""
    if isinstance(key, str):
        is_it = all_imports.pgpy.PGPKey.from_blob(key)
        if getattr(is_it[0], "magic").split()[0] == "PUBLIC":
            return True
    if getattr(key, "magic").split()[0] == "PUBLIC":
        return True
    return False


def sign(data, key):
    """Sign a message with a given message and private key.
    Public keys will return an error, incorrect private keys will return an error, empty key will return an error.
    Return signed message or error if something went wrong."""
    privkey, _ = all_imports.pgpy.PGPKey.from_file(key)
    if not is_public(privkey):
        return privkey.decrypt(all_imports.pgpy.PGPKey.sign(data)).message.decode("utf-8")
    elif is_public(privkey):
        return "Public", False


def verify(enc_data, key):
    """Verify a message with a given message and public key.
    Private keys will return an error, incorrect public keys will return an error, empty key will return an error.
    Return verification or error if something went wrong."""
    pubkey, _ = all_imports.pgpy.PGPKey.from_file(key)
    if is_public(pubkey):
        return pubkey.sign(all_imports.pgpy.PGPKey.verify(pubkey, enc_data),
                           cipher = all_imports.SymmetricKeyAlgorithm.AES256,
                           hash = all_imports.HashAlgorithm.SHA512), True
    elif not is_public(pubkey):
        return "Private", False
