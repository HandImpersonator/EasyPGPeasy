# menu.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import all_imports


def create_remove_import():
    import_v_p_k_eng = [[all_imports.pSG.Text("Paste public key:")],
                        [all_imports.pSG.Text("(Note, keep window where you copied the"
                                              " public key OPEN until imported here.)")],
                        [all_imports.pSG.Multiline(autoscroll = True, key = "V_P_K", size = (58, 30), )],
                        [all_imports.pSG.Button("Import", key = 700, size = (26, 0)),
                         all_imports.pSG.Button("Menu", key = 800, size = (26, 0))]]
    import_v_p_k_esp = [[all_imports.pSG.Text("Pega la clave pública:")],
                        [all_imports.pSG.Text("(Nota, mantener ventana de donde copia la clave pública ABIERTA hasta "
                                              "que se haya importado aquí.)")],
                        [all_imports.pSG.Multiline(autoscroll = True, key = "V_P_K", size = (58, 30))],
                        [all_imports.pSG.Button("Importar", key = 700, size = (26, 0)),
                         all_imports.pSG.Button("Menú", key = 800, size = (26, 0))]]

    window_v_p_k_eng = all_imports.pSG.Window("EZPZ PGP - Import Public Key", import_v_p_k_eng, disable_close = True,
                                              element_justification = "center")
    window_v_p_k_esp = all_imports.pSG.Window("EZPZ PGP - Importar clave pública", import_v_p_k_esp,
                                              disable_close = True, element_justification = "center")

    return window_v_p_k_eng, window_v_p_k_esp
