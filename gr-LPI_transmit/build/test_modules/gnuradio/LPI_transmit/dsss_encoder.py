#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2026 god.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from collections import deque
from gnuradio import gr

class dsss_encoder(gr.sync_block):
    """
    docstring for block dsss_encoder
    """
    def __init__(self, data, seed):
        gr.sync_block.__init__(self,
            name="dsss_encoder",
            in_sig=None,
            out_sig=[np.int32, ])
    
        self._data = data
        self._seed= seed
        self._poly = [3,len(seed)]
        self._out_queue = deque()
        self.lfsr_seq = self.gen_lfsr()
        #define_preamble
        self.preamble = "1100"


    def gen_lfsr(self):
        # generates lsfr random vector of bits
        seed = self._seed
        poly = self._poly
        lfsr = []
        for  i in range(2**len(seed) - 1):
            feedback = 0
            for p in poly:
                feedback ^= int(seed[p-1])  # xor with the bit in tap
            
            # The output is the last bit
            #print(seed)
            lfsr.append(int(seed[-1:]) )
            seed = ''.join([(str(feedback))] + list(seed[:-1]))
        return(lfsr)
        # Shift and insert feedback at the beginning
    def str_to_bit(self):
        # modulator
        
        binary_data = ''.join(format(ord(char), '08b') for char in self._data)

        # spread the bits by lfsr
        for bit in self.preamble:
            self._out_queue.extend((-1)**int(bit) * self.lfsr_seq)
        

        for bit in binary_data:
            self._out_queue.extend((-1)**int(bit) * self.lfsr_seq)

    def work(self, input_items, output_items):
        out = output_items[0]
        
    
        # <+signal processing here+>
        self.str_to_bit()
        
        for i in range(len(out)):
            if len(self._out_queue) == 0:
                return -1
            
            out[i] = self._out_queue.popleft()
            #print(out[i])
        return len(output_items[0])