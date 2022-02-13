# edsv.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imp


# key marker classes for convenience
class Key(object):
    pass


class Public(Key):
    pass


class Private(Key):
    pass


def pgpy_decrypt(enc_data, file, key, lang, dec):
    """Decrypt a plaintext message with a given encrypted message and Private key.
    Public keys will return an error, incorrect Private keys and incorrect Private key passphrase will return an error,
    empty key will return an error.
    Return decrypted file/message or error if something went wrong."""

    dec_data, error1, error2, fin, privkey, values = "", "", "", "", "", {}

    try:
        privkey, _ = all_imp.pgpy.PGPKey.from_file(key)
    except all_imp.pgpy.errors.PGPError:
        error_dec_eng = ["Incorrect padding: Error in Private key.", "Returning to menu.", "Decrypt error!"]
        error_dec_esp = ["Incorrect padding: Error en clave Privada.", "Volviendo al menú.", "¡Error descifrando!"]
        if lang == "eng":
            error1 = error_dec_eng[0] + "\n" + error_dec_eng[1]
            error2 = error_dec_eng[2]
        if not lang:
            error1 = error_dec_esp[0] + "\n" + error_dec_esp[1]
            error2 = error_dec_esp[2]
        all_imp.pSG.popup_error(error1, title = error2)

    choose_pass_eng, choose_pass_esp = all_imp.choose_layout.crem_pass()
    if lang == "eng":
        event, values = choose_pass_eng.read()
        choose_pass_eng.close()
    elif lang == "esp":
        event, values = choose_pass_esp.read()
        choose_pass_esp.close()
    password = values["pass"]

    with privkey.unlock(password):
        if not file:
            if not is_public(str(privkey), lang):
                if all_imp.os.path.exists(enc_data):
                    message = open(enc_data, "r").read().strip()
                    dec_message = open(dec + "/auto_decrypted_message.txt", "w")
                else:
                    message = str(enc_data)
                    dec_message = open(dec + "/decrypted_message.txt", "w")
                try:
                    data = all_imp.pgpy.PGPMessage.from_blob(str(message))
                    dec_data = str((privkey.decrypt(data)).message)
                    dec_message.write(str(dec_data))
                    dec_message.close()
                    all_imp.pyclip.copy(str(dec_data).strip())
                    if lang == "eng":
                        fin = "Done! Copied to clipboard and saved in ./Output/Decrypted."
                    elif lang == "esp":
                        fin = "¡Hecho! Copiado a portapapeles y guardado en ./Output/Decrypted."
                    return str(dec_data), fin
                except NotImplementedError:
                    error_dec_eng = ["The imported or pasted message might not be encrypted or correctly imported.",
                                     "Returning to menu.", "Decrypt error!"]
                    error_dec_esp = ["El mensaje copiado o importado puede no estar cifrado o importado correctamente.",
                                     "Volviendo al menú.", "¡Error descifrando!"]
                    if lang == "eng":
                        error1 = error_dec_eng[0] + "\n" + error_dec_eng[1]
                        error2 = error_dec_eng[2]
                    if not lang:
                        error1 = error_dec_esp[0] + "\n" + error_dec_esp[1]
                        error2 = error_dec_esp[2]
                except all_imp.pgpy.errors.PGPError:
                    error_dec_eng = ["Cannot decrypt the file/message with this key.", "Returning to menu.",
                                     "Decrypt error!"]
                    error_dec_esp = ["No se puede descifrar el fichero/mensaje con esta clave privada.",
                                     "Volviendo al menú.", "¡Error descifrando!"]
                    if lang == "eng":
                        error1 = error_dec_eng[0] + "\n" + error_dec_eng[1]
                        error2 = error_dec_eng[2]
                    if not lang:
                        error1 = error_dec_esp[0] + "\n" + error_dec_esp[1]
                        error2 = error_dec_esp[2]
                except TypeError:
                    error_dec_eng = ["Cannot decrypt.", "Returning to menu.", "Decrypt error!"]
                    error_dec_esp = ["No se puede descifrar.", "Volviendo al menú.", "¡Error descifrando!"]
                    if lang == "eng":
                        error1 = error_dec_eng[0] + "\n" + error_dec_eng[1]
                        error2 = error_dec_eng[2]
                    if not lang:
                        error1 = error_dec_esp[0] + "\n" + error_dec_esp[1]
                        error2 = error_dec_esp[2]
                    all_imp.pSG.popup_error(error1, title = error2)
                except ValueError:
                    error_dec_eng = ["Expected: ASCII-armored PGP data, not a valid Private key to decrypt.",
                                     "Returning to menu.", "Decrypt error!"]
                    error_dec_esp = ["Expected: ASCII-armored PGP data, no es una clave Privada válida para descifrar.",
                                     "Volviendo al menú.", "¡Error descifrando!"]
                    if lang == "eng":
                        error1 = error_dec_eng[0] + "\n" + error_dec_eng[1]
                        error2 = error_dec_eng[2]
                    if not lang:
                        error1 = error_dec_esp[0] + "\n" + error_dec_esp[1]
                        error2 = error_dec_esp[2]
                all_imp.pSG.popup_error(error1, title = error2)
                return None, None
            elif is_public(str(privkey), lang):
                error_popup_eng = ["Error. Provided key to decrypt was a Public key.",
                                   "Cannot decrypt with the correct Private key.", "Returning to menu.",
                                   "Error decrypting!"]
                error_popup_esp = ["Error. La clave usada para descifrar era una clave pública.",
                                   "No se puede descifrar sin la clave privada correcta.", "Volviendo al menú.",
                                   "¡Error descifrando!"]
                if lang == "eng":
                    error1 = error_popup_eng[0] + "\n" + error_popup_eng[1] + error_popup_eng[2]
                    error2 = error_popup_eng[3]
                if not lang:
                    error1 = error_popup_esp[0] + "\n" + error_popup_esp[1] + error_popup_esp[2]
                    error2 = error_popup_esp[3]
                all_imp.pSG.popup_error(error1, title = error2)
                return None, None
        else:
            if not is_public(str(privkey), lang):
                message = open(enc_data, "rb").read().strip()
                original_name = ".".join(enc_data.split("/")[-1].split(".")[:-2])
                try:
                    data = all_imp.pgpy.PGPMessage.from_blob(message)
                    dec_data = (privkey.decrypt(data)).message
                    if isinstance(dec_data, str):
                        dec_message = open(dec + "/" + original_name, "w")
                        dec_message.write(str(dec_data))
                    else:
                        dec_message = open(dec + "/" + original_name, "wb")
                        dec_message.write(bytes(dec_data))
                    dec_message.close()
                    if lang == "eng":
                        fin = "Done! Saved in ./Output/Decrypted."
                    elif lang == "esp":
                        fin = "¡Hecho! Guardado en ./Output/Decrypted."
                    all_imp.pSG.popup_auto_close(fin, auto_close_duration = 1, button_type = 5, title = fin)
                except NotImplementedError:
                    error_dec_eng = ["The imported or pasted message might not be encrypted or correctly imported.",
                                     "Returning to menu.", "Decrypt error!"]
                    error_dec_esp = ["El mensaje copiado o importado puede no estar cifrado o importado correctamente.",
                                     "Volviendo al menú.", "¡Error descifrando!"]
                    if lang == "eng":
                        error1 = error_dec_eng[0] + "\n" + error_dec_eng[1]
                        error2 = error_dec_eng[2]
                    if not lang:
                        error1 = error_dec_esp[0] + "\n" + error_dec_esp[1]
                        error2 = error_dec_esp[2]
                    all_imp.pSG.popup_error(error1, title = error2)
                except all_imp.pgpy.errors.PGPError:
                    error_dec_eng = ["Cannot decrypt the file/message with this key.", "Returning to menu.",
                                     "Decrypt error!"]
                    error_dec_esp = ["No se puede descifrar el fichero/mensaje con esta clave privada.",
                                     "Volviendo al menú.", "¡Error descifrando!"]
                    if lang == "eng":
                        error1 = error_dec_eng[0] + "\n" + error_dec_eng[1]
                        error2 = error_dec_eng[2]
                    if not lang:
                        error1 = error_dec_esp[0] + "\n" + error_dec_esp[1]
                        error2 = error_dec_esp[2]
                    all_imp.pSG.popup_error(error1, title = error2)
                # except TypeError:
                #     error_dec_eng = ["Cannot decrypt.", "Returning to menu.", "Decrypt error!"]
                #     error_dec_esp = ["No se puede descifrar.", "Volviendo al menú.", "¡Error descifrando!"]
                #     if lang == "eng":
                #         error1 = error_dec_eng[0] + "\n" + error_dec_eng[1]
                #         error2 = error_dec_eng[2]
                #     if not lang:
                #         error1 = error_dec_esp[0] + "\n" + error_dec_esp[1]
                #         error2 = error_dec_esp[2]
                #     all_imp.pSG.popup_error(error1, title = error2)
                except ValueError:
                    error_dec_eng = ["Expected: ASCII-armored PGP data, not a valid Private key to decrypt.",
                                     "Returning to menu.", "Decrypt error!"]
                    error_dec_esp = ["Esperado: ASCII-armored PGP data, no es una clave Privada válida para descifrar.",
                                     "Volviendo al menú.", "¡Error descifrando!"]
                    if lang == "eng":
                        error1 = error_dec_eng[0] + "\n" + error_dec_eng[1]
                        error2 = error_dec_eng[2]
                    if not lang:
                        error1 = error_dec_esp[0] + "\n" + error_dec_esp[1]
                        error2 = error_dec_esp[2]
                    all_imp.pSG.popup_error(error1, title = error2)
            elif is_public(str(privkey), lang):
                error_popup_eng = ["Error. Provided key to decrypt was a Public key.",
                                   "Cannot decrypt with the correct Private key.", "Returning to menu.",
                                   "Error decrypting!"]
                error_popup_esp = ["Error. La clave usada para descifrar era una clave pública.",
                                   "No se puede descifrar sin la clave privada correcta.", "Volviendo al menú.",
                                   "¡Error descifrando!"]
                if lang == "eng":
                    error1 = error_popup_eng[0] + "\n" + error_popup_eng[1] + error_popup_eng[2]
                    error2 = error_popup_eng[3]
                if not lang:
                    error1 = error_popup_esp[0] + "\n" + error_popup_esp[1] + error_popup_esp[2]
                    error2 = error_popup_esp[3]
                all_imp.pSG.popup_error(error1, title = error2)


