# enc.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imp


def ef(enc, event, imported, lang, mes_enc_eng, mes_enc_esp, values):
    """Function that handles the encryption process.
    Returns events, mode choice and values if there were any typed in."""

    done, error1, error2, fin, mode, out_enc = "", "", "", "", "", ""

    if not values["input"].strip():
        empty_eng = ["Cannot encrypt empty data.", "Returning to menu.", "Error!"]
        empty_esp = ["No se pueden cifrar datos vacíos.", "Volviendo al menú.", "¡Error!"]
        if lang:
            error1 = empty_eng[0] + "\n" + empty_eng[1]
            error2 = empty_eng[2]
        elif not lang:
            error1 = empty_esp[0] + "\n" + empty_esp[1]
            error2 = empty_esp[2]
        all_imp.pSG.popup_error(error1, title = error2)
    elif values["input"].strip():
        if all_imp.os.path.isfile(imported + "/v_imported_public.asc"):
            out_enc, fin = all_imp.edsv.pgpy_encrypt(values["input"].strip(), False,
                                                     imported + "/v_imported_public.asc", lang, enc)
            update_button = ["Encrypt", "Cifrar"]
            pressed = True
            if lang:
                mes_enc_eng["output"].update(value = str(out_enc))
                mes_enc_eng["xclipp"].update(visible = False)
                mes_enc_eng.Element("enc").Update((update_button[0], "Reset")[pressed])
                mes_enc_eng.refresh()
                if fin:
                    all_imp.pSG.popup_auto_close(fin, auto_close_duration = 1, button_type = 5, title = fin)
                event, values = mes_enc_eng.read()
                mes_enc_eng.close()
            elif not lang:
                mes_enc_esp["output"].update(value = str(out_enc))
                mes_enc_esp["xclipp"].update(visible = False)
                mes_enc_esp.Element("enc").Update((update_button[1], "Reset")[pressed])
                mes_enc_esp.refresh()
                if fin:
                    all_imp.pSG.popup_auto_close(fin, auto_close_duration = 1, button_type = 5, title = fin)
                event, values = mes_enc_esp.read()
                mes_enc_esp.close()
        else:
            no_pub_eng = ["Public key to encrypt message does not exist.", "Returning to menu", "Error!"]
            no_pub_esp = ["La clave pública para cifrar el mensaje no existe.", "Volviendo al menu", "¡Error!"]
            if lang:
                error1 = no_pub_eng[0] + "\n" + no_pub_eng[1]
                error2 = no_pub_eng[2]
            elif not lang:
                error1 = no_pub_esp[0] + "\n" + no_pub_esp[1]
                error2 = no_pub_esp[2]
            all_imp.pSG.popup_error(error1, title = error2)
    mode = None
    if event == 800:
        mode = None
    if mes_enc_eng[event].GetText() == "Reset" or mes_enc_esp[event].GetText() == "Reset":
        mode = 15
    if event == 600:
        all_imp.sys.exit(0)

    return event, mode, values


def em(enc, event, imported, lang, mes_enc_eng, mes_enc_esp):
    """Function that allows to choose the encryption mode.
    Returns events, mode choice and values if there were any typed in."""

    error1, error2, fin, mode, paste, window_title, values = "", "", "", "", "", "", ""

    choose_enc_eng, choose_enc_esp = all_imp.choose_layout.crem_encrypt()
    if lang and event not in [14, 16]:
        event, values = choose_enc_eng.read()
        choose_enc_eng.close()
    elif not lang and event not in [14, 16]:
        event, values = choose_enc_esp.read()
        choose_enc_esp.close()

    if event == 14:
        if lang:
            event, values = mes_enc_eng.read()
        elif not lang:
            event, values = mes_enc_esp.read()

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
                mes_enc_eng["input"].update(value = paste)
                mes_enc_eng["xclipp"].update(visible = toggle)
                event, values = mes_enc_eng.read()
            elif not lang:
                mes_enc_esp["input"].update(value = paste)
                mes_enc_esp["xclipp"].update(visible = toggle)
                event, values = mes_enc_esp.read()

    elif event == 16:
        if all_imp.os.path.isfile(imported + "/v_imported_public.asc"):
            if lang:
                window_title = "Document to encrypt:"
            elif not lang:
                window_title = "Documento a cifrar:"
            fname = all_imp.pSG.popup_get_file(window_title, title = window_title)
            if fname:
                all_imp.edsv.pgpy_encrypt(fname, True, imported + "/v_imported_public.asc", lang, enc)
        else:
            no_pub_eng = ["Public key to encrypt message does not exist.", "Returning to menu", "Error!"]
            no_pub_esp = ["La clave pública para cifrar el mensaje no existe.", "Volviendo al menu", "¡Error!"]
            if lang:
                error1 = no_pub_eng[0] + "\n" + no_pub_eng[1]
                error2 = no_pub_eng[2]
            elif not lang:
                error1 = no_pub_esp[0] + "\n" + no_pub_esp[1]
                error2 = no_pub_esp[2]
            all_imp.pSG.popup_error(error1, title = error2)
        mode = None

    return event, mode, values
