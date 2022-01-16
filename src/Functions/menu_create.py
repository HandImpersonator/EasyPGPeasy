# menu_create.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports


def create_remove_menu(height, width):
    """Create menu window layout.
    Return created layout."""
    text_eng = ["Choose PGP bit size:", "Create PGP KeyPair", "Import PGP Public key",
                "Import message to verify", "Import signature to verify", "Encrypt", "Decrypt", "Sign WIP",
                "Verify WIP", "Language", "Help", "Close"]
    text_esp = ["Elige tamaño de bit de PGP:", "Crear par de claves PGP", "Importar clave PGP Pública",
                "Importar mensaje a verificar", "Importar firma a verificar", "Cifrar", "Descifrar", "Firmar WIP",
                "Verificar WIP", "Idioma", "Ayuda", "Cerrar"]

    layout_selector_eng = [[all_imports.pSG.Text(text_eng[0])], [
        all_imports.pSG.DropDown(default_value = 4096, key = "value", readonly = True, size = (width, 0),
                                 auto_size_text = True, values = (4096, 8192, 16384))],
                           [all_imports.pSG.Button(text_eng[1], key = 100, size = (width, 0))],
                           [all_imports.pSG.Button(text_eng[2], key = 112, size = (width, 0))],
                           [all_imports.pSG.Button(text_eng[3], key = 110, size = (width, 0))],
                           [all_imports.pSG.Button(text_eng[4], key = 114, size = (width, 0))],
                           [all_imports.pSG.Button(text_eng[5], key = 200, size = (width, 0))],
                           [all_imports.pSG.Button(text_eng[6], key = 300, size = (width, 0))],
                           [all_imports.pSG.Button(text_eng[7], key = 250, size = (width, 0))],
                           [all_imports.pSG.Button(text_eng[8], key = 350, size = (width, 0))],
                           [all_imports.pSG.Button(text_eng[9], key = 400, size = (width, 0))],
                           [all_imports.pSG.Button(text_eng[10], key = 500, size = (width, 0))],
                           [all_imports.pSG.Button(text_eng[11], key = 600, size = (width, 0))]]
    layout_selector_esp = [[all_imports.pSG.Text(text_esp[0])], [
        all_imports.pSG.DropDown(default_value = 4096, key = "value", readonly = True, size = (width, height),
                                 values = (4096, 8192))],
                           [all_imports.pSG.Button(text_esp[1], key = 100, size = (width, 0))],
                           [all_imports.pSG.Button(text_esp[2], key = 112, size = (width, 0))],
                           [all_imports.pSG.Button(text_esp[3], key = 110, size = (width, 0))],
                           [all_imports.pSG.Button(text_esp[4], key = 114, size = (width, 0))],
                           [all_imports.pSG.Button(text_esp[5], key = 200, size = (width, 0))],
                           [all_imports.pSG.Button(text_esp[6], key = 300, size = (width, 0))],
                           [all_imports.pSG.Button(text_esp[7], key = 250, size = (width, 0))],
                           [all_imports.pSG.Button(text_esp[8], key = 350, size = (width, 0))],
                           [all_imports.pSG.Button(text_esp[9], key = 400, size = (width, 0))],
                           [all_imports.pSG.Button(text_esp[10], key = 500, size = (width, 0))],
                           [all_imports.pSG.Button(text_esp[11], key = 600, size = (width, 0))]]

    window_menu_eng = all_imports.pSG.Window("EZPZ PGP - Select mode:", layout_selector_eng, disable_close = True,
                                             element_justification = "center", size = (width, height),
                                             text_justification = "center")
    window_menu_esp = all_imports.pSG.Window("EZPZ PGP - Seleccionar modo:", layout_selector_esp, disable_close = True,
                                             element_justification = "center", size = (width, height),
                                             text_justification = "center")

    return window_menu_eng, window_menu_esp
