# help_layout.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imp


def crem_coffee():
    """Create coffee window layout.
    Returns coffee layout."""
    width = 65

    add = ["Bitcoin", "Ethereum", "Monero", "ZCash Transparent", "ZCash Shielded", "Algorand",
           "Alogrand Assets\n(HDL, YLDY, STBL, TREES)",
           "Harmony", "Litecoin", "Tezos", "Cosmos", "Stellar"]
    text_eng = ["\n", "Send only listed Assets, other Assets sent won't be received, they'll be lost.",
                "Clicking a button will copy the address to clipboard and show a QR.",
                "The QR code will show for 5 seconds.", "Thanks for the coffee! :)", "Menu"]
    text_esp = ["\n", "Manda sólo los Asset, otros Asset no se recibirán, se perderán.",
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
    width1 = 75
    width2 = 78

    text_eng = ["This is a very simple and easy to use PGP tool.\n",
                "· Folders will be created on the directory where the tool runs.",
                "· Create 4096, 8192 and 16384 bit PGP Keypair which get automatically saved in Keys folder.",
                "· Keys will be saved to files and overwritten on every creation.",
                "· Use your own keypair by changing contents of the created Key files.",
                "· All imports will be overwritten when you import new messages and PGP content.\n",
                "· Encrypt files and messages with an imported third-party Public key",
                "· Decrypt files and messages that were encrypted with your Public key.",
                "· Sign files and messages with the Private key inside Keys folder.",
                "· Verify signed file and messages with the imported message, Public key and Signature.\n",
                "· Language change is also available, though only english and spanish.\n",
                "If you really like the tool I created, you could help me by buying me a coffee if you want. :)"]
    buttons_eng = ["Buy coffee", "Menu"]
    texts_esp = ["Esta es una herramienta PGP my fácil de usar.",
                 "· Crear pares de claves de 4096, 8192 o 16384 bits que se guardan en la carpeta Keys.",
                 "· Las carpetas se crean automáticamente en el directorio donde se ejecute la herramienta.",
                 "· Las claves se guardan en ficheros en la carpeta Keys y se sobreescriben cada creación.",
                 "· Para usar tus propias claves cambia el contenido de las claves creadas.",
                 "· Todos los imports se sobreescriben cuando se importan nuevos mensajes y contenido PGP.\n",
                 "· Cifra ficheros y mensajes con la clave Pública importada de terceras personas.",
                 "· Descifra ficheros y mensajes que fueron cifrados con tu clave Pública.",
                 "· Firma ficheros y mensajes con la clave Privada den la carpeta Keys.",
                 "· Verifica la firma de ficheros y mensajes importando el mensaje firmado, la clave Pública y Firma.",
                 "\n· Se puede cambiar de idioma, pero solo entre español e inglés.\n",
                 "Si te gustó la herramienta que he creado, puedes apoyarme comprandome un café si quieres. :)"]
    buttons_esp = ["Comprar café", "Menú"]

    layout_help_eng = [[all_imp.pSG.Text(text_eng[0], justification = "left")],
                       [all_imp.pSG.Text(text_eng[1], justification = "left")],
                       [all_imp.pSG.Text(text_eng[2], justification = "left")],
                       [all_imp.pSG.Text(text_eng[3], justification = "left")],
                       [all_imp.pSG.Text(text_eng[4], justification = "left")],
                       [all_imp.pSG.Text(text_eng[5], justification = "left")],
                       [all_imp.pSG.Text(text_eng[6], justification = "left")],
                       [all_imp.pSG.Text(text_eng[7], justification = "left")],
                       [all_imp.pSG.Text(text_eng[8], justification = "left")],
                       [all_imp.pSG.Text(text_eng[9], justification = "left")],
                       [all_imp.pSG.Text(text_eng[10], justification = "left")],
                       [all_imp.pSG.Text(text_eng[11], justification = "left")],
                       [all_imp.pSG.Button(buttons_eng[0], focus = False, key = 666, size = (width1, 0))],
                       [all_imp.pSG.Button(buttons_eng[1], focus = False, key = 800, size = (width1, 0))]]
    layout_help_esp = [[all_imp.pSG.Text(texts_esp[0], justification = "left")],
                       [all_imp.pSG.Text(texts_esp[1], justification = "left")],
                       [all_imp.pSG.Text(texts_esp[2], justification = "left")],
                       [all_imp.pSG.Text(texts_esp[3], justification = "left")],
                       [all_imp.pSG.Text(texts_esp[4], justification = "left")],
                       [all_imp.pSG.Text(texts_esp[5], justification = "left")],
                       [all_imp.pSG.Text(texts_esp[6], justification = "left")],
                       [all_imp.pSG.Text(texts_esp[7], justification = "left")],
                       [all_imp.pSG.Text(texts_esp[8], justification = "left")],
                       [all_imp.pSG.Text(texts_esp[9], justification = "left")],
                       [all_imp.pSG.Text(texts_esp[10], justification = "left")],
                       [all_imp.pSG.Text(texts_esp[11], justification = "left")],
                       [all_imp.pSG.Button(buttons_esp[0], focus = False, key = 666, size = (width2, 0))],
                       [all_imp.pSG.Button(buttons_esp[1], focus = False, key = 800, size = (width2, 0))]]

    window_help_eng = all_imp.pSG.Window("EZPZ PGP - Short help window", layout_help_eng, disable_close = True)
    window_help_esp = all_imp.pSG.Window("EZPZ PGP - Ventana de ayuda rápida", layout_help_esp, disable_close = True)

    return window_help_eng, window_help_esp
