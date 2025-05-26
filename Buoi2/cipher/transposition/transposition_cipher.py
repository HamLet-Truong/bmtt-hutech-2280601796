class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text[col] += text[pointer]
                pointer += key
        return ''.join(encrypted_text)

    def decrypt(self, text, key):
        num_cols = key
        num_rows = -(-len(text) // key)  # Làm tròn lên
        num_shaded_boxes = (num_cols * num_rows) - len(text)

        plaintext = [''] * num_rows
        col = 0
        row = 0

        for symbol in text:
            plaintext[row] += symbol
            row += 1

            if (row == num_rows) or (row == num_rows - 1 and col >= num_cols - num_shaded_boxes):
                row = 0
                col += 1

        return ''.join(plaintext)