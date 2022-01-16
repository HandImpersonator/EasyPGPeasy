# EZPZ-PGP.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports

empty1, empty2 = "", ""
expected_error = ""
event = None
lang = True
mode = None
pressed1, pressed2, pressed3, pressed4 = False, False, False, False
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

    if not (all_imports.os.path.exists(imported)):
        try:
            all_imports.os.mkdir(imported, access_rights)
        except OSError:
            if lang:
                all_imports.pSG.popup_auto_close("Creation of the directory %s failed." % imported,
                                                 auto_close_duration = 2, button_type = 5, title = "Error!", )
            elif not lang:
                all_imports.pSG.popup_auto_close("Ha fallado la creación del directorio %s." % imported,
                                                 auto_close_duration = 2, button_type = 5, title = "¡Error!")
    if not (all_imports.os.path.exists(keys)):
        try:
            all_imports.os.mkdir(keys, access_rights)
        except OSError:
            if lang:
                all_imports.pSG.popup_auto_close("Creation of the directory %s failed." % keys,
                                                 auto_close_duration = 2, button_type = 5, title = "Error!", )
            elif not lang:
                all_imports.pSG.popup_auto_close("Ha fallado la creación del directorio %s." % keys,
                                                 auto_close_duration = 2, button_type = 5, title = "¡Error!")
    if not (all_imports.os.path.exists(messages)):
        try:
            all_imports.os.mkdir(messages, access_rights)
        except OSError:
            if lang:
                all_imports.pSG.popup_auto_close("Creation of the directory %s failed." % messages,
                                                 auto_close_duration = 2, button_type = 5, title = "Error!", )
            elif not lang:
                all_imports.pSG.popup_auto_close("Ha fallado la creación del directorio %s." % messages,
                                                 auto_close_duration = 2, button_type = 5, title = "¡Error!")

    if mode == 10:
        if lang:
            event, values = mes_enc_eng.read()
        elif not lang:
            event, values = mes_enc_esp.read()
    elif mode == 20:
        if lang:
            event, values = mes_dec_eng.read()
        elif not lang:
            event, values = mes_dec_esp.read()
    elif mode == 30:
        choose_sig_eng, choose_sig_esp = all_imports.sign_choose_create.create_remove_sign()
        if lang and event != 50:
            event, values = choose_sig_eng.read()
        elif not lang and event != 50:
            event, values = choose_sig_esp.read()
        choose_sig_eng.close()
        choose_sig_esp.close()
        if event == 50:
            if lang:
                event, values = mes_sig_eng.read()
            elif not lang:
                event, values = mes_sig_esp.read()
            mes_sig_eng.close()
            mes_sig_esp.close()

        elif event == 60:
            if all_imports.os.path.isfile(keys + "/private.asc"):
                if all_imports.os.path.isfile(messages + "/encrypted_message.txt"):
                    all_imports.enc_dec.pgpy_sign(messages + "/encrypted_message.txt", keys + "/private.asc", messages)
                    if lang:
                        all_imports.pSG.popup_auto_close("Done!", auto_close_duration = 0.8,
                                                         button_type = 5)
                    elif not lang:
                        all_imports.pSG.popup_auto_close("¡Hecho!", auto_close_duration = 0.8,
                                                         button_type = 5)
                    choose_sig_eng.close()
                    choose_sig_esp.close()
                else:
                    all_imports.pSG.popup_error("No message to sign found in Messages folder.")
                mode = None
            else:
                no_priv_error_eng = ["Private key to sign message does not exist.", "Error!"]
                no_priv_error_esp = ["La clave privada para firmar el mensaje no existe.", "¡Error!"]
                if lang:
                    empty1 = no_priv_error_eng[0]
                    empty2 = no_priv_error_eng[1]
                elif not lang:
                    empty1 = no_priv_error_esp[0]
                    empty2 = no_priv_error_esp[1]
                all_imports.pSG.popup_error(empty1, title = empty2)
    elif mode == 40:
        if lang:
            event, values = mes_ver_eng.read()
        elif not lang:
            event, values = mes_ver_esp.read()

    if event == "xclipp":
        paste = all_imports.pyclip.paste(text = True).strip()
        toggle = False
        if lang:
            if mode == 10:
                mes_enc_eng["input"].update(value = paste)
                mes_enc_eng["xclipp"].update(visible = toggle)
                event, values = mes_enc_eng.read()
            if mode == 20:
                mes_dec_eng["input"].update(value = paste)
                mes_dec_eng["xclipp"].update(visible = toggle)
                event, values = mes_dec_eng.read()
            if mode == 30:
                mes_sig_eng["input"].update(value = paste)
                mes_sig_eng["xclipp"].update(visible = toggle)
                event, values = mes_sig_eng.read()
            if mode == 40:
                mes_ver_eng["input"].update(value = paste)
                mes_ver_eng["xclipp"].update(visible = toggle)
                event, values = mes_ver_eng.read()
        elif not lang:
            if mode == 10:
                mes_enc_esp["input"].update(value = paste)
                mes_enc_esp["xclipp"].update(visible = toggle)
                event, values = mes_enc_esp.read()
            if mode == 20:
                mes_dec_esp["input"].update(value = paste)
                mes_dec_esp["xclipp"].update(visible = toggle)
                event, values = mes_dec_esp.read()
            if mode == 30:
                mes_sig_esp["input"].update(value = paste)
                mes_sig_esp["xclipp"].update(visible = toggle)
                event, values = mes_sig_esp.read()
            if mode == 40:
                mes_ver_esp["input"].update(value = paste)
                mes_ver_esp["xclipp"].update(visible = toggle)
                event, values = mes_ver_esp.read()

    if event == "enc":
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
                    out_enc = all_imports.enc_dec.pgpy_encrypt(values["input"], imported + "/v_public.asc", messages)
                    update_button = ["Encrypt", "Cifrar"]
                    pressed1 = not pressed1
                    if lang:
                        mes_enc_eng["output"].update(value = str(out_enc))
                        mes_enc_eng.Element("enc").Update((update_button[0], "Reset")[pressed1])
                        event, values = mes_enc_eng.read()
                    elif not lang:
                        mes_enc_esp["output"].update(value = str(out_enc))
                        mes_enc_esp.Element("enc").Update((update_button[1], "Reset")[pressed1])
                        event, values = mes_enc_esp.read()
                    if event == "xclipc":
                        all_imports.pyclip.copy(str(out_enc))
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
            mode = None
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

    if event == "dec":
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
            if values["input"]:
                out_dec = all_imports.enc_dec.pgpy_decrypt(values["input"], keys + "/private.asc", messages)
                update_button = ["Decrypt", "Descifrar"]
                pressed2 = not pressed2
                if lang:
                    mes_dec_eng["output"].update(value = str(out_dec))
                    mes_dec_eng.Element("dec").Update((update_button[0], "Reset")[pressed2])
                    event, values = mes_dec_eng.read()
                elif not lang:
                    mes_dec_esp["output"].update(value = str(out_dec))
                    mes_dec_esp.Element("dec").Update((update_button[1], "Reset")[pressed2])
                    event, values = mes_dec_esp.read()
                if event == "xclipc":
                    all_imports.pyclip.copy(str(out_dec))
        except ValueError:
            if lang:
                all_imports.pSG.popup_error("Expected: ASCII-armored PGP data, not a valid PGP Public key to encrypt.")
            if not lang:
                all_imports.pSG.popup_error("Expected: ASCII-armored PGP data, no hay clave pública PGP válida para "
                                            "cifrar.")
            mes_enc_eng.close()
            mes_enc_esp.close()

        if event == 800:
            mes_sig_eng.close()
            mes_sig_esp.close()
            mode = None

        if mes_dec_eng[event].get_text() == "Reset" or mes_dec_esp[event].get_text() == "Reset":
            mes_dec_eng.close()
            mes_dec_esp.close()

    if event == "sig":
        try:
            if not values["input"]:
                empty_error_eng = ["Cannot sign empty data.", "Error!"]
                empty_error_esp = ["No se pueden firmar datos vacíos.", "¡Error!"]
                if lang:
                    empty1 = empty_error_eng[0]
                    empty2 = empty_error_eng[1]
                elif not lang:
                    empty1 = empty_error_esp[0]
                    empty2 = empty_error_esp[1]
                all_imports.pSG.popup_error(empty1, title = empty2)
                event = 50
                mes_sig_eng.close()
                mes_sig_esp.close()
            if values["input"]:
                if all_imports.os.path.isfile(keys + "/private.asc"):
                    out_sig = all_imports.enc_dec.pgpy_sign(values["input"], keys + "/private.asc", messages)
                    update_button = ["Sign", "Firmar"]
                    pressed3 = not pressed3
                    if lang:
                        mes_sig_eng["output"].update(value = str(out_sig))
                        mes_sig_eng.Element("sig").Update((update_button[0], "Reset")[pressed3])
                        event, values = mes_sig_eng.read()
                    elif not lang:
                        mes_sig_esp["output"].update(value = str(out_sig))
                        mes_sig_esp.Element("sig").Update((update_button[1], "Reset")[pressed3])
                        event, values = mes_sig_esp.read()
                    if event == "xclipc":
                        all_imports.pyclip.copy(str(out_sig))
                else:
                    no_pub_error_eng = ["Private key to sign message does not exist.", "Error!"]
                    no_pub_error_esp = ["La clave privada para firmar el mensaje no existe.", "¡Error!"]
                    if lang:
                        empty1 = no_pub_error_eng[0]
                        empty2 = no_pub_error_eng[1]
                    elif not lang:
                        empty1 = no_pub_error_esp[0]
                        empty2 = no_pub_error_esp[1]
                    all_imports.pSG.popup_error(empty1, title = empty2)
                    mode = None
                    mes_sig_eng.close()
                    mes_sig_esp.close()
            if mes_sig_eng[event].get_text() == "Reset" or mes_sig_esp[event].get_text() == "Reset":
                mes_sig_eng.close()
                mes_sig_esp.close()
                event = 50
        except ValueError:
            expected_error_eng = ["Expected: ASCII-armored PGP data, not a valid PGP Public key to encrypt.", "Error!"]
            expected_error_esp = ["Expected: ASCII-armored PGP data, no hay clave pública PGP válida para "
                                  "cifrar.", "¡Error!"]
            if lang:
                all_imports.pSG.popup_error(expected_error_eng[0], title = expected_error_eng[1])
            if not lang:
                all_imports.pSG.popup_error(expected_error_esp[0], title = expected_error_esp[1])
            mes_sig_eng.close()
            mes_sig_esp.close()

        if event == 800:
            mes_sig_eng.close()
            mes_sig_esp.close()
            mode = None

        if mes_dec_eng[event].get_text() == "Reset" or mes_dec_esp[event].get_text() == "Reset":
            mes_dec_eng.close()
            mes_dec_esp.close()

    if event == "ver":
        try:
            if not values["input"]:
                empty_error_eng = ["Cannot verify empty data.", "Error!"]
                empty_error_esp = ["No se pueden verificar datos vacíos.", "¡Error!"]
                if lang:
                    empty1 = empty_error_eng[0]
                    empty2 = empty_error_eng[1]
                elif not lang:
                    empty1 = empty_error_esp[0]
                    empty2 = empty_error_esp[1]
                all_imports.pSG.popup_error(empty1, title = empty2)
            elif values["input"]:
                if all_imports.os.path.isfile(imported + "/v_public.asc"):
                    out_ver = all_imports.enc_dec.pgpy_verify(values["input"], imported + "/v_signed_message.txt",
                                                              imported + "/v_public.asc", messages)
                    update_button = ["Verify", "Verificar"]
                    pressed4 = not pressed4
                    if lang:
                        mes_ver_eng["output"].update(value = str(out_ver))
                        mes_ver_eng.Element("ver").Update((update_button[0], "Reset")[pressed4])
                        event, values = mes_sig_eng.read()
                    elif not lang:
                        mes_ver_esp["output"].update(value = str(out_ver))
                        mes_ver_esp.Element("ver").Update((update_button[1], "Reset")[pressed4])
                        event, values = mes_ver_esp.read()
                    if event == "xclipc":
                        all_imports.pyclip.copy(str(out_ver))
                else:
                    no_pub_error_eng = ["Public key to verify message does not exist.", "Error!"]
                    no_pub_error_esp = ["La clave pública para verificar el mensaje no existe.", "¡Error!"]
                    if lang:
                        empty1 = no_pub_error_eng[0]
                        empty2 = no_pub_error_eng[1]
                    elif not lang:
                        empty1 = no_pub_error_esp[0]
                        empty2 = no_pub_error_esp[1]
                    all_imports.pSG.popup_error(empty1, title = empty2)
            mes_ver_eng.close()
            mes_ver_esp.close()
        except ValueError:
            if lang:
                expected_error = ["Expected: ASCII-armored PGP data, not a valid PGP Public key to encrypt.", "Error!"]
            elif not lang:
                expected_error = ["Expected: ASCII-armored PGP data, no hay clave pública PGP válida para "
                                  "cifrar.", "¡Error!"]
            all_imports.pSG.popup_error(expected_error[0], title = expected_error[1])
            mes_ver_eng.close()
            mes_ver_esp.close()

        if event == 800:
            mes_sig_eng.close()
            mes_sig_esp.close()
            mode = None

        if mes_dec_eng[event].get_text() == "Reset" or mes_dec_esp[event].get_text() == "Reset":
            mes_dec_eng.close()
            mes_dec_esp.close()

    if event == 600:
        exit(0)

    if event == 800:
        mode = None
        mes_enc_eng.close()
        mes_dec_eng.close()
        mes_sig_eng.close()
        mes_ver_eng.close()
        mes_enc_esp.close()
        mes_dec_esp.close()
        mes_sig_esp.close()
        mes_ver_esp.close()
