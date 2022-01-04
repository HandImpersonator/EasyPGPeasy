# menu.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import all_imports


def create_remove_menu(height, width):
    layout_selector_eng = [[all_imports.pSG.Text("Choose PGP bit size:")], [
        all_imports.pSG.DropDown(default_value = 4096, key = "value", readonly = True, size = (width, 0),
                                 auto_size_text = True,
                                 values = (4096, 8192))],
                           [all_imports.pSG.Button("Create PGP Pair", key = 100, size = (width, 0))],
                           [all_imports.pSG.Button("Import PGP Public/Private Key", key = "v_p_k", size = (width, 0))],
                           [all_imports.pSG.Button("Encrypt", key = 200, size = (width, 0))],
                           [all_imports.pSG.Button("Decrypt", key = 300, size = (width, 0))],
                           [all_imports.pSG.Button("Sign WIP", key = 200, size = (width, 0))],
                           [all_imports.pSG.Button("Verify WIP", key = 300, size = (width, 0))],
                           [all_imports.pSG.Button("Language", key = 400, size = (width, 0))],
                           [all_imports.pSG.Button("Help", key = 500, size = (width, 0))],
                           [all_imports.pSG.Button("Close", key = 600, size = (width, 0))]]
    layout_selector_esp = [[all_imports.pSG.Text("Elige tamaño de bit de PGP:")], [
        all_imports.pSG.DropDown(default_value = 4096, key = "value", readonly = True, size = (width, height),
                                 values = (4096, 8192))],
                           [all_imports.pSG.Button("Crear par PGP", key = 100, size = (width, 0))],
                           [all_imports.pSG.Button("Importar clave PGP Pública/Privada", key = "v_p_k",
                                                   size = (width, 0))],
                           [all_imports.pSG.Button("Cifrar", key = 200, size = (width, 0))],
                           [all_imports.pSG.Button("Descifrar", key = 300, size = (width, 0))],
                           [all_imports.pSG.Button("Firmar WIP", key = 200, size = (width, 0))],
                           [all_imports.pSG.Button("Verificar WIP", key = 300, size = (width, 0))],
                           [all_imports.pSG.Button("Idioma", key = 400, size = (width, 0))],
                           [all_imports.pSG.Button("Ayuda", key = 500, size = (width, 0))],
                           [all_imports.pSG.Button("Cerrar", key = 600, size = (width, 0))]]

    window_menu_eng = all_imports.pSG.Window("EZPZ PGP - Select mode:", layout_selector_eng, disable_close = True,
                                             element_justification = "center", size = (width, height),
                                             text_justification = "center")
    window_menu_esp = all_imports.pSG.Window("EZPZ PGP - Seleccionar modo:", layout_selector_esp, disable_close = True,
                                             element_justification = "center", size = (width, height),
                                             text_justification = "center")

    return window_menu_eng, window_menu_esp
