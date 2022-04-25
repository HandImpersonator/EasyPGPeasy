# ver.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imp


def vm(event, key, lang, mes, sig, ver):
    """Function that allows to choose the verifying mode.
    Returns events, mode choice and values if there were any typed in."""

    error1, error2, fin, mode, window_title, values = "", "", "", "", "", ""

    choose_ver_eng, choose_ver_esp = all_imp.choose_layout.crem_verify()
    if lang == "eng" and event not in [44, 46]:
        event, values = choose_ver_eng.read()
        choose_ver_eng.close()
    elif lang == "esp" and event not in [44, 46]:
        event, values = choose_ver_esp.read()
        choose_ver_esp.close()

    if event == 44:
        if all_imp.os.path.isfile(mes):
            all_imp.edsv.pgpy_verify(False, mes, key, lang, sig, ver)
        else:
            no_pub_eng = ["Message to be verified is not imported.", "Error verifying!"]
            no_pub_esp = ["El mensaje a verificar no está importade.", "¡Error verificando!"]
            if lang == "eng":
                error1 = no_pub_eng[0]
                error2 = no_pub_eng[1]
            elif lang == "esp":
                error1 = no_pub_esp[0]
                error2 = no_pub_esp[1]
            all_imp.pSG.popup_error(error1, title = error2)

    elif event == 46:
        if lang == "eng":
            window_title = "Document to verify:"
        elif lang == "esp":
            window_title = "Documento a verificar:"
        mes = all_imp.pSG.popup_get_file(window_title, title = window_title)
        if mes:
            all_imp.edsv.pgpy_verify(True, mes, key, lang, sig, ver)
    event = None
    mode = None

    if event == 800:
        event = None
        mode = None
    if event == 600:
        all_imp.sys.exit(0)

    return event, mode, values
