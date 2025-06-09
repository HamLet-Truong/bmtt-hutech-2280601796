def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    T = [int(4294967296 * abs(__import__('math').sin(i + 1))) & 0xFFFFFFFF for i in range(64)]

    original_length = len(message) * 8
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += original_length.to_bytes(8, 'little')

    shifts = ([7,12,17,22]*4 + [5,9,14,20]*4 + [4,11,16,23]*4 + [6,10,15,21]*4)

    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        A, B, C, D = a0, b0, c0, d0

        for j in range(64):
            if j < 16:
                f = (B & C) | (~B & D)
                g = j
            elif j < 32:
                f = (D & B) | (~D & C)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = B ^ C ^ D
                g = (3 * j + 5) % 16
            else:
                f = C ^ (B | ~D)
                g = (7 * j) % 16

            temp = (A + f + T[j] + words[g]) & 0xFFFFFFFF
            A, D, C, B = D, C, B, (B + left_rotate(temp, shifts[j])) & 0xFFFFFFFF

        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF

    return '{:08x}{:08x}{:08x}{:08x}'.format(a0, b0, c0, d0)

input_string = input("Nhập chuỗi cần băm: ")
md5_hash = md5(input_string.encode('utf-8'))
print("Mã băm MD5 của chuỗi '{}' là: {}".format(input_string, md5_hash))
