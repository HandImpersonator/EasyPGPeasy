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


def pgpy_decrypt(enc_data, key, lang, messages):
    """Decrypt a plaintext message with a given encrypted message and private key.
    Public keys will return an error, incorrect private keys will return an error, empty key will return an error.
    Return plaintext message or error if something went wrong."""
    error1, error2 = "", ""
    privkey, _ = all_imports.pgpy.PGPKey.from_file(key)
    if not is_public(privkey):
        if all_imports.os.path.exists(enc_data):
            mes = open(enc_data, "r")
            message = mes.read().strip()
        else:
            message = str(enc_data)
        data = all_imports.pgpy.PGPMessage.from_blob(str(message))
        dec_data = str((privkey.decrypt(data)).message)
        dec_message = open(messages + "/decrypted_message.txt", "w")
        dec_message.write(str(dec_data))
        dec_message.close()
        return str(dec_data), True
    elif is_public(privkey):
        error_popup_eng = ["Error. Provided key to decrypt was a public key.",
                           "Cannot decrypt with the correct private key.", "Returning to menu.", "Error decrypting!"]
        error_popup_esp = ["Error. La clave usada para descifrar era una clave pública.",
                           "No se puede descifrar sin la clave privada correcta.", "Volviendo al menú.",
                           "¡Error descifrando!"]
        if lang:
            error1 = error_popup_eng[0] + "\n" + error_popup_eng[1] + error_popup_eng[2]
            error2 = error_popup_eng[3]
        if not lang:
            error1 = error_popup_esp[0] + "\n" + error_popup_esp[1] + error_popup_esp[2]
            error2 = error_popup_esp[3]
        all_imports.pSG.popup_error(error1, title = error2)
        return _, False


def pgpy_encrypt(data, key, lang, messages):
    """Encrypt a message with a given plaintext message and public key.
    Private keys will return an error, incorrect public keys will return an error, empty key will return an error.
    Return encrypted message or error if something went wrong."""
    error1, error2 = "", ""
    pubkey, _ = all_imports.pgpy.PGPKey.from_file(key)
    if is_public(pubkey):
        mes = all_imports.pgpy.PGPMessage.new(data)
        enc_data = (pubkey.encrypt(mes, cipher = all_imports.SymmetricKeyAlgorithm.AES256,
                                   hash = all_imports.HashAlgorithm.SHA512))
        enc_message = open(messages + "/encrypted_message.txt", "w")
        enc_message.write(str(enc_data))
        enc_message.close()
        return str(enc_data), True
    elif not is_public(pubkey):
        error_popup_eng = ["Error. Provided key to encrypt was a private key, try importing the public key again.",
                           "Returning to menu.", "Error encrypting!"]
        error_popup_esp = ["Error. La clave pública usada para cifrar era una clave privada, ",
                           "intenta importar la clave pública de nuevo.", "Volviendo al menú.",
                           "¡Error cifrando!"]
        if lang:
            error1 = error_popup_eng[0] + "\n" + error_popup_eng[1]
            error2 = error_popup_eng[2]
        if not lang:
            error1 = error_popup_esp[0] + "\n" + error_popup_esp[1]
            error2 = error_popup_esp[2]
        all_imports.pSG.popup_error(error1, title = error2)
        return _, False


def is_public(key):
    """Checks whether the given key is a public or a private key, using magic property."""
    if isinstance(key, str):
        is_it = all_imports.pgpy.PGPKey.from_blob(key)
        if getattr(is_it[0], "magic").split()[0] == "PUBLIC":
            return True
    if getattr(key, "magic").split()[0] == "PUBLIC":
        return True
    return False


def is_signature(imp, key, lang):
    """Checks whether the given key is a signature, using magic property."""
    done, error1, error2, is_it = "", "", "", ""
    if isinstance(key, str):
        try:
            is_it = all_imports.pgpy.PGPSignature.from_blob(key)
        except all_imports.pgpy.errors.PGPError:
            error_popup_eng = ["Incorrect padding or invalid base64-encoded string:",
                               "incorrect number of data characters.", "Incorrect signature!"]
            error_popup_esp = ["Cadena codificada en base-64 no válida:",
                               "Número de caracteres incorrecto.", "¡Firma incorrecta!"]
            if lang:
                error1 = error_popup_eng[0] + error_popup_eng[1]
                error2 = error_popup_eng[2]
            if not lang:
                error1 = error_popup_esp[0] + error_popup_esp[1]
                error2 = error_popup_esp[2]
            all_imports.pSG.popup_error(error1, title = error2)
        if getattr(is_it, "magic") == "SIGNATURE":
            text_file_v = open(imp + "/v_imported_signature.txt", "w")
            text_file_v.write(str(key))
            text_file_v.close()
            if lang:
                done = "Done!"
            elif not lang:
                done = "¡Hecho!"
            all_imports.pSG.popup_auto_close(done, auto_close_duration = 0.8, button_type = 5)
            return True
    if getattr(key, "magic").split()[0] == "SIGNATURE":
        text_file_v = open(imp + "/v_imported_signature.txt", "w")
        text_file_v.write(str(key))
        text_file_v.close()
        if lang:
            done = "Done!"
        elif not lang:
            done = "¡Hecho!"
        all_imports.pSG.popup_auto_close(done, auto_close_duration = 0.8, button_type = 5)
        return True
    return False


