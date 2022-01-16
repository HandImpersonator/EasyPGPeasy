# EZPZ-PGP

This is a simple and easy to use PGP tool.

## Features

[X] Create new PGP Keypairs, able to choose between 4096 and 8192 bit keys.

[X] Paste from clipboard on all import windows.

[X] Import Public/Private PGP Keypairs.

[X] Import Message

[X] Import Signature

[X] Encrypt message.

[X] Decrypt message.

[ ] Sign messages.

[ ] Verify message.

[X] Switch language.

[ ] Share Public PGP Key button.

[X] Help.

## TODO

Add copy to clipboard buttons, several bug checks, error control, release to an executable.

## What you can do

You can create new PGP Keypairs, they'll be automatically saved in two separate files appropriately named in `src/Keys`, which will be used when Decrypting and signing messages. Please note, every time you create new Keypairs, the old ones will be overwritten.

Importing your previosuly created Keypairs is also something you can do, they'll be also named, in the folder `src/Imported`, and also rewritten with every import. Th imported public keys will be used in encrypting and verifying. Please note imported Private PGP keys will be saved in `src/Keys` as the tool doesn't recognize or use private keys elsewhere.

Encrypting, decrypting, signing and verifying messages (the latter two are WIP) using the created keys and imported keys where necessary.

Language change (only English and Spanish, I know no other languages).

A TL;DR short help window.

## How to use the tool

If you want to create a PGP Keypair, select the bit size to use and create it, it will automatically create a Keypair with a random name, surname and email. Created Keypairs will be overwritten on every button press and will be automatically saved in `./Keys`folder.

If you want to import a PGP Public Key to encrypt a message for someone, a message (encrypted or not) that you'd like to verify a signature of, and import the the signagture of the message you also imported, click the necessary buttons and import them. If they get imported incorrectly, they'll print out errors in future operations, there are some checks in place to prevent major errors during the import operations but I can't forsee everything. Imported keys, messages and signatures will be automatically saved with a correspondant name inside `./Imported` folder.

If you want to encrypt a message, you first need to import the PGP Public Key, otherwise it'd print and error of either missing PGP Public Key or Public Key incorrectly imported, then type or paste the message, click encrypt and in the output the encrypted message will show, it'll automatically save in a file in `./Messages` folder.

If you want to decrypt a message someone encrypted with your PGP Public Key, first, make sure the original Keypair of the Public Key you shared is still in place.
Paste the encrypted message, press decrpyt and voilà.

If you want to sign a message, you have two options, type a plaintext message and press sign, it'll sign the message with your PGP Public Key in the folder `./Keys`and save a copy of the signed message and the signature in `./Messages`, second option is to sign an encrypted message you created, it'll read the file of the encrypted message in `./Messages`that should have been previously created, it'll sign the message and automatically save the signature in that same folder.

If you want to verify a message, it should've been imported previously, along with the corresponding PGP Public Key to verify that signature, clicking the verify button will grab those two files, verify the signature matches and give a positive or negative result.

## Dependencies

You'll need xclip for the copy/paste to/from clipboard buttons to work.

### Ubuntu

`apt install xclip`

### Fedora

`dnf install xclip`

### Python

Python libraries used in this tool were:

PySimpleGUI, os, pgpy, png, pyclip, pyqrcode, random, string

Python libraries you'll need to install, with: `python -m pip install PySimpleGUI pgpy pypng pyclip pyqrcode`

## Usage

Execute `python EZPZ-PGP.py` and navigate through the menus. Expect bugs and errors it's still a WIP.

### Coffee

Last but not least, if you found the tool useful and would like to help me out and buy me a coffee, I've included the addresses in the tool that'll be copied to clipboard automatically. I'll paste them here too if that's allowed.

## ENJOY THE TOOL!
