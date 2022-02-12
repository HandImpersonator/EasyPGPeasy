# ver.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imp


def vm(event, imported, lang, ver):
    """Function that allows to choose the verifying mode.
    Returns events, mode choice and values if there were any typed in."""

    done, error1, error2, fin, mode, window_title, values = "", "", "", "", "", "", ""

    choose_ver_eng, choose_ver_esp = all_imp.choose_layout.crem_verify()
    if lang and event != [44, 46]:
        event, values = choose_ver_eng.read()
        choose_ver_eng.close()
    elif not lang and event != [44, 46]:
        event, values = choose_ver_esp.read()
        choose_ver_esp.close()

    if event == 44:
        if all_imp.os.path.isfile(imported + "/v_imported_message.txt"):
            if all_imp.os.path.isfile(imported + "/v_imported_public.asc"):
                if all_imp.os.path.isfile(imported + "/v_imported_signature.txt"):
                    mes = imported + "/v_imported_message.txt"
                    key = imported + "/v_imported_public.asc"
                    sig = imported + "/v_imported_signature.txt"
                    fin = all_imp.edsv.pgpy_verify(False, mes, key, lang, sig, ver)
                    if fin:
                        all_imp.pSG.popup_auto_close(fin, auto_close_duration = 1, button_type = 5, title = fin)
                else:
                    no_ver_eng = ["Signature to verify message is not imported.", "Returning to menu.", "Error!"]
                    no_ver_esp = ["La firma para verificar el mensaje no está importado.", "Volviendo al menú.",
                                  "Error!"]
                    if lang:
                        error1 = no_ver_eng[0] + "\n" + no_ver_eng[1]
                        error2 = no_ver_eng[2]
                    elif not lang:
                        error1 = no_ver_esp[0] + "\n" + no_ver_esp[1]
                        error2 = no_ver_esp[2]
                    all_imp.pSG.popup_error(error1, title = error2)
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
                all_imp.pSG.popup_error(error1, title = error2)
        else:
            no_pub_eng = ["Message to be verified is not imported.", "Returning to menu.", "Error!"]
            no_pub_esp = ["El mensaje a verificar no está importade.", "Volviendo al menú.", "¡Error!"]
            if lang:
                error1 = no_pub_eng[0] + "\n" + no_pub_eng[1]
                error2 = no_pub_eng[2]
            elif not lang:
                error1 = no_pub_esp[0] + "\n" + no_pub_esp[1]
                error2 = no_pub_esp[2]
            all_imp.pSG.popup_error(error1, title = error2)
        mode = None

    elif event == 46:
        if all_imp.os.path.isfile(imported + "/v_imported_public.asc"):
            if all_imp.os.path.isfile(imported + "/v_imported_signature.txt"):
                if lang:
                    window_title = "Document to verify:"
                elif not lang:
                    window_title = "Documento a verificar:"
                mes = all_imp.pSG.popup_get_file(window_title, title = window_title)
                key = imported + "/v_imported_public.asc"
                sig = imported + "/v_imported_signature.txt"
                if mes:
                    fin = all_imp.edsv.pgpy_verify(True, mes, key, lang, sig, ver)
                if fin:
                    all_imp.pSG.popup_auto_close(fin, auto_close_duration = 1, button_type = 5, title = fin)
            else:
                no_ver_eng = ["Signature to verify message is not imported.", "Returning to menu.", "Error!"]
                no_ver_esp = ["La firma para verificar el mensaje no está importado.", "Volviendo al menú.", "Error!"]
                if lang:
                    error1 = no_ver_eng[0] + "\n" + no_ver_eng[1]
                    error2 = no_ver_eng[2]
                elif not lang:
                    error1 = no_ver_esp[0] + "\n" + no_ver_esp[1]
                    error2 = no_ver_esp[2]
                all_imp.pSG.popup_error(error1, title = error2)
        else:
            no_pub_eng = ["Public key to verify message is not imported.", "Returning to menu.", "Error!"]
            no_pub_esp = ["La clave pública para verificar el mensaje no está importada.", "Volviendo al menú.",
                          "¡Error!"]
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
    if event == 600:
        all_imp.sys.exit(0)

    return event, mode, values
