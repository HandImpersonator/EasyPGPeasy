# lang_layout.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imp


def crem_language():
    """Create language window layout.
    Return created layout."""

    width = 15

    button_eng = ["English", "Spanish", "Menu"]
    button_esp = ["Inglés", "Español", "Menú"]

    layout_language_eng = [[all_imp.pSG.Button(button_eng[0], focus = False, key = 454, size = (width, 0))],
                           [all_imp.pSG.Button(button_eng[1], focus = False, key = 455, size = (width, 0))],
                           [all_imp.pSG.Button(button_eng[2], focus = False, key = 800, size = (width, 0))]]
    layout_language_esp = [[all_imp.pSG.Button(button_esp[0], focus = False, key = 454, size = (width, 0))],
                           [all_imp.pSG.Button(button_esp[1], focus = False, key = 455, size = (width, 0))],
                           [all_imp.pSG.Button(button_esp[2], focus = False, key = 800, size = (width, 0))]]

    window_language_eng = all_imp.pSG.Window("EZPZ PGP - Language selection", layout_language_eng, disable_close = True,
                                             element_justification = "center")
    window_language_esp = all_imp.pSG.Window("EZPZ PGP - Selección de idioma", layout_language_esp, disable_close = True,
                                             element_justification = "center")

    return window_language_eng, window_language_esp
