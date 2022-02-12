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
password, pressed = "", False
values = {}
window_title = ""


# Folder creations.
if not (all_imp.os.path.exists(imported)):
    try:
        all_imp.os.mkdir(imported, access_rights)
    except OSError:
        folder_error_eng = ["Creation of the directory %s failed." % imported, "Error!"]
        folder_error_esp = ["Ha fallado la creación del directorio %s." % imported, "¡Error!"]
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
        folder_error_eng = ["Creation of the directory %s failed." % keys, "Error!"]
        folder_error_esp = ["Ha fallado la creación del directorio %s. " % keys, "¡Error!"]
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
        folder_error_eng = ["Creation of the directory %s failed." % output, "Error!"]
        folder_error_esp = ["Ha fallado la creación del directorio %s." % output, "¡Error!"]
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
        folder_error_eng = ["Creation of the directory %s failed." % encrypted, "Error!"]
        folder_error_esp = ["Ha fallado la creación del directorio %s." % encrypted, "¡Error!"]
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
        folder_error_eng = ["Creation of the directory %s failed." % decrypted, "Error!"]
        folder_error_esp = ["Ha fallado la creación del directorio %s." % decrypted, "¡Error!"]
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
        folder_error_eng = ["Creation of the directory %s failed." % signed, "Error!"]
        folder_error_esp = ["Ha fallado la creación del directorio %s." % signed, "¡Error!"]
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
        folder_error_eng = ["Creation of the directory %s failed." % verified, "Error!"]
        folder_error_esp = ["Ha fallado la creación del directorio %s." % verified, "¡Error!"]
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
        pressed = False
        event, mode, values = all_imp.enc.em(encrypted, event, imported, lang, mes_enc_eng, mes_enc_esp)

    # Decryption selected.
    elif mode == 20:
        pressed = False
        event, mode, values = all_imp.dec.dm(decrypted, event, imported, keys, lang, mes_dec_eng, mes_dec_esp)

    # Signing selected.
    elif mode == 30:
        pressed = False
        event, mode, values = all_imp.sig.sm(encrypted, event, keys, lang, mes_sig_eng, mes_sig_esp, signed)

    # Verifying selected.
    elif mode == 40:
        pressed = False
        event, mode, values = all_imp.ver.vm(event, imported, lang, verified)

    # Perform encryption of plaintext message.
    if event == "enc":
        event, mode, values = all_imp.enc.ef(encrypted, event, imported, lang, mes_enc_eng, mes_enc_esp, values)

    # Perform decryption encrypted message
    if event == "dec":
        event, mode, values = all_imp.dec.df(decrypted, event, keys, lang, mes_dec_eng, mes_dec_esp, values)

    # Perfonm singing of message.
    if event == "sig":
        event, mode, values = all_imp.sig.sf(event, keys, lang, mes_sig_eng, mes_sig_esp, signed, values)

    # Exit tool.
    if event == 600:
        all_imp.sys.exit(0)

    # Show menu.
    if event == 800:
        mode = None
