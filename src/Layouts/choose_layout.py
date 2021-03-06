# choose_layout.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imp


def crem_decrypt():
    """Create decryption choosing window layout.
    Return created layout."""

    width = 40

    buttons_eng = ["Encrypted message", "Autodecryption", "File", "Menu"]
    buttons_esp = ["Mensaje cifrado", "Autodescifrado", "Fichero", "Menú"]

    layout_dec_choose_eng = [[all_imp.pSG.Button(buttons_eng[0], focus = False, key = 24, size = (width, 0))],
                             [all_imp.pSG.Button(buttons_eng[1], focus = False, key = 25, size = (width, 0))],
                             [all_imp.pSG.Button(buttons_eng[2], focus = False, key = 26, size = (width, 0))],
                             [all_imp.pSG.Button(buttons_eng[3], focus = False, key = 800, size = (width, 0))]]
    layout_dec_choose_esp = [[all_imp.pSG.Button(buttons_esp[0], focus = False, key = 24, size = (width, 0))],
                             [all_imp.pSG.Button(buttons_esp[1], focus = False, key = 25, size = (width, 0))],
                             [all_imp.pSG.Button(buttons_esp[2], focus = False, key = 26, size = (width, 0))],
                             [all_imp.pSG.Button(buttons_esp[3], focus = False, key = 800, size = (width, 0))]]

    window_dec_choose_eng = all_imp.pSG.Window("EasyPGPeasy - Decrypt mode choose", layout_dec_choose_eng,
                                               disable_close = True, element_justification = "center")
    window_dec_choose_esp = all_imp.pSG.Window("EasyPGPeasy - Elegir modo descifrado", layout_dec_choose_esp,
                                               disable_close = True, element_justification = "center")

    return window_dec_choose_eng, window_dec_choose_esp


def crem_encrypt():
    """Create encryption choosing window layout.
    Return created layout."""

    width = 40

    buttons_eng = ["Message", "File", "Menu"]
    buttons_esp = ["Mensaje", "Fichero", "Menú"]

    layout_dec_choose_eng = [[all_imp.pSG.Button(buttons_eng[0], focus = False, key = 14, size = (width, 0))],
                             [all_imp.pSG.Button(buttons_eng[1], focus = False, key = 16, size = (width, 0))],
                             [all_imp.pSG.Button(buttons_eng[2], focus = False, key = 800, size = (width, 0))]]
    layout_dec_choose_esp = [[all_imp.pSG.Button(buttons_esp[0], focus = False, key = 14, size = (width, 0))],
                             [all_imp.pSG.Button(buttons_esp[1], focus = False, key = 16, size = (width, 0))],
                             [all_imp.pSG.Button(buttons_esp[2], focus = False, key = 800, size = (width, 0))]]

    window_dec_choose_eng = all_imp.pSG.Window("EasyPGPeasy - Encrypt mode choose", layout_dec_choose_eng,
                                               disable_close = True, element_justification = "center")
    window_dec_choose_esp = all_imp.pSG.Window("EasyPGPeasy - Elegir modo cifrado", layout_dec_choose_esp,
                                               disable_close = True, element_justification = "center")

    return window_dec_choose_eng, window_dec_choose_esp


def crem_kp():
    """Create keypair choosing window layout.
    Return created layout."""

    width = 40

    buttons_eng = ["Random name", "Custom name", "Menu"]
    buttons_esp = ["Nombre aleatorio", "Nombre custom", "Menú"]

    layout_kp_choose_eng = [[all_imp.pSG.Button(buttons_eng[0], focus = False, key = 116, size = (width, 0))],
                            [all_imp.pSG.Button(buttons_eng[1], focus = False, key = 118, size = (width, 0))],
                            [all_imp.pSG.Button(buttons_eng[2], focus = False, key = 800, size = (width, 0))]]
    layout_kp_choose_esp = [[all_imp.pSG.Button(buttons_esp[0], focus = False, key = 116, size = (width, 0))],
                            [all_imp.pSG.Button(buttons_esp[1], focus = False, key = 118, size = (width, 0))],
                            [all_imp.pSG.Button(buttons_esp[2], focus = False, key = 800, size = (width, 0))]]

    window_kp_choose_eng = all_imp.pSG.Window("EasyPGPeasy - Keypair mode choose", layout_kp_choose_eng,
                                              disable_close = True, element_justification = "center")
    window_kp_choose_esp = all_imp.pSG.Window("EasyPGPeasy - Elección modo par de claves", layout_kp_choose_esp,
                                              disable_close = True, element_justification = "center")

    return window_kp_choose_eng, window_kp_choose_esp


