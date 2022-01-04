# menu.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import all_imports


def create_remove_language():
    width = 15

    layout_language_eng = [[all_imports.pSG.Button("English", key = 454, size = (width, 0))],
                           [all_imports.pSG.Button("Spanish", key = 455, size = (width, 0))],
                           [all_imports.pSG.Button("Menu", key = 800, size = (width, 0))]]
    layout_language_esp = [[all_imports.pSG.Button("Inglés", key = 454, size = (width, 0))],
                           [all_imports.pSG.Button("Español", key = 455, size = (width, 0))],
                           [all_imports.pSG.Button("Menú", key = 800, size = (width, 0))]]

    window_language_eng = all_imports.pSG.Window("EZPZ PGP - Language selection", layout_language_eng,
                                                 disable_close = True, element_justification = "center")
    window_language_esp = all_imports.pSG.Window("EZPZ PGP - Seleccionar idioma", layout_language_esp,
                                                 disable_close = True, element_justification = "center")

    return window_language_eng, window_language_esp
