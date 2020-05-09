from piccolo_cipher import piccolokeygen, piccoloencrypt, piccolodecrypt

class Piccolo:
    def __init__(self, key="", bit=128):
        if bit != 128:
            if bit != 80:
                raise ValueError

        self.bit = bit
        self.key = piccolokeygen.piccolokeygen(bit) if key == "" else key

    def getKey(self):
        return self.key

    def encrypt(self, string):
        ascii = []
        cipher = []
        estring = ""

        for i in range(len(string)):
            ascii.append(string[i])

        for i in range(len(ascii)):
            cipher.append(piccoloencrypt.encrypt(ascii[i], self.key, self.bit))

        for i in range(len(cipher)):
            estring.join(format(cipher[i], 'x'))

        return estring

    def decrypt(self, estring):
        hexlist = []
        decipher = []
        string = ""

        for i in range(len(estring) / 2):
            hexlist.append(estring[i*2:(i+1)*2])
        
        for i in range(len(hexlist)):
            decipher.append(piccolodecrypt.decrypt(int(hexlist[i], 16), self.key, self.bit))

        for i in range(len(decipher)):
            string.join(chr(decipher[i]))

        return string