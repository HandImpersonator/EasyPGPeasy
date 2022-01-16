# enc_dec_create.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imports


def create_remove_sign():
    """Create encryption and decryption windows layout.
    Return created layout."""
    width1 = 16
    width2 = 60
    width3 = 27

    enc_dec_mode_eng = ["Encrypt", "Decrypt", "Sign", "Verify"]
    enc_dec_mode_esp = ["Cifrar", "Descifrar", "Firmar", "Verificar"]
    inp_out_eng = ["Input:", "Output:"]
    inp_out_esp = ["Entrada:", "Salida:"]
    button_eng = ["Copy to clipboard", "Paste from clipboard", "Menu", "Close"]
    button_esp = ["Copiar a portapapeles", "Pegar del portapapeles", "Menú", "Cerrar"]

    # English
    input_column_enc_eng = [[all_imports.pSG.Text(inp_out_eng[0])], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "input", size = (width2, 10))],
                            [all_imports.pSG.Button(enc_dec_mode_eng[0], key = "enc", size = (width3, 0)),
                             all_imports.pSG.Button(button_eng[1], key = "xclipp", size = (width3, 0))]]
    output_column_enc_eng = [[all_imports.pSG.Text(inp_out_eng[1])], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "output", size = (width2, 25),
                                  write_only = True)]]
    input_column_dec_eng = [[all_imports.pSG.Text(inp_out_eng[0])], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "input", size = (width2, 10))],
                            [all_imports.pSG.Button(enc_dec_mode_eng[1], key = "dec", size = (width3, 0)),
                             all_imports.pSG.Button(button_eng[1], key = "xclipp", size = (width3, 0))]]
    output_column_dec_eng = [[all_imports.pSG.Text(inp_out_eng[1])], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "output", size = (width2, 25),
                                  write_only = True)]]
    input_column_sig_eng = [[all_imports.pSG.Text(inp_out_eng[0])], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "input", size = (width2, 10))],
                            [all_imports.pSG.Button(enc_dec_mode_eng[2], key = "sig", size = (width3, 0)),
                             all_imports.pSG.Button(button_eng[1], key = "xclipp", size = (width3, 0))]]
    output_column_sig_eng = [[all_imports.pSG.Text(inp_out_eng[1])], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "output", size = (width2, 25),
                                  write_only = True)]]
    input_column_ver_eng = [[all_imports.pSG.Text(inp_out_eng[0])], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "input", size = (width2, 10))],
                            [all_imports.pSG.Button(enc_dec_mode_eng[3], key = "ver", size = (width3, 0)),
                             all_imports.pSG.Button(button_eng[1], key = "xclipp", size = (width3, 0))]]
    output_column_ver_eng = [[all_imports.pSG.Text(inp_out_eng[1])], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "output", size = (width2, 25),
                                  write_only = True)]]

    # Spanish
    input_column_enc_esp = [[all_imports.pSG.Text(inp_out_esp[0])], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "input", size = (width2, 10))],
                            [all_imports.pSG.Button(enc_dec_mode_esp[0], key = "enc", size = (width3, 0)),
                             all_imports.pSG.Button(button_esp[1], key = "xclipp", size = (width3, 0))]]
    output_column_enc_esp = [[all_imports.pSG.Text(inp_out_esp[1])], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "output", size = (width2, 25),
                                  write_only = True)]]
    input_column_dec_esp = [[all_imports.pSG.Text(inp_out_esp[0])], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "input", size = (width2, 10))],
                            [all_imports.pSG.Button(enc_dec_mode_esp[1], key = "dec", size = (width3, 0)),
                             all_imports.pSG.Button(button_esp[1], key = "xclipp", size = (width3, 0))]]
    output_column_dec_esp = [[all_imports.pSG.Text(inp_out_esp[1])], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "output", size = (width2, 25),
                                  write_only = True)]]
    input_column_sig_esp = [[all_imports.pSG.Text(inp_out_esp[0])], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "input", size = (width2, 10))],
                            [all_imports.pSG.Button(enc_dec_mode_esp[2], key = "sig", size = (width3, 0)),
                             all_imports.pSG.Button(button_esp[1], key = "xclipp", size = (width3, 0))]]
    output_column_sig_esp = [[all_imports.pSG.Text(inp_out_esp[1])], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "output", size = (width2, 25),
                                  write_only = True)]]
    input_column_ver_esp = [[all_imports.pSG.Text(inp_out_esp[0])], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "input", size = (width2, 10))],
                            [all_imports.pSG.Button(enc_dec_mode_esp[3], key = "ver", size = (width3, 0)),
                             all_imports.pSG.Button(button_esp[1], key = "xclipp", size = (width3, 0))]]
    output_column_ver_esp = [[all_imports.pSG.Text(inp_out_esp[1])], [
        all_imports.pSG.Multiline(autoscroll = True, enable_events = False, key = "output", size = (width2, 25),
                                  write_only = True)]]

    layout_text_enc_eng = [[all_imports.pSG.Column(input_column_enc_eng, element_justification = "center")],
                           [all_imports.pSG.HSeparator()],
                           [all_imports.pSG.Column(output_column_enc_eng, element_justification = "center")],
                           [all_imports.pSG.Button(button_eng[0], key = "xclipc", size = (width1, 0)),
                           all_imports.pSG.Button(button_eng[2], key = 800, size = (width1, 0)),
                           all_imports.pSG.Button(button_eng[3],  key = 600, size = (width1, 0))]]
    layout_text_dec_eng = [[all_imports.pSG.Column(input_column_dec_eng, element_justification = "center")],
                           [all_imports.pSG.HSeparator()],
                           [all_imports.pSG.Column(output_column_dec_eng, element_justification = "center")],
                           [all_imports.pSG.Button(button_eng[0], key = "xclipc", size = (width1, 0)),
                           all_imports.pSG.Button(button_eng[2], key = 800, size = (width1, 0)),
                           all_imports.pSG.Button(button_eng[3],  key = 600, size = (width1, 0))]]
    layout_text_sig_eng = [[all_imports.pSG.Column(input_column_sig_eng, element_justification = "center")],
                           [all_imports.pSG.HSeparator()],
                           [all_imports.pSG.Column(output_column_sig_eng, element_justification = "center")],
                           [all_imports.pSG.Button(button_eng[0], key = "xclipc", size = (width1, 0)),
                           all_imports.pSG.Button(button_eng[2], key = 800, size = (width1, 0)),
                           all_imports.pSG.Button(button_eng[3],  key = 600, size = (width1, 0))]]
    layout_text_ver_eng = [[all_imports.pSG.Column(input_column_ver_eng, element_justification = "center")],
                           [all_imports.pSG.HSeparator()],
                           [all_imports.pSG.Column(output_column_ver_eng, element_justification = "center")],
                           [all_imports.pSG.Button(button_eng[0], key = "xclipc", size = (width1, 0)),
                           all_imports.pSG.Button(button_eng[2], key = 800, size = (width1, 0)),
                           all_imports.pSG.Button(button_eng[3],  key = 600, size = (width1, 0))]]
    layout_text_enc_esp = [[all_imports.pSG.Column(input_column_enc_esp, element_justification = "center")],
                           [all_imports.pSG.HSeparator()],
                           [all_imports.pSG.Column(output_column_enc_esp, element_justification = "center")],
                           [all_imports.pSG.Button(button_esp[0], key = "xclipc", size = (width1, 0)),
                           all_imports.pSG.Button(button_esp[2], key = 800, size = (width1, 0)),
                           all_imports.pSG.Button(button_esp[3],  key = 600, size = (width1, 0))]]
    layout_text_dec_esp = [[all_imports.pSG.Column(input_column_dec_esp, element_justification = "center")],
                           [all_imports.pSG.HSeparator()],
                           [all_imports.pSG.Column(output_column_dec_esp, element_justification = "center")],
                           [all_imports.pSG.Button(button_esp[0], key = "xclipc", size = (width1, 0)),
                           all_imports.pSG.Button(button_esp[2], key = 800, size = (width1, 0)),
                           all_imports.pSG.Button(button_esp[3],  key = 600, size = (width1, 0))]]
    layout_text_sig_esp = [[all_imports.pSG.Column(input_column_sig_esp, element_justification = "center")],
                           [all_imports.pSG.HSeparator()],
                           [all_imports.pSG.Column(output_column_sig_esp, element_justification = "center")],
                           [all_imports.pSG.Button(button_esp[0], key = "xclipc", size = (width1, 0)),
                           all_imports.pSG.Button(button_esp[2], key = 800, size = (width1, 0)),
                           all_imports.pSG.Button(button_esp[3],  key = 600, size = (width1, 0))]]
    layout_text_ver_esp = [[all_imports.pSG.Column(input_column_ver_esp, element_justification = "center")],
                           [all_imports.pSG.HSeparator()],
                           [all_imports.pSG.Column(output_column_ver_esp, element_justification = "center")],
                           [all_imports.pSG.Button(button_esp[0], key = "xclipc", size = (width1, 0)),
                           all_imports.pSG.Button(button_esp[2], key = 800, size = (width1, 0)),
                           all_imports.pSG.Button(button_esp[3],  key = 600, size = (width1, 0))]]

    message_enc_eng = all_imports.pSG.Window("EZPZ PGP - " + enc_dec_mode_eng[0], layout_text_enc_eng,
                                             disable_close = True, element_justification = "center")
    message_dec_eng = all_imports.pSG.Window("EZPZ PGP - " + enc_dec_mode_eng[1], layout_text_dec_eng,
                                             disable_close = True, element_justification = "center")
    message_sig_eng = all_imports.pSG.Window("EZPZ PGP - " + enc_dec_mode_eng[2], layout_text_sig_eng,
                                             disable_close = True, element_justification = "center")
    message_ver_eng = all_imports.pSG.Window("EZPZ PGP - " + enc_dec_mode_eng[3], layout_text_ver_eng,
                                             disable_close = True, element_justification = "center")
    message_enc_esp = all_imports.pSG.Window("EZPZ PGP - " + enc_dec_mode_esp[0], layout_text_enc_esp,
                                             disable_close = True, element_justification = "center")
    message_dec_esp = all_imports.pSG.Window("EZPZ PGP - " + enc_dec_mode_esp[1], layout_text_dec_esp,
                                             disable_close = True, element_justification = "center")
    message_sig_esp = all_imports.pSG.Window("EZPZ PGP - " + enc_dec_mode_esp[2], layout_text_sig_esp,
                                             disable_close = True, element_justification = "center")
    message_ver_esp = all_imports.pSG.Window("EZPZ PGP - " + enc_dec_mode_esp[3], layout_text_ver_esp,
                                             disable_close = True, element_justification = "center")

    return message_enc_eng, message_enc_esp, message_dec_eng, message_dec_esp, message_sig_eng, message_sig_esp, \
        message_ver_eng, message_ver_esp
