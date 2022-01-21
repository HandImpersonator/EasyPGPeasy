# create_pgp_pair.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports

"""Creates a keypair of given key length."""


def get_random_string(length):
    """Choose a random string of a given length.
    Return random string."""
    # With combination of lower and upper case
    result_str = ''.join(all_imports.random.choice(all_imports.string.ascii_letters) for _ in range(length))
    return result_str


def pgpy_create_keypair(email, keys, name, size, custom):
    """Create a keypair of a given size."""

    real_email, real_name = None, None

    # We can start by generating a primary key. For this example, we'll use RSA, but it could be DSA or ECDSA as well
    private = all_imports.pgpy.PGPKey.new(all_imports.PubKeyAlgorithm.RSAEncryptOrSign, size)

    if not name or not email:
        custom = False

    if custom:
        real_name = name
        real_email = email
    elif not custom:
        real_name = get_random_string(8) + " " + get_random_string(12)
        real_email = get_random_string(12) + "@fakersa.pokemon"

    # We now have some key material, but our new key doesn't have a user ID yet, and therefore is not yet usable!
    uid = all_imports.pgpy.PGPUID.new(real_name, email = real_email)

    # Now we must add the new user id to the key. We'll need to specify all of our preferences at this point
    # because PGPy doesn't have any built-in key preference defaults at this time
    # this example is similar to GnuPG 2.1.x defaults, with no expiration or preferred keyserver.
    private.add_uid(uid, usage = {all_imports.KeyFlags.Sign, all_imports.KeyFlags.EncryptCommunications,
                                  all_imports.KeyFlags.EncryptStorage},
                    hashes = [all_imports.HashAlgorithm.SHA256, all_imports.HashAlgorithm.SHA384,
                              all_imports.HashAlgorithm.SHA512], ciphers = [all_imports.SymmetricKeyAlgorithm.AES256],
                    compression = [all_imports.CompressionAlgorithm.ZLIB, all_imports.CompressionAlgorithm.BZ2,
                                   all_imports.CompressionAlgorithm.ZIP, all_imports.CompressionAlgorithm.Uncompressed])

    public = private.pubkey

    text_file_private = open(keys + "/private.asc", "w")
    text_file_private.write(str(private))
    text_file_private.close()
    text_file_public = open(keys + "/public.asc", "w")
    text_file_public.write(str(public))
    text_file_public.close()
