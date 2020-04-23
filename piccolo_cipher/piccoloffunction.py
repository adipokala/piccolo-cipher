from pyfinite import ffield

# S-Box Layer
sbox = {
    0x0: 0xe,
    0x1: 0x4,
    0x2: 0xb,
    0x3: 0x2,
    0x4: 0x3,
    0x5: 0x8,
    0x6: 0x0,
    0x7: 0x9,
    0x8: 0x1,
    0x9: 0xa,
    0xa: 0x7,
    0xb: 0xf,
    0xc: 0x6,
    0xd: 0xc,
    0xe: 0x5,
    0xf: 0xd
}

# Diffusion Matrix
M = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]

def ffunction(x):
    x16 = []
    for i in range(4):
        x16.append((x >> i) & 0xffff)

    x4 = []
    for i in range(4):
        temp = []
        for j in range(4):
            temp.append(sbox[(x >> i) & 0xf])
        x4.append(temp)
    
    F = ffield.FField(4)
    x4d = []
    for i in range(4):
        for k in range(4):
            sum = 0
            for j in range(4):
                sum += F.Multiply(M[i][j], x4[k][j])
            x4d.append(sum)

    return x4d