def pgpy_encrypt(data, file, key, lang, enc):
    """Encrypt a message with a given plaintext file/message and Public key.
    Private keys will return an error, incorrect Public keys will return an error, empty key will return an error.
    Return encrypted file/message or error if something went wrong."""

    enc_data, error1, error2, fin, pubkey = "", "", "", "", ""

    try:
        pubkey, _ = all_imp.pgpy.PGPKey.from_file(key)
    except all_imp.pgpy.errors.PGPError:
        error_enc_eng = ["Incorrect padding: Import Public key again", "Returning to menu.", "Encrypt error!"]
        error_enc_esp = ["Incorrect padding: Importar clave Pública de nuevo.", "Volviendo al menú.",
                         "¡Error cifrando!"]
        if lang == "eng":
            error1 = error_enc_eng[0] + "\n" + error_enc_eng[1]
            error2 = error_enc_eng[2]
        if not lang:
            error1 = error_enc_esp[0] + "\n" + error_enc_esp[1]
            error2 = error_enc_esp[2]
        all_imp.pSG.popup_error(error1, title = error2)

    if is_public(str(pubkey), lang):
        if not file:
            mes = all_imp.pgpy.PGPMessage.new(data, compression = all_imp.CompressionAlgorithm.BZ2, sensitive = True)
            try:
                enc_data = (pubkey.encrypt(mes, cipher = all_imp.SymmetricKeyAlgorithm.AES256,
                                           hash = [all_imp.HashAlgorithm.SHA512]))
                enc_message = open(enc + "/encrypted_message.txt", "w")
                enc_message.write(str(enc_data))
                enc_message.close()
                all_imp.pyclip.copy(str(enc_data).strip())
                if lang == "eng":
                    fin = "Done! Copied to clipboard and saved in ./Output/Encrypted."
                elif lang == "esp":
                    fin = "¡Hecho! Copiado a portapapeles y guardado en ./Output/Encrypted."
                return str(enc_data), fin
            except all_imp.pgpy.errors.PGPError:
                error_enc_eng = ["Cannot encrypt the file/message with the imported Public key, import it again.",
                                 "Returning to menu.", "Decrypt error!"]
                error_enc_esp = ["No se puede cifrar el fichero/mensaje con la clave Pública importada, "
                                 "impórtala de nuevo.", "Volviendo al menú.", "¡Error descifrando!"]
                if lang == "eng":
                    error1 = error_enc_eng[0] + "\n" + error_enc_eng[1]
                    error2 = error_enc_eng[2]
                if not lang:
                    error1 = error_enc_esp[0] + "\n" + error_enc_esp[1]
                    error2 = error_enc_esp[2]
            except TypeError:
                error_enc_eng = ["Cannot encrypt.", "Returning to menu.", "Encrypt error!"]
                error_enc_esp = ["No se puede cifrar.", "Volviendo al menú.", "¡Error cifrando!"]
                if lang == "eng":
                    error1 = error_enc_eng[0] + "\n" + error_enc_eng[1]
                    error2 = error_enc_eng[2]
                if not lang:
                    error1 = error_enc_esp[0] + "\n" + error_enc_esp[1]
                    error2 = error_enc_esp[2]
            except ValueError:
                error_enc_eng = ["Expected: ASCII-armored PGP data, not a valid PGP Public key to encrypt.",
                                 "Returning to menu.", "Encrypt error!"]
                error_enc_esp = ["Expected: ASCII-armored PGP data, no hay clave PGP Pública válida para cifrar.",
                                 "Volviendo al menú.", "¡Error cifrando!"]
                if lang == "eng":
                    error1 = error_enc_eng[0] + "\n" + error_enc_eng[1]
                    error2 = error_enc_eng[2]
                if not lang:
                    error1 = error_enc_esp[0] + "\n" + error_enc_esp[1]
                    error2 = error_enc_esp[2]
            all_imp.pSG.popup_error(error1, title = error2)
            return None, None
        else:
            data_file = open(data, "rb").read().strip()
            mes = all_imp.pgpy.PGPMessage.new(data_file, compression = all_imp.CompressionAlgorithm.BZ2,
                                              sensitive = True)
            try:
                enc_data = (pubkey.encrypt(mes, cipher = all_imp.SymmetricKeyAlgorithm.AES256,
                                           hash = all_imp.HashAlgorithm.SHA512))
                file_name = data.split("/")[-1]
                enc_message = open(enc + "/" + file_name + ".pgp.PK", "wb")
                enc_message.write(bytes(enc_data))
                enc_message.close()
                if lang == "eng":
                    fin = "Done! Saved in ./Output/Encrypted."
                elif lang == "esp":
                    fin = "¡Hecho! Guardado en ./Output/Encrypted."
                all_imp.pSG.popup_auto_close(fin, auto_close_duration = 1, button_type = 5, title = fin)
            except all_imp.pgpy.errors.PGPError:
                error_enc_eng = ["Cannot encrypt the file/message with the imported Public key.",
                                 "Returning to menu.", "Decrypt error!"]
                error_enc_esp = ["No se puede cifrar el fichero/mensaje con la clave Pública importada.",
                                 "Volviendo al menú.", "¡Error descifrando!"]
                if lang == "eng":
                    error1 = error_enc_eng[0] + "\n" + error_enc_eng[1]
                    error2 = error_enc_eng[2]
                if not lang:
                    error1 = error_enc_esp[0] + "\n" + error_enc_esp[1]
                    error2 = error_enc_esp[2]
                all_imp.pSG.popup_error(error1, title = error2)
            except TypeError:
                error_enc_eng = ["Cannot encrypt.", "Returning to menu.", "Encrypt error!"]
                error_enc_esp = ["No se puede cifrar.", "Volviendo al menú.", "¡Error cifrando!"]
                if lang == "eng":
                    error1 = error_enc_eng[0] + "\n" + error_enc_eng[1]
                    error2 = error_enc_eng[2]
                if not lang:
                    error1 = error_enc_esp[0] + "\n" + error_enc_esp[1]
                    error2 = error_enc_esp[2]
                all_imp.pSG.popup_error(error1, title = error2)
            except ValueError:
                error_enc_eng = ["Expected: ASCII-armored PGP data, not a valid PGP Public key to encrypt.",
                                 "Returning to menu.", "Encrypt error!"]
                error_enc_esp = ["Expected: ASCII-armored PGP data, no hay clave PGP Pública válida para cifrar.",
                                 "Volviendo al menú.", "¡Error cifrando!"]
                if lang == "eng":
                    error1 = error_enc_eng[0] + "\n" + error_enc_eng[1]
                    error2 = error_enc_eng[2]
                if not lang:
                    error1 = error_enc_esp[0] + "\n" + error_enc_esp[1]
                    error2 = error_enc_esp[2]
                all_imp.pSG.popup_error(error1, title = error2)
    elif not is_public(str(pubkey), lang):
        error_popup_eng = ["Error. Provided key to encrypt was a Private key, try importing the Public key again.",
                           "Returning to menu.", "Error encrypting!"]
        error_popup_esp = ["Error. La clave Pública usada para cifrar era una clave Privada, ",
                           "intenta importar la clave Pública de nuevo.", "Volviendo al menú.",
                           "¡Error cifrando!"]
        if lang == "eng":
            error1 = error_popup_eng[0] + "\n" + error_popup_eng[1]
            error2 = error_popup_eng[2]
        if not lang:
            error1 = error_popup_esp[0] + "\n" + error_popup_esp[1]
            error2 = error_popup_esp[2]
        all_imp.pSG.popup_error(error1, title = error2)
        return None, None


