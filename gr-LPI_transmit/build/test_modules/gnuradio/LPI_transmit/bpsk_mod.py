#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2026 cheetah.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from gnuradio import gr

class bpsk_mod(gr.sync_block):
    """
    docstring for block bpsk_mod
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="bpsk_mod",
            in_sig=[int, ],
            out_sig=[np.float64, ])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        out[:] = in0
        return len(output_items[0])
