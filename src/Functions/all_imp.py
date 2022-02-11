# all_imp.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

# CODE NUMBERS
"""
1 - 12: Show Coffee Addresses
15: Encrypt mode
20: Decrypt mode
30: Sign mode
40: Verify mode
14: Encrypt message mode
16: Encrypt file mode
24: Manual decrypt mode
25: File decrypt mode
26: Automatic decrypt mode
34: Plaintext sign mode
35: Encrypted message sign mode
36: File sign mode
44: Automatic verify mode
46: Verify file mode
100: Create PGP Keypair
110: Import message mode
112: Import Public Key mode
114: Import Signature mode
200: Choose encrypt mode
300: Choose decrypt mode
250: Choose sign mode
350: Choose verify mode
400: Choose language mode
454: English language
455: Spanish language
500: Show help mode
600: Exit
660: Create custom
666: Show coffee mode
700: Import confirm
800: Show Menu mode
"""

"""Contains all imports necessary."""

import PySimpleGUI as pSG
from src.Functions import create_pgp_pair, dec, edsv, enc, menu, sig, ver
from src.Layouts import choose_layout, eds_layout, help_layout, imp_layout, lang_layout, menu_layout
from pgpy.constants import CompressionAlgorithm, HashAlgorithm, KeyFlags, PubKeyAlgorithm,SymmetricKeyAlgorithm
import os, pgpy, png, pyclip, pyqrcode, random, string, sys, time
