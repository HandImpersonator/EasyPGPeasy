# sign_choose_create.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports


def create_remove_sign():
    """Create signature choose window layout.
    Return creted layout."""
    width = 40

    buttons_eng = ["Plaintext", "Encrypted text", "Menu"]
    buttons_esp = ["Texto en claro", "Texto cifrado", "Menú"]

    layout_sign_choose_eng = [[all_imports.pSG.Button(buttons_eng[0], focus = False, key = 50, size = (width, 0))],
                              [all_imports.pSG.Button(buttons_eng[1], focus = False, key = 60, size = (width, 0))],
                              [all_imports.pSG.Button(buttons_eng[2], focus = False, key = 800, size = (width, 0))]]
    layout_sign_choose_esp = [[all_imports.pSG.Button(buttons_esp[0], focus = False, key = 50, size = (width, 0))],
                              [all_imports.pSG.Button(buttons_esp[1], focus = False, key = 60, size = (width, 0))],
                              [all_imports.pSG.Button(buttons_esp[2], focus = False, key = 800, size = (width, 0))]]

    window_sign_choose_eng = all_imports.pSG.Window("EZPZ PGP - Sign mode choose", layout_sign_choose_eng,
                                                    disable_close = True, element_justification = "center")
    window_sign_choose_esp = all_imports.pSG.Window("EZPZ PGP - Elegir modo de firma", layout_sign_choose_esp,
                                                    disable_close = True, element_justification = "center")

    return window_sign_choose_eng, window_sign_choose_esp
