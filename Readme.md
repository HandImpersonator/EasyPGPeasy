# EZPZ-PGP

This is a simple and easy (hopefully) to use PGP tool.

## Features

[X] Create new PGP Keypairs, able to choose between 4096, 8192 and 16384 (overkill perhaps) bit keys.

[X] Paste from clipboard.

[X] Import messages, PGP Public Keys and PGP Signatures.

[X] Encrypt, Decrypt, Sign and Verify files and messages.

[X] Switch language.

[X] Small help window.

## TODO

Release to a standalone executable.

## File directory structure

```bash
.
├── EZPZ-PGP.py
├── Imported
├── Keys
├── Output
│   ├── Decrypted
│   ├── Encrypted
│   ├── Signed
│   └── Verified
└── src
    ├── Functions
    │   ├── all_imp.py
    │   ├── create_pgp_pair.py
    │   ├── dec.py
    │   ├── edsv.py
    │   ├── enc.py
    │   ├── menu.py
    │   ├── sig.py
    │   └── ver.py
    └── Layouts
        ├── choose_layout.py
        ├── eds_layout.py
        ├── help_layout.py
        ├── imp_layout.py
        ├── lang_layout.py
        └── menu_layout.py

10 directories, 15 files
```

## Important file locations

- Private key: ```./Keys/private.asc```
- Public key: ```./Keys/public.asc```
- Imported Public key for encryption and verification: ```./Imported/v_imported_public.asc```
- Imported Messages (encrypted or plaintext): ```./Imported/v_imported_message.txt```
- imported Signatures for verification: ```./Imported/v_imported_signature.txt```
- Encrypted messages: ```./Output/Encrypted/encrypted_message.txt```
- Encrypted files: ```./Output/Encrypted/[original_filename.ext].pgp.PK```
- Decrypted messages: ```./Output/Decrypted/(auto_)decrypted_message.txt```
- Decrypted files: ```./Output/Decrypted/[original_filename.ext]```
- Signed plaintext messages: ```./Output/Signed/signed_text.txt```
- Signed encrypted messages: ```./Output/Signed/encrypted_signed.txt```
- Signed files: ```./Output/Signed/[original_filename.ext]_signature.txt```
- Verified texts: ```./Output/Verified/v_verified_message.txt```

## What the tool can do

Create new PGP Keypairs, they'll be automatically saved in two separate files appropriately named in `./Keys`, which will be used when Encrypting, Decrypting, Signing and Verifying signature files and messages. Please note, every time you create new Keypairs, the old ones will be overwritten. If you want to use your own Keypairs, create a new pair to check if the formatting and replace the content of the created ones with your own.

Imported Public PGP Keys, messages (in order to sign or verify them) and signatures (that correspond to the imported message) will be saved in `./Imported`, and also rewritten with every import. The imported public keys will be used in encrypting and verifying. Please note imported Private PGP keys will be saved in `./Imported`.

Encrypting, decrypting, signing and verifying files and messages using the created keys and imported keys where necessary.

Language change (only English and Spanish, I know no other languages).

A TL;DR short help window.

## How to use the tool

If you want to create a PGP Keypair, select the bit size to use, choose whether you want a random or your own name, surname and email, type a passphrase for your PGP Private Key and create it. It will automatically create a Keypair with the chosen name, surname and email. Created Keypairs will be overwritten on every button press and will be automatically saved in `./Keys` folder. Any operation that needs to use the PGP Private Key will ask for the passphrase.

You can import a message that was encrypted with your public key to automatically decrypt it, if the encrypted message was signed and you import the signature you can verify it, import a plaintext message and it's signature to verify it. 
You can import a PGP Public Key to encrypt a message.
All of the above also applies with files and everything imported will be in the folder `./Imported`.

If you want to encrypt a file/message, you first need to import the PGP Public Key, then type or paste the message, click encrypt and in the output the encrypted message will show and save in `./Output/Encrypted` folder.

If you want to decrypt a file/message someone encrypted with your PGP Public Key, first, paste the encrypted message, press decrypt, type the passphrase and voilà, if the encrypted message was imported, you can autodecrypt, you can also choose to decrypt a file you encrypted. Decrypted files amd messages will be saved in `./Output/Decrypted`.

If you want to sign a file/message, you can type a plaintext message, and press sign, you can automatically sign a message that was imported, be it plaintext or encrypted, or a file and will be saved in `./Output/Signed`. The signing operation requires you to type the PGP Private Key passphrase.

If you want to verify a file/message, you need import the message, import the PGP Public Key, import the signature along with the corresponding PGP Public Key to verify that message, if will give a positive or negative result and save the verified message in `./Output/Verified`, it will not save anything when verifying a file.

If anything goes wrong, an error will pop up and redirect you to the menu.
If the tool crashes please open a ticket, with clear instructions on your steps to encounter the issue and I'll try and replicate the issue on my end and fix it the best I can.

## Requirements

You'll need xclip for the copy/paste to/from clipboard actions to work.

### Ubuntu

`apt install python3-tk xclip`

### Fedora

`dnf install python3-tk xclip`

### Python dependecies

- Python 3.6+
- PySimpleGUI
- pgpy
- png
- pyclip
- pyqrcode

Install with: `python -m pip install PySimpleGUI pgpy pypng pyclip pyqrcode`

### Tails

If you wish to use it with TAILS, for whatever reason, follow the next steps to use it (not recommended).

```sudo torify apt-get update```

```sudo torify apt-get install python3-pip gcc zlib1g-dev python3-tk```

```torify python3 -m pip install setuptools wheel```

```torify python3 -m pip install pyinstaller pyclip pypng pgpy pyqrcode PySimpleGUI tk```

```python3 EZPZ-PGP.py```

What I do recommend is creating the release, copying it to a USB, rebooting TAILS so it's back to default TAILS and then executing the release from the home directory (if you have created Keypairs I suggest you have them on the USB to use them).

```pyinstaller -F EZPZ-PGP.py```

The release will be in the dist folder, make it executable and you're golden.

### Usage

Execute `python EZPZ-PGP.py` (or `python3 EZPZ-PGP.py` depends on your system) and navigate through the menus, or execute one of the releases.

### Releases

Tried on Fedora 34, Fedora 35, TAILS 4.27, several windows 10 builds (currently trying to build for Mac and try it).

### PGP Public Key

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
=2k/C
-----END PGP PUBLIC KEY BLOCK-----
```

## Credits

Thanks to the guys who wrote the following Python libraries/modules, couldn't have done it without their awesome code:
- https://github.com/SecurityInnovation/PGPy
- https://github.com/spyoungtech/pyclip
- https://github.com/drj11/pypng
- https://github.com/mnooner256/pyqrcode
- https://github.com/PySimpleGUI/PySimpleGUI

### Coffee

Last but not least, if you found the tool useful and would like to help me out and buy me a coffee, I've included the addresses in the tool that'll be copied to clipboard automatically whilst a 5 second popup shows a QR code you can scan.

#### Sidenote

UNIX users should have no issue, though I've only been able to test on Fedora, will continue testing.

Mac users, it should work like with UNIX users.

Windows users, only PDF and txt files work when encrypting and decrypting, other file formats aren't recoverable as far as I've tested.

## ENJOY THE TOOL!
