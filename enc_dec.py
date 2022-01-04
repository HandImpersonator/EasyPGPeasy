# enc_dec.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import all_imports


# key marker classes for convenience
class Key(object):
    pass


class Public(Key):
    pass


class Private(Key):
    pass


def pgpy_decrypt(enc_data, key):
    privkey, _ = all_imports.pgpy.PGPKey.from_file(key)
    if not is_public(privkey):
        return privkey.decrypt(all_imports.pgpy.PGPMessage.from_blob(enc_data)).message.decode("utf-8")
    if is_public(privkey):
        return "Public", False


def pgpy_encrypt(data, key):
    pubkey, _ = all_imports.pgpy.PGPKey.from_file(key)
    if is_public(pubkey):
        return pubkey.encrypt(all_imports.pgpy.PGPMessage.new(data),
                              cipher = all_imports.SymmetricKeyAlgorithm.AES256,
                              hash = all_imports.HashAlgorithm.SHA512), True
    elif not is_public(pubkey):
        return "Private", False


def is_public(key):
    is_it = all_imports.pgpy.PGPKey.from_blob(key)
    return getattr(is_it[0], "is_public")


def sign(data, key):
    privkey, _ = all_imports.pgpy.PGPKey.from_file(key)
    if not is_public(privkey):
        return privkey.decrypt(all_imports.pgpy.PGPKey.sign(data)).message.decode("utf-8")
    elif is_public(privkey):
        return "Public", False


def verify(enc_data, key):
    pubkey, _ = all_imports.pgpy.PGPKey.from_file(key)
    if is_public(pubkey):
        return pubkey.sign(all_imports.pgpy.PGPKey.verify(pubkey, enc_data),
                           cipher = all_imports.SymmetricKeyAlgorithm.AES256,
                           hash = all_imports.HashAlgorithm.SHA512), True
    elif not is_public(pubkey):
        return "Private", False
