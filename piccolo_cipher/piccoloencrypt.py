from piccolo_cipher import piccolokeyscheduling, piccoloffunction, piccoloroundpermutation

def encrypt(X, key, bit):
    wk = piccolokeyscheduling.generate_white_keys(bit, key)
    rk = piccolokeyscheduling.generate_round_keys(bit, key)

    return encryptAlgo(X, wk, rk, bit)
    

def encryptAlgo(X, wk, rk, bit):
    x16 = convert64ToFour16s(X)
    x16[0] = x16[0] ^ wk[0]
    x16[2] = x16[2] ^ wk[1]

    r = 0
    if bit == 80:
        r = 25
    else:
        r = 31

    for i in range(r - 2):
        x16[1] = x16[1] ^ piccoloffunction.ffunction(x16[0]) ^ rk[2 * i]
        x16[3] = x16[3] ^ piccoloffunction.ffunction(x16[2]) ^ rk[(2 * i) + 1]
        x16 = convert64ToFour16s(piccoloroundpermutation.round_permutation(convertFour16sTo64(x16)))

    x16[1] = x16[1] ^ piccoloffunction.ffunction(x16[0]) ^ rk[(2 * r) - 2]
    x16[3] = x16[3] ^ piccoloffunction.ffunction(x16[2]) ^ rk[(2 * r) - 1]
    x16[0] = x16[0] ^ wk[2]
    x16[2] = x16[2] ^ wk[3]

    return convertFour16sTo64(x16)

# Pass 64 bit data and returns 16 bit array of length of 4
def convert64ToFour16s(X):
    x16 = []
    for i in range(4):
        x16.append((X >> (16 * (3 - i))) & 0xffff)
    return x16

# Pass 16 bit array of length 4 and returns 64 bit data
def convertFour16sTo64(x16):
    X = 0
    for i in range(4):
        X = X | (x16[i] << (16 * (3 - i)))
    return X