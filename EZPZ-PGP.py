# EZPZ-PGP.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports


"""Creates the menu window and makes all the encryption, decryption, signing and verification process, automating
file saving and file reading, copying/pasting to/from clipboard."""

access_rights = 0o755
copied, error1, error2, fin, paste = "", "", "", "", ""
curr_path = all_imports.os.getcwd()
event, lang, mode = None, True, None
imported = curr_path + "/src/Imported"
keys = curr_path + "/src/Keys"
messages = curr_path + "/src/Messages"
pressed1, pressed2, pressed3, pressed4 = False, False, False, False
values = {}

while True:

    while mode is None:
        lang, mode = all_imports.menu.create_menu(lang, imported, keys)

    mes_enc_eng, mes_enc_esp, mes_dec_eng, mes_dec_esp, mes_sig_eng, mes_sig_esp, mes_ver_eng, mes_ver_esp = \
        all_imports.enc_dec_create.create_remove_enc_dec()

    if not (all_imports.os.path.exists(imported)):
        try:
            all_imports.os.mkdir(imported, access_rights)
        except OSError:
            folder_error_eng = ["Creation of the directory %s failed." % imported, "Error!"]
            folder_error_esp = ["Ha fallado la creación del directorio %s." % imported, "¡Error!"]
            if lang:
                error1 = folder_error_eng[0]
                error2 = folder_error_eng[1]
            elif not lang:
                error1 = folder_error_esp[0]
                error2 = folder_error_esp[1]
            all_imports.pSG.popup_auto_close(error1, auto_close_duration = 2, button_type = 5, title = error2)

    if not (all_imports.os.path.exists(keys)):
        try:
            all_imports.os.mkdir(keys, access_rights)
        except OSError:
            folder_error_eng = ["Creation of the directory %s failed." % keys, "Error!"]
            folder_error_esp = ["Ha fallado la creación del directorio %s. " % keys, "¡Error!"]
            if lang:
                error1 = folder_error_eng[0]
                error2 = folder_error_eng[1]
            elif not lang:
                error1 = folder_error_esp[0]
                error2 = folder_error_esp[1]
            all_imports.pSG.popup_auto_close(error1, auto_close_duration = 2, button_type = 5, title = error2)

    if not (all_imports.os.path.exists(messages)):
        try:
            all_imports.os.mkdir(messages, access_rights)
        except OSError:
            folder_error_eng = ["Creation of the directory %s failed." % messages, "Error!"]
            folder_error_esp = ["Ha fallado la creación del directorio %s." % messages, "¡Error!"]
            if lang:
                error1 = folder_error_eng[0]
                error2 = folder_error_eng[1]
            elif not lang:
                error1 = folder_error_esp[0]
                error2 = folder_error_esp[1]
            all_imports.pSG.popup_auto_close(error1, auto_close_duration = 2, button_type = 5, title = error2)

    if mode == 15:
        pressed1 = False
        if lang:
            event, values = mes_enc_eng.read()
        elif not lang:
            event, values = mes_enc_esp.read()
    elif mode == 20:
        pressed2 = False
        choose_dec_eng, choose_dec_esp = all_imports.decrypt_choose_create.create_remove_choose_decrypt()
        if lang and event != [70, 80]:
            event, values = choose_dec_eng.read()
        elif not lang and event != [70, 80]:
            event, values = choose_dec_esp.read()
        choose_dec_eng.close()
        choose_dec_esp.close()
        if event == 70:
            if lang:
                event, values = mes_dec_eng.read()
            elif not lang:
                event, values = mes_dec_esp.read()
        elif event == 80:
            if all_imports.os.path.isfile(keys + "/private.asc"):
                if all_imports.os.path.isfile(imported + "/v_imported_message.txt"):
                    all_imports.enc_dec.pgpy_decrypt(imported + "/v_imported_message.txt", keys + "/private.asc", lang,
                                                     messages)
                    if lang:
                        fin = "Done!"
                    elif not lang:
                        fin = "¡Hecho!"
                    all_imports.pSG.popup_auto_close(fin, auto_close_duration = 0.8, button_type = 5, title = fin)
                else:
                    no_mes_eng = ["No message to decrypt found in Imported folder.", "Returning to menu.", "Error!"]
                    no_mes_esp = ["No existe un mensaje descifrar en la carpeta Imported.", "Volviendo al menú",
                                  "¡Error!"]
                    if lang:
                        error1 = no_mes_eng[0] + "\n" + no_mes_eng[1]
                        error2 = no_mes_eng[2]
                    elif not lang:
                        error1 = no_mes_esp[0] + "\n" + no_mes_esp[1]
                        error2 = no_mes_esp[2]
                    all_imports.pSG.popup_error(error1, title = error2)
            else:
                no_priv_eng = ["Private key to decrypt message does not exist.", "Returning to menu.", "Error!"]
                no_priv_esp = ["La clave privada para descifrar el mensaje no existe.", "Volviendo al menú.", "¡Error!"]
                if lang:
                    error1 = no_priv_eng[0] + "\n" + no_priv_eng[1]
                    error2 = no_priv_eng[2]
                elif not lang:
                    error1 = no_priv_esp[0] + "\n" + no_priv_esp[1]
                    error2 = no_priv_esp[2]
                all_imports.pSG.popup_error(error1, title = error2)
            mode = None
    elif mode == 30:
        pressed3 = False
        choose_sig_eng, choose_sig_esp = all_imports.sign_choose_create.create_remove_sign()
        if lang and event != [50, 60]:
            event, values = choose_sig_eng.read()
        elif not lang and event != [50, 60]:
            event, values = choose_sig_esp.read()
        choose_sig_eng.close()
        choose_sig_esp.close()
        if event == 50:
            if lang:
                event, values = mes_sig_eng.read()
            elif not lang:
                event, values = mes_sig_esp.read()
        elif event == 60:
            if all_imports.os.path.isfile(keys + "/private.asc"):
                if all_imports.os.path.isfile(messages + "/encrypted_message.txt"):
                    all_imports.enc_dec.pgpy_sign(messages + "/encrypted_message.txt", keys + "/private.asc", lang,
                                                  messages)
                    if lang:
                        fin = "Done!"
                    elif not lang:
                        fin = "¡Hecho!"
                    all_imports.pSG.popup_auto_close(fin, auto_close_duration = 0.8, button_type = 5, title = fin)
                else:
                    no_mes_eng = ["No message to sign found in Messages folder.", "Returning to menu.", "Error!"]
                    no_mes_esp = ["No existe un mensaque firmar en la carpeta Messages.", "Volviendo al menú.",
                                  "¡Error!"]
                    if lang:
                        error1 = no_mes_eng[0] + "\n" + no_mes_eng[1]
                        error2 = no_mes_eng[2]
                    elif not lang:
                        error1 = no_mes_esp[0] + "\n" + no_mes_esp[1]
                        error2 = no_mes_esp[2]
                    all_imports.pSG.popup_error(error1, title = error2)
            else:
                no_priv_eng = ["Private key to sign message does not exist.", "Returning to menu.", "Error!"]
                no_priv_esp = ["La clave privada para firmar el mensaje no existe.", "Volviendo al menú.",
                               "¡Error!"]
                if lang:
                    error1 = no_priv_eng[0] + "\n" + no_priv_eng[1]
                    error2 = no_priv_eng[2]
                elif not lang:
                    error1 = no_priv_esp[0] + "\n" + no_priv_esp[1]
                    error2 = no_priv_esp[2]
                all_imports.pSG.popup_error(error1, title = error2)
            mode = None
    elif mode == 40:  # Still has to be checked.
        try:
            if all_imports.os.path.isfile(imported + "/v_imported_message.txt"):
                if all_imports.os.path.isfile(imported + "/v_imported_public.asc"):
                    if all_imports.os.path.isfile(imported + "/v_imported_signature.txt"):
                        mes = imported + "/v_imported_message.txt"
                        key = imported + "/v_imported_public.asc"
                        sig = imported + "/v_imported_signature.txt"
                        out_ver, done = all_imports.enc_dec.pgpy_verify(mes, key, lang, imported, sig)
                        if lang:
                            fin = "Done!"
                        elif not lang:
                            fin = "¡Hecho!"
                        all_imports.pSG.popup_auto_close(fin, auto_close_duration = 0.8, button_type = 5, title = fin)
                    else:
                        no_sig_eng = ["Signature to verify message is not imported.", "Returning to menu.",
                                      "Error!"]
                        no_sig_esp = ["La firma para verificar el mensaje no está importado.", "Volviendo al menú.",
                                      "Error!"]
                        if lang:
                            error1 = no_sig_eng[0] + "\n" + no_sig_eng[1]
                            error2 = no_sig_eng[2]
                        elif not lang:
                            error1 = no_sig_esp[0] + "\n" + no_sig_esp[1]
                            error2 = no_sig_esp[2]
                        all_imports.pSG.popup_error(error1, title = error2)
                else:
                    no_pub_eng = ["Public key to verify message is not imported.", "Returning to menu.", "Error!"]
                    no_pub_esp = ["La clave pública para verificar el mensaje no está importado.", "Volviendo al menú.",
                                  "¡Error!"]
                    if lang:
                        error1 = no_pub_eng[0] + "\n" + no_pub_eng[1]
                        error2 = no_pub_eng[2]
                    elif not lang:
                        error1 = no_pub_esp[0] + "\n" + no_pub_esp[1]
                        error2 = no_pub_esp[2]
                    all_imports.pSG.popup_error(error1, title = error2)
            else:
                no_pub_eng = ["Message to be verified is not imported.", "Returning to menu.", "Error!"]
                no_pub_esp = ["El mensaje a verificar no está importade.", "Volviendo al menú.",
                              "¡Error!"]
                if lang:
                    error1 = no_pub_eng[0] + "\n" + no_pub_eng[1]
                    error2 = no_pub_eng[2]
                elif not lang:
                    error1 = no_pub_esp[0] + "\n" + no_pub_esp[1]
                    error2 = no_pub_esp[2]
                all_imports.pSG.popup_error(error1, title = error2)
            mode = None
            if event == 800:
                mode = None
            if mes_ver_eng[event].GetText() == "Reset" or mes_ver_esp[event].GetText() == "Reset":
                mode = 20
            if event == 600:
                exit(0)
        except ValueError:
            error_ver_eng = ["Expected: ASCII-armored PGP data, not a valid PGP Public key to verify.",
                             "Returning to menu.", "Verify error!"]
            error_ver_esp = ["Expected: ASCII-armored PGP data, no hay clave PGP Pública válida para verificar",
                             "Volviendo al menú.", "¡Error verificando!"]
            if lang:
                error1 = error_ver_eng[0] + "\n" + error_ver_eng[1]
                error2 = error_ver_eng[2]
            if not lang:
                error1 = error_ver_eng[0] + "\n" + error_ver_eng[1]
                error2 = error_ver_eng[2]
            all_imports.pSG.popup_error(error1, title = error2)
            mode = None
            mes_ver_eng.close()
            mes_ver_esp.close()

    if event == "xclipp":
        try:
            paste = str(all_imports.pyclip.paste(text = True).strip())
        except BaseException:
            if lang:
                paste = "Clipboard was empty, here you go."
            elif not lang:
                paste = "El portapapeles estaba vacío, aquí tienes."
        toggle = False
        if lang:
            if mode == 15:
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
        elif not lang:
            if mode == 15:
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

    if event == "enc":
        if not values["input"].strip():
            empty_eng = ["Cannot encrypt empty data.", "Error!"]
            empty_esp = ["No se pueden cifrar datos vacíos.", "¡Error!"]
            if lang:
                error1 = empty_eng[0]
                error2 = empty_eng[1]
            elif not lang:
                error1 = empty_esp[0]
                error2 = empty_esp[1]
            all_imports.pSG.popup_error(error1, title = error2)
            mes_enc_eng.close()
            mes_enc_esp.close()
        try:
            if values["input"].strip():
                if all_imports.os.path.isfile(imported + "/v_imported_public.asc"):
                    out_enc, done = all_imports.enc_dec.pgpy_encrypt(values["input"].strip(),
                                                                     imported + "/v_imported_public.asc",
                                                                     lang, messages)
                    update_button = ["Encrypt", "Cifrar"]
                    pressed1 = True
                    if done:
                        if lang:
                            mes_enc_eng["output"].update(value = str(out_enc))
                            mes_enc_eng["xclipc"].update(visible = True)
                            mes_enc_eng["xclipp"].update(visible = False)
                            mes_enc_eng.Element("enc").Update((update_button[0], "Reset")[pressed1])
                            event, values = mes_enc_eng.read()
                        elif not lang:
                            mes_enc_esp["output"].update(value = str(out_enc))
                            mes_enc_esp["xclipc"].update(visible = True)
                            mes_enc_esp["xclipp"].update(visible = False)
                            mes_enc_esp.Element("enc").Update((update_button[1], "Reset")[pressed1])
                            event, values = mes_enc_esp.read()
                        if event == "xclipc":
                            all_imports.pyclip.copy(str(out_enc))
                            if lang:
                                fin = "Done!"
                            elif not lang:
                                fin = "¡Hecho!"
                            all_imports.pSG.popup_auto_close(fin, auto_close_duration = 0.8, button_type = 5,
                                                             title = fin)
                else:
                    no_pub_eng = ["Public key to encrypt message does not exist.", "Returning to menu", "Error!"]
                    no_pub_esp = ["La clave pública para cifrar el mensaje no existe.", "Volviendo al menu", "¡Error!"]
                    if lang:
                        error1 = no_pub_eng[0] + "\n" + no_pub_eng[1]
                        error2 = no_pub_eng[2]
                    elif not lang:
                        error1 = no_pub_esp[0] + "\n" + no_pub_esp[1]
                        error2 = no_pub_esp[2]
                    all_imports.pSG.popup_error(error1, title = error2)
                mode = None
            if event == 800:
                mode = None
            if mes_enc_eng[event].GetText() == "Reset" or mes_enc_esp[event].GetText() == "Reset":
                mode = 15
            if event == 600:
                exit(0)
        except ValueError:
            error_enc_eng = ["Expected: ASCII-armored PGP data, not a valid PGP Public key to encrypt.",
                             "Returning to menu.", "Encrypt error!"]
            error_enc_esp = ["Expected: ASCII-armored PGP data, no hay clave PGP Pública válida para cifrar.",
                             "Volviendo al menú.", "¡Error cifrando!"]
            if lang:
                error1 = error_enc_eng[0] + "\n" + error_enc_eng[1]
                error2 = error_enc_eng[2]
            if not lang:
                error1 = error_enc_esp[0] + "\n" + error_enc_esp[1]
                error2 = error_enc_esp[2]
            all_imports.pSG.popup_error(error1, title = error2)
            mode = None
        mes_enc_eng.close()
        mes_enc_esp.close()

    if event == "dec":
        if not values["input"].strip():
            empty_error_eng = ["Cannot decrypt empty data.", "Error!"]
            empty_error_esp = ["No se pueden descifrar datos vacíos.", "¡Error!"]
            if lang:
                error1 = empty_error_eng[0]
                error2 = empty_error_eng[1]
            elif not lang:
                error1 = empty_error_esp[0]
                error2 = empty_error_esp[1]
            all_imports.pSG.popup_error(error1, title = error2)
            mes_dec_eng.close()
            mes_dec_esp.close()
        try:
            if values["input"].strip():
                if all_imports.os.path.isfile(keys + "/private.asc"):
                    out_dec, done = all_imports.enc_dec.pgpy_decrypt(values["input"].strip(), keys + "/private.asc",
                                                                     lang, messages)
                    update_button = ["Decrypt", "Descifrar"]
                    pressed1 = True
                    if done:
                        if lang:
                            mes_dec_eng["output"].update(value = str(out_dec))
                            mes_dec_eng["xclipc"].update(visible = True)
                            mes_dec_eng["xclipp"].update(visible = False)
                            mes_dec_eng.Element("enc").Update((update_button[0], "Reset")[pressed2])
                            event, values = mes_dec_eng.read()
                        elif not lang:
                            mes_dec_esp["output"].update(value = str(out_dec))
                            mes_dec_esp["xclipc"].update(visible = True)
                            mes_dec_esp["xclipp"].update(visible = False)
                            mes_dec_esp.Element("enc").Update((update_button[1], "Reset")[pressed2])
                            event, values = mes_dec_esp.read()
                        if event == "xclipc":
                            all_imports.pyclip.copy(str(out_dec))
                            if lang:
                                fin = "Done!"
                            elif not lang:
                                fin = "¡Hecho!"
                            all_imports.pSG.popup_auto_close(fin, auto_close_duration = 0.8, button_type = 5,
                                                             title = fin)
                else:
                    no_pub_eng = ["Private key to decrypt message does not exist.", "Returning to menu", "Error!"]
                    no_pub_esp = ["La clave privada para descifrar el mensaje no existe.", "Volviendo al menu",
                                  "¡Error!"]
                    if lang:
                        error1 = no_pub_eng[0] + "\n" + no_pub_eng[1]
                        error2 = no_pub_eng[2]
                    elif not lang:
                        error1 = no_pub_esp[0] + "\n" + no_pub_esp[1]
                        error2 = no_pub_esp[2]
                    all_imports.pSG.popup_error(error1, title = error2)
                mode = None
            if event == 800:
                mode = None
            if mes_dec_eng[event].GetText() == "Reset" or mes_dec_esp[event].GetText() == "Reset":
                mode = 15
            if event == 600:
                exit(0)
        except ValueError:
            error_dec_eng = ["Expected: ASCII-armored PGP data, not a valid PGP Private key to decrypt.",
                             "Returning to menu.", "Decrypt error!"]
            error_dec_esp = ["Expected: ASCII-armored PGP data, no hay clave PGP Privada válida para descifrar.",
                             "Volviendo al menú.", "¡Error descifrando!"]
            if lang:
                error1 = error_dec_eng[0] + "\n" + error_dec_eng[1]
                error2 = error_dec_eng[2]
            if not lang:
                error1 = error_dec_esp[0] + "\n" + error_dec_esp[1]
                error2 = error_dec_esp[2]
            all_imports.pSG.popup_error(error1, title = error2)
            mode = None
        mes_dec_eng.close()
        mes_dec_esp.close()

    if event == "sig":
        if not values["input"].strip():
            empty_error_eng = ["Cannot sign empty data.", "Error!"]
            empty_error_esp = ["No se pueden firmar datos vacíos.", "¡Error!"]
            if lang:
                error1 = empty_error_eng[0]
                error2 = empty_error_eng[1]
            elif not lang:
                error1 = empty_error_esp[0]
                error2 = empty_error_esp[1]
            all_imports.pSG.popup_error(error1, title = error2)
            mes_sig_eng.close()
            mes_sig_esp.close()
        try:
            if values["input"].strip():
                if all_imports.os.path.isfile(keys + "/private.asc"):
                    out_sig, done = all_imports.enc_dec.pgpy_sign(values["input"].strip(), keys + "/private.asc", lang,
                                                                  messages)
                    update_button = ["Sign", "Firmar"]
                    pressed3 = True
                    if done:
                        if lang:
                            mes_sig_eng["output"].update(value = str(out_sig))
                            mes_sig_eng["xclipc"].update(visible = True)
                            mes_sig_eng["xclipp"].update(visible = False)
                            mes_sig_eng.Element("sig").Update((update_button[0], "Reset")[pressed3])
                            event, values = mes_sig_eng.read()
                        if not lang:
                            mes_sig_esp["output"].update(value = str(out_sig))
                            mes_sig_esp["xclipc"].update(visible = True)
                            mes_sig_esp["xclipp"].update(visible = False)
                            mes_sig_esp.Element("sig").Update((update_button[1], "Reset")[pressed3])
                            event, values = mes_sig_esp.read()
                        if event == "xclipc":
                            all_imports.pyclip.copy(str(out_sig))
                            if lang:
                                fin = "Done!"
                            elif not lang:
                                fin = "¡Hecho!"
                            all_imports.pSG.popup_auto_close(fin, auto_close_duration = 0.8, button_type = 5,
                                                             title = fin)
                else:
                    no_priv_eng = ["Private key to sign message does not exist.", "Returning to menu",
                                   "Error!"]
                    no_priv_esp = ["La clave privada para firmar el mensaje no existe.", "Volviendo al menu",
                                   "¡Error!"]
                    if lang:
                        error1 = no_priv_eng[0] + "\n" + no_priv_eng[1]
                        error2 = no_priv_eng[2]
                    elif not lang:
                        error1 = no_priv_esp[0] + "\n" + no_priv_esp[1]
                        error2 = no_priv_esp[2]
                    all_imports.pSG.popup_error(error1, title = error2)
                mode = None
            if event == 800:
                mode = None
            if mes_sig_eng[event].GetText() == "Reset" or mes_sig_esp[event].GetText() == "Reset":
                mode = 15
            if event == 600:
                exit(0)
        except ValueError:
            error_sig_eng = ["Expected: ASCII-armored PGP data, not a valid PGP Private key to sign.",
                             "Returning to menu.", "Sign error!"]
            error_sig_esp = ["Expected: ASCII-armored PGP data, no hay clave PGP Privada válida para firmar.",
                             "Volviendo al menú.", "¡Error firmando!"]
            if lang:
                error1 = error_sig_eng[0] + "\n" + error_sig_eng[1]
                error2 = error_sig_eng[2]
            if not lang:
                error1 = error_sig_esp[0] + "\n" + error_sig_esp[1]
                error2 = error_sig_esp[2]
            all_imports.pSG.popup_error(error1, title = error2)
            mode = None
        mes_sig_eng.close()
        mes_sig_esp.close()

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
