# create_pgp_pair.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imp


def get_random_string(length):
    """Choose a random string of a given length.
    Return random string."""
    # With combination of lower and upper case
    result_str = ''.join(all_imp.random.choice(all_imp.string.ascii_letters) for _ in range(length))
    return result_str


def pgpy_create_keypair(email, keys, lang, name, size, custom):
    """Create a keypair of a given size."""

    fin, real_email, real_name, values = "", None, None, {}

    # We can start by generating a primary key. For this example, we'll use RSA, but it could be DSA or ECDSA as well
    private = all_imp.pgpy.PGPKey.new(all_imp.PubKeyAlgorithm.RSAEncryptOrSign, size)

    if not name or not email:
        custom = False

    if custom:
        real_name = name
        real_email = email
    elif not custom:
        real_name = get_random_string(8) + " " + get_random_string(12)
        real_email = get_random_string(12) + "@fakersa.pokemon"

    # We now have some key material, but our new key doesn't have a user ID yet, and therefore is not yet usable!
    uid = all_imp.pgpy.PGPUID.new(real_name, email = real_email)

    # Now we must add the new user id to the key. We'll need to specify all of our preferences at this point
    # because PGPy doesn't have any built-in key preference defaults at this time
    # this example is similar to GnuPG 2.1.x defaults, with no expiration or preferred keyserver.

    private.add_uid(uid, usage = {all_imp.KeyFlags.Sign, all_imp.KeyFlags.EncryptCommunications,
                                  all_imp.KeyFlags.EncryptStorage},
                    hashes = [all_imp.HashAlgorithm.SHA512], ciphers = [all_imp.SymmetricKeyAlgorithm.AES256],
                    compression = [all_imp.CompressionAlgorithm.BZ2])

    choose_pass_eng, choose_pass_esp = all_imp.choose_layout.crem_pass()
    if lang == "eng":
        event, values = choose_pass_eng.read()
    elif lang == "esp":
        event, values = choose_pass_esp.read()
    password = values["pass"]
    choose_pass_eng.close()
    choose_pass_esp.close()

    private.protect(password, all_imp.SymmetricKeyAlgorithm.AES256, all_imp.HashAlgorithm.SHA512)

    public = private.pubkey

    text_file_private = open(keys + "/private.asc", "w")
    text_file_private.write(str(private))
    text_file_private.close()
    text_file_public = open(keys + "/public.asc", "w")
    text_file_public.write(str(public))
    text_file_public.close()

    if lang == "eng":
        fin = "Done! Saved in folder Keys."
    elif lang == "esp":
        fin = "¡Hecho! Guardado en carpeta Keys."
    all_imp.pSG.popup_auto_close(fin, auto_close_duration = 1.2, button_type = 5, title = fin)
