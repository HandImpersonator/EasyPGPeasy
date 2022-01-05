# import_create.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports


def create_remove_import():
    """Create import window layout.
    Return created layout."""
    text_eng = ["Paste public key:", "(Note, keep window where you copied the public key OPEN until imported here.)"]
    buttons_eng = ["Import", "Menu"]
    text_esp = ["Pega la clave pública:",
                "(Nota, mantener ventana de donde copia la clave pública ABIERTA hasta que se haya importado aquí.)"]
    buttons_esp = ["Importar", "Menú"]

    import_v_p_k_eng = [[all_imports.pSG.Text(text_eng[0])], [all_imports.pSG.Text(text_eng[1])],
                        [all_imports.pSG.Multiline(autoscroll = True, key = "V_P_K", size = (58, 30))],
                        [all_imports.pSG.Button(buttons_eng[0], key = 700, size = (26, 0)),
                         all_imports.pSG.Button(buttons_eng[1], key = 800, size = (26, 0))]]
    import_v_p_k_esp = [[all_imports.pSG.Text(text_esp[0])], [all_imports.pSG.Text(text_esp[1])],
                        [all_imports.pSG.Multiline(autoscroll = True, key = "V_P_K", size = (58, 30))],
                        [all_imports.pSG.Button(buttons_esp[0], key = 700, size = (26, 0)),
                         all_imports.pSG.Button(buttons_esp[1], key = 800, size = (26, 0))]]

    window_v_p_k_eng = all_imports.pSG.Window("EZPZ PGP - Import Public Key", import_v_p_k_eng, disable_close = True,
                                              element_justification = "center")
    window_v_p_k_esp = all_imports.pSG.Window("EZPZ PGP - Importar clave pública", import_v_p_k_esp,
                                              disable_close = True, element_justification = "center")

    return window_v_p_k_eng, window_v_p_k_esp
