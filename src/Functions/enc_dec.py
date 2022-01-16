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


def pgpy_decrypt(enc_data, key, messages):
    """Decrypt a plaintext message with a given encrypted message and private key.
    Public keys will return an error, incorrect private keys will return an error, empty key will return an error.
    Return plaintext message or error if something went wrong."""
    privkey, _ = all_imports.pgpy.PGPKey.from_file(key)
    if not is_public(privkey):
        mes = all_imports.pgpy.PGPMessage.from_blob(enc_data)
        dec_data = (privkey.decrypt(mes)).message
        dec_message = open(messages + "/decrypted_message.txt", "w")
        dec_message.write(str(dec_data))
        dec_message.close()
        return dec_data
    elif is_public(privkey):
        all_imports.pSG.popup_error("Error. Provided key to decrypt was a public key, try importing the public "
                                    "key again.")


def pgpy_encrypt(data, key, messages):
    """Encrypt a message with a given plaintext message and public key.
    Private keys will return an error, incorrect public keys will return an error, empty key will return an error.
    Return encrypted message or error if something went wrong."""
    pubkey, _ = all_imports.pgpy.PGPKey.from_file(key)
    if is_public(pubkey):
        mes = all_imports.pgpy.PGPMessage.new(data)
        enc_data = (pubkey.encrypt(mes, cipher = all_imports.SymmetricKeyAlgorithm.AES256,
                                   hash = all_imports.HashAlgorithm.SHA512))
        enc_message = open(messages + "/encrypted_message.txt", "w")
        enc_message.write(str(enc_data))
        enc_message.close()
        return enc_data
    elif not is_public(pubkey):
        all_imports.pSG.popup_error("Error. Provided key to encrypt was a private key, try importing the public "
                                    "key again.")


def is_public(key):
    """Checks whether the given key is a public or a private key, using magic property."""
    if isinstance(key, str):
        is_it = all_imports.pgpy.PGPKey.from_blob(key)
        if getattr(is_it[0], "magic").split()[0] == "PUBLIC":
            return True
    if getattr(key, "magic").split()[0] == "PUBLIC":
        return True
    return False


def is_signature(key):
    """Checks whether the given key is a public or a private key, using magic property."""
    if isinstance(key, str):
        is_it = ""
        try:
            is_it = all_imports.pgpy.PGPSignature.from_blob(key)
        except all_imports.pgpy.errors.PGPError:
            all_imports.pSG.popup_error("Incorrect padding or invalid base64-encoded string: incorrect number of data "
                                        "characters.", title = "¡Error importing!")
        if getattr(is_it, "magic") == "SIGNATURE":
            return True
    if getattr(key, "magic").split()[0] == "SIGNATURE":
        return True
    return False


def pgpy_sign(data, key, messages):
    """Sign a message with a given message and private key.
    Public keys will return an error, incorrect private keys will return an error, empty key will return an error.
    Return signed message or error if something went wrong."""
    privkey, _ = all_imports.pgpy.PGPKey.from_file(key)
    if not is_public(privkey):
        if all_imports.os.path.exists(data):
            mes = open(data, "r")
            message = mes.read().strip()
        else:
            message = str(data)
        sig_data = (privkey.sign(message))
        sig_message1 = open(messages + "/signed_message.txt", "w")
        sig_message2 = open(messages + "/message_signature.txt", "w")
        sig_message1.write(str(data))
        sig_message2.write(str(sig_data))
        sig_message1.close()
        sig_message2.close()
        return sig_data
    elif is_public(privkey):
        all_imports.pSG.popup_error("Error. Provided key to sign was a public key, try creating the private key "
                                    "again.")


def pgpy_verify(inp, sig_data, key, messages):
    """Verify a message with a given message and public key.
    Private keys will return an error, incorrect public keys will return an error, empty key will return an error.
    Return verification or error if something went wrong."""
    pubkey, _ = all_imports.pgpy.PGPKey.from_file(key)
    sig = all_imports.pgpy.PGPSignature.from_file(sig_data)
    if is_public(pubkey):
        ver_mes = pubkey.verify(inp, sig)
        ver_message = open(messages + "/verified_message.txt", "w")
        ver_message.write(str(ver_mes))
        ver_message.write(str(inp))
        ver_message.close()
        return
    elif not is_public(pubkey):
        all_imports.pSG.popup_error("Error. Provided key to verify was a private key, try importing the public "
                                    "key again.")
