# dec.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imp


def df(dec, event, keys, lang, mes_dec_eng, mes_dec_esp, values):
    """Function that handles the decryption process.
    Returns events, mode choice and values if there were any typed in."""

    error1, error2, fin, mode, out_dec = "", "", "", "", ""

    if not values["input"].strip():
        empty_error_eng = ["Cannot decrypt empty data.", "Returning to menu.", "Error decrypting!"]
        empty_error_esp = ["No se pueden descifrar datos vacíos.", "Volviendo al menú.", "¡Error descifrando!"]
        if lang == "eng":
            error1 = empty_error_eng[0] + "\n" + empty_error_eng[1]
            error2 = empty_error_eng[2]
        elif lang == "esp":
            error1 = empty_error_esp[0] + "\n" + empty_error_esp[1]
            error2 = empty_error_esp[2]
        all_imp.pSG.popup_error(error1, title = error2)
        mes_dec_eng.close()
        mes_dec_esp.close()
    elif values["input"].strip():
        if all_imp.os.path.isfile(keys + "/private.asc"):
            try:
                out_dec, fin = all_imp.edsv.pgpy_decrypt(values["input"].strip(), False, keys + "/private.asc", lang,
                                                         dec)
            except all_imp.pgpy.errors.PGPDecryptionError:
                error_pass_eng = ["The passphrase is incorrect.", "Returning to menu.", "Error decrypting!"]
                error_pass_esp = ["La contraseña es incorrecta.", "Volviendo al menú.", "¡Error descifrando!"]
                if lang == "eng":
                    error1 = error_pass_eng[0] + "\n" + error_pass_eng[1]
                    error2 = error_pass_eng[2]
                elif lang == "esp":
                    error1 = error_pass_esp[0] + "\n" + error_pass_esp[1]
                    error2 = error_pass_esp[2]
                all_imp.pSG.popup_error(error1, title = error2)
                mes_dec_eng.close()
                mes_dec_esp.close()
            except TypeError:
                pass
            update_button = ["Decrypt", "Descifrar"]
            pressed = True
            if fin:
                if lang == "eng":
                    mes_dec_eng["output"].update(value = str(out_dec))
                    mes_dec_eng["xclipp"].update(visible = False)
                    mes_dec_eng.Element("dec").Update((update_button[0], "Reset")[pressed])
                    mes_dec_eng.refresh()
                    all_imp.pSG.popup_auto_close(fin, auto_close_duration = 1, button_type = 5, title = fin)
                    event, values = mes_dec_eng.read()
                    mes_dec_eng.close()
                elif lang == "esp":
                    mes_dec_esp["output"].update(value = str(out_dec))
                    mes_dec_esp["xclipp"].update(visible = False)
                    mes_dec_esp.Element("dec").Update((update_button[1], "Reset")[pressed])
                    mes_dec_esp.refresh()
                    all_imp.pSG.popup_auto_close(fin, auto_close_duration = 1, button_type = 5, title = fin)
                    event, values = mes_dec_esp.read()
                    mes_dec_esp.close()

            mes_dec_eng.close()
            mes_dec_esp.close()
        else:
            no_priv_eng = ["Private key to decrypt message does not exist.", "Returning to menu.", "Error decrypting!"]
            no_priv_esp = ["La clave privada para descifrar el mensaje no existe.", "Volviendo al menú.",
                           "¡Error descifrando!"]
            if lang == "eng":
                error1 = no_priv_eng[0] + "\n" + no_priv_eng[1]
                error2 = no_priv_eng[2]
            elif lang == "esp":
                error1 = no_priv_esp[0] + "\n" + no_priv_esp[1]
                error2 = no_priv_esp[2]
            all_imp.pSG.popup_error(error1, title = error2)
            mes_dec_eng.close()
            mes_dec_esp.close()
    mode = None
    if event == 800:
        mode = None
        mes_dec_eng.close()
        mes_dec_esp.close()
    if mes_dec_eng[event].GetText() == "Reset" or mes_dec_esp[event].GetText() == "Reset":
        event = 24
        mode = 20
    if event == 600:
        all_imp.sys.exit(0)

    return event, mode, values