def pgpy_sign(data, key, lang, messages):
    """Sign a message with a given message and private key.
    Public keys will return an error, incorrect private keys will return an error, empty key will return an error.
    Return signature or error if something went wrong."""
    error1, error2 = "", ""
    privkey, _ = all_imports.pgpy.PGPKey.from_file(key)
    if not is_public(privkey):
        if all_imports.os.path.exists(data):
            mes = open(data, "r")
            message = mes.read().strip()
            sig_message1 = open(messages + "/auto_signed_message.txt", "w")
            sig_message2 = open(messages + "/auto_message_signature.txt", "w")
        else:
            message = str(data)
            sig_message1 = open(messages + "/signed_message.txt", "w")
            sig_message2 = open(messages + "/message_signature.txt", "w")
        sig_data = str(privkey.sign(message))
        sig_message1.write(str(message))
        sig_message2.write(str(sig_data))
        sig_message1.close()
        sig_message2.close()
        all_imports.pyclip.copy(str(sig_data))
        return str(sig_data), True
    elif is_public(privkey):
        error_popup_eng = ["Error. Provided key to sign was a public key, try checking the ",
                           "private key used.\nReturning to menu.", "Error sigining!"]
        error_popup_esp = ["Error. La clave usada para firmar era una clave pública, ",
                           "intenta importar la clave pública de nuevo.\nVolviendo al menú."]
        if lang:
            error1 = error_popup_eng[0] + error_popup_eng[1]
            error2 = error_popup_eng[2]
        if not lang:
            error1 = error_popup_esp[0] + error_popup_esp[1]
            error2 = error_popup_esp[2]
        all_imports.pSG.popup_error(error1, title = error2)


def pgpy_verify(inp, key, lang, imported, sig_data):
    """Verify a message with a given message and public key.
    Private keys will return an error, incorrect public keys will return an error, empty key will return an error.
    Return verification or error if something went wrong."""
    error1, error2 = "", ""
    inp_mes = open(inp).read()
    pubkey, _ = all_imports.pgpy.PGPKey.from_file(key)
    sig = all_imports.pgpy.PGPSignature.from_file(sig_data)
    if is_public(pubkey):
        ver_mes = pubkey.verify(inp_mes, sig)
        if ver_mes.__bool__():
            ver_message = open(imported + "/v_verified_message.txt", "w")
            ver_message.write(str(inp_mes))
            ver_message.close()
            return str(ver_mes), True
        else:
            error_popup_eng = ["Message and signature do not match, cannot verify.", "Error verifying!"]
            error_popup_esp = ["El mensaje y la firma no coinciden, no se puede verificar.", "¡Error verificando!"]
            if lang:
                error1 = error_popup_eng[0]
                error2 = error_popup_eng[1]
            elif not lang:
                error1 = error_popup_esp[0]
                error2 = error_popup_esp[1]
            all_imports.pSG.popup_error(error1, title = error2)
            return _, False
    elif not is_public(pubkey):
        error_popup_eng = ["Error. Provided key to verify was a private key, try importing the public key again.",
                           "Returning to menu.", "Error verifying!"]
        error_popup_esp = ["Error. la clave pública usada para verificar era una clave privada, ",
                           "intenta importar la clave pública de nuevo key again.", "Volviendo al menú.",
                           "¡Error verificando!"]
        if lang:
            error1 = error_popup_eng[0] + "\n" + error_popup_eng[1]
            error2 = error_popup_eng[2]
        if not lang:
            error1 = error_popup_esp[0] + error_popup_esp[1] + "\n" + error_popup_esp[2]
            error2 = error_popup_esp[3]
        all_imports.pSG.popup_error(error1, title = error2)
        return _, False
