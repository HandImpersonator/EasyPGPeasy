# EZPZ-PGP.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imp


"""Creates the menu window and makes all the encryption, decryption, signing and verification process, automating
file saving and file reading, pasting from clipboard."""

access_rights = 0o755
copied, error1, error2, fin, paste = "", "", "", "", ""
curr_path = all_imp.os.getcwd()
done, event, lang, mode = False, None, "eng", None
imported = curr_path + "/Imported"
keys = curr_path + "/Keys"
output = curr_path + "/Output"
encrypted = output + "/Encrypted"
decrypted = output + "/Decrypted"
signed = output + "/Signed"
verified = output + "/Verified"
out_dec, out_sig = "", ""
password = ""
values = {}
window_title = ""


# Folder creations.
if not (all_imp.os.path.exists(imported)):
    try:
        all_imp.os.mkdir(imported, access_rights)
    except OSError:
        folder_error_eng = ["Creation of the directory %s failed." % imported, "Error creating folder!"]
        folder_error_esp = ["Ha fallado la creación del directorio %s." % imported, "¡Error creando fichero!"]
        if lang == "eng":
            error1 = folder_error_eng[0]
            error2 = folder_error_eng[1]
        elif lang == "esp":
            error1 = folder_error_esp[0]
            error2 = folder_error_esp[1]
        all_imp.pSG.popup_auto_close(error1, auto_close_duration = 2, button_type = 5, title = error2)

if not (all_imp.os.path.exists(keys)):
    try:
        all_imp.os.mkdir(keys, access_rights)
    except OSError:
        folder_error_eng = ["Creation of the directory %s failed." % keys, "Error creating folder!"]
        folder_error_esp = ["Ha fallado la creación del directorio %s. " % keys, "¡Error creando fichero!"]
        if lang == "eng":
            error1 = folder_error_eng[0]
            error2 = folder_error_eng[1]
        elif lang == "esp":
            error1 = folder_error_esp[0]
            error2 = folder_error_esp[1]
        all_imp.pSG.popup_auto_close(error1, auto_close_duration = 2, button_type = 5, title = error2)

if not (all_imp.os.path.exists(output)):
    try:
        all_imp.os.mkdir(output, access_rights)
    except OSError:
        folder_error_eng = ["Creation of the directory %s failed." % output, "Error creating folder!"]
        folder_error_esp = ["Ha fallado la creación del directorio %s." % output, "¡Error creando fichero!"]
        if lang == "eng":
            error1 = folder_error_eng[0]
            error2 = folder_error_eng[1]
        elif lang == "esp":
            error1 = folder_error_esp[0]
            error2 = folder_error_esp[1]
        all_imp.pSG.popup_auto_close(error1, auto_close_duration = 2, button_type = 5, title = error2)

if not (all_imp.os.path.exists(encrypted)):
    try:
        all_imp.os.mkdir(encrypted, access_rights)
    except OSError:
        folder_error_eng = ["Creation of the directory %s failed." % encrypted, "Error creating folder!"]
        folder_error_esp = ["Ha fallado la creación del directorio %s." % encrypted, "¡Error creando fichero!"]
        if lang == "eng":
            error1 = folder_error_eng[0]
            error2 = folder_error_eng[1]
        elif lang == "esp":
            error1 = folder_error_esp[0]
            error2 = folder_error_esp[1]
        all_imp.pSG.popup_auto_close(error1, auto_close_duration = 2, button_type = 5, title = error2)

if not (all_imp.os.path.exists(decrypted)):
    try:
        all_imp.os.mkdir(decrypted, access_rights)
    except OSError:
        folder_error_eng = ["Creation of the directory %s failed." % decrypted, "Error creating folder!"]
        folder_error_esp = ["Ha fallado la creación del directorio %s." % decrypted, "¡Error creando fichero!"]
        if lang == "eng":
            error1 = folder_error_eng[0]
            error2 = folder_error_eng[1]
        elif lang == "esp":
            error1 = folder_error_esp[0]
            error2 = folder_error_esp[1]
        all_imp.pSG.popup_auto_close(error1, auto_close_duration = 2, button_type = 5, title = error2)

if not (all_imp.os.path.exists(signed)):
    try:
        all_imp.os.mkdir(signed, access_rights)
    except OSError:
        folder_error_eng = ["Creation of the directory %s failed." % signed, "Error creating folder!"]
        folder_error_esp = ["Ha fallado la creación del directorio %s." % signed, "¡Error creando fichero!"]
        if lang == "eng":
            error1 = folder_error_eng[0]
            error2 = folder_error_eng[1]
        elif lang == "esp":
            error1 = folder_error_esp[0]
            error2 = folder_error_esp[1]
        all_imp.pSG.popup_auto_close(error1, auto_close_duration = 2, button_type = 5, title = error2)

