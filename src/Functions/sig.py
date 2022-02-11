# sig.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imp


def sf(event, keys, lang, mes_sig_eng, mes_sig_esp, sig, values):
    """Function that handles the signing process.
    Returns events, mode choice and values if there were any typed in."""

    done, error1, error2, fin, mode, out_sig = "", "", "", "", "", ""

    if not values["input"].strip():
        empty_error_eng = ["Cannot sign empty data.", "Error!"]
        empty_error_esp = ["No se pueden firmar datos vacíos.", "¡Error!"]
        if lang:
            error1 = empty_error_eng[0]
            error2 = empty_error_eng[1]
        elif not lang:
            error1 = empty_error_esp[0]
            error2 = empty_error_esp[1]
        all_imp.pSG.popup_error(error1, title = error2)
    elif values["input"].strip():
        if all_imp.os.path.isfile(keys + "/private.asc"):
            try:
                out_sig, fin = all_imp.edsv.pgpy_sign(values["input"].strip(), False, keys + "/private.asc", lang, sig)
            except all_imp.pgpy.errors.PGPDecryptionError:
                error_pass_eng = ["The passphrase is incorrect.", "Returning to menu.", "Error!"]
                error_pass_esp = ["La contraseña es incorrecta.", "Volviendo al menú.", "¡Error!"]
                if lang:
                    error1 = error_pass_eng[0] + "\n" + error_pass_eng[1]
                    error2 = error_pass_eng[2]
                elif not lang:
                    error1 = error_pass_esp[0] + "\n" + error_pass_esp[1]
                    error2 = error_pass_esp[2]
                all_imp.pSG.popup_error(error1, title = error2)
            update_button = ["Sign", "Firmar"]
            pressed = True
            if lang:
                mes_sig_eng["output"].update(value = str(out_sig))
                mes_sig_eng["xclipp"].update(visible = False)
                mes_sig_eng.Element("sig").Update((update_button[0], "Reset")[pressed])
                mes_sig_eng.refresh()
                if fin:
                    all_imp.pSG.popup_auto_close(fin, auto_close_duration = 1, button_type = 5, title = fin)
                event, values = mes_sig_eng.read()
                mes_sig_eng.close()
            if not lang:
                mes_sig_esp["output"].update(value = str(out_sig))
                mes_sig_esp["xclipp"].update(visible = False)
                mes_sig_esp.Element("sig").Update((update_button[1], "Reset")[pressed])
                mes_sig_eng.refresh()
                if fin:
                    all_imp.pSG.popup_auto_close(fin, auto_close_duration = 1, button_type = 5, title = fin)
                event, values = mes_sig_esp.read()
                mes_sig_esp.close()
        else:
            no_priv_eng = ["Private key to sign message does not exist.", "Returning to menu", "Error!"]
            no_priv_esp = ["La clave privada para firmar el mensaje no existe.", "Volviendo al menu", "¡Error!"]
            if lang:
                error1 = no_priv_eng[0] + "\n" + no_priv_eng[1]
                error2 = no_priv_eng[2]
            elif not lang:
                error1 = no_priv_esp[0] + "\n" + no_priv_esp[1]
                error2 = no_priv_esp[2]
            all_imp.pSG.popup_error(error1, title = error2)
        mode = None
    if event == 800:
        mode = None
    if mes_sig_eng[event].GetText() == "Reset" or mes_sig_esp[event].GetText() == "Reset":
        mode = 30
    if event == 600:
        all_imp.sys.exit(0)

    return event, mode, values


