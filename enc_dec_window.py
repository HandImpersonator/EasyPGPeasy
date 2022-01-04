# enc_dec_window.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import all_imports


def enc_dec_create():
    enc_dec_mode = ["Encrypt", "Cifrar", "Decrypt", "Descifrar"]

    input_column_enc_eng = [[all_imports.pSG.Text("Input:")], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "input", size = (50, 10))],
                            [all_imports.pSG.Button("Encrypt", key = "enc")]]
    output_column_enc_eng = [[all_imports.pSG.Text("Output:")], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "output", size = (50, 25),
                                  write_only = True)]]
    input_column_enc_esp = [[all_imports.pSG.Text("Entrada:")], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "input", size = (50, 10))],
                            [all_imports.pSG.Button("Cifrar", key = "enc")]]
    output_column_enc_esp = [[all_imports.pSG.Text("Salida:")], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "output", size = (50, 25),
                                  write_only = True)]]
    input_column_dec_eng = [[all_imports.pSG.Text("Input:")], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "input", size = (50, 10))],
                            [all_imports.pSG.Button("Decrypt", key = "dec")]]
    output_column_dec_eng = [[all_imports.pSG.Text("Output:")], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "output", size = (50, 25),
                                  write_only = True)]]
    input_column_dec_esp = [[all_imports.pSG.Text("Entrada:")], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "input", size = (50, 10))],
                            [all_imports.pSG.Button("Descifrar", key = "dec")]]
    output_column_dec_esp = [[all_imports.pSG.Text("Salida:")], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "output", size = (50, 25),
                                  write_only = True)]]

    # ----- Full layout -----
    layout_text_enc_eng = [[all_imports.pSG.Column(input_column_enc_eng, element_justification = "center")],
                           [all_imports.pSG.HSeparator()],
                           [all_imports.pSG.Column(output_column_enc_eng, element_justification = "center")],
                           [all_imports.pSG.Button("Menu", key = 800)], [all_imports.pSG.Button("Close", key = 600)]]
    layout_text_enc_esp = [[all_imports.pSG.Column(input_column_enc_esp, element_justification = "center")],
                           [all_imports.pSG.HSeparator()],
                           [all_imports.pSG.Column(output_column_enc_esp, element_justification = "center")],
                           [all_imports.pSG.Button("Menú", key = 800)], [all_imports.pSG.Button("Cerrar", key = 600)]]
    layout_text_dec_eng = [[all_imports.pSG.Column(input_column_dec_eng, element_justification = "center")],
                           [all_imports.pSG.HSeparator()],
                           [all_imports.pSG.Column(output_column_dec_eng, element_justification = "center")],
                           [all_imports.pSG.Button("Menu", key = 800)], [all_imports.pSG.Button("Close", key = 600)]]
    layout_text_dec_esp = [[all_imports.pSG.Column(input_column_dec_esp, element_justification = "center")],
                           [all_imports.pSG.HSeparator()],
                           [all_imports.pSG.Column(output_column_dec_esp, element_justification = "center")],
                           [all_imports.pSG.Button("Menú", key = 800)], [all_imports.pSG.Button("Cerrar", key = 600)]]

    message_enc_eng = all_imports.pSG.Window("EZPZ PGP - " + enc_dec_mode[0], layout_text_enc_eng, disable_close = True,
                                             element_justification = "center")
    message_enc_esp = all_imports.pSG.Window("EZPZ PGP - " + enc_dec_mode[1], layout_text_enc_esp, disable_close = True,
                                             element_justification = "center")
    message_dec_eng = all_imports.pSG.Window("EZPZ PGP - " + enc_dec_mode[2], layout_text_dec_eng, disable_close = True,
                                             element_justification = "center")
    message_dec_esp = all_imports.pSG.Window("EZPZ PGP - " + enc_dec_mode[3], layout_text_dec_esp, disable_close = True,
                                             element_justification = "center")

    return message_enc_eng, message_enc_esp, message_dec_eng, message_dec_esp