if not (all_imp.os.path.exists(verified)):
    try:
        all_imp.os.mkdir(verified, access_rights)
    except OSError:
        folder_error_eng = ["Creation of the directory %s failed." % verified, "Error creating folder!"]
        folder_error_esp = ["Ha fallado la creación del directorio %s." % verified, "¡Error creando fichero!"]
        if lang == "eng":
            error1 = folder_error_eng[0]
            error2 = folder_error_eng[1]
        elif lang == "esp":
            error1 = folder_error_esp[0]
            error2 = folder_error_esp[1]
        all_imp.pSG.popup_auto_close(error1, auto_close_duration = 2, button_type = 5, title = error2)

while True:

    # Create menu.
    while mode is None:
        lang, mode = all_imp.menu.create_menu(lang, imported, keys)

    mes_enc_eng, mes_enc_esp, mes_dec_eng, mes_dec_esp, mes_sig_eng, mes_sig_esp = all_imp.eds_layout.crem_enc_dec()

    # Encryption selected.
    if mode == 15:
        key = imported + "/v_imported_public.asc"
        if all_imp.os.path.isfile(key):
            event, mode, values = all_imp.enc.em(encrypted, event, key, lang, mes_enc_eng, mes_enc_esp)
        else:
            no_pub_eng = ["Public key to encrypt file does not exist.", "Error encrypting!"]
            no_pub_esp = ["La clave pública para file el mensaje no existe.", "¡Error cifrando!"]
            if lang == "eng":
                error1 = no_pub_eng[0]
                error2 = no_pub_eng[1]
            elif lang == "esp":
                error1 = no_pub_esp[0]
                error2 = no_pub_esp[1]
            all_imp.pSG.popup_error(error1, title = error2)

    # Decryption selected.
    elif mode == 20:
        key = keys + "/private.asc"
        mes = imported + "/v_imported_message.txt"
        if all_imp.os.path.isfile(key):
            event, mode, values = all_imp.dec.dm(decrypted, event, key, lang, mes, mes_dec_eng, mes_dec_esp)
        else:
            no_priv_eng = ["Private key to decrypt message does not exist.", "Error decrypting!"]
            no_priv_esp = ["La clave privada para descifrar el mensaje no existe.", "¡Error descifrando!"]
            if lang == "eng":
                error1 = no_priv_eng[0]
                error2 = no_priv_eng[1]
            elif lang == "esp":
                error1 = no_priv_esp[0]
                error2 = no_priv_esp[1]
            all_imp.pSG.popup_error(error1, title = error2)

    # Signing selected.
    elif mode == 30:
        key = keys + "/private.asc"
        enc = encrypted + "/encrypted_message.txt"
        if all_imp.os.path.isfile(key):
            event, mode, values = all_imp.sig.sm(enc, event, key, lang, mes_sig_eng, mes_sig_esp, signed)
        else:
            no_priv_eng = ["Private key to sign message does not exist.", "Error signing!"]
            no_priv_esp = ["La clave privada para firmar el mensaje no existe.", "¡Error firmando!"]
            if lang == "eng":
                error1 = no_priv_eng[0]
                error2 = no_priv_eng[1]
            elif lang == "esp":
                error1 = no_priv_esp[0]
                error2 = no_priv_esp[1]
            all_imp.pSG.popup_error(error1, title = error2)

    # Verifying selected.
    elif mode == 40:
        key = imported + "/v_imported_public.asc"
        mes = imported + "/v_imported_message.txt"
        sig = imported + "/v_imported_signature.txt"
        if all_imp.os.path.isfile(key):
            if all_imp.os.path.isfile(sig):
                event, mode, values = all_imp.ver.vm(event, key, lang, mes, sig, verified)
            else:
                no_ver_eng = ["Signature to verify message is not imported.", "Error verifying!"]
                no_ver_esp = ["La firma para verificar el mensaje no está importado.", "¡Error verificando!"]
                if lang == "eng":
                    error1 = no_ver_eng[0]
                    error2 = no_ver_eng[1]
                elif lang == "esp":
                    error1 = no_ver_esp[0]
                    error2 = no_ver_esp[1]
                all_imp.pSG.popup_error(error1, title = error2)
        else:
            no_pub_eng = ["Public key to verify message is not imported.", "Error verifying!"]
            no_pub_esp = ["La clave pública para verificar el mensaje no está importado.", "¡Error verificando!"]
            if lang == "eng":
                error1 = no_pub_eng[0]
                error2 = no_pub_eng[1]
            elif lang == "esp":
                error1 = no_pub_esp[0]
                error2 = no_pub_esp[1]
            all_imp.pSG.popup_error(error1, title = error2)

    # Perform encryption of plaintext message.
    if event == "enc":
        key = imported + "/v_imported_public.asc"
        event, mode, values = all_imp.enc.ef(encrypted, event, key, lang, mes_enc_eng, mes_enc_esp, values)

    # Perform decryption of encrypted message
    if event == "dec":
        key = keys + "/private.asc"
        event, mode, values = all_imp.dec.df(decrypted, event, key, lang, mes_dec_eng, mes_dec_esp, values)

    # Perfonm singing of message.
    if event == "sig":
        key = keys + "/private.asc"
        event, mode, values = all_imp.sig.sf(event, key, lang, mes_sig_eng, mes_sig_esp, signed, values)

    # Exit tool.
    if event == 600:
        all_imp.sys.exit(0)
