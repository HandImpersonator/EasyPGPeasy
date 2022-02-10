# menu.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imp


def create_menu(lang, imp, ks):
    """Handles all the menu choices and redirects to the corresponding windows, to import, or handle the data that need
    the keypairs.
    Returns choices made."""

    error1, error2, fin, paste, well_is_it = "", "", "", "", ""
    email, event, event1, imp_eng, imp_esp, mode_text, name, ok = None, False, False, None, None, None, None, False
    height, values, width = 440, [], 320

    while True:

        menu_eng, menu_esp = all_imp.menu_layout.crem_menu(height, width)

        # Show menu.
        if not event or event == 800:
            if lang:
                event, values = menu_eng.read()
                menu_eng.close()
            elif not lang:
                event, values = menu_esp.read()
                menu_esp.close()

        # Create PGP Pair.
        if event == 100:
            size = tuple(values.items())[0][1]
            keypair_choose_eng, keypair_choose_esp = all_imp.choose_layout.crem_kp()
            if lang:
                event, values = keypair_choose_eng.read()
                keypair_choose_eng.close()
            elif not lang:
                event, values = keypair_choose_esp.read()
                keypair_choose_esp.close()

            if event == 800:
                event = False

            # Random name PGP Keypair.
            if event == 116:
                all_imp.create_pgp_pair.pgpy_create_keypair(email, ks, lang, name, size, False)
                event = False

            # Custom name PGP Keypair.
            elif event == 118:
                ne_choose_eng, ne_choose_esp = all_imp.choose_layout.crem_ne()
                if lang:
                    event, values = ne_choose_eng.read()
                    ne_choose_eng.close()
                elif not lang:
                    event, values = ne_choose_esp.read()
                    ne_choose_esp.close()
                if event == 660:
                    name, email = (str(tuple(values.items())[0][1]), str(tuple(values.items())[1][1]))
                    all_imp.create_pgp_pair.pgpy_create_keypair(email, ks, lang, name, size, True)
                event = False

        # Import handling
        if event in [110, 112, 114]:
            if event == 110:
                imp_eng, imp_esp = all_imp.imp_layout.crem_enc_import()
            elif event == 112:
                imp_eng, imp_esp = all_imp.imp_layout.crem_pub_import()
            elif event == 114:
                imp_eng, imp_esp = all_imp.imp_layout.crem_sig_import()

            if lang:
                event1, values = imp_eng.read()
            elif not lang:
                event1, values = imp_esp.read()

            # Paste from clipboard.
            if event1 == "xclipp":
                try:
                    paste = str(all_imp.pyclip.paste(text = True).strip())
                except BaseException:
                    if lang:
                        paste = "Clipboard was empty, here you go."
                    elif not lang:
                        paste = "El portapapeles estaba vacío, aquí tienes."
                toggle = False
                # Update window with pasted content.
                if lang:
                    if event == 110:
                        imp_eng[110].update(value = paste)
                    elif event == 112:
                        imp_eng[112].update(value = paste)
                    elif event == 114:
                        imp_eng[114].update(value = paste)
                    imp_eng["xclipp"].update(visible = toggle)
                    event1, values = imp_eng.read()
                    imp_eng.close()
                elif not lang:
                    if event == 110:
                        imp_esp[110].update(value = paste)
                    elif event == 112:
                        imp_esp[112].update(value = paste)
                    elif event == 114:
                        imp_esp[114].update(value = paste)
                    imp_eng["xclipp"].update(visible = toggle)
                    event1, values = imp_eng.read()
                    imp_esp.close()
            vp = (tuple(values.items())[0][0], tuple(values.items())[0][1])
            imp_eng.close()
            imp_esp.close()

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
                    all_imp.pSG.popup_error(error1, title = error2)
                elif vp[1]:

                    # Import message.
                    if vp[0] == 110:
                        text_file_v = open(imp + "/v_imported_message.txt", "w")
                        text_file_v.write(str(vp[1]))
                        text_file_v.close()
                        ok = True

                    # Import public key
                    elif vp[0] == 112:
                        well_is_it = all_imp.edsv.is_public(vp[1], lang)
                        if well_is_it:
                            text_file_v = open(imp + "/v_imported_public.asc", "w")
                            text_file_v.write(str(vp[1]))
                            text_file_v.close()
                            ok = True
                        else:
                            error_popup_eng = ["Not a valid Public key.", "Error encrypting!"]
                            error_popup_esp = ["No es una clave Pública válida.", "¡Error cifrando!"]
                            if lang:
                                error1 = error_popup_eng[0]
                                error2 = error_popup_eng[1]
                            if not lang:
                                error1 = error_popup_esp[0]
                                error2 = error_popup_esp[1]
                            all_imp.pSG.popup_error(error1, title = error2)

                    # Import signature
                    elif vp[0] == 114:
                        well_is_it = all_imp.edsv.is_signature(str(vp[1]), lang)
                        if well_is_it:
                            text_file_v = open(imp + "/v_imported_signature.txt", "w")
                            text_file_v.write(str(vp[1]))
                            text_file_v.close()
                            ok = True
                        else:
                            error_popup_eng = ["Not a valid Signature.", "Error encrypting!"]
                            error_popup_esp = ["No es una Firma válida.", "¡Error cifrando!"]
                            if lang:
                                error1 = error_popup_eng[0]
                                error2 = error_popup_eng[1]
                            if not lang:
                                error1 = error_popup_esp[0]
                                error2 = error_popup_esp[1]
                            all_imp.pSG.popup_error(error1, title = error2)

                    # Show finished message
                    if ok:
                        if lang:
                            fin = "Done! Saved in Imported."
                        elif not lang:
                            fin = "¡Hecho! Guardado en Imported."
                        all_imp.pSG.popup_auto_close(fin, auto_close_duration = 1.2, button_type = 5, title = fin)
                        event = False

            if event1 == 800:
                event = False

        if event in [200, 300, 250, 350]:
            # Select encrypt mode.
            if event == 200:
                mode_text = 15

            # Select decrypt mode.
            elif event == 300:
                mode_text = 20

            # Select sign mode.
            elif event == 250:
                mode_text = 30

            # Select verify mode.
            elif event == 350:
                mode_text = 40

            break

        # Toggle language.
        if event == 400:
            lang_eng, lang_esp = all_imp.lang_layout.crem_language()
            if lang:
                event, values = lang_eng.read()
                lang_eng.close()
                if event == 455:
                    lang = False
            elif not lang:
                event, values = lang_esp.read()
                lang_esp.close()
                if event == 454:
                    lang = True
            event = False
            mode_text = None

        # Show help.
        if event == 500:
            help_eng, help_esp = all_imp.help_layout.crem_help()
            if lang:
                event, values = help_eng.read()
                help_eng.close()
            elif not lang:
                event, values = help_esp.read()
                help_esp.close()

            # Show coffee.
            while event == 666:
                coffee_eng, coffee_esp = all_imp.help_layout.crem_coffee()
                if lang:
                    event, values = coffee_eng.read()
                    coffee_eng.close()
                elif not lang:
                    event, values = coffee_esp.read()
                    coffee_esp.close()

                if event == 800:
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

                title = {1: "Bitcoin", 2: "Ethereum", 3: "Monero", 4: "ZCash Transparent", 5: "ZCash Shielded",
                         6: "Algorand", 7: "Alogrand Assets", 8: "Harmony", 9: "Litecoin", 10: "Tezos", 11: "Cosmos",
                         12: "Stellar"}
                if event in range(1, 13):
                    all_imp.pyclip.copy(addresses[(event - 1)])
                    img = all_imp.pyqrcode.create(addresses[(event - 1)], error = "H", version = 12, mode = "binary")
                    img.png(title[event], scale = 6, module_color = [0, 0, 0, 128])
                    all_imp.pSG.popup_timed("Closing in 5 seconds...", auto_close_duration = 5, button_type = 5,
                                            image = title[event], title = title[event])
                    all_imp.os.remove(title[event])
                event = 666

        # Exit
        if event == 600:
            exit(0)

    return lang, mode_text