def crem_ne():
    """Create name and email input window layout.
    Return created layout."""

    width1 = 40
    width2 = 45

    text_eng = ["Name:", "Email:"]
    buttons_eng = ["Create", "Menu"]
    text_esp = ["Nombre:", "Correo:"]
    buttons_esp = ["Crear", "Menú"]

    layout_ne_choose_eng = [[all_imp.pSG.Text(text_eng[0], auto_size_text = True, enable_events = False),
                             all_imp.pSG.Input(do_not_clear = False, focus = False, key = "name", size = (width1, 0))],
                            [all_imp.pSG.Text(text_eng[1], auto_size_text = True, enable_events = False),
                             all_imp.pSG.Input(do_not_clear = False, focus = False, key = "email", size = (width1, 0))],
                            [all_imp.pSG.Button(buttons_eng[0], focus = False, key = 660, size = (width2, 0))],
                            [all_imp.pSG.Button(buttons_eng[1], focus = False, key = 800, size = (width2, 0))]]
    layout_ne_choose_esp = [[all_imp.pSG.Text(text_esp[0], auto_size_text = True, enable_events = False),
                             all_imp.pSG.Input(do_not_clear = False, focus = False, key = "name", size = (width1, 0))],
                            [all_imp.pSG.Text(text_esp[1], auto_size_text = True, enable_events = False),
                             all_imp.pSG.Input(do_not_clear = False, focus = False, key = "email", size = (width1, 0))],
                            [all_imp.pSG.Button(buttons_esp[0], focus = False, key = 660, size = (width2, 0))],
                            [all_imp.pSG.Button(buttons_esp[1], focus = False, key = 800, size = (width2, 0))]]

    window_ne_choose_eng = all_imp.pSG.Window("EasyPGPeasy - PGP choose creation mode", layout_ne_choose_eng,
                                              disable_close = True, element_justification = "center")
    window_ne_choose_esp = all_imp.pSG.Window("EasyPGPeasy - Elegir modo de creación de PGP", layout_ne_choose_esp,
                                              disable_close = True, element_justification = "center")

    return window_ne_choose_eng, window_ne_choose_esp


def crem_pass():
    """Create password choosing window layout.
    Return created layout."""

    width = 40

    text_eng = "Private key passphrase:"
    buttons_eng = "Accept"
    text_esp = "Contraseña clave Privada:"
    buttons_esp = "Aceptar"

    layout_pass_choose_eng = [[all_imp.pSG.Text(text_eng)],
                              [all_imp.pSG.Input(do_not_clear = False, focus = False, key = "pass", size = (width, 0))],
                              [all_imp.pSG.Button(buttons_eng, bind_return_key = True, focus = False, key = "acc",
                                                  size = (width, 0))]]
    layout_pass_choose_esp = [[all_imp.pSG.Text(text_esp)],
                              [all_imp.pSG.Input(do_not_clear = False, focus = False, key = "pass",
                                                 size = (width, 0))],
                              [all_imp.pSG.Button(buttons_esp, bind_return_key = True, focus = False, key = "acc",
                                                  size = (width, 0))]]

    window_pass_choose_eng = all_imp.pSG.Window("EasyPGPeasy - Password input", layout_pass_choose_eng,
                                                disable_close = True, element_justification = "center")
    window_pass_choose_esp = all_imp.pSG.Window("EasyPGPeasy - Introducir contraseña", layout_pass_choose_esp,
                                                disable_close = True, element_justification = "center")

    return window_pass_choose_eng, window_pass_choose_esp


def crem_sign():
    """Create signature choose window layout.
    Return creted layout."""

    width = 40

    buttons_eng = ["Plaintext", "Encrypted message", "File", "Menu"]
    buttons_esp = ["Texto en claro", "Mensaje cifrado", "Fichero", "Menú"]

    layout_sign_choose_eng = [[all_imp.pSG.Button(buttons_eng[0], focus = False, key = 34, size = (width, 0))],
                              [all_imp.pSG.Button(buttons_eng[1], focus = False, key = 35, size = (width, 0))],
                              [all_imp.pSG.Button(buttons_eng[2], focus = False, key = 36, size = (width, 0))],
                              [all_imp.pSG.Button(buttons_eng[3], focus = False, key = 800, size = (width, 0))]]
    layout_sign_choose_esp = [[all_imp.pSG.Button(buttons_esp[0], focus = False, key = 34, size = (width, 0))],
                              [all_imp.pSG.Button(buttons_esp[1], focus = False, key = 35, size = (width, 0))],
                              [all_imp.pSG.Button(buttons_esp[2], focus = False, key = 36, size = (width, 0))],
                              [all_imp.pSG.Button(buttons_esp[3], focus = False, key = 800, size = (width, 0))]]

    window_sign_choose_eng = all_imp.pSG.Window("EasyPGPeasy - Sign mode choose", layout_sign_choose_eng,
                                                disable_close = True, element_justification = "center")
    window_sign_choose_esp = all_imp.pSG.Window("EasyPGPeasy - Elegir modo de firma", layout_sign_choose_esp,
                                                disable_close = True, element_justification = "center")

    return window_sign_choose_eng, window_sign_choose_esp


def crem_verify():
    """Create signature choose window layout.
    Return creted layout."""
    width = 40

    buttons_eng = ["Autoverify", "File", "Menu"]
    buttons_esp = ["Autoveirificar", "Fichero", "Menú"]

    layout_sign_choose_eng = [[all_imp.pSG.Button(buttons_eng[0], focus = False, key = 44, size = (width, 0))],
                              [all_imp.pSG.Button(buttons_eng[1], focus = False, key = 46, size = (width, 0))],
                              [all_imp.pSG.Button(buttons_eng[2], focus = False, key = 800, size = (width, 0))]]
    layout_sign_choose_esp = [[all_imp.pSG.Button(buttons_esp[0], focus = False, key = 44, size = (width, 0))],
                              [all_imp.pSG.Button(buttons_esp[1], focus = False, key = 46, size = (width, 0))],
                              [all_imp.pSG.Button(buttons_esp[2], focus = False, key = 800, size = (width, 0))]]

    window_sign_choose_eng = all_imp.pSG.Window("EasyPGPeasy - Sign mode choose", layout_sign_choose_eng,
                                                disable_close = True, element_justification = "center")
    window_sign_choose_esp = all_imp.pSG.Window("EasyPGPeasy - Elegir modo de firma", layout_sign_choose_esp,
                                                disable_close = True, element_justification = "center")

    return window_sign_choose_eng, window_sign_choose_esp
