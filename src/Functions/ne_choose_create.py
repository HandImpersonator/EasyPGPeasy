# ne_choose_create.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports


def create_remove_choose_ne():
    """Create name and email input window layout.
    Return created layout."""
    width1 = 40
    width2 = 45

    buttons_eng = ["Create", "Menu"]
    buttons_esp = ["Crear", "Menú"]

    layout_ne_choose_eng = [[all_imports.pSG.Text("Name:", auto_size_text = True, enable_events = False),
                             all_imports.pSG.Input(do_not_clear = False, focus = False, key = "name",
                                                   size = (width1, 0))],
                            [all_imports.pSG.Text("Email:", auto_size_text = True, enable_events = False),
                             all_imports.pSG.Input(do_not_clear = False, focus = False, key = "email",
                                                   size = (width1, 0))],
                            [all_imports.pSG.Button(buttons_eng[0], focus = False, key = 660, size = (width2, 0))],
                            [all_imports.pSG.Button(buttons_eng[1], focus = False, key = 800, size = (width2, 0))]]
    layout_ne_choose_esp = [[all_imports.pSG.Text("Nombre:", auto_size_text = True, enable_events = False),
                             all_imports.pSG.Input(do_not_clear = False, focus = False, key = "name",
                                                   size = (width1, 0))],
                            [all_imports.pSG.Text("Correo:", auto_size_text = True, enable_events = False),
                             all_imports.pSG.Input(do_not_clear = False, focus = False, key = "email",
                                                   size = (width1, 0))],
                            [all_imports.pSG.Button(buttons_esp[0], focus = False, key = 660, size = (width2, 0))],
                            [all_imports.pSG.Button(buttons_esp[1], focus = False, key = 800, size = (width2, 0))]]

    window_ne_choose_eng = all_imports.pSG.Window("EZPZ PGP - PGP choose creation mode", layout_ne_choose_eng,
                                                  disable_close = True, element_justification = "center")
    window_ne_choose_esp = all_imports.pSG.Window("EZPZ PGP - Elegir modo de creación de PGP", layout_ne_choose_esp,
                                                  disable_close = True, element_justification = "center")

    return window_ne_choose_eng, window_ne_choose_esp
