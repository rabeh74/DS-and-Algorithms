# class to cigher and decigher capital words

class CaesarCipher:

    def __init__(self , k):
        self._k = k
        enocder=[None for i in range(26)]
        decoder = [None for i in range(26)]

        for i in range(26):
            # to get shifted char and save it in encoder or decoder
            enocder[i] = chr((i+k)%26 + ord("A"))
            decoder[i] = chr((i-k)%26 +ord("A"))
        self._forward = ''.join(enocder)
        self._backword = ''.join(decoder)

    def cipher(self , msg):
        return self._transform(msg , self._forward)

    def decipher(self , msg):
        return self._transform(msg , self._backword)

    def _transform(self , msg , code):
        msg=list(msg)
        for i in range(len(msg)):
            c=msg[i]
            if c.isupper():
                # to get idx of char in arr which has length of 26
                idx = ord(c) - ord("A")
                msg[i]=code[idx]
        return "".join(msg)

if __name__ == "__main__" :
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE S."
    coded = cipher.cipher(message)
    print( "Secret:"   , coded)
    answer = cipher.decipher(coded)
    print( "Message:" , answer)

