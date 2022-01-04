# menu.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import all_imports


def create_remove_coffee():
    width = 60

    layout_coffee_eng = [[all_imports.pSG.Button("BTC", key = 1, size = (width, 0))],
                         [all_imports.pSG.Button("ETH", key = 2, size = (width, 0))],
                         [all_imports.pSG.Button("XMR", key = 3, size = (width, 0))],
                         [all_imports.pSG.Button("ZEC Transparent", key = 4, size = (width, 0))],
                         # ZCash t1Y2UiueGFLNYQMtcW4dpbKmsuoQ1hVnhyeE
                         [all_imports.pSG.Button("ZEC Shielded", key = 5, size = (width, 0))],
                         # ZCash t1Y2UiuGFLNYQMtcW4dpbKmsuoQ1hVnhyeE
                         [all_imports.pSG.Button("ALGO", key = 6, size = (width, 0))], [
                             all_imports.pSG.Button("ALGO ASA\n(HDL, YLDY, CryptoTrees, STBL)", key = 7,
                                                    size = (width, 0))],
                         [all_imports.pSG.Button("ONE", key = 8, size = (width, 0))],
                         [all_imports.pSG.Button("LTC", key = 9, size = (width, 0))],
                         [all_imports.pSG.Button("XTZ", key = 10, size = (width, 0))],
                         [all_imports.pSG.Button("ATOM", key = 11, size = (width, 0))],
                         [all_imports.pSG.Button("XLM", key = 12, size = (width, 0))], [all_imports.pSG.Text("\n")],
                         [all_imports.pSG.Text("Send only listed ASA on ALSO ASA, other ASA sent won't be received.")],
                         [all_imports.pSG.Text("Clicking a button will copy the address to clipboard and show a QR.")],
                         [all_imports.pSG.Text("The QR code will show for 5 seconds.")],
                         [all_imports.pSG.Text("Thanks for the coffee! :)")],
                         [all_imports.pSG.Button("Menu", key = 800, size = (width, 0))]]
    layout_coffee_esp = [[all_imports.pSG.Button("BTC", key = 1, size = (width, 0))],
                         [all_imports.pSG.Button("ETH", key = 2, size = (width, 0))],
                         [all_imports.pSG.Button("XMR", key = 3, size = (width, 0))],
                         [all_imports.pSG.Button("ZEC Transparent", key = 4, size = (width, 0))],
                         # ZCash t1Y2UiuGFLNYQMtcW4dpbKmsuoQ1hVnhyeE
                         [all_imports.pSG.Button("ZEC Shielded", key = 5, size = (width, 0))],
                         # ZCash t1Y2UiuGFLNYQMtcW4dpbKmsuoQ1hVnhyeE
                         [all_imports.pSG.Button("ALGO", key = 6, size = (width, 0))], [
                             all_imports.pSG.Button("ALGO ASA\n(HDL, YLDY, CryptoTrees, STBL)", key = 7,
                                                    size = (width, 0))],
                         [all_imports.pSG.Button("ONE", key = 8, size = (width, 0))],
                         [all_imports.pSG.Button("LTC", key = 9, size = (width, 0))],
                         [all_imports.pSG.Button("XTZ", key = 10, size = (width, 0))],
                         [all_imports.pSG.Button("ATOM", key = 11, size = (width, 0))],
                         [all_imports.pSG.Button("XLM", key = 12, size = (width, 0))], [all_imports.pSG.Text("\n")],
                         [all_imports.pSG.Text("Manda sólo los ASA listados, otros ASA no se recibirán, se perderán.")],
                         [all_imports.pSG.Text("Haciendo click en cada botón copiará la dirección y mostrará un QR.")],
                         [all_imports.pSG.Text("El código QR se mostrará durante 5 segundos.")],
                         [all_imports.pSG.Text("¡Gracias por el café! :)")],
                         [all_imports.pSG.Button("Menú", key = 800, size = (width, 0))]]

    window_coffee_eng = all_imports.pSG.Window("EZPZ PGP - Buy me a coffee", layout_coffee_eng, disable_close = True,
                                               element_justification = "center")
    window_coffee_esp = all_imports.pSG.Window("EZPZ PGP - Cómprame un café", layout_coffee_esp, disable_close = True,
                                               element_justification = "center")

    return window_coffee_eng, window_coffee_esp
