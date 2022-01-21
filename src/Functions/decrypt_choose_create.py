# decrypt_choose_create.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports


def create_remove_choose_decrypt():
    """Create decryption choosing window layout.
    Return created layout."""
    width = 40

    buttons_eng = ["Encrypted message", "Autodecryption", "Menu"]
    buttons_esp = ["Mensaje cifrado", "Autodescifrado", "Menú"]

    layout_dec_choose_eng = [[all_imports.pSG.Button(buttons_eng[0], focus = False, key = 70, size = (width, 0))],
                             [all_imports.pSG.Button(buttons_eng[1], focus = False, key = 80, size = (width, 0))],
                             [all_imports.pSG.Button(buttons_eng[2], focus = False, key = 800, size = (width, 0))]]
    layout_dec_choose_esp = [[all_imports.pSG.Button(buttons_esp[0], focus = False, key = 70, size = (width, 0))],
                             [all_imports.pSG.Button(buttons_esp[1], focus = False, key = 80, size = (width, 0))],
                             [all_imports.pSG.Button(buttons_esp[2], focus = False, key = 800, size = (width, 0))]]

    window_dec_choose_eng = all_imports.pSG.Window("EZPZ PGP - Decrypt choose", layout_dec_choose_eng,
                                                   disable_close = True, element_justification = "center")
    window_dec_choose_esp = all_imports.pSG.Window("EZPZ PGP - Decrypt choose", layout_dec_choose_esp,
                                                   disable_close = True, element_justification = "center")

    return window_dec_choose_eng, window_dec_choose_esp
