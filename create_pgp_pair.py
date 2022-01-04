# create_pgp_pair.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import all_imports


def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(all_imports.random.choice(all_imports.string.ascii_letters) for _ in range(length))
    # print random string
    return result_str


def pgpy_create_keypair(size):
    # we can start by generating a primary key. For this example, we'll use RSA, but it could be DSA or ECDSA as well
    private = all_imports.pgpy.PGPKey.new(all_imports.PubKeyAlgorithm.RSAEncryptOrSign, size)

    name = get_random_string(8) + " " + get_random_string(12)
    real_email = get_random_string(12) + "@fakersa.pokemon"

    # we now have some key material, but our new key doesn't have a user ID yet, and therefore is not yet usable!
    uid = all_imports.pgpy.PGPUID.new(name, email = real_email)

    # now we must add the new user id to the key. We'll need to specify all of our preferences at this point
    # because PGPy doesn't have any built-in key preference defaults at this time
    # this example is similar to GnuPG 2.1.x defaults, with no expiration or preferred keyserver
    private.add_uid(uid, usage = {all_imports.KeyFlags.Sign, all_imports.KeyFlags.EncryptCommunications,
                                  all_imports.KeyFlags.EncryptStorage},
                    hashes = [all_imports.HashAlgorithm.SHA256, all_imports.HashAlgorithm.SHA384,
                              all_imports.HashAlgorithm.SHA512], ciphers = [all_imports.SymmetricKeyAlgorithm.AES256],
                    compression = [all_imports.CompressionAlgorithm.ZLIB, all_imports.CompressionAlgorithm.BZ2,
                                   all_imports.CompressionAlgorithm.ZIP, all_imports.CompressionAlgorithm.Uncompressed])

    public = private.pubkey

    return private, public
