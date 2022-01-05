# coffee_create.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports


def create_remove_coffee():
    """Create coffee window lavyout.
    Returns coffee layout."""
    width = 60

    add = ["BTC", "ETH", "XMR", "ZEC Transparent", "ZEC Shielded", "ALGO", "ALGO ASA",
           "\n(HDL, YLDY, CryptoTrees, STBL)", "ONE", "LTC", "XTZ", "ATOM", "XLM"]
    text_eng = ["\n", "Send only listed ASA on ALSO ASA, other ASA sent won't be received, and be lost.",
                "Clicking a button will copy the address to clipboard and show a QR.",
                "The QR code will show for 5 seconds.", "Thanks for the coffee! :)", "Menu"]
    text_esp = ["\n", "Manda sólo los ASA listados, otros ASA no se recibirán, se perderán.",
                "Haciendo click en cada botón copiará la dirección y mostrará un QR.",
                "El código QR se mostrará durante 5 segundos.", "¡Gracias por el café! :)", "Menu"]

    layout_coffee_eng = [[all_imports.pSG.Button(add[0], key = 1, size = (width, 0))],
                         [all_imports.pSG.Button(add[1], key = 2, size = (width, 0))],
                         [all_imports.pSG.Button(add[2], key = 3, size = (width, 0))],
                         [all_imports.pSG.Button(add[3], key = 4, size = (width, 0))],
                         [all_imports.pSG.Button(add[4], key = 5, size = (width, 0))],
                         # ZCash t1Y2UiuGFLNYQMtcW4dpbKmsuoQ1hVnhyeE
                         [all_imports.pSG.Button(add[5], key = 6, size = (width, 0))],
                         [all_imports.pSG.Button(add[6], key = 7, size = (width, 0))],
                         [all_imports.pSG.Button(add[7], key = 8, size = (width, 0))],
                         [all_imports.pSG.Button(add[8], key = 9, size = (width, 0))],
                         [all_imports.pSG.Button(add[9], key = 10, size = (width, 0))],
                         [all_imports.pSG.Button(add[10], key = 11, size = (width, 0))],
                         [all_imports.pSG.Button(add[11], key = 12, size = (width, 0))],
                         [all_imports.pSG.Text(text_eng[0])], [all_imports.pSG.Text(text_eng[1])],
                         [all_imports.pSG.Text(text_eng[2])], [all_imports.pSG.Text(text_eng[3])],
                         [all_imports.pSG.Text(text_eng[4])],
                         [all_imports.pSG.Button(add[12], key = 800, size = (width, 0))]]
    layout_coffee_esp = [[all_imports.pSG.Button(add[0], key = 1, size = (width, 0))],
                         [all_imports.pSG.Button(add[1], key = 2, size = (width, 0))],
                         [all_imports.pSG.Button(add[2], key = 3, size = (width, 0))],
                         [all_imports.pSG.Button(add[3], key = 4, size = (width, 0))],
                         [all_imports.pSG.Button(add[4], key = 5, size = (width, 0))],
                         [all_imports.pSG.Button(add[5], key = 6, size = (width, 0))],
                         [all_imports.pSG.Button(add[6], key = 7, size = (width, 0))],
                         [all_imports.pSG.Button(add[7], key = 8, size = (width, 0))],
                         [all_imports.pSG.Button(add[8], key = 9, size = (width, 0))],
                         [all_imports.pSG.Button(add[9], key = 10, size = (width, 0))],
                         [all_imports.pSG.Button(add[10], key = 11, size = (width, 0))],
                         [all_imports.pSG.Button(add[11], key = 12, size = (width, 0))],
                         [all_imports.pSG.Text(text_esp[0])], [all_imports.pSG.Text(text_esp[1])],
                         [all_imports.pSG.Text(text_esp[2])], [all_imports.pSG.Text(text_esp[3])],
                         [all_imports.pSG.Text(text_esp[4])],
                         [all_imports.pSG.Button(add[12], key = 800, size = (width, 0))]]

    window_coffee_eng = all_imports.pSG.Window("EZPZ PGP - Buy me a coffee", layout_coffee_eng, disable_close = True,
                                               element_justification = "center")
    window_coffee_esp = all_imports.pSG.Window("EZPZ PGP - Cómprame un café", layout_coffee_esp, disable_close = True,
                                               element_justification = "center")

    return window_coffee_eng, window_coffee_esp
