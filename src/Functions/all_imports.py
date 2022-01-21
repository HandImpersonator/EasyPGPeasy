# all_imports.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

# CODE NUMBERS
"""
1 -12: Show Coffee Addresses
15: Encrypt mode
20: Decrypt mode
30: Sign mode
40: Verify mode
50: Plaintext sign mode
60: Automatic sign mode
70: Manual decrypt mode
80: Automatic decrypt mode
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
from src.Functions import coffee_create, create_pgp_pair, decrypt_choose_create, enc_dec, enc_dec_create
from src.Functions import help_create, import_enc_create, import_pub_create, import_sig_create, kp_choose_create
from src.Functions import language_create, menu, menu_create, ne_choose_create, sign_choose_create
import os
import pgpy
import png
import pyclip
import pyqrcode
import random
import string

from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
