# EZPZ-PGP

This is a simple and easy to use PGP tool.

## Features

[X] Create new PGP Keypairs, able to choose between 4096, 8192 and 16384 (overkill) bit keys.

[X] Paste from clipboard.

[X] Import messages, PGP Public Keys and PGP Signatures.

[X] Encrypt, Decrypt, Sign and Verify files and messages.

[X] Switch language.

[X] Small help window.

## TODO

Release to an executable.

## What the tool can do

Create new PGP Keypairs, they'll be automatically saved in two separate files appropriately named in `src/Keys`, which will be used when Encrypting, Decrypting, Signing and Verifying signature files and messages. Please note, every time you create new Keypairs, the old ones will be overwritten. If you want to use your own Keypairs, create a new pair to check if the formatting and replace the content of the created ones with your own.

Imported Public PGP Keys, messages (in order to sign or verify them) and signatures (that correspond to the imported message) will be saved in `src/Imported`, and also rewritten with every import. The imported public keys will be used in encrypting and verifying. Please note imported Private PGP keys will be saved in `src/Imported`.

Encrypting, decrypting, signing and verifying files and messages using the created keys and imported keys where necessary.

Language change (only English and Spanish, I know no other languages).

A TL;DR short help window.

## How to use the tool

If you want to create a PGP Keypair, select the bit size to use, choose whether you want a random or your own name, surname and email, type a passphrase for your PGP Private Key and create it. It will automatically create a Keypair with the chosen name, surname and email. Created Keypairs will be overwritten on every button press and will be automatically saved in `./Keys`folder. Any operation that needs to use the PGP Private Key will ask for the passphrase.

You can import a message that was encrypted with your public key to automatically decrypt it, if the encrypted message was signed and you import the signature you can verify it, import a plaintext message and it's signature to verify it. 
You can import a PGP Public Key to encrypt a message.
All of the above also applies with files and everything imported with be in the folder `./Imported`

If you want to encrypt a file/message, you first need to import the PGP Public Key, then type or paste the message, click encrypt and in the output the encrypted message will show and save in `./Output/Encrypted` folder.

If you want to decrypt a file/message someone encrypted with your PGP Public Key, first, paste the encrypted message, press decrypt, type the passphrase and voilà, if the encrypted message was imported, you can autodecrypt, you can also choose to decrypt a file you encrypted. Decrypted files amd messages will be saved in `./Output/Decrypted`.

If you want to sign a file/message, you can type a plaintext message, and press sign, you can automatically sign a message that was imported, be it plaintext or encrypted, or a file and will be saved in `./Output/Signed`. The signing operation requires you to type the PGP Private Key passphrase.

If you want to verify a file/message, you need import the message, import the PGP Public Key, import the signature along with the corresponding PGP Public Key to verify that message, if will give a positive or negative result and save the verified message in `./Output/Verified`, it will not save anything when verifying a file.

If anything goes wrong, an error will pop up and redirect you to the menu.
If the tool crashes please open a ticket, with clear instructions on your steps to encounter the issue and I'll try and replicate the issue on my end and fix it the best I can.

## Dependencies

You'll need xclip for the copy/paste to/from clipboard actions to work.

### Ubuntu

`apt install python-tk xclip`

### Fedora

`dnf install python-tk xclip`

### Python

Python libraries used in this tool were:

PySimpleGUI, os, pgpy, png, pyclip, pyqrcode, random, string

Python libraries you'll need to install, with: `python -m pip install PySimpleGUI pgpy pypng pyclip pyqrcode`

## Usage

Execute `python EZPZ-PGP.py` and navigate through the menus..

### Coffee

Last but not least, if you found the tool useful and would like to help me out and buy me a coffee, I've included the addresses in the tool that'll be copied to clipboard automatically whilst a 5 second popup shows a QR code you can scan.

## ENJOY THE TOOL!
