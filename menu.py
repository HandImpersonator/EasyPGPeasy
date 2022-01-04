# menu.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import all_imports
import png


def create_menu(lang):

    event = False
    height = 370
    values = {}
    width = 360

    while True:

        menu_eng, menu_esp = all_imports.menu_create.create_remove_menu(height, width)
        if not event or event == 800:
            if lang:
                event, values = menu_eng.read()
            elif not lang:
                event, values = menu_esp.read()

        # Create PGP Pair.
        if event == 100:
            private_key, public_key = all_imports.create_pgp_pair.pgpy_create_keypair(values["value"])
            text_file_private = open("./Keys/private.asc", "w")
            text_file_private.write(str(private_key))
            text_file_private.close()
            text_file_public = open("./Keys/public.asc", "w")
            text_file_public.write(str(public_key))
            text_file_public.close()
            if lang:
                all_imports.pSG.popup_auto_close("Done!", auto_close_duration = 0.8, button_type = 5, title = "Done!")
                menu_eng.close()
            elif not lang:
                all_imports.pSG.popup_auto_close("¡Hecho!", auto_close_duration = 0.8, button_type = 5,
                                                 title = "¡Hecho!")
                menu_esp.close()

        # Import V_Public key.
        if event == "v_p_k":
            imp_eng, imp_esp = all_imports.import_create.create_remove_import()
            if lang:
                menu_eng.close()
                event, values = imp_eng.read()
            elif not lang:
                menu_esp.close()
                event, values = imp_esp.read()

            if event == 700:
                vpk = values["V_P_K"]
                if not vpk:
                    if lang:
                        all_imports.pSG.popup_error("Cannot import empty data.")
                    elif not lang:
                        all_imports.pSG.popup_error("No se puede importar datos vacíos.")
                    event = "v_p_k"
                    imp_eng.close()
                    imp_esp.close()
                if vpk:
                    try:
                        is_it = all_imports.enc_dec.is_public(vpk)
                        if is_it:
                            text_file_v_public = open("./Keys/v_public.asc", "w")
                            text_file_v_public.write(str(vpk))
                            text_file_v_public.close()
                            if lang:
                                all_imports.pSG.popup_auto_close("Done!", auto_close_duration = 0.8, button_type = 5)
                                imp_eng.close()
                            elif not lang:
                                all_imports.pSG.popup_auto_close("¡Hecho!", auto_close_duration = 0.8, button_type = 5)
                                imp_esp.close()
                        elif not is_it:
                            all_imports.pSG.popup_error("Imported key is not a valid PUBLIC PGP key.")
                    except ValueError:
                        if lang:
                            all_imports.pSG.popup_error("Expected: ASCII-armored PGP data, "
                                                        "not a valid PGP Public key to import.")
                        if not lang:
                            all_imports.pSG.popup_error("Expected: ASCII-armored PGP data, "
                                                        "no es una clave pública PGP válida para importar.")
                        imp_eng.close()
                        imp_esp.close()
                        mode_text = None
                        break

            if event == 800:
                imp_eng.close()
                imp_esp.close()

        # Select encrypt mode.
        if event == 200:
            menu_eng.close()
            menu_esp.close()
            mode_text = True
            break

        # Select decrypt mode.
        if event == 300:
            menu_eng.close()
            menu_esp.close()
            mode_text = False
            break

        # Toggle language.
        if event == 400:
            if lang:
                lang_eng, lang_esp = all_imports.language_create.create_remove_language()
                event, values = lang_eng.read()
                if event == 454:
                    pass
                    lang_eng.close()
                    menu_eng.close()
                elif event == 455:
                    lang = False
                    lang_eng.close()
                    menu_eng.close()
                    return lang, None
                if event == 800:
                    lang_eng.close()
                    menu_eng.close()
            elif not lang:
                lang_eng, lang_esp = all_imports.language_create.create_remove_language()
                event, values = lang_esp.read()
                if event == 454:
                    lang = True
                    lang_esp.close()
                    menu_esp.close()
                    return lang, None
                elif event == 455:
                    pass
                    lang_esp.close()
                    menu_esp.close()
                if event == 800:
                    lang_esp.close()
                    menu_esp.close()

        # Show help.
        if event == 500:
            help_eng, help_esp = all_imports.help_create.create_remove_help()
            if lang:
                menu_eng.close()
                event, values = help_eng.read()
                if event == 800:
                    help_eng.close()
            elif not lang:
                menu_esp.close()
                help_eng, help_esp = all_imports.help_create.create_remove_help()
                event, values = help_esp.read()

            help_eng.close()
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

                if event == 1:
                    all_imports.pyclip.copy(
                        "bc1qxzgzrwmgd7l02cd2engq5rfvpdhkp6degglach")
                elif event == 2:
                    all_imports.pyclip.copy(
                        "0xA7eA66c2Ef113006c51A6c140EC4147464d8f260")
                    # all_imports.pSG.popup(title = "ETH",
                    # image = "./Coffee/ETH.")
                elif event == 3:
                    all_imports.pyclip.copy("88khuWDVBMrXMoBnDNdCA6CfuhBiejrgFRYFm2Qh6D9YUrUGsFLHcbahSnkUw8ThZG42"
                                            "jP75vWLwrbupjAEcBwWbH3jzsf3")  # all_imports.pSG.popup(title = "XMR",
                    # image = "./Coffee/XMR.")
                elif event == 4:
                    all_imports.pyclip.copy(
                        "t1Y2UiuGFLNYQMtcW4dpbKmsuoQ1hVnhyeE")  # all_imports.pSG.popup(title = "ZEC",
                    # image = "./Coffee/ZEC.")
                elif event == 5:
                    all_imports.pyclip.copy(
                        "t1Y2UiuGFLNYQMtcW4dpbKmsuoQ1hVnhyeE")  # all_imports.pSG.popup(title = "ZEC",
                    # image = "./Coffee/ZEC.")
                elif event == 6:
                    all_imports.pyclip.copy(
                        "WJEU5DEYA32ICA7KSLMRIFOCLR2ZXJNKZRXH2AVA7FKTS277NODZDX3OII")  # all_imports.pSG.popup(
                    # title = "ALGO", image = "./Coffee/ALGO.")
                elif event == 7:
                    all_imports.pyclip.copy(
                        "HQNLZBEGEG6XJ5JL63H4ALGP7XVC5UUTSCXYGNG57HCH7BBQYINMYUU3LY")  # all_imports.pSG.popup(
                    # title = "ALGO ASA", image = "./Coffee/ALGO_ASA.")
                elif event == 8:
                    all_imports.pyclip.copy(
                        "one15t6qgqv9cs7k0pae5z6w2yusxuehrackaf22gr")  # all_imports.pSG.popup(title = "ONE",
                    # image = "./Coffee/ONE.")
                elif event == 9:
                    all_imports.pyclip.copy(
                        "ltc1qjthj8smy3t77wlwwwlu799c6vvm3rftdet7306")  # all_imports.pSG.popup(title = "LTC",
                    # image = "./Coffee/LTC.")
                elif event == 10:
                    all_imports.pyclip.copy(
                        "tz1VeDF5BPwqWXYJLwzTP4APwhTbjUYV9e9p")  # all_imports.pSG.popup(title = "XTZ",
                    # image = "./Coffee/XTZ.")
                elif event == 11:
                    all_imports.pyclip.copy(
                        "cosmos1xq7ywms0rh46plkhyt3s2zetw2e02a5xvp0h0v")  # all_imports.pSG.popup(title = "ATOM",
                    # image = "./Coffee/ATOM.")
                elif event == 12:
                    all_imports.pyclip.copy(
                        "GCKDR5KJLNE2T54T6EGOOI7V2CBZBL5XWJUAPXJVWLEBSUYY5A4OOLKJ")  # all_imports.pSG.popup(
                    # title = "XLM", image = "./Coffee/XLM.")
                title = {1: "BTC", 2: "ETH", 3: "XMR", 4: "ZEC", 5: "ZEC", 6: "ALGO", 7: "ALGO ASA", 8: "ONE",
                         9: "LTC", 10: "XTZ", 11: "ATOM", 12: "XLM"}
                big_code = all_imports.pyqrcode.create(all_imports.pyclip.paste(text = True), error = "H",
                                                       version = 12, mode = 'binary')
                big_code.png('./Coffee/code.png', scale = 6, module_color = [0, 0, 0, 128])
                all_imports.pSG.popup_auto_close(auto_close_duration = 5, button_type = 5, image = "./Coffee/code.png",
                                                 title = title[event])

                coffee_eng.close()
                coffee_esp.close()
                event = 666

        # Exit
        if event == 600:
            menu_eng.close()
            menu_esp.close()
            exit(0)

    return lang, mode_text
