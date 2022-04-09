# eds_layout.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Functions import all_imp


def crem_enc_dec():
    """Create encryption, decryption and signing windows layout.
    Return created layout."""

    width1 = 16
    width2 = 60
    width3 = 27

    enc_dec_mode_eng = ["Encrypt", "Decrypt", "Sign", "Verify"]
    inp_out_eng = ["Input:", "Output:"]
    button_eng = ["Paste from clipboard", "Menu", "Close"]
    enc_dec_mode_esp = ["Cifrar", "Descifrar", "Firmar", "Verificar"]
    inp_out_esp = ["Entrada:", "Salida:"]
    button_esp = ["Pegar del portapapeles", "Menú", "Cerrar"]

    # English
    input_column_enc_eng = [[all_imp.pSG.Text(inp_out_eng[0])], [
        all_imp.pSG.Multiline(autoscroll = True, enable_events = False, focus = True, key = "input",
                              size = (width2, 10))],
                            [all_imp.pSG.Button(enc_dec_mode_eng[0], focus = False, key = "enc", size = (width3, 0)),
                                all_imp.pSG.Button(button_eng[0], focus = False, key = "xclipp", size = (width3, 0))]]
    output_column_enc_eng = [[all_imp.pSG.Text(inp_out_eng[1])], [
        all_imp.pSG.Multiline(autoscroll = True, disabled = True, enable_events = False, key = "output",
                              size = (width2, 25), write_only = True)]]
    input_column_dec_eng = [[all_imp.pSG.Text(inp_out_eng[0])], [
        all_imp.pSG.Multiline(autoscroll = True, enable_events = False, focus = True, key = "input",
                              size = (width2, 10))],
                            [all_imp.pSG.Button(enc_dec_mode_eng[1], focus = False, key = "dec", size = (width3, 0)),
                                all_imp.pSG.Button(button_eng[0], focus = False, key = "xclipp", size = (width3, 0))]]
    output_column_dec_eng = [[all_imp.pSG.Text(inp_out_eng[1])], [
        all_imp.pSG.Multiline(autoscroll = True, disabled = True, enable_events = False, key = "output",
                              size = (width2, 25), write_only = True)]]
    input_column_sig_eng = [[all_imp.pSG.Text(inp_out_eng[0])], [
        all_imp.pSG.Multiline(autoscroll = True, enable_events = False, focus = True, key = "input",
                              size = (width2, 10))],
                            [all_imp.pSG.Button(enc_dec_mode_eng[2], focus = False, key = "sig", size = (width3, 0)),
                                all_imp.pSG.Button(button_eng[0], focus = False, key = "xclipp", size = (width3, 0))]]
    output_column_sig_eng = [[all_imp.pSG.Text(inp_out_eng[1])], [
        all_imp.pSG.Multiline(autoscroll = True, disabled = True, enable_events = False, key = "output",
                              size = (width2, 25), write_only = True)]]

    # Spanish
    input_column_enc_esp = [[all_imp.pSG.Text(inp_out_esp[0])], [
        all_imp.pSG.Multiline(autoscroll = True, enable_events = False, focus = True, key = "input",
                              size = (width2, 10))],
                            [all_imp.pSG.Button(enc_dec_mode_esp[0], focus = False, key = "enc", size = (width3, 0)),
                                all_imp.pSG.Button(button_esp[0], focus = False, key = "xclipp", size = (width3, 0))]]
    output_column_enc_esp = [[all_imp.pSG.Text(inp_out_esp[1])], [
        all_imp.pSG.Multiline(autoscroll = True, disabled = True, enable_events = False, key = "output",
                              size = (width2, 25), write_only = True)]]
    input_column_dec_esp = [[all_imp.pSG.Text(inp_out_esp[0])], [
        all_imp.pSG.Multiline(autoscroll = True, enable_events = False, focus = True, key = "input",
                              size = (width2, 10))],
                            [all_imp.pSG.Button(enc_dec_mode_esp[1], focus = False, key = "dec", size = (width3, 0)),
                                all_imp.pSG.Button(button_esp[0], focus = False, key = "xclipp", size = (width3, 0))]]
    output_column_dec_esp = [[all_imp.pSG.Text(inp_out_esp[1])], [
        all_imp.pSG.Multiline(autoscroll = True, disabled = True, enable_events = False, key = "output",
                              size = (width2, 25), write_only = True)]]
    input_column_sig_esp = [[all_imp.pSG.Text(inp_out_esp[0])], [
        all_imp.pSG.Multiline(autoscroll = True, enable_events = False, focus = True, key = "input",
                              size = (width2, 10))],
                            [all_imp.pSG.Button(enc_dec_mode_esp[2], focus = False, key = "sig", size = (width3, 0)),
                                all_imp.pSG.Button(button_esp[0], focus = False, key = "xclipp", size = (width3, 0))]]
    output_column_sig_esp = [[all_imp.pSG.Text(inp_out_esp[1])], [
        all_imp.pSG.Multiline(autoscroll = True, disabled = True, enable_events = False, key = "output",
                              size = (width2, 25), write_only = True)]]

    layout_text_enc_eng = [[all_imp.pSG.Column(input_column_enc_eng, element_justification = "center")],
                           [all_imp.pSG.HSeparator()],
                           [all_imp.pSG.Column(output_column_enc_eng, element_justification = "center")], [
                               all_imp.pSG.Button(button_eng[1], focus = False, key = 800, size = (width1, 0)),
                               all_imp.pSG.Button(button_eng[2], focus = False, key = 600, size = (width1, 0))]]
    layout_text_dec_eng = [[all_imp.pSG.Column(input_column_dec_eng, element_justification = "center")],
                           [all_imp.pSG.HSeparator()],
                           [all_imp.pSG.Column(output_column_dec_eng, element_justification = "center")], [
                               all_imp.pSG.Button(button_eng[1], focus = False, key = 800, size = (width1, 0)),
                               all_imp.pSG.Button(button_eng[2], focus = False, key = 600, size = (width1, 0))]]
    layout_text_sig_eng = [[all_imp.pSG.Column(input_column_sig_eng, element_justification = "center")],
                           [all_imp.pSG.HSeparator()],
                           [all_imp.pSG.Column(output_column_sig_eng, element_justification = "center")], [
                               all_imp.pSG.Button(button_eng[1], focus = False, key = 800, size = (width1, 0)),
                               all_imp.pSG.Button(button_eng[2], focus = False, key = 600, size = (width1, 0))]]
    layout_text_enc_esp = [[all_imp.pSG.Column(input_column_enc_esp, element_justification = "center")],
                           [all_imp.pSG.HSeparator()],
                           [all_imp.pSG.Column(output_column_enc_esp, element_justification = "center")], [
                               all_imp.pSG.Button(button_esp[1], focus = False, key = 800, size = (width1, 0)),
                               all_imp.pSG.Button(button_esp[2], focus = False, key = 600, size = (width1, 0))]]
    layout_text_dec_esp = [[all_imp.pSG.Column(input_column_dec_esp, element_justification = "center")],
                           [all_imp.pSG.HSeparator()],
                           [all_imp.pSG.Column(output_column_dec_esp, element_justification = "center")], [
                               all_imp.pSG.Button(button_esp[1], focus = False, key = 800, size = (width1, 0)),
                               all_imp.pSG.Button(button_esp[2], focus = False, key = 600, size = (width1, 0))]]
    layout_text_sig_esp = [[all_imp.pSG.Column(input_column_sig_esp, element_justification = "center")],
                           [all_imp.pSG.HSeparator()],
                           [all_imp.pSG.Column(output_column_sig_esp, element_justification = "center")], [
                               all_imp.pSG.Button(button_esp[1], focus = False, key = 800, size = (width1, 0)),
                               all_imp.pSG.Button(button_esp[2], focus = False, key = 600, size = (width1, 0))]]

    mes_enc_eng = all_imp.pSG.Window("EZPZ PGP - " + enc_dec_mode_eng[0], layout_text_enc_eng, disable_close = True,
                                     element_justification = "center")
    mes_dec_eng = all_imp.pSG.Window("EZPZ PGP - " + enc_dec_mode_eng[1], layout_text_dec_eng, disable_close = True,
                                     element_justification = "center")
    mes_sig_eng = all_imp.pSG.Window("EZPZ PGP - " + enc_dec_mode_eng[2], layout_text_sig_eng, disable_close = True,
                                     element_justification = "center")
    mes_enc_esp = all_imp.pSG.Window("EZPZ PGP - " + enc_dec_mode_esp[0], layout_text_enc_esp, disable_close = True,
                                     element_justification = "center")
    mes_dec_esp = all_imp.pSG.Window("EZPZ PGP - " + enc_dec_mode_esp[1], layout_text_dec_esp, disable_close = True,
                                     element_justification = "center")
    mes_sig_esp = all_imp.pSG.Window("EZPZ PGP - " + enc_dec_mode_esp[2], layout_text_sig_esp, disable_close = True,
                                     element_justification = "center")

    return mes_enc_eng, mes_enc_esp, mes_dec_eng, mes_dec_esp, mes_sig_eng, mes_sig_esp