def is_public(key, lang):
    """Checks whether the given key is a Public key, using magic property.
    Returns True if it is."""

    error1, error2, is_it = "", "", ""

    try:
        is_it = all_imp.pgpy.PGPKey.from_blob(key)
    except all_imp.pgpy.errors.PGPError:
        inc_pad_eng = ["Incorrect padding or invalid base64-encoded string: incorrect number of data characters.",
                       "Incorrect Public key!"]
        inc_pad_esp = ["Cadena codificada en base-64 no válida: Número de caracteres incorrecto.",
                       "Clave pública incorrecta!"]
        if lang == "eng":
            error1 = inc_pad_eng[0]
            error2 = inc_pad_eng[1]
        elif lang == "esp":
            error1 = inc_pad_esp[0]
            error2 = inc_pad_esp[1]
        all_imp.pSG.popup_error(error1, title = error2)
    except ValueError:
        arm_eng = ["Expected: ASCII-armored PGP data, not a valid PGP Public key or not a valid PGP Signature "
                   "to import.", "Returning to menu.", "Error!"]
        arm_esp = ["Expected: ASCII-armored PGP data: no es una clave pública PGP válida "
                   "o no es una Firma PGP válida para importar.", "Volviendo al menú", "¡Error!"]
        if lang == "eng":
            error1 = arm_eng[0] + "\n" + arm_eng[1]
            error2 = arm_eng[2]
        elif lang == "esp":
            error1 = arm_esp[0] + "\n" + arm_esp[1]
            error2 = arm_esp[2]
        all_imp.pSG.popup_error(error1, title = error2)

    try:
        if getattr(is_it[0], "magic").split()[0] == "PUBLIC":
            return True
    except IndexError:
        return False


