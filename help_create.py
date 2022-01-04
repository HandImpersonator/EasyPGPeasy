# menu.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import all_imports


def create_remove_help():
    width = 76

    layout_help_eng = [[all_imports.pSG.Text("This is a very simple and easy to use PGP tool.")],
                       [all_imports.pSG.Text("You can:")],
                       [all_imports.pSG.Text("· Create 4096 and 8192 bit PGP keypair which get automatically saved")],
                       [all_imports.pSG.Text("in a file each, in Keys folder.")],
                       [all_imports.pSG.Text("· Folders will be created on the directory where the tool runs.")],
                       [all_imports.pSG.Text("\n")],
                       [all_imports.pSG.Text("· Encrypt messages with an imported third-party public key")],
                       [all_imports.pSG.Text("· Decrypt messages that were encrypted with your created public key.")],
                       [all_imports.pSG.Text("· Use your own keypair by changing contents of the created key files.")],
                       [all_imports.pSG.Text("\n")],
                       [all_imports.pSG.Text("· Keys will be saved to files and overwritten on every creation.")],
                       [all_imports.pSG.Text("· Imported publkeys will also be rewritten when you import new keys.")],
                       [all_imports.pSG.Text("\n")],
                       [all_imports.pSG.Text("· Language change is also available, though only english and spanish.")],
                       [all_imports.pSG.Text("\n")],
                       [all_imports.pSG.Text("If you really like the tool I created, you could help me by"
                                             "buying me a coffee if you want. :)")],
                       [all_imports.pSG.Button("Coffee", key = 666, size = (width, 0))],
                       [all_imports.pSG.Button("Menu", key = 800, size = (width, 0))]]
    layout_help_esp = [[all_imports.pSG.Text("Esta es una herramienta PGP my fácil de usar.")],
                       [all_imports.pSG.Text("Puedes:")],
                       [all_imports.pSG.Text("· Crear pares de claves de 4096 and 8192 bits que se guardan")],
                       [all_imports.pSG.Text("automáticamente en un fichero cada uno en la carpeta Keys.")],
                       [all_imports.pSG.Text("· Las carpetas se crean automáticamente en el directorio.")],
                       [all_imports.pSG.Text("donde se ejecute la herramienta.")], [all_imports.pSG.Text("\n")],
                       [all_imports.pSG.Text("· Cifra mensajes con una clave pública importada de terceras personas.")],
                       [all_imports.pSG.Text("· Descifra mensajes que fueron cifrados con tu clave pública.")],
                       [all_imports.pSG.Text("· Cambia el contenido de las claves creadas, usa tus propias claves.")],
                       [all_imports.pSG.Text("\n")],
                       [all_imports.pSG.Text("· Las claves se guardan en ficheros y se sobreescriben cada creación.")],
                       [all_imports.pSG.Text("· Las claves públicas importadas también se sobreescriben cuando se")],
                       [all_imports.pSG.Text("  importan nuevas claves públicas.")], [all_imports.pSG.Text("\n")],
                       [all_imports.pSG.Text("· Se puede cambiar de idioma, pero solo entre español e inglés.")],
                       [all_imports.pSG.Text("\n")],
                       [all_imports.pSG.Text("Si te gustó la herramienta que he creado, puedes apoyarme comprandome un "
                                             "café si quieres. :)")],
                       [all_imports.pSG.Button("Café", key = 666, size = (width, 0))],
                       [all_imports.pSG.Button("Menú", key = 800, size = (width, 0))]]

    window_help_eng = all_imports.pSG.Window("EZPZ PGP - Buy me a coffee", layout_help_eng, disable_close = True,
                                             element_justification = "center")
    window_help_esp = all_imports.pSG.Window("EZPZ PGP - Cómprame un café", layout_help_esp, disable_close = True,
                                             element_justification = "center")

    return window_help_eng, window_help_esp
