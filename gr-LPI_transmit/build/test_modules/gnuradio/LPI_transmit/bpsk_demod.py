#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2026 shlomo.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from gnuradio import gr

class bpsk_demod(gr.sync_block):
    """
    docstring for block bpsk_demod
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="bpsk_demod",
            in_sig=[np.complex64, ],
            out_sig=[np.float32, ])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        
        out[:] = np.float32((np.real(in0)>0 ))#least geometric distance
        return len(output_items[0])
