# help_create.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports


def create_remove_help():
    """Create help window layout.
    Return created layout."""
    width = 76

    text_eng = ["This is a very simple and easy to use PGP tool.", "You can:",
                "· Create 4096 and 8192 bit PGP keypair which get automatically saved",
                "in a file each, in Keys folder.", "· Folders will be created on the directory where the tool runs.",
                "\n", "· Encrypt messages with an imported third-party public key",
                "· Decrypt messages that were encrypted with your created public key.",
                "· Use your own keypair by changing contents of the created key files.", "\n",
                "· Keys will be saved to files and overwritten on every creation.",
                "· Imported pubkeys will also be rewritten when you import new keys.", "\n",
                "· Language change is also available, though only english and spanish.", "\n",
                "If you really like the tool I created, you could help me by buying me a coffee if you want. :)"]
    buttons_eng = ["Coffee", "Menu"]
    texts_esp = ["Esta es una herramienta PGP my fácil de usar.", "Puedes:",
                 "· Crear pares de claves de 4096 and 8192 bits que se guardan",
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
    buttons_esp = ["Café", "Menú"]

    layout_help_eng = [[all_imports.pSG.Text(text_eng[0])], [all_imports.pSG.Text(text_eng[1])],
                       [all_imports.pSG.Text(text_eng[2])], [all_imports.pSG.Text(text_eng[3])],
                       [all_imports.pSG.Text(text_eng[4])], [all_imports.pSG.Text(text_eng[5])],
                       [all_imports.pSG.Text(text_eng[6])], [all_imports.pSG.Text(text_eng[7])],
                       [all_imports.pSG.Text(text_eng[8])], [all_imports.pSG.Text(text_eng[9])],
                       [all_imports.pSG.Text(text_eng[10])], [all_imports.pSG.Text(text_eng[11])],
                       [all_imports.pSG.Text(text_eng[12])], [all_imports.pSG.Text(text_eng[13])],
                       [all_imports.pSG.Text(text_eng[14])], [all_imports.pSG.Text(text_eng[15])],
                       [all_imports.pSG.Button(buttons_eng[0], focus = False, key = 666, size = (width, 0))],
                       [all_imports.pSG.Button(buttons_eng[1], focus = False, key = 800, size = (width, 0))]]
    layout_help_esp = [[all_imports.pSG.Text(texts_esp[0])], [all_imports.pSG.Text(texts_esp[1])],
                       [all_imports.pSG.Text(texts_esp[2])], [all_imports.pSG.Text(texts_esp[3])],
                       [all_imports.pSG.Text(texts_esp[4])], [all_imports.pSG.Text(texts_esp[5])],
                       [all_imports.pSG.Text(texts_esp[6])], [all_imports.pSG.Text(texts_esp[7])],
                       [all_imports.pSG.Text(texts_esp[8])], [all_imports.pSG.Text(texts_esp[9])],
                       [all_imports.pSG.Text(texts_esp[10])], [all_imports.pSG.Text(texts_esp[11])],
                       [all_imports.pSG.Text(texts_esp[12])], [all_imports.pSG.Text(texts_esp[13])],
                       [all_imports.pSG.Text(texts_esp[14])], [all_imports.pSG.Text(texts_esp[15])],
                       [all_imports.pSG.Button(buttons_esp[0], focus = False, key = 666, size = (width, 0))],
                       [all_imports.pSG.Button(buttons_esp[1], focus = False, key = 800, size = (width, 0))]]

    window_help_eng = all_imports.pSG.Window("EZPZ PGP - Short help window", layout_help_eng, disable_close = True,
                                             element_justification = "center")
    window_help_esp = all_imports.pSG.Window("EZPZ PGP - Ventana de ayuda corta", layout_help_esp, disable_close = True,
                                             element_justification = "center")

    return window_help_eng, window_help_esp
