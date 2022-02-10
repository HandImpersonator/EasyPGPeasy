# help_layout.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imp


def crem_coffee():
    """Create coffee window layout.
    Returns coffee layout."""
    width = 65

    add = ["Bitcoin", "Ethereum", "Monero", "ZCash Transparent", "ZCash Shielded", "Algorand", "Alogrand Assets",
           "Harmony", "Litecoin", "Tezos", "Cosmos", "Stellar"]
    text_eng = ["\n", "Send only listed ASA on ALSO ASA, other ASA sent won't be received, and be lost.",
                "Clicking a button will copy the address to clipboard and show a QR.",
                "The QR code will show for 5 seconds.", "Thanks for the coffee! :)", "Menu"]
    text_esp = ["\n", "Manda sólo los ASA listados, otros ASA no se recibirán, se perderán.",
                "Haciendo click en cada botón copiará la dirección y mostrará un QR.",
                "El código QR se mostrará durante 5 segundos.", "¡Gracias por el café! :)", "Menu"]

    layout_coffee_eng = [[all_imp.pSG.Button(add[0], focus = False, key = 1, size = (width, 0))],
                         [all_imp.pSG.Button(add[1], focus = False, key = 2, size = (width, 0))],
                         [all_imp.pSG.Button(add[2], focus = False, key = 3, size = (width, 0))],
                         [all_imp.pSG.Button(add[3], focus = False, key = 4, size = (width, 0))],
                         [all_imp.pSG.Button(add[4], focus = False, key = 5, size = (width, 0))],
                         [all_imp.pSG.Button(add[5], focus = False, key = 6, size = (width, 0))],
                         [all_imp.pSG.Button(add[6], focus = False, key = 7, size = (width, 0))],
                         [all_imp.pSG.Button(add[7], focus = False, key = 8, size = (width, 0))],
                         [all_imp.pSG.Button(add[8], focus = False, key = 9, size = (width, 0))],
                         [all_imp.pSG.Button(add[9], focus = False, key = 10, size = (width, 0))],
                         [all_imp.pSG.Button(add[10], focus = False, key = 11, size = (width, 0))],
                         [all_imp.pSG.Button(add[11], focus = False, key = 12, size = (width, 0))],
                         [all_imp.pSG.Text(text_eng[0])], [all_imp.pSG.Text(text_eng[1])],
                         [all_imp.pSG.Text(text_eng[2])], [all_imp.pSG.Text(text_eng[3])],
                         [all_imp.pSG.Text(text_eng[4])],
                         [all_imp.pSG.Button(text_eng[5], focus = False, key = 800, size = (width, 0))]]
    layout_coffee_esp = [[all_imp.pSG.Button(add[0], focus = False, key = 1, size = (width, 0))],
                         [all_imp.pSG.Button(add[1], focus = False, key = 2, size = (width, 0))],
                         [all_imp.pSG.Button(add[2], focus = False, key = 3, size = (width, 0))],
                         [all_imp.pSG.Button(add[3], focus = False, key = 4, size = (width, 0))],
                         [all_imp.pSG.Button(add[4], focus = False, key = 5, size = (width, 0))],
                         [all_imp.pSG.Button(add[5], focus = False, key = 6, size = (width, 0))],
                         [all_imp.pSG.Button(add[6], focus = False, key = 7, size = (width, 0))],
                         [all_imp.pSG.Button(add[7], focus = False, key = 8, size = (width, 0))],
                         [all_imp.pSG.Button(add[8], focus = False, key = 9, size = (width, 0))],
                         [all_imp.pSG.Button(add[9], focus = False, key = 10, size = (width, 0))],
                         [all_imp.pSG.Button(add[10], focus = False, key = 11, size = (width, 0))],
                         [all_imp.pSG.Button(add[11], focus = False, key = 12, size = (width, 0))],
                         [all_imp.pSG.Text(text_esp[0])], [all_imp.pSG.Text(text_esp[1])],
                         [all_imp.pSG.Text(text_esp[2])], [all_imp.pSG.Text(text_esp[3])],
                         [all_imp.pSG.Text(text_esp[4])],
                         [all_imp.pSG.Button(text_esp[5], focus = False, key = 800, size = (width, 0))]]

    window_coffee_eng = all_imp.pSG.Window("EZPZ PGP - Buy me a coffee", layout_coffee_eng, disable_close = True,
                                           element_justification = "center")
    window_coffee_esp = all_imp.pSG.Window("EZPZ PGP - Cómprame un café", layout_coffee_esp, disable_close = True,
                                           element_justification = "center")

    return window_coffee_eng, window_coffee_esp


