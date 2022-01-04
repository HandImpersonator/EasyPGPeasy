# EZPZ-PGP

This is a simple and easy to use PGP tool.

## Features

[X] Create new PGP Keypairs, able to choose between 4096 and 8192 bit keys.\n

[X] Import Public/Private PGP Keypairs.

[X] Encrypt messages.

[X] Decrypt messages.

[ ] Sign messages.

[ ] Verify messages.

[X] Switch languages.

[ ] Share Public PGP Key button.

[X] Help.

## TODO

Add copy to clipboard buttons, several bug checks, error control, release to an executable.

## What you can do

You can create new PGP Keypairs, they'll be automatically saved in two separate files appropriately named in `src/Keys`, which will be used when Descrypting and signing messages. Please note, every time you create new Keypairs, the old ones will be overwritten.

Importing your previosuly created Keypairs is also something you can do, they'll be also named, in the folder `src/Imported`, and also rewritten with every import. Th imported public keys will be used in encrypting and verifying. Please note imported Private PGP keys will be saved in `src/Keys` as the tool doesn't recognize or use private keys elsewhere.

Encrypting, decrypting, signing and verifying messages (the latter two are WIP) using the created keys and imported keys where necessary.

Language change (only English and Spanish, I know no other languages).

A TL;DR short help window.

## Dependencies

Python libraries used in this tool were:

PySimpleGUI, os, pgpy, png, pyclip, pyqrcode, random, string

Python libraries you'll need to install, with: `python -m pip install PySimpleGUI pgpy pypng pyclip pyqrcode`

## Usage

Execute `python EZPZ-PGP.py` and navigate through the menus.

### Coffee

Last but not least, if you found the tool useful and would like to help me out and buy me a coffee, I've included the addresses in the tool that'll be copied to clipboard automatically. I'll paste them here too if that's allowed.

## ENJOY THE TOOL!