def sm(enc, event, keys, lang, mes_sig_eng, mes_sig_esp, sig):
    """Function that allows to choose the signing mode.
    Returns events, mode choice and values if there were any typed in."""

    done, error1, error2, fin, mode, paste, window_title, values = "", "", "", "", "", "", "", ""

    choose_sig_eng, choose_sig_esp = all_imp.choose_layout.crem_sign()
    if lang and event != [34, 35, 36]:
        event, values = choose_sig_eng.read()
        choose_sig_eng.close()
    elif not lang and event != [34, 35, 36]:
        event, values = choose_sig_esp.read()
        choose_sig_esp.close()

    if event == 34:
        if lang:
            event, values = mes_sig_eng.read()
        elif not lang:
            event, values = mes_sig_esp.read()

        # Paste from clipboard.
        if event == "xclipp":
            try:
                paste = str(all_imp.pyclip.paste(text = True).strip())
            except BaseException:
                if lang:
                    paste = "Clipboard was empty, here you go."
                elif not lang:
                    paste = "El portapapeles estaba vacío, aquí tienes."
            toggle = False

            # Update window with pasted content.
            if lang:
                mes_sig_eng["input"].update(value = paste)
                mes_sig_eng["xclipp"].update(visible = toggle)
                event, values = mes_sig_eng.read()
            elif not lang:
                mes_sig_esp["input"].update(value = paste)
                mes_sig_esp["xclipp"].update(visible = toggle)
                event, values = mes_sig_esp.read()

    elif event == 35:
        if all_imp.os.path.isfile(keys + "/private.asc"):
            if all_imp.os.path.isfile(enc + "/encrypted_message.txt"):
                try:
                    _, fin = all_imp.edsv.pgpy_sign(enc + "/encrypted_message.txt", False, keys + "/private.asc", lang,
                                                    sig)
                except all_imp.pgpy.errors.PGPDecryptionError:
                    error_pass_eng = ["The passphrase is incorrect.", "Returning to menu.", "Error!"]
                    error_pass_esp = ["La contraseña es incorrecta.", "Volviendo al menú.", "¡Error!"]
                    if lang:
                        error1 = error_pass_eng[0] + "\n" + error_pass_eng[1]
                        error2 = error_pass_eng[2]
                    elif not lang:
                        error1 = error_pass_esp[0] + "\n" + error_pass_esp[1]
                        error2 = error_pass_esp[2]
                    all_imp.pSG.popup_error(error1, title = error2)
                if fin:
                    all_imp.pSG.popup_auto_close(fin, auto_close_duration = 1, button_type = 5, title = fin)
            else:
                no_mes_eng = ["No message to sign found in Messages folder.", "Returning to menu.", "Error!"]
                no_mes_esp = ["No existe un mensaque firmar en la carpeta Messages.", "Volviendo al menú.", "¡Error!"]
                if lang:
                    error1 = no_mes_eng[0] + "\n" + no_mes_eng[1]
                    error2 = no_mes_eng[2]
                elif not lang:
                    error1 = no_mes_esp[0] + "\n" + no_mes_esp[1]
                    error2 = no_mes_esp[2]
                all_imp.pSG.popup_error(error1, title = error2)
        else:
            no_priv_eng = ["Private key to sign message does not exist.", "Returning to menu.", "Error!"]
            no_priv_esp = ["La clave privada para firmar el mensaje no existe.", "Volviendo al menú.", "¡Error!"]
            if lang:
                error1 = no_priv_eng[0] + "\n" + no_priv_eng[1]
                error2 = no_priv_eng[2]
            elif not lang:
                error1 = no_priv_esp[0] + "\n" + no_priv_esp[1]
                error2 = no_priv_esp[2]
            all_imp.pSG.popup_error(error1, title = error2)

    elif event == 36:
        if all_imp.os.path.isfile(keys + "/private.asc"):
            if lang:
                window_title = "Document to sign:"
            elif not lang:
                window_title = "Documento a firmar:"
            fname = all_imp.pSG.popup_get_file(window_title, title = window_title)
            if fname:
                try:
                    all_imp.edsv.pgpy_sign(fname, True, keys + "/private.asc", lang, sig)
                except all_imp.pgpy.errors.PGPDecryptionError:
                    error_pass_eng = ["The passphrase is incorrect.", "Returning to menu.", "Error!"]
                    error_pass_esp = ["La contraseña es incorrecta.", "Volviendo al menú.", "¡Error!"]
                    if lang:
                        error1 = error_pass_eng[0] + "\n" + error_pass_eng[1]
                        error2 = error_pass_eng[2]
                    elif not lang:
                        error1 = error_pass_esp[0] + "\n" + error_pass_esp[1]
                        error2 = error_pass_esp[2]
                    all_imp.pSG.popup_error(error1, title = error2)
        else:
            no_priv_eng = ["Private key to sign message does not exist.", "Returning to menu.", "Error!"]
            no_priv_esp = ["La clave privada para firmar el mensaje no existe.", "Volviendo al menú.", "¡Error!"]
            if lang:
                error1 = no_priv_eng[0] + "\n" + no_priv_eng[1]
                error2 = no_priv_eng[2]
            elif not lang:
                error1 = no_priv_esp[0] + "\n" + no_priv_esp[1]
                error2 = no_priv_esp[2]
            all_imp.pSG.popup_error(error1, title = error2)
    mode = None

    return event, mode, values