def is_signature(key, lang):
    """Checks whether the given key is a signature, using magic property.
    Returns True if it is."""

    done, error1, error2, is_it = "", "", "", ""

    try:
        is_it = all_imp.pgpy.PGPSignature.from_blob(key)
    except all_imp.pgpy.errors.PGPError:
        inc_pad_eng = ["Incorrect padding or invalid base64-encoded string: incorrect number of data characters.",
                       "Incorrect signature!"]
        inc_pad_esp = ["Cadena codificada en base-64 no válida: Número de caracteres incorrecto.", "Firma incorrecta!"]
        if lang == "eng":
            error1 = inc_pad_eng[0]
            error2 = inc_pad_eng[1]
        elif lang == "esp":
            error1 = inc_pad_esp[0]
            error2 = inc_pad_esp[1]
        all_imp.pSG.popup_error(error1, title = error2)
    except ValueError:
        arm_eng = ["Expected: ASCII-armored PGP data, not a valid PGP Public key or not a valid "
                   "PGP Signature to import.", "Returning to menu.", "Error!"]
        arm_esp = ["Expected: ASCII-armored PGP data: no es una clave pública PGP válida "
                   "o no es una Firma PGP válida para importar.", "Volviendo al menú", "¡Error!"]
        if lang == "eng":
            error1 = arm_eng[0] + "\n" + arm_eng[1]
            error2 = arm_eng[2]
        elif lang == "esp":
            error1 = arm_esp[0] + "\n" + arm_esp[1]
            error2 = arm_esp[2]
        all_imp.pSG.popup_error(error1, title = error2)

    try:
        if is_it:
            if getattr(is_it, "magic") == "SIGNATURE":
                return True
    except IndexError:
        return False


