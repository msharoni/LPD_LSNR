from collections import deque
import numpy as np

def gen_lfsr(seed, poly):
    # generates lsfr random vector of bits
    lfsr = []
    for  i in range(2**len(seed) - 1):
        feedback = 0
        for p in poly:
            feedback ^= int(seed[p-1])  # xor with the bit in tap
        
        # The output is the last bit
        #print(seed)
        lfsr.append(2 * int(seed[-1:]) - 1)
        seed = ''.join([(str(feedback))] + list(seed[:-1]))
    return(lfsr)
    # Shift and insert feedback at the beginning



def str_to_bit(data, seed, poly):
    # modulator
    out_queue = deque()
    binary_data = ''.join(format(ord(char), '08b') for char in data)

    # add preamble
    preamble = "1111"

    lfsr = np.array(gen_lfsr(seed, poly))

    # spread the bits by lfsr
    for bit in preamble:
        out_queue.extend((-1)**int(bit) * lfsr)
    

    for bit in binary_data:
        out_queue.extend((-1)**int(bit) * lfsr)

    return out_queue


def gen_lfsr(seed, poly):
    # generates lsfr random vector of bits
    lfsr = []
    for  i in range(2**len(seed) - 1):
        feedback = 0
        for p in poly:
            feedback ^= int(seed[p-1])  # xor with the bit in tap
        
        # The output is the last bit
        #print(seed)
        lfsr.append(2 * int(seed[-1:]) - 1)
        seed = ''.join([(str(feedback))] + list(seed[:-1]))
    return(lfsr)
    # Shift and insert feedback at the beginning
   
def signal_to_ascii(bit_array):
    # 1. Ensure we have a NumPy array and threshold to 0s and 1s
    # (x > 0) gives True for 1, False for -1. .astype(int) makes it 1 and 0.
    bits = (np.array(bit_array) < 0).astype(np.uint8)

    # 2. Check if the length is a multiple of 8 (1 byte = 8 bits)
    # If you have a preamble, you should slice it off before calling this!
    num_bytes = len(bits) // 8
    if num_bytes == 0:
        return ""

    # 3. Reshape into a matrix of (N bytes, 8 bits)
    bit_matrix = bits[:num_bytes * 8].reshape(-1, 8)

    # 4. Create an array of powers of 2: [128, 64, 32, 16, 8, 4, 2, 1]
    powers = 2 ** np.arange(7, -1, -1)

    # 5. Matrix multiply to get ASCII decimal values
    ascii_values = np.dot(bit_matrix, powers)

    # 6. Convert integers to characters and join
    return "".join(chr(b) for b in ascii_values)

def bit_to_str(signal, seed, poly):
    mode = 1
    sens = 0.9
    lfsr = np.array(gen_lfsr(seed, poly))
    threshold = len(lfsr) * sens
    bits = []
    buff = deque()

    counter = 0
    for i in range(len(signal)):
        #buff.popleft()
        buff.append(np.real(signal[i]))
        counter += 1
        #if counter == len(2*lfsr*t*fs):
        #    np.correlate(list(buff), lfsr)
        if mode and len(buff) == len(lfsr):
            if abs(np.dot(lfsr, buff)) > threshold:
                bits.append(np.sign(np.dot(lfsr, buff)))
            buff = deque()
    return bits

    
        


data = 'g-d is king'
seed = '1101'
poly = [2,3,4]

d = str_to_bit(data, seed, poly)
bits = bit_to_str(d, seed, poly)
print(signal_to_ascii(bits))