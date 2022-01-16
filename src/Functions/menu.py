# menu.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports


def create_menu(lang, imp, ks):
    event, event1 = False, False
    imp_eng, imp_esp = None, None
    lang_eng, lang_esp = "", ""
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
            private_key, public_key = all_imports.create_pgp_pair.pgpy_create_keypair(size)
            text_file_private = open(ks + "/private.asc", "w")
            text_file_private.write(str(private_key))
            text_file_private.close()
            text_file_public = open(ks + "/public.asc", "w")
            text_file_public.write(str(public_key))
            text_file_public.close()
            if lang:
                all_imports.pSG.popup_auto_close("Done!", auto_close_duration = 0.8, button_type = 5, title = "Done!")
            elif not lang:
                all_imports.pSG.popup_auto_close("¡Hecho!", auto_close_duration = 0.8, button_type = 5,
                                                 title = "¡Hecho!")
            menu_eng.close()
            menu_esp.close()
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
                    paste = all_imports.pyclip.paste(text = True).decode("utf-8").strip()
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
                    paste = all_imports.pyclip.paste(text = True).decode("utf-8").strip()
                    if event == 110:
                        imp_eng[110].update(value = paste)
                    elif event == 112:
                        imp_eng[112].update(value = paste)
                    elif event == 114:
                        imp_eng[114].update(value = paste)
                    imp_eng["xclipp"].update(visible = toggle)
                    event1, values = imp_eng.read()
            vp = (tuple(values.items())[0][0], tuple(values.items())[0][1])

            if event1 == 700:
                if not vp[1]:
                    if lang:
                        all_imports.pSG.popup_error("Cannot import empty data.")
                    elif not lang:
                        all_imports.pSG.popup_error("No se puede importar datos vacíos.")
                    imp_eng.close()
                    imp_esp.close()
                elif vp[1]:
                    try:
                        if vp[0] == 110:
                            text_file_v = open(imp + "/v_imported_message.txt", "w")
                            text_file_v.write(str(vp[1]))
                            text_file_v.close()
                            if lang:
                                all_imports.pSG.popup_auto_close("Done!", auto_close_duration = 0.8,
                                                                 button_type = 5)
                            elif not lang:
                                all_imports.pSG.popup_auto_close("¡Hecho!", auto_close_duration = 0.8,
                                                                 button_type = 5)
                            event = False
                            imp_eng.close()
                            imp_esp.close()
                        elif vp[0] == 112:
                            well_is_it = all_imports.enc_dec.is_public(vp[1])
                            if well_is_it:
                                text_file_v = open(imp + "/v_public.asc", "w")
                                text_file_v.write(str(vp[1]))
                                text_file_v.close()
                                event = False
                            elif not well_is_it:
                                if lang:
                                    all_imports.pSG.popup_error("Not a valid PUBLIC PGP key.")
                                elif not lang:
                                    all_imports.pSG.popup_error("No es una clave PÚBLICA válida.")
                            imp_eng.close()
                            imp_esp.close()
                        elif vp[0] == 114:
                            well_is_it = all_imports.enc_dec.is_signature(vp[1])
                            if well_is_it:
                                text_file_v = open(imp + "/v_signature.txt", "w")
                                text_file_v.write(str(vp[1]))
                                text_file_v.close()
                                if lang:
                                    all_imports.pSG.popup_auto_close("Done!", auto_close_duration = 0.8,
                                                                     button_type = 5)
                                elif not lang:
                                    all_imports.pSG.popup_auto_close("¡Hecho!", auto_close_duration = 0.8,
                                                                     button_type = 5)
                                imp_eng.close()
                                imp_esp.close()
                                event = False
                            elif not well_is_it:
                                if lang:
                                    all_imports.pSG.popup_error("Not a valid signature key.")
                                    imp_eng.close()
                                elif not lang:
                                    all_imports.pSG.popup_error("No es una signature válida.")
                                    imp_esp.close()
                    except ValueError:
                        if lang:
                            all_imports.pSG.popup_error("Expected: ASCII-armored PGP data, "
                                                        "not a valid PGP Public key or not a valid PGP Signature "
                                                        "to import.")
                        if not lang:
                            all_imports.pSG.popup_error("Expected: ASCII-armored PGP data, "
                                                        "no es una clave pública PGP válida o no es una Firma PGP "
                                                        "válida para importar.")
                        imp_eng.close()
                        imp_esp.close()
            if event1 == 800:
                imp_eng.close()
                imp_esp.close()
                event = False

        # Select encrypt mode.
        if event == 200:
            menu_eng.close()
            menu_esp.close()
            mode_text = 10
            break

        # Select decrypt mode.
        if event == 300:
            menu_eng.close()
            menu_esp.close()
            mode_text = 20
            break

        # Select sign mode.
        if event == 250:
            menu_eng.close()
            menu_esp.close()
            mode_text = 30
            break

        # Select verify mode.
        if event == 350:
            menu_eng.close()
            menu_esp.close()
            mode_text = 40
            break

        # Toggle language.
        if event == 400:
            if lang:
                lang_eng, lang_esp = all_imports.language_create.create_remove_language()
                event, values = lang_eng.read()
                if event == 454:
                    lang_eng.close()
                    menu_eng.close()
                    event = False
                elif event == 455:
                    lang = False
                    lang_eng.close()
                    menu_eng.close()
                    return lang, None
            elif not lang:
                lang_eng, lang_esp = all_imports.language_create.create_remove_language()
                event, values = lang_esp.read()
                if event == 454:
                    lang = True
                    lang_esp.close()
                    menu_esp.close()
                    return lang, None
                elif event == 455:
                    lang_esp.close()
                    menu_esp.close()
                    event = False
            if event == 800:
                lang_eng.close()
                menu_eng.close()
                lang_esp.close()
                menu_esp.close()

        # Show help.
        if event == 500:
            help_eng, help_esp = all_imports.help_create.create_remove_help()
            if lang:
                menu_eng.close()
                event, values = help_eng.read()
            elif not lang:
                menu_esp.close()
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
                    all_imports.pyclip.copy("bc1qxzgzrwmgd7l02cd2engq5rfvpdhkp6degglach")
                elif event == 2:
                    all_imports.pyclip.copy("0xA7eA66c2Ef113006c51A6c140EC4147464d8f260")
                elif event == 3:
                    all_imports.pyclip.copy("88khuWDVBMrXMoBnDNdCA6CfuhBiejrgFRYFm2Qh6D9YUrUGsFLHcbahSnkUw8ThZG42"
                                            "jP75vWLwrbupjAEcBwWbH3jzsf3")
                elif event == 4:
                    all_imports.pyclip.copy("t1Y2UiuGFLNYQMtcW4dpbKmsuoQ1hVnhyeE")
                elif event == 5:
                    all_imports.pyclip.copy("t1Y2UiuGFLNYQMtcW4dpbKmsuoQ1hVnhyeE")
                elif event == 6:
                    all_imports.pyclip.copy("WJEU5DEYA32ICA7KSLMRIFOCLR2ZXJNKZRXH2AVA7FKTS277NODZDX3OII")
                elif event == 7:
                    all_imports.pyclip.copy("HQNLZBEGEG6XJ5JL63H4ALGP7XVC5UUTSCXYGNG57HCH7BBQYINMYUU3LY")
                elif event == 8:
                    all_imports.pyclip.copy("one15t6qgqv9cs7k0pae5z6w2yusxuehrackaf22gr")
                elif event == 9:
                    all_imports.pyclip.copy("ltc1qjthj8smy3t77wlwwwlu799c6vvm3rftdet7306")
                elif event == 10:
                    all_imports.pyclip.copy("tz1VeDF5BPwqWXYJLwzTP4APwhTbjUYV9e9p")
                elif event == 11:
                    all_imports.pyclip.copy("cosmos1xq7ywms0rh46plkhyt3s2zetw]2e02a5xvp0h0v")
                elif event == 12:
                    all_imports.pyclip.copy("GCKDR5KJLNE2T54T6EGOOI7V2CBZBL5XWJUAPXJVWLEBSUYY5A4OOLKJ")
                title = {1: "BTC", 2: "ETH", 3: "XMR", 4: "ZEC", 5: "ZEC", 6: "ALGO", 7: "ALGO ASA", 8: "ONE", 9: "LTC",
                         10: "XTZ", 11: "ATOM", 12: "XLM"}
                img = all_imports.pyqrcode.create(all_imports.pyclip.paste(text = True), error = "H", version = 12,
                                                  mode = 'binary')
                img.png(title[event], scale = 6, module_color = [0, 0, 0, 128])
                all_imports.pSG.popup_auto_close(auto_close_duration = 5, button_type = 5, image = title[event],
                                                 title = title[event])
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