def pgpy_sign(data, file, key, lang, sig):
    """Sign a file/message with a given message and Private key.
    Public keys will return an error, incorrect Private keys and incorrect Private key passphrase will return an error,
    empty key will return an error.
    Return message signature or error if something went wrong."""

    auto, error1, error2, privkey, values = False, "", "", "", {}

    try:
        privkey, _ = all_imp.pgpy.PGPKey.from_file(key)
    except all_imp.pgpy.errors.PGPError:
        error_sig_eng = ["Incorrect padding: Error in Private key.", "Returning to menu.", "Signing error!"]
        error_sig_esp = ["Padding incorrecto: Error en clave Privada.", "Volviendo al menú.", "¡Error firmando!"]
        if lang == "eng":
            error1 = error_sig_eng[0] + "\n" + error_sig_eng[1]
            error2 = error_sig_eng[2]
        if not lang:
            error1 = error_sig_esp[0] + "\n" + error_sig_esp[1]
            error2 = error_sig_esp[2]
        all_imp.pSG.popup_error(error1, title = error2)

    choose_pass_eng, choose_pass_esp = all_imp.choose_layout.crem_pass()
    if lang == "eng":
        event, values = choose_pass_eng.read()
        choose_pass_eng.close()
    elif lang == "esp":
        event, values = choose_pass_esp.read()
        choose_pass_esp.close()
    password = values["pass"]

    with privkey.unlock(password):
        if not is_public(str(privkey), lang):
            if not file:
                if all_imp.os.path.exists(data):
                    message = open(data, "r").read().strip()
                    sig_message = open(sig + "/encrypted_signed.txt", "w")
                    auto = True
                else:
                    message = str(data).strip()
                    sig_message = open(sig + "/signed_text.txt", "w")
                    auto = False
                try:
                    sig_data = str(privkey.sign(message))
                    comp = "-----BEGIN PGP SIGNED MESSAGE-----\n\n" + str(message) + "\n\n" + str(sig_data)
                    sig_message.write(comp)
                    sig_message.close()
                    all_imp.pyclip.copy(str(sig_data).strip())
                    if auto:
                        if lang == "eng":
                            fin = "Signed! Saved in ./Output/Signed."
                        elif lang == "esp":
                            fin = "¡Firmado! Guardado en ./Output/Signed."
                    elif not auto:
                        if lang == "eng":
                            fin = "Signed! Copied to clipboard and saved in ./Output/Signed."
                        elif lang == "esp":
                            fin = "¡Firmado! Copiado a portapapeles y guardado en ./Output/Signed."
                    return str(sig_data), fin
                except all_imp.pgpy.errors.PGPError:
                    error_sig_eng = ["Cannot sign the file/message with the Private key.", "Returning to menu.",
                                     "Signing error!"]
                    error_sig_esp = ["No se puede firmar el fichero/mensaje con la clave Privada.",
                                     "Volviendo al menú.", "¡Error firmando!"]
                    if lang == "eng":
                        error1 = error_sig_eng[0] + "\n" + error_sig_eng[1]
                        error2 = error_sig_eng[2]
                    if not lang:
                        error1 = error_sig_esp[0] + "\n" + error_sig_esp[1]
                        error2 = error_sig_esp[2]
                except TypeError:
                    error_sig_eng = ["Cannot sign.", "Returning to menu.", "Sign error!"]
                    error_sig_esp = ["No se puede firmar.", "Volviendo al menú.", "¡Error firmando!"]
                    if lang == "eng":
                        error1 = error_sig_eng[0] + "\n" + error_sig_eng[1]
                        error2 = error_sig_eng[2]
                    if not lang:
                        error1 = error_sig_esp[0] + "\n" + error_sig_esp[1]
                        error2 = error_sig_esp[2]
                except ValueError:
                    error_sig_eng = ["Expected: ASCII-armored PGP data, not a valid PGP Private key to sign.",
                                     "Returning to menu.", "Signing error!"]
                    error_sig_esp = ["Expected: ASCII-armored PGP data, no hay clave PGP Privada válida para firmar.",
                                     "Volviendo al menú.", "¡Error firmando!"]
                    if lang == "eng":
                        error1 = error_sig_eng[0] + "\n" + error_sig_eng[1]
                        error2 = error_sig_eng[2]
                    if not lang:
                        error1 = error_sig_esp[0] + "\n" + error_sig_esp[1]
                        error2 = error_sig_esp[2]
                all_imp.pSG.popup_error(error1, title = error2)
                return None, None
            else:
                if not is_public(str(privkey), lang):
                    sign_file = open(data, "rb").read().strip()
                    try:
                        file_name = data.split("/")[-1]
                        sig_data = str(privkey.sign(sign_file))
                        sig_file = open(sig + "/" + file_name + "_signature.txt", "w")
                        sig_file.write(str(sig_data))
                        sig_file.close()
                        if lang == "eng":
                            fin = "Signed! Saved in ./Output/Signed."
                        elif lang == "esp":
                            fin = "¡Firmado! Gardado en ./Output/Signed."
                        all_imp.pSG.popup_auto_close(fin, auto_close_duration = 1, button_type = 5, title = fin)
                    except all_imp.pgpy.errors.PGPError:
                        error_sig_eng = ["Cannot sign the file/message with the Private key.", "Returning to menu.",
                                         "Signing error!"]
                        error_sig_esp = ["No se puede firmar el fichero/mensaje con la clave Privada.",
                                         "Volviendo al menú.", "¡Error firmando!"]
                        if lang == "eng":
                            error1 = error_sig_eng[0] + "\n" + error_sig_eng[1]
                            error2 = error_sig_eng[2]
                        if not lang:
                            error1 = error_sig_esp[0] + "\n" + error_sig_esp[1]
                            error2 = error_sig_esp[2]
                        all_imp.pSG.popup_error(error1, title = error2)
                    except TypeError:
                        error_sig_eng = ["Cannot sign.", "Returning to menu.", "Sign error!"]
                        error_sig_esp = ["No se puede firmar.", "Volviendo al menú.", "¡Error firmando!"]
                        if lang == "eng":
                            error1 = error_sig_eng[0] + "\n" + error_sig_eng[1]
                            error2 = error_sig_eng[2]
                        if not lang:
                            error1 = error_sig_esp[0] + "\n" + error_sig_esp[1]
                            error2 = error_sig_esp[2]
                        all_imp.pSG.popup_error(error1, title = error2)
                    except ValueError:
                        error_sig_eng = ["Expected: ASCII-armored PGP data, not a valid PGP Private key to sign.",
                                         "Returning to menu.", "Signing error!"]
                        error_sig_esp = ["Expected: ASCII-armored PGP data, no hay clave PGP Privada válida "
                                         "para firmar.", "Volviendo al menú.", "¡Error firmando!"]
                        if lang == "eng":
                            error1 = error_sig_eng[0] + "\n" + error_sig_eng[1]
                            error2 = error_sig_eng[2]
                        if not lang:
                            error1 = error_sig_esp[0] + "\n" + error_sig_esp[1]
                            error2 = error_sig_esp[2]
                        all_imp.pSG.popup_error(error1, title = error2)
        elif is_public(str(privkey), lang):
            error_popup_eng = ["Error. Provided key to sign was a Public key, try checking the Private key used.\n",
                               "Returning to menu.", "Error sigining!"]
            error_popup_esp = ["Error. La clave usada para firmar era una clave Pública, comprueba la clave Privada ",
                               "que se está usando.\nVolviendo al menú.", "¡Error firmando!"]
            if lang == "eng":
                error1 = error_popup_eng[0] + error_popup_eng[1]
                error2 = error_popup_eng[2]
            if not lang:
                error1 = error_popup_esp[0] + error_popup_esp[1]
                error2 = error_popup_esp[2]
            all_imp.pSG.popup_error(error1, title = error2)


