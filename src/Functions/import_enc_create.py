# import_enc_create.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports


def create_remove_enc_import():
    """Create import window layout.
    Return created layout."""
    text_eng = ["Paste message:", "(Note, keep window where you copied the signed message OPEN until imported here. ",
                                  "You can import plaintext and encrypted messages, the tool will not differenciate ",
                                  "between them when it comes to saving them or verifying them as long as a file ",
                                  "exists with the imported message, the imported public key and the imported ",
                                  "signature to verify everything.)"]
    buttons_eng = ["Paste from clipboard", "Import", "Menu"]
    text_esp = ["Pega el mensaje:",
                "(Nota, mantener la ventana de donde copia el mensaje firmado ",
                "ABIERTA hasta que se haya importado aquí.",
                "Se puede importar tanto un texto en claro como un texto cifrado, la herramienta no hará distinción ",
                "a la hora de guardarlo ni verificarlo mientras exista un fichero con el mensaje importado, ",
                "la clave pública importada y la firma importada para verificarlo todo.)"]
    buttons_esp = ["Pegar del portapales", "Importar", "Menú"]

    import_v_p_e_eng = [[all_imports.pSG.Text(text_eng[0])], [all_imports.pSG.Text(text_eng[1])],
                        [all_imports.pSG.Text(text_eng[2])], [all_imports.pSG.Text(text_eng[3])],
                        [all_imports.pSG.Text(text_eng[4])], [all_imports.pSG.Text(text_eng[5])],
                        [all_imports.pSG.Button(buttons_eng[0], key = "xclipp", size = (58, 0))],
                        [all_imports.pSG.Multiline(autoscroll = True, key = 110, size = (58, 30))],
                        [all_imports.pSG.Button(buttons_eng[1], key = 700, size = (26, 0)),
                         all_imports.pSG.Button(buttons_eng[2], key = 800, size = (26, 0))]]
    import_v_p_e_esp = [[all_imports.pSG.Text(text_esp[0])], [all_imports.pSG.Text(text_esp[1])],
                        [all_imports.pSG.Text(text_esp[2])], [all_imports.pSG.Text(text_esp[3])],
                        [all_imports.pSG.Text(text_esp[4])],
                        [all_imports.pSG.Button(buttons_esp[0], key = "xclipp", size = (58, 0))],
                        [all_imports.pSG.Multiline(autoscroll = True, key = 110, size = (58, 30))],
                        [all_imports.pSG.Button(buttons_esp[1], key = 700, size = (26, 0)),
                         all_imports.pSG.Button(buttons_esp[2], key = 800, size = (26, 0))]]

    window_v_p_e_eng = all_imports.pSG.Window("EZPZ PGP - Import Message", import_v_p_e_eng, disable_close = True,
                                              element_justification = "center")
    window_v_p_e_esp = all_imports.pSG.Window("EZPZ PGP - Importar Mensaje", import_v_p_e_esp,
                                              disable_close = True, element_justification = "center")

    return window_v_p_e_eng, window_v_p_e_esp
