# main-pgp.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import all_imports

event = None
lang = True
mode = None
values = {}

curr_path = all_imports.os.getcwd()
access_rights = 0o755
coffee = curr_path + "/Coffee"
keys = curr_path + "/Keys"
messages = curr_path + "/Messages"

while True:

    while mode is None:
        if lang:
            lang, mode = all_imports.menu.create_menu(lang)
        elif not lang:
            lang, mode = all_imports.menu.create_menu(lang)

    mes_enc_eng, mes_enc_esp, mes_dec_eng, mes_dec_esp = all_imports.enc_dec_window.enc_dec_create()

    try:
        if (all_imports.os.path.exists(coffee)) or (all_imports.os.path.exists(keys)) or (
                all_imports.os.path.exists(messages)):
            all_imports.os.rmdir(coffee)
            all_imports.os.rmdir(keys)
            all_imports.os.rmdir(messages)
        if not (all_imports.os.path.exists(coffee)) or not (all_imports.os.path.exists(keys)) or not (
                all_imports.os.path.exists(messages)):
            all_imports.os.mkdir(coffee, access_rights)
            all_imports.os.mkdir(keys, access_rights)
            all_imports.os.mkdir(messages, access_rights)
    except OSError:
        if lang:
            all_imports.pSG.popup_auto_close("Creation of the directory %s failed." % coffee,
                                             auto_close_duration = 2, button_type = 5, title = "Error!", )
            all_imports.pSG.popup_auto_close("Creation of the directory %s failed." % keys,
                                             auto_close_duration = 2, button_type = 5, title = "Error!", )
            all_imports.pSG.popup_auto_close("Creation of the directory %s failed." % messages,
                                             auto_close_duration = 2, button_type = 5, title = "Error!")
        elif not lang:
            all_imports.pSG.popup_auto_close("Ha fallado la creación del directorio %s." % coffee,
                                             auto_close_duration = 2, button_type = 5, title = "¡Error!")
            all_imports.pSG.popup_auto_close("Ha fallado la creación del directorio %s." % keys,
                                             auto_close_duration = 2, button_type = 5, title = "¡Error!")
            all_imports.pSG.popup_auto_close("Ha fallado la creación del directorio %s." % messages,
                                             auto_close_duration = 2, button_type = 5, title = "¡Error!")

    if mode:
        if lang:
            event, values = mes_enc_eng.read()
        elif not lang:
            event, values = mes_enc_esp.read()
    elif not mode:
        if lang:
            event, values = mes_dec_eng.read()
        elif not lang:
            event, values = mes_dec_esp.read()

    pressed1, pressed2 = False, False

    if event == "enc":
        pressed1 = not pressed1
        try:
            if not values["input"]:
                if lang:
                    all_imports.pSG.popup_error("Cannot encrypt empty data.", title = "Error!")
                elif not lang:
                    all_imports.pSG.popup_error("No se pueden cifrar datos vacíos.", title = "¡Error!")
            if values["input"]:
                out_enc = all_imports.enc_dec.pgpy_encrypt(values["input"], "./Keys/v_public.asc")
                enc_message = open("./Messages/enc_message.txt", "w")
                enc_message.write(str(out_enc))
                enc_message.close()
                if lang:
                    mes_enc_eng["output"].update(value = out_enc)
                    mes_enc_eng.Element("enc").Update(("Encrypt", "Reset")[pressed1])
                    event, values = mes_enc_eng.read()
                elif not lang:
                    mes_enc_esp["output"].update(value = out_enc)
                    mes_enc_esp.Element("enc").Update(("Cifrar", "Reset")[pressed1])
                    event, values = mes_enc_esp.read()
            if mes_enc_eng[event].get_text() == "Reset" or mes_enc_esp[event].get_text() == "Reset":
                mes_enc_eng.close()
                mes_enc_esp.close()
        except ValueError:
            if lang:
                all_imports.pSG.popup_error("Expected: ASCII-armored PGP data, not a valid PGP Public key to encrypt.")
            if not lang:
                all_imports.pSG.popup_error("Expected: ASCII-armored PGP data, no hay clave pública PGP válida para "
                                            "cifrar.")
            mes_enc_eng.close()
            mes_enc_esp.close()
            break

    elif event == "dec":
        pressed2 = not pressed2
        try:
            if not values["input"]:
                if lang:
                    all_imports.pSG.popup_error("Cannot encrypt empty data.", title = "Error!")
                elif not lang:
                    all_imports.pSG.popup_error("No se pueden cifrar datos vacíos.", title = "¡Error!")
            if values["input"]:
                out_dec = all_imports.enc_dec.pgpy_decrypt(values["input"], "./Keys/private.asc")
                dec_message = open("./Messages/dec_message.txt", "w")
                dec_message.write(str(out_dec))
                dec_message.close()
                if lang:
                    mes_dec_eng["output"].update(value = out_dec)
                    mes_dec_eng.Element("dec").Update(("Decrypt", "Reset")[pressed2])
                    event, values = mes_dec_eng.read()
                elif not lang:
                    mes_dec_esp["output"].update(value = out_dec)
                    mes_dec_esp.Element("dec").Update(("Decrypt", "Reset")[pressed2])
                    event, values = mes_dec_esp.read()
        except ValueError:
            if lang:
                all_imports.pSG.popup_error("Expected: ASCII-armored PGP data, not a valid PGP Public key to encrypt.")
            if not lang:
                all_imports.pSG.popup_error("Expected: ASCII-armored PGP data, no hay clave pública PGP válida para "
                                            "cifrar.")
            mes_enc_eng.close()
            mes_enc_esp.close()
            break

        if mes_dec_eng[event].get_text() == "Reset" or mes_dec_esp[event].get_text() == "Reset":
            mes_dec_eng.close()
            mes_dec_esp.close()

    if event == 600:
        exit(0)

    if event == 800:
        mode = None
        mes_enc_eng.close()
        mes_dec_eng.close()
        mes_enc_esp.close()
        mes_dec_esp.close()