def pgpy_verify(file, imp, key, lang, sig_data, ver):
    """Verify a message with a given file/message and Public key.
    Private keys will return an error, incorrect Public keys will return an error, empty key will return an error.
    Return verification or error if something went wrong."""

    error1, error2, fin, imp_mes, pubkey, ver_mes = "", "", "", "", "", ""

    if not file:
        imp_mes = open(imp, "r").read().strip()
    else:
        imp_mes = open(imp, "rb").read().strip()

    try:
        pubkey, _ = all_imp.pgpy.PGPKey.from_file(key)
    except all_imp.pgpy.errors.PGPError:
        error_ver_eng = ["Incorrect padding: Import Public key again", "Returning to menu.", "Verifying error!"]
        error_ver_esp = ["Padding incorrecto: Importar clave Pública de nuevo.", "Volviendo al menú.",
                         "¡Error verificando!"]
        if lang == "eng":
            error1 = error_ver_eng[0] + "\n" + error_ver_eng[1]
            error2 = error_ver_eng[2]
        if not lang:
            error1 = error_ver_esp[0] + "\n" + error_ver_esp[1]
            error2 = error_ver_esp[2]
        all_imp.pSG.popup_error(error1, title = error2)

    sig = all_imp.pgpy.PGPSignature.from_file(sig_data)

    if is_public(str(pubkey), lang):
        try:
            ver_mes = pubkey.verify(imp_mes, sig)
        except all_imp.pgpy.errors.PGPError:
            error_ver_eng = ["Cannot verify the file/message with the imported Public key.", "Returning to menu.",
                             "Verify error!"]
            error_ver_esp = ["No se puede verificar el fichero/mensaje con la clave Pública importada.",
                             "Volviendo al menú.", "¡Error verificando!"]
            if lang == "eng":
                error1 = error_ver_eng[0] + "\n" + error_ver_eng[1]
                error2 = error_ver_eng[2]
            if not lang:
                error1 = error_ver_esp[0] + "\n" + error_ver_esp[1]
                error2 = error_ver_esp[2]
            all_imp.pSG.popup_error(error1, title = error2)
        except TypeError:
            error_ver_eng = ["Cannot verify.", "Returning to menu.", "Verify error!"]
            error_ver_esp = ["No se puede verificar.", "Volviendo al menú.", "¡Error verificando!"]
            if lang == "eng":
                error1 = error_ver_eng[0] + "\n" + error_ver_eng[1]
                error2 = error_ver_eng[2]
            if not lang:
                error1 = error_ver_esp[0] + "\n" + error_ver_esp[1]
                error2 = error_ver_esp[2]
            all_imp.pSG.popup_error(error1, title = error2)
        except ValueError:
            error_ver_eng = ["Expected: ASCII-armored PGP data, not a valid PGP Public key to verify.",
                             "Returning to menu.", "Verify error!"]
            error_ver_esp = ["Expected: ASCII-armored PGP data, no hay clave PGP Pública válida para verificar.",
                             "Volviendo al menú.", "¡Error verificando!"]
            if lang == "eng":
                error1 = error_ver_eng[0] + "\n" + error_ver_eng[1]
                error2 = error_ver_eng[2]
            if not lang:
                error1 = error_ver_esp[0] + "\n" + error_ver_esp[1]
                error2 = error_ver_esp[2]
            all_imp.pSG.popup_error(error1, title = error2)
        if ver_mes.__bool__():
            if not file:
                ver_message = open(ver + "/v_verified_message.txt", "w")
                ver_message.write(str(imp_mes))
                ver_message.close()
            if lang == "eng":
                fin = "Verified!"
            elif lang == "esp":
                fin = "¡Verificado!"
            return fin
        else:
            error_popup_eng = ["File/Message and signature do not match!", "Error verifying!"]
            error_popup_esp = ["¡El fichero/mensaje y la firma no coinciden!", "¡Error verificando!"]
            if lang == "eng":
                error1 = error_popup_eng[0]
                error2 = error_popup_eng[1]
            elif lang == "esp":
                error1 = error_popup_esp[0]
                error2 = error_popup_esp[1]
    elif not is_public(str(pubkey), lang):
        error_popup_eng = ["Error. Provided key to verify was a Private key, try importing the Public key again.",
                           "Returning to menu.", "Error verifying!"]
        error_popup_esp = ["Error. la clave Pública usada para verificar era una clave Privada, ",
                           "intenta importar la clave Pública de nuevo key again.", "Volviendo al menú.",
                           "¡Error verificando!"]
        if lang == "eng":
            error1 = error_popup_eng[0] + "\n" + error_popup_eng[1]
            error2 = error_popup_eng[2]
        if not lang:
            error1 = error_popup_esp[0] + error_popup_esp[1] + "\n" + error_popup_esp[2]
            error2 = error_popup_esp[3]
    all_imp.pSG.popup_error(error1, title = error2)
    return None