def dm(dec, event, imported, keys, lang, mes_dec_eng, mes_dec_esp):
    """Function that allows to choose the decryption mode.
    Returns events, mode choice and values if there were any typed in."""

    error1, error2, fin, mode, paste, window_title, values = "", "", "", "", "", "", ""

    choose_dec_eng, choose_dec_esp = all_imp.choose_layout.crem_decrypt()
    if lang == "eng" and event not in [24, 25, 26]:
        event, values = choose_dec_eng.read()
        choose_dec_eng.close()
    elif lang == "esp" and event not in [24, 25, 26]:
        event, values = choose_dec_esp.read()
        choose_dec_esp.close()

    if event == 24:
        if all_imp.os.path.isfile(keys + "/private.asc"):
            if lang == "eng":
                event, values = mes_dec_eng.read()
            elif lang == "esp":
                event, values = mes_dec_esp.read()

            # Paste from clipboard.
            if event == "xclipp":
                try:
                    paste = str(all_imp.pyclip.paste(text = True).strip())
                except BaseException:
                    if lang == "eng":
                        paste = "Clipboard was empty, here you go."
                    elif lang == "esp":
                        paste = "El portapapeles estaba vacío, aquí tienes."
                toggle = False

                # Update window with pasted content.
                if lang == "eng":
                    mes_dec_eng["input"].update(value = paste)
                    mes_dec_eng["xclipp"].update(visible = toggle)
                    event, values = mes_dec_eng.read()
                elif lang == "esp":
                    mes_dec_esp["input"].update(value = paste)
                    mes_dec_esp["xclipp"].update(visible = toggle)
                    event, values = mes_dec_esp.read()
        else:
            no_priv_eng = ["Private key to decrypt message does not exist.", "Returning to menu.", "Error decrypting!"]
            no_priv_esp = ["La clave privada para descifrar el mensaje no existe.", "Volviendo al menú.",
                           "¡Error descifrando!"]
            if lang == "eng":
                error1 = no_priv_eng[0] + "\n" + no_priv_eng[1]
                error2 = no_priv_eng[2]
            elif lang == "esp":
                error1 = no_priv_esp[0] + "\n" + no_priv_esp[1]
                error2 = no_priv_esp[2]
            all_imp.pSG.popup_error(error1, title = error2)
            event = None
        mode = None
        if event == 800:
            mes_dec_eng.close()
            mes_dec_esp.close()
        if event == 600:
            all_imp.sys.exit(0)

    elif event == 25:
        if all_imp.os.path.isfile(keys + "/private.asc"):
            if all_imp.os.path.isfile(imported + "/v_imported_message.txt"):
                try:
                    _, fin = all_imp.edsv.pgpy_decrypt(imported + "/v_imported_message.txt", False,
                                                       keys + "/private.asc", lang, dec)
                except all_imp.pgpy.errors.PGPDecryptionError:
                    error_pass_eng = ["The passphrase is incorrect.", "Returning to menu.", "Error decrypting!"]
                    error_pass_esp = ["La contraseña es incorrecta.", "Volviendo al menú.", "¡Error descifrando!"]
                    if lang == "eng":
                        error1 = error_pass_eng[0] + "\n" + error_pass_eng[1]
                        error2 = error_pass_eng[2]
                    elif lang == "esp":
                        error1 = error_pass_esp[0] + "\n" + error_pass_esp[1]
                        error2 = error_pass_esp[2]
                    all_imp.pSG.popup_error(error1, title = error2)
                if fin:
                    all_imp.pSG.popup_auto_close(fin, auto_close_duration = 1, button_type = 5, title = fin)
            else:
                no_mes_eng = ["No message to decrypt found in ./Imported.", "Returning to menu.", "Error decrypting!"]
                no_mes_esp = ["No existe un mensaje para descifrar en ./Imported.", "Volviendo al menú",
                              "¡Error descifrando!"]
                if lang == "eng":
                    error1 = no_mes_eng[0] + "\n" + no_mes_eng[1]
                    error2 = no_mes_eng[2]
                elif lang == "esp":
                    error1 = no_mes_esp[0] + "\n" + no_mes_esp[1]
                    error2 = no_mes_esp[2]
                all_imp.pSG.popup_error(error1, title = error2)
        else:
            no_priv_eng = ["Private key to decrypt message does not exist.", "Returning to menu.", "Error decrypting!"]
            no_priv_esp = ["La clave privada para descifrar el mensaje no existe.", "Volviendo al menú.",
                           "¡Error descifrando!"]
            if lang == "eng":
                error1 = no_priv_eng[0] + "\n" + no_priv_eng[1]
                error2 = no_priv_eng[2]
            elif lang == "esp":
                error1 = no_priv_esp[0] + "\n" + no_priv_esp[1]
                error2 = no_priv_esp[2]
            all_imp.pSG.popup_error(error1, title = error2)
        event = None
        mode = None

    elif event == 26:
        if all_imp.os.path.isfile(keys + "/private.asc"):
            if lang == "eng":
                window_title = "Document to decrypt:"
            elif lang == "esp":
                window_title = "Documento a descifrar:"
            fname = all_imp.pSG.popup_get_file(window_title, title = window_title)
            if fname:
                extension = fname.split(".")[-2] + "." + fname.split(".")[-1]
                if extension == "pgp.PK":
                    try:
                        all_imp.edsv.pgpy_decrypt(fname, True, keys + "/private.asc", lang, dec)
                    except all_imp.pgpy.errors.PGPDecryptionError:
                        error_pass_eng = ["The passphrase is incorrect.", "Returning to menu.", "Error decrypting!"]
                        error_pass_esp = ["La contraseña es incorrecta.", "Volviendo al menú.", "¡Error descifrando!"]
                        if lang == "eng":
                            error1 = error_pass_eng[0] + "\n" + error_pass_eng[1]
                            error2 = error_pass_eng[2]
                        elif lang == "esp":
                            error1 = error_pass_esp[0] + "\n" + error_pass_esp[1]
                            error2 = error_pass_esp[2]
                        all_imp.pSG.popup_error(error1, title = error2)
                else:
                    file_ext_eng = ["Incorrect file extension to decrypt.", "Returning to menu.", "Error decrypting!"]
                    file_ext_esp = ["La extensión del fichero a descifrar es incorrecta.", "Volviendo al menú.",
                                    "¡Error descifrando!"]
                    if lang == "eng":
                        error1 = file_ext_eng[0] + "\n" + file_ext_eng[1]
                        error2 = file_ext_eng[2]
                    elif lang == "esp":
                        error1 = file_ext_esp[0] + "\n" + file_ext_esp[1]
                        error2 = file_ext_esp[2]
                    all_imp.pSG.popup_error(error1, title = error2)
        else:
            no_priv_eng = ["Private key to decrypt file does not exist.", "Returning to menu.", "Error decrypting!"]
            no_priv_esp = ["La clave privada para descifrar el fichero no existe.", "Volviendo al menú.",
                           "¡Error descifrando!"]
            if lang == "eng":
                error1 = no_priv_eng[0] + "\n" + no_priv_eng[1]
                error2 = no_priv_eng[2]
            elif lang == "esp":
                error1 = no_priv_esp[0] + "\n" + no_priv_esp[1]
                error2 = no_priv_esp[2]
            all_imp.pSG.popup_error(error1, title = error2)
        event = None
        mode = None

    return event, mode, values
