#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2026 shlomo.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr

class dsss_decode(gr.sync_block):
    """
    docstring for block dsss_decode
    """
    def __init__(self, samp_rate, t_sym, seed):
        gr.sync_block.__init__(self,
            name="dsss_decode",
            in_sig=[<+numpy.float32+>, ],
            out_sig=None)


    def work(self, input_items, output_items):
        in0 = input_items[0]
        # <+signal processing here+>
        return len(input_items[0])
