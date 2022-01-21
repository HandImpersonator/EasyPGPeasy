# menu_create.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports


def create_remove_menu(height, width):
    """Create menu window layout.
    Return created layout."""
    text_eng = ["Choose PGP bit size:", "Create PGP KeyPair", "Import PGP Public key", "Import message to verify",
                "Import signature to verify", "Encrypt", "Decrypt", "Sign", "Verify", "Language", "Help", "Close"]
    text_esp = ["Elige tamaño de bit de PGP:", "Crear par de claves PGP", "Importar clave PGP Pública",
                "Importar mensaje a verificar", "Importar firma a verificar", "Cifrar", "Descifrar", "Firmar",
                "Verificar", "Idioma", "Ayuda", "Cerrar"]

    layout_menu_eng = [[all_imports.pSG.Text(text_eng[0])], [
        all_imports.pSG.DropDown(auto_size_text = True, change_submits = False, default_value = 4096, key = "value",
                                 readonly = True, size = (width, 0), values = (4096, 8192, 16384))],
                       [all_imports.pSG.Button(text_eng[1], focus = False, key = 100, size = (width, 0))],
                       [all_imports.pSG.Button(text_eng[2], focus = False, key = 112, size = (width, 0))],
                       [all_imports.pSG.Button(text_eng[3], focus = False, key = 110, size = (width, 0))],
                       [all_imports.pSG.Button(text_eng[4], focus = False, key = 114, size = (width, 0))],
                       [all_imports.pSG.Button(text_eng[5], focus = False, key = 200, size = (width, 0))],
                       [all_imports.pSG.Button(text_eng[6], focus = False, key = 300, size = (width, 0))],
                       [all_imports.pSG.Button(text_eng[7], focus = False, key = 250, size = (width, 0))],
                       [all_imports.pSG.Button(text_eng[8], focus = False, key = 350, size = (width, 0))],
                       [all_imports.pSG.Button(text_eng[9], focus = False, key = 400, size = (width, 0))],
                       [all_imports.pSG.Button(text_eng[10], focus = False, key = 500, size = (width, 0))],
                       [all_imports.pSG.Button(text_eng[11], focus = False, key = 600, size = (width, 0))]]
    layout_menu_esp = [[all_imports.pSG.Text(text_esp[0])], [
        all_imports.pSG.DropDown(default_value = 4096, key = "value", readonly = True, size = (width, height),
                                 values = (4096, 8192, 16384))],
                       [all_imports.pSG.Button(text_esp[1], focus = False, key = 100, size = (width, 0))],
                       [all_imports.pSG.Button(text_esp[2], focus = False, key = 112, size = (width, 0))],
                       [all_imports.pSG.Button(text_esp[3], focus = False, key = 110, size = (width, 0))],
                       [all_imports.pSG.Button(text_esp[4], focus = False, key = 114, size = (width, 0))],
                       [all_imports.pSG.Button(text_esp[5], focus = False, key = 200, size = (width, 0))],
                       [all_imports.pSG.Button(text_esp[6], focus = False, key = 300, size = (width, 0))],
                       [all_imports.pSG.Button(text_esp[7], focus = False, key = 250, size = (width, 0))],
                       [all_imports.pSG.Button(text_esp[8], focus = False, key = 350, size = (width, 0))],
                       [all_imports.pSG.Button(text_esp[9], focus = False, key = 400, size = (width, 0))],
                       [all_imports.pSG.Button(text_esp[10], focus = False, key = 500, size = (width, 0))],
                       [all_imports.pSG.Button(text_esp[11], focus = False, key = 600, size = (width, 0))]]

    window_menu_eng = all_imports.pSG.Window("EZPZ PGP - Select mode:", layout_menu_eng, disable_close = True,
                                             element_justification = "center", size = (width, height),
                                             text_justification = "center")
    window_menu_esp = all_imports.pSG.Window("EZPZ PGP - Seleccionar modo:", layout_menu_esp, disable_close = True,
                                             element_justification = "center", size = (width, height),
                                             text_justification = "center")

    return window_menu_eng, window_menu_esp
