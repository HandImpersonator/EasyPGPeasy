# imp_layout.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imp


def crem_enc_import():
    """Create message import window layout.
    Return created layout."""

    text_eng = ["Paste message:", "(Note, keep window where you copied the signed message OPEN until imported here. ",
                "You can import plaintext and encrypted messages, the tool will not differenciate ",
                "between them when it comes to saving them.)"]
    buttons_eng = ["Paste from clipboard", "Import", "Menu"]
    text_esp = ["Pega el mensaje:", "(Nota, mantener la ventana de donde copia el mensaje firmado ",
                "ABIERTA hasta que se haya importado aquí.",
                "Se puede importar tanto un texto en claro como un texto cifrado, la herramienta no hará distinción ",
                "a la hora de guardarlo.)"]
    buttons_esp = ["Pegar del portapales", "Importar", "Menú"]

    import_v_p_e_eng = [[all_imp.pSG.Text(text_eng[0])], [all_imp.pSG.Text(text_eng[1])],
                        [all_imp.pSG.Text(text_eng[2])], [all_imp.pSG.Text(text_eng[3])],
                        [all_imp.pSG.Button(buttons_eng[0], focus = False, key = "xclipp", size = (58, 0))],
                        [all_imp.pSG.Multiline(autoscroll = True, focus = True, key = 110, size = (58, 30))],
                        [all_imp.pSG.Button(buttons_eng[1], focus = False, key = 700, size = (26, 0)),
                         all_imp.pSG.Button(buttons_eng[2], focus = False, key = 800, size = (26, 0))]]
    import_v_p_e_esp = [[all_imp.pSG.Text(text_esp[0])], [all_imp.pSG.Text(text_esp[1])],
                        [all_imp.pSG.Text(text_esp[2])], [all_imp.pSG.Text(text_esp[3])],
                        [all_imp.pSG.Text(text_esp[4])],
                        [all_imp.pSG.Button(buttons_esp[0], focus = False, key = "xclipp", size = (58, 0))],
                        [all_imp.pSG.Multiline(autoscroll = True, focus = True, key = 110, size = (58, 30))],
                        [all_imp.pSG.Button(buttons_esp[1], focus = False, key = 700, size = (26, 0)),
                         all_imp.pSG.Button(buttons_esp[2], focus = False, key = 800, size = (26, 0))]]

    window_v_p_e_eng = all_imp.pSG.Window("EasyPGPeasy - Import Message", import_v_p_e_eng, disable_close = True,
                                          element_justification = "center")
    window_v_p_e_esp = all_imp.pSG.Window("EasyPGPeasy - Importar Mensaje", import_v_p_e_esp, disable_close = True,
                                          element_justification = "center")

    return window_v_p_e_eng, window_v_p_e_esp


def crem_pub_import():
    """Create Public key import window layout.
    Return created layout."""

    text_eng = ["Paste Public key:", "(Note, keep window where you copied the Public key OPEN until imported here.)"]
    buttons_eng = ["Paste from clipboard", "Import", "Menu"]
    text_esp = ["Pega la clave Pública:",
                "(Nota, mantener ventana de donde copia la clave Pública ABIERTA hasta que se haya importado aquí.)"]
    buttons_esp = ["Pegar del portapales", "Importar", "Menú"]

    import_v_p_k_eng = [[all_imp.pSG.Text(text_eng[0])], [all_imp.pSG.Text(text_eng[1])],
                        [all_imp.pSG.Button(buttons_eng[0], focus = False, key = "xclipp", size = (58, 0))],
                        [all_imp.pSG.Multiline(autoscroll = True, focus = True, key = 112, size = (58, 30))],
                        [all_imp.pSG.Button(buttons_eng[1], focus = False, key = 700, size = (26, 0)),
                         all_imp.pSG.Button(buttons_eng[2], focus = False, key = 800, size = (26, 0))]]
    import_v_p_k_esp = [[all_imp.pSG.Text(text_esp[0])], [all_imp.pSG.Text(text_esp[1])],
                        [all_imp.pSG.Button(buttons_esp[0], focus = False, key = "xclipp", size = (58, 0))],
                        [all_imp.pSG.Multiline(autoscroll = True, focus = True, key = 112, size = (58, 30))],
                        [all_imp.pSG.Button(buttons_esp[1], focus = False, key = 700, size = (26, 0)),
                         all_imp.pSG.Button(buttons_esp[2], focus = False, key = 800, size = (26, 0))]]

    window_v_p_k_eng = all_imp.pSG.Window("EasyPGPeasy - Import Public Key", import_v_p_k_eng, disable_close = True,
                                          element_justification = "center")
    window_v_p_k_esp = all_imp.pSG.Window("EasyPGPeasy - Importar clave pública", import_v_p_k_esp,
                                          disable_close = True, element_justification = "center")

    return window_v_p_k_eng, window_v_p_k_esp


def crem_sig_import():
    """Create signature import window layout.
    Return created layout."""

    text_eng = ["Paste signature:", "(Note, keep window where you copied the signature OPEN until imported here.)"]
    buttons_eng = ["Paste from clipboard", "Import", "Menu"]
    text_esp = ["Pega la firma:",
                "(Nota, mantener ventana de donde copia la firma ABIERTA hasta que se haya importado aquí.)"]
    buttons_esp = ["Pegar del portapales", "Importar", "Menú"]

    import_v_p_s_eng = [[all_imp.pSG.Text(text_eng[0])], [all_imp.pSG.Text(text_eng[1])],
                        [all_imp.pSG.Button(buttons_eng[0], focus = False, key = "xclipp", size = (58, 0))],
                        [all_imp.pSG.Multiline(autoscroll = True, focus = True, key = 114, size = (58, 30))],
                        [all_imp.pSG.Button(buttons_eng[1], focus = False, key = 700, size = (26, 0)),
                         all_imp.pSG.Button(buttons_eng[2], focus = False, key = 800, size = (26, 0))]]
    import_v_p_s_esp = [[all_imp.pSG.Text(text_esp[0])], [all_imp.pSG.Text(text_esp[1])],
                        [all_imp.pSG.Button(buttons_esp[0], focus = False, key = "xclipp", size = (58, 0))],
                        [all_imp.pSG.Multiline(autoscroll = True, focus = True, key = 114, size = (58, 30))],
                        [all_imp.pSG.Button(buttons_esp[1], focus = False, key = 700, size = (26, 0)),
                         all_imp.pSG.Button(buttons_esp[2], focus = False, key = 800, size = (26, 0))]]

    window_v_p_s_eng = all_imp.pSG.Window("EasyPGPeasy - Import Signature", import_v_p_s_eng, disable_close = True,
                                          element_justification = "center")
    window_v_p_s_esp = all_imp.pSG.Window("EasyPGPeasy - Importar Firma", import_v_p_s_esp, disable_close = True,
                                          element_justification = "center")

    return window_v_p_s_eng, window_v_p_s_esp
