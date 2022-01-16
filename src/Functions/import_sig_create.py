# import_sig_create.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports


def create_remove_sig_import():
    """Create import window layout.
    Return created layout."""
    text_eng = ["Paste signature:", "(Note, keep window where you copied the signature OPEN until imported here.)"]
    buttons_eng = ["Paste from clipboard", "Import", "Menu"]
    text_esp = ["Pega la firma:",
                "(Nota, mantener ventana de donde copia la firma ABIERTA hasta que se haya importado aquí.)"]
    buttons_esp = ["Pegar del portapales", "Importar", "Menú"]

    import_v_p_s_eng = [[all_imports.pSG.Text(text_eng[0])], [all_imports.pSG.Text(text_eng[1])],
                        [all_imports.pSG.Button(buttons_eng[0], key = "xclipp", size = (58, 0))],
                        [all_imports.pSG.Multiline(autoscroll = True, key = 114, size = (58, 30))],
                        [all_imports.pSG.Button(buttons_eng[1], key = 700, size = (26, 0)),
                         all_imports.pSG.Button(buttons_eng[2], key = 800, size = (26, 0))]]
    import_v_p_s_esp = [[all_imports.pSG.Text(text_esp[0])], [all_imports.pSG.Text(text_esp[1])],
                        [all_imports.pSG.Button(buttons_esp[0], key = "xclipp", size = (58, 0))],
                        [all_imports.pSG.Multiline(autoscroll = True, key = 114, size = (58, 30))],
                        [all_imports.pSG.Button(buttons_esp[1], key = 700, size = (26, 0)),
                         all_imports.pSG.Button(buttons_esp[2], key = 800, size = (26, 0))]]

    window_v_p_s_eng = all_imports.pSG.Window("EZPZ PGP - Import Firma", import_v_p_s_eng, disable_close = True,
                                              element_justification = "center")
    window_v_p_s_esp = all_imports.pSG.Window("EZPZ PGP - Importar Firma", import_v_p_s_esp,
                                              disable_close = True, element_justification = "center")

    return window_v_p_s_eng, window_v_p_s_esp
