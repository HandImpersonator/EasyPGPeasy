# EZPZ-PGP.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports

empty1, empty2, = "", ""
event = None
lang = True
mode = None
values = {}

curr_path = all_imports.os.getcwd()
access_rights = 0o755
imported = curr_path + "/src/Imported"
keys = curr_path + "/src/Keys"
messages = curr_path + "/src/Messages"

while True:

    while mode is None:
        lang, mode = all_imports.menu.create_menu(lang, imported, keys)

    mes_enc_eng, mes_enc_esp, mes_dec_eng, mes_dec_esp, mes_sig_eng, mes_sig_esp, mes_ver_eng, mes_ver_esp = \
        all_imports.enc_dec_create.create_remove_enc_dec()

    try:
        if not (all_imports.os.path.exists(imported)) or not (all_imports.os.path.exists(keys)) or not (
                all_imports.os.path.exists(messages)):
            all_imports.os.mkdir(imported, access_rights)
            all_imports.os.mkdir(keys, access_rights)
            all_imports.os.mkdir(messages, access_rights)
    except OSError:
        if lang:
            all_imports.pSG.popup_auto_close("Creation of the directory %s failed." % imported, auto_close_duration = 2,
                                             button_type = 5, title = "Error!", )
            all_imports.pSG.popup_auto_close("Creation of the directory %s failed." % keys, auto_close_duration = 2,
                                             button_type = 5, title = "Error!", )
            all_imports.pSG.popup_auto_close("Creation of the directory %s failed." % messages, auto_close_duration = 2,
                                             button_type = 5, title = "Error!")
        elif not lang:
            all_imports.pSG.popup_auto_close("Ha fallado la creación del directorio %s." % imported,
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
                empty_error_eng = ["Cannot encrypt empty data.", "Error!"]
                empty_error_esp = ["No se pueden cifrar datos vacíos.", "¡Error!"]
                if lang:
                    empty1 = empty_error_eng[0]
                    empty2 = empty_error_eng[1]
                elif not lang:
                    empty1 = empty_error_esp[0]
                    empty2 = empty_error_esp[1]
                all_imports.pSG.popup_error(empty1, title = empty2)
            elif values["input"]:
                if all_imports.os.path.isfile(imported + "/v_public.asc"):
                    out_enc = all_imports.enc_dec.pgpy_encrypt(values["input"], imported + "/v_public.asc")
                    if out_enc == "Private":
                        mes_enc_eng["output"].update(value = "Error. Provided key to encrypt was a private key, "
                                                             "try importing the public key again.")
                        mes_enc_eng.Element("enc").Update(("Encrypt", "Reset")[pressed1])
                        event, values = mes_enc_eng.read()
                    else:
                        enc_message = open(messages + "/enc_message.txt", "w")
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
                else:
                    no_pub_error_eng = ["Public key to encrypt message does not exist.", "Error!"]
                    no_pub_error_esp = ["La clave pública para cifrar el mensaje no existe.", "¡Error!"]
                    if lang:
                        empty1 = no_pub_error_eng[0]
                        empty2 = no_pub_error_eng[1]
                    elif not lang:
                        empty1 = no_pub_error_esp[0]
                        empty2 = no_pub_error_esp[1]
                    all_imports.pSG.popup_error(empty1, title = empty2)
            mes_enc_eng.close()
            mes_enc_esp.close()
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
                out_dec = all_imports.enc_dec.pgpy_decrypt(values["input"], keys + "/private.asc")
                dec_message = open(messages + "/dec_message.txt", "w")
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
