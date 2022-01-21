# menu.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports

"""Handles all the menu choices and redirects to the corresponding windows, to import, or handle the data that need 
the keypairs."""


def create_menu(lang, imp, ks):
    error1, error2, fin = "", "", ""
    email, imp_eng, imp_esp, mode_text, name = None, None, None, None, None
    event, event1 = False, False
    height = 440
    values = []
    width = 320

    while True:

        menu_eng, menu_esp = all_imports.menu_create.create_remove_menu(height, width)
        if not event or event == 800:
            if lang:
                event, values = menu_eng.read()
            elif not lang:
                event, values = menu_esp.read()

        # Create PGP Pair.
        if event == 100:
            size = tuple(values.items())[0][1]
            menu_eng.close()
            menu_esp.close()
            keypair_choose_eng, keypair_choose_esp = all_imports.kp_choose_create.create_remove_choose_kp()
            if lang:
                event, values = keypair_choose_eng.read()
            elif not lang:
                event, values = keypair_choose_esp.read()
            keypair_choose_eng.close()
            keypair_choose_esp.close()
            if event == 800:
                event = False

            if event == 116:
                all_imports.create_pgp_pair.pgpy_create_keypair(email, ks, name, size, False)
                if lang:
                    fin = "Done!"
                elif not lang:
                    fin = "¡Hecho!"
                all_imports.pSG.popup_auto_close(fin, auto_close_duration = 0.8, button_type = 5, title = fin)
                event = False
            elif event == 118:
                ne_choose_eng, ne_choose_esp = all_imports.ne_choose_create.create_remove_choose_ne()
                if lang:
                    event, values = ne_choose_eng.read()
                elif not lang:
                    event, values = ne_choose_esp.read()
                if event == 660:
                    name, email = (str(tuple(values.items())[0][1]), str(tuple(values.items())[1][1]))
                    all_imports.create_pgp_pair.pgpy_create_keypair(email, ks, name, size, True)
                    if lang:
                        fin = "Done!"
                    elif not lang:
                        fin = "¡Hecho!"
                    all_imports.pSG.popup_auto_close(fin, auto_close_duration = 0.8, button_type = 5, title = fin)
                ne_choose_eng.close()
                ne_choose_esp.close()
                event = False

        # Import.
        if event == 110 or event == 112 or event == 114:
            if event == 110:
                imp_eng, imp_esp = all_imports.import_enc_create.create_remove_enc_import()
            elif event == 112:
                imp_eng, imp_esp = all_imports.import_pub_create.create_remove_pub_import()
            elif event == 114:
                imp_eng, imp_esp = all_imports.import_sig_create.create_remove_sig_import()

            if lang:
                menu_eng.close()
                event1, values = imp_eng.read()
                if event1 == "xclipp":
                    toggle = False
                    paste = all_imports.pyclip.paste(text = True).strip()
                    if event == 110:
                        imp_eng[110].update(value = paste)
                    elif event == 112:
                        imp_eng[112].update(value = paste)
                    elif event == 114:
                        imp_eng[114].update(value = paste)
                    imp_eng["xclipp"].update(visible = toggle)
                    event1, values = imp_eng.read()

            elif not lang:
                menu_esp.close()
                event1, values = imp_esp.read()
                if event1 == "xclipp":
                    toggle = False
                    paste = all_imports.pyclip.paste(text = True).strip()
                    if event == 110:
                        imp_eng[110].update(value = paste)
                    elif event == 112:
                        imp_eng[112].update(value = paste)
                    elif event == 114:
                        imp_eng[114].update(value = paste)
                    imp_eng["xclipp"].update(visible = toggle)
                    event1, values = imp_eng.read()
            vp = (tuple(values.items())[0][0],  tuple(values.items())[0][1])

            if event1 == 700:
                if not vp[1]:
                    empty_eng = ["Cannot import empty data.", "Error!"]
                    empty_esp = ["No se puede importar datos vacíos.", "¡Error!"]
                    if lang:
                        error1 = empty_eng[0]
                        error2 = empty_eng[1]
                    elif not lang:
                        error1 = empty_esp[0]
                        error2 = empty_esp[1]
                    all_imports.pSG.popup_error(error1, title = error2)
                elif vp[1]:
                    # Import message.
                    if vp[0] == 110:
                        text_file_v = open(imp + "/v_imported_message.txt", "w")
                        text_file_v.write(str(vp[1]))
                        text_file_v.close()
                        if lang:
                            fin = "Done!"
                        elif not lang:
                            fin = "¡Hecho!"
                        all_imports.pSG.popup_auto_close(fin, auto_close_duration = 0.8, button_type = 5, title = fin)
                        event = False

                    # Import public key
                    elif vp[0] == 112:
                        try:
                            well_is_it = all_imports.enc_dec.is_public(vp[1])
                            if well_is_it:
                                text_file_v = open(imp + "/v_imported_public.asc", "w")
                                text_file_v.write(str(vp[1]))
                                text_file_v.close()
                                if lang:
                                    fin = "Done!"
                                elif not lang:
                                    fin = "¡Hecho!"
                                all_imports.pSG.popup_auto_close(fin, auto_close_duration = 0.8, button_type = 5,
                                                                 title = fin)
                                event = False
                            elif not well_is_it:
                                val_pub_eng = ["Not a valid PUBLIC PGP key.", "Error!"]
                                val_pub_esp = ["No es una clave PÚBLICA válida.", "¡Error!"]
                                if lang:
                                    error1 = val_pub_eng[0]
                                    error2 = val_pub_eng[1]
                                elif not lang:
                                    error1 = val_pub_esp[0]
                                    error2 = val_pub_esp[1]
                                all_imports.pSG.popup_error(error1, title = error2)
                        except all_imports.pgpy.errors.PGPError:
                            inc_pad_eng = ["Incorrect padding or invalid base64-encoded string: "
                                           "incorrect number of data characters.", "Incorrect public key!"]
                            inc_pad_esp = ["Cadena codificada en base-64 no válida: Número de caracteres incorrecto.",
                                           "Clave pública incorrecta!"]
                            if lang:
                                error1 = inc_pad_eng[0]
                                error2 = inc_pad_eng[1]
                            elif not lang:
                                error1 = inc_pad_esp[0]
                                error2 = inc_pad_esp[1]
                            all_imports.pSG.popup_error(error1, title = error2)
                        except ValueError:
                            arm_eng = ["Expected: ASCII-armored PGP data, not a valid PGP Public key or not a valid "
                                       "PGP Signature to import.", "Returning to menu.", "Error!"]
                            arm_esp = ["Expected: ASCII-armored PGP data: no es una clave pública PGP válida "
                                       "o no es una Firma PGP válida para importar.", "Volviendo al menú", "¡Error!"]
                            if lang:
                                error1 = arm_eng[0] + "\n" + arm_eng[1]
                                error2 = arm_eng[2]
                            elif not lang:
                                error1 = arm_esp[0] + "\n" + arm_esp[1]
                                error2 = arm_esp[2]
                            all_imports.pSG.popup_error(error1, title = error2)
                    # Import signature
                    elif vp[0] == 114:
                        try:
                            well_is_it = all_imports.enc_dec.is_signature(imp, vp[1], lang)
                            if not well_is_it:
                                val_eng = ["Not a valid signature key.", "Error importing!"]
                                val_esp = ["No es una firma válida.", "¡Error importando!"]
                                if lang:
                                    error1 = val_eng[0]
                                    error2 = val_eng[1]
                                elif not lang:
                                    error1 = val_esp[0]
                                    error2 = val_esp[1]
                                all_imports.pSG.popup_error(error1, title = error2)
                            else:
                                event = False
                        except all_imports.pgpy.errors.PGPError:
                            inc_pad_eng = ["Incorrect padding or invalid base64-encoded string: "
                                           "incorrect number of data characters.", "Incorrect signature!"]
                            inc_pad_esp = ["Cadena codificada en base-64 no válida: Número de caracteres incorrecto.",
                                           "Firma incorrecta!"]
                            if lang:
                                error1 = inc_pad_eng[0]
                                error2 = inc_pad_eng[1]
                            elif not lang:
                                error1 = inc_pad_esp[0]
                                error2 = inc_pad_esp[1]
                            all_imports.pSG.popup_error(error1, title = error2)
                        except ValueError:
                            arm_eng = ["Expected: ASCII-armored PGP data, not a valid PGP Public key or not a valid "
                                       "PGP Signature to import.", "Returning to menu.", "Error!"]
                            arm_esp = ["Expected: ASCII-armored PGP data: no es una clave pública PGP válida "
                                       "o no es una Firma PGP válida para importar.", "Volviendo al menú", "¡Error!"]
                            if lang:
                                error1 = arm_eng[0] + "\n" + arm_eng[1]
                                error2 = arm_eng[2]
                            elif not lang:
                                error1 = arm_esp[0] + "\n" + arm_esp[1]
                                error2 = arm_esp[2]
                            all_imports.pSG.popup_error(error1, title = error2)
                imp_eng.close()
                imp_esp.close()

            if event1 == 800:
                imp_eng.close()
                imp_esp.close()
                event = False

        if event in [200, 300, 250, 350]:
            # Select encrypt mode.
            if event == 200:
                mode_text = 15

            # Select decrypt mode.
            if event == 300:
                mode_text = 20

            # Select sign mode.
            if event == 250:
                mode_text = 30

            # Select verify mode.
            if event == 350:
                mode_text = 40
            menu_eng.close()
            menu_esp.close()
            break

        # Toggle language.
        if event == 400:
            lang_eng, lang_esp = all_imports.language_create.create_remove_language()
            menu_eng.close()
            menu_esp.close()
            if lang:
                event, values = lang_eng.read()
                if event == 455:
                    lang = False
                lang_eng.close()
            elif not lang:
                event, values = lang_esp.read()
                if event == 454:
                    lang = True
                lang_esp.close()
            event = False
            mode_text = None

        # Show help.
        if event == 500:
            help_eng, help_esp = all_imports.help_create.create_remove_help()
            menu_eng.close()
            menu_esp.close()
            if lang:
                event, values = help_eng.read()
                help_eng.close()
            elif not lang:
                event, values = help_esp.read()
                help_esp.close()

            # Show coffee.
            while event == 666:
                coffee_eng, coffee_esp = all_imports.coffee_create.create_remove_coffee()
                if lang:
                    event, values = coffee_eng.read()
                elif not lang:
                    event, values = coffee_esp.read()

                if event == 800:
                    coffee_eng.close()
                    coffee_esp.close()
                    break

                addresses = ["bc1qxzgzrwmgd7l02cd2engq5rfvpdhkp6degglach", "0xA7eA66c2Ef113006c51A6c140EC4147464d8f260",
                             "88khuWDVBMrXMoBnDNdCA6CfuhBiejrgFRYFm2Qh6D9YUrUGs"
                             "FLHcbahSnkUw8ThZG42jP75vWLwrbupjAEcBwWbH3jzsf3", "t1Y2UiuGFLNYQMtcW4dpbKmsuoQ1hVnhyeE",
                             "zs10cgw0hgyz8hdx0pgqfu8eufqvr4m7t2yw2mxym5ma4z836y9sjrwrzaqfj4nrsflrfl7y6pshds",
                             "WJEU5DEYA32ICA7KSLMRIFOCLR2ZXJNKZRXH2AVA7FKTS277NODZDX3OII",
                             "HQNLZBEGEG6XJ5JL63H4ALGP7XVC5UUTSCXYGNG57HCH7BBQYINMYUU3LY",
                             "one15t6qgqv9cs7k0pae5z6w2yusxuehrackaf22gr",
                             "ltc1qjthj8smy3t77wlwwwlu799c6vvm3rftdet7306", "tz1VeDF5BPwqWXYJLwzTP4APwhTbjUYV9e9p",
                             "cosmos1xq7ywms0rh46plkhyt3s2zetw2e02a5xvp0h0v",
                             "GCKDR5KJLNE2T54T6EGOOI7V2CBZBL5XWJUAPXJVWLEBSUYY5A4OOLKJ"]

                title = {1: "BTC", 2: "ETH", 3: "XMR", 4: "ZEC", 5: "ZEC", 6: "ALGO", 7: "ALGO ASA", 8: "ONE", 9: "LTC",
                         10: "XTZ", 11: "ATOM", 12: "XLM"}
                if event in range(1, 13):
                    all_imports.pyclip.copy(addresses[(event - 1)])
                    img = all_imports.pyqrcode.create(addresses[(event - 1)], error = "H", version = 12,
                                                      mode = "binary")
                    img.png(title[event], scale = 6, module_color = [0, 0, 0, 128])
                    all_imports.pSG.popup_auto_close(auto_close_duration = 5, button_type = 5,
                                                     image = title[event], title = title[event])
                    all_imports.os.remove(title[event])
                coffee_eng.close()
                coffee_esp.close()
                event = 666

        # Exit
        if event == 600:
            menu_eng.close()
            menu_esp.close()
            exit(0)

    return lang, mode_text
