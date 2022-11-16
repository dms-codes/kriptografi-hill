import string
import numpy as np

key = 'LIDH'
m = 2
plaintext = 'ES'
print('Plaintext:',plaintext)    
def get_matrix_m(m,key):
    array_m = []
    for row in range(m):
        array_m.append([])
        for column in range(m):
            array_m[-1].append(string.ascii_uppercase.index(key[2*row+column]))
    matrix_m = np.array(array_m)
    return matrix_m

def get_matrix_p(m,plaintext):
    array_plaintext_blocks = []
    for block in range(len(plaintext)//m):
        array_plaintext_blocks.append([])
        for column in range(m):
            array_plaintext_blocks[-1].append(string.ascii_uppercase.index(plaintext[2*block+column]))
    matrix_p = np.array(array_plaintext_blocks)
    return matrix_p

matrix_m = get_matrix_m(m,key)
print('M =',matrix_m)

matrix_p = get_matrix_p(m,plaintext)
print('P =',matrix_p)

ciphertext = ''
for p in matrix_p:
    row = np.mod(matrix_m.dot(p.transpose()),26)
    for col in row:
        c = string.ascii_uppercase[col]
        ciphertext += c

print('Ciphertext:',ciphertext)    
