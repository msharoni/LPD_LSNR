#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2026 god.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from collections import deque
from gnuradio import gr

class dsss_encoder(gr.sync_block):
    """
    docstring for block dsss_encoder
    """
    def __init__(self, data,seed1, seed2):
        gr.sync_block.__init__(self,
            name="dsss_encoder",
            in_sig=None,
            out_sig=[np.int8, ])
        self._data = data
        self._seed1 = seed1
        self._seed2 = seed2
        self._poly = [1,2,3,4,10]
        self._out_queue = deque()
        self.bit_to_str()
        self.lfsr()

    def lfsr(poly, seed):

        feedback = 0
        for p in poly:
            feedback ^= int(seed[p-1])  # xor with the bit in tap
        
        # The output is the last bit
        output = seed[-1]
        new_seed = ''.join([(str(feedback))] + list(seed[:-1]))
        # Shift and insert feedback at the beginning
        return output, new_seed

    def bit_to_str(self, data, seed1, seed2, length_needed):
        # 1. Convert input string to a binary string (8 bits per char)
        binary_data = ''.join(format(ord(char), '08b') for char in data)
        
        # 2. Initialize LFSRs with your seeds
        reg1 = seed1, seed2
        gold_seq = []

        for i in range(len(binary_data)):
            # shift the seed and get the xor val
            output1, seed1 = self.lfsr(self._poly, self._seed1)
            self._seed1 = seed1   
            self._out_queue.append(int(output1) ^ int(binary_data[i]))       

    def work(self, input_items, output_items):
        out = output_items[0]
        # <+signal processing here+>
        for i in range(len(out)):
            if len(self._out_queue) == 0:
                return -1
            else:
                 out[i] = self._out_queue.popleft()
        return len(output_items[0])
