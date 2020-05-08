from piccolo_cipher import piccolokeyscheduling, piccoloencrypt

def decrypt(X, key, bit):
    wk = piccolokeyscheduling.generate_white_keys(bit, key)
    rk = piccolokeyscheduling.generate_round_keys(bit, key)

    new_rk = rk
    new_wk = []
    new_wk.append(wk[2])
    new_wk.append(wk[3])
    new_wk.append(wk[0])
    new_wk.append(wk[1])

    r = 0
    if bit == 80:
        r = 25
    else:
        r = 31

    for i in range(r - 1):
        rk[2 * i] = rk[(2 * r) - (2 * i) - 2] if (i % 2 == 0) else rk[(2 * r) - (2 * i) - 1]
        rk[(2 * i) + 1] = rk[(2 * r) - (2 * i) - 2] if (i % 2 == 0) else rk[(2 * r) - (2 * i) - 1]

    return piccoloencrypt.encryptAlgo(X, wk, rk, bit)