def crem_help():
    """Create help window layout.
    Return created layout."""
    width = 76

    text_eng = ["This is a very simple and easy to use PGP tool. You can:",
                "· Create 4096, 8192 and 16384 bit PGP Keypair which get automatically saved",
                "in a file each, in Keys folder.", "· Folders will be created on the directory where the tool runs.",
                "\n", "· Encrypt messages and files with an imported third-party Public key",
                "· Decrypt messages and files that were encrypted with your created Public key.",
                "· Sign messages and files with the Private key inside Keys folder.",
                "· Verify signed messages and files with the imported Public key.",
                "· Use your own keypair by changing contents of the created key files.", "\n",
                "· Keys will be saved to files and overwritten on every creation.",
                "· Imported pubkeys will also be rewritten when you import new keys.", "\n",
                "· Language change is also available, though only english and spanish.", "\n",
                "If you really like the tool I created, you could help me by buying me a coffee if you want. :)"]
    buttons_eng = ["Buy coffee", "Menu"]
    texts_esp = ["Esta es una herramienta PGP my fácil de usar.", "Puedes:",
                 "· Crear pares de claves de 4096, 8192 o 16384 bits que se guardan",
                 "automáticamente en un fichero cada uno en la carpeta Keys.",
                 "· Las carpetas se crean automáticamente en el directorio.", "donde se ejecute la herramienta.", "\n",
                 "· Cifra mensajes con una clave pública importada de terceras personas.",
                 "· Descifra mensajes que fueron cifrados con tu clave pública.",
                 "· Cambia el contenido de las claves creadas, usa tus propias claves.", "\n",
                 "· Las claves se guardan en ficheros y se sobreescriben cada creación.",
                 "· Las claves públicas importadas también se sobreescriben cuando se",
                 "  importan nuevas claves públicas.", "\n",
                 "· Se puede cambiar de idioma, pero solo entre español e inglés.", "\n",
                 "Si te gustó la herramienta que he creado, puedes apoyarme comprandome un café si quieres. :)"]
    buttons_esp = ["Comprar café", "Menú"]

    layout_help_eng = [[all_imp.pSG.Text(text_eng[0])], [all_imp.pSG.Text(text_eng[1])],
                       [all_imp.pSG.Text(text_eng[2])], [all_imp.pSG.Text(text_eng[3])],
                       [all_imp.pSG.Text(text_eng[4])], [all_imp.pSG.Text(text_eng[5])],
                       [all_imp.pSG.Text(text_eng[6])], [all_imp.pSG.Text(text_eng[7])],
                       [all_imp.pSG.Text(text_eng[8])], [all_imp.pSG.Text(text_eng[9])],
                       [all_imp.pSG.Text(text_eng[10])], [all_imp.pSG.Text(text_eng[11])],
                       [all_imp.pSG.Text(text_eng[12])], [all_imp.pSG.Text(text_eng[13])],
                       [all_imp.pSG.Text(text_eng[14])], [all_imp.pSG.Text(text_eng[15])],
                       [all_imp.pSG.Text(text_eng[16])],
                       [all_imp.pSG.Button(buttons_eng[0], focus = False, key = 666, size = (width, 0))],
                       [all_imp.pSG.Button(buttons_eng[1], focus = False, key = 800, size = (width, 0))]]
    layout_help_esp = [[all_imp.pSG.Text(texts_esp[0])], [all_imp.pSG.Text(texts_esp[1])],
                       [all_imp.pSG.Text(texts_esp[2])], [all_imp.pSG.Text(texts_esp[3])],
                       [all_imp.pSG.Text(texts_esp[4])], [all_imp.pSG.Text(texts_esp[5])],
                       [all_imp.pSG.Text(texts_esp[6])], [all_imp.pSG.Text(texts_esp[7])],
                       [all_imp.pSG.Text(texts_esp[8])], [all_imp.pSG.Text(texts_esp[9])],
                       [all_imp.pSG.Text(texts_esp[10])], [all_imp.pSG.Text(texts_esp[11])],
                       [all_imp.pSG.Text(texts_esp[12])], [all_imp.pSG.Text(texts_esp[13])],
                       [all_imp.pSG.Text(texts_esp[14])], [all_imp.pSG.Text(texts_esp[15])],
                       [all_imp.pSG.Button(buttons_esp[0], focus = False, key = 666, size = (width, 0))],
                       [all_imp.pSG.Button(buttons_esp[1], focus = False, key = 800, size = (width, 0))]]

    window_help_eng = all_imp.pSG.Window("EZPZ PGP - Short help window", layout_help_eng, disable_close = True,
                                         element_justification = "center")
    window_help_esp = all_imp.pSG.Window("EZPZ PGP - Ventana de ayuda rápida", layout_help_esp, disable_close = True,
                                         element_justification = "center")

    return window_help_eng, window_help_esp
