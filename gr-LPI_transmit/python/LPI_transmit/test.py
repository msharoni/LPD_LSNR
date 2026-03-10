from collections import deque

def lfsr(poly, seed):
    feedback = 0
    for p in poly:
        feedback ^= int(seed[p-1])  # xor with the bit in tap
    
    # The output is the last bit
    output = seed[-1]
    new_seed = ''.join([(str(feedback))] + list(seed[:-1]))
    # Shift and insert feedback at the beginning
    return output, new_seed

def bit_to_str(data, seed1, poly):
    out_queue = deque()

    # 1. Convert input string to a binary string (8 bits per char)
    binary_data = ''.join(format(ord(char), '08b') for char in data)
    
    # 3. Generate Gold Sequence bits via XORing two LFSR outputs
    for i in range(len(binary_data)):
        # shift the seed and get the xor val
        output1, seed1 = lfsr(poly, seed1)
        out_queue.append(int(output1) ^ int(binary_data[i]))      
    print(out_queue)

data = 'aabb'
seed = '111'
poly = [2,3]

bit_to_str(data, seed, poly)