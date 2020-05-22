# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three lower case characters.
# Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes,
# and the knowledge that the plain text must contain common English words,
# decrypt the message and find the sum of the ASCII values in the original text.
#

MOUNT_1 = 'The'
MOUNT_2 = 'the'
MOUNT_3 = 'and'
KEY_LEN = 3
# COUNT_MOUNT = 5
from collections import Counter

def get_data(file_name):
    with open(file_name, 'rb') as f:
        data = f.read().split(b',')
    return data

def decrypt(cipher):
    cipher = padding(cipher)
    possible_keys = []
    for ch_1 in range(ord('a'), ord('z') + 1):
        for ch_2 in range(ord('a'), ord('z') + 1):
            for ch_3 in range(ord('a'), ord('z') + 1):
                key = [ch_1, ch_2, ch_3]
                if try_key(cipher, key):
                    print(key)
                    print('-'*30)
                    possible_keys.append(key)

def xor_key_bytes(cipher, key):
    return ''.join([chr(int(cipher_ch) ^ key_ch) for (cipher_ch,key_ch) in zip(cipher, key)])


def try_key(cipher, key):
    plain = ''
    for i in range(0, len(cipher), KEY_LEN):
        plain += xor_key_bytes(cipher[i:i+KEY_LEN], key)
    if MOUNT_1 in plain or MOUNT_2 in plain:
        if MOUNT_3 in plain:
            if Counter(plain).most_common()[0][0] == ' ':
                print(plain)
                print(calc_bytes_sum(plain))
                return True
    return False

def calc_bytes_sum(data):
    return sum([ord(ch) for ch in data])

def padding(cipher):
    if len(cipher) % KEY_LEN != 0:
        cipher += [0] * (KEY_LEN - len(cipher) % KEY_LEN)
    return cipher


def main():
    file_name = 'cipher.txt'
    cipher = get_data(file_name)
    # print(cipher[:5])
    plain = decrypt(cipher)
    # print(int(cipher[0]))
if __name__ == '__main__':
    main()

# An extract taken from the introduction of one of Euler's most celebrated papers, "De summis serierum reciprocarum" [On the sums of series of reciprocals]: I have recently found, quite unexpectedly, an elegant expression for the entire sum of this series 1 + 1/4 + 1/9 + 1/16 + etc., which depends on the quadrature of the circle, so that if the true sum of this series is obtained, from it at once the quadrature of the circle follows. Namely, I have found that the sum of this series is a sixth part of the square of the perimeter of the circle whose diameter is 1; or by putting the sum of this series equal to s, it has the ratio sqrt(6) multiplied by s to 1 of the perimeter to the diameter. I will soon show that the sum of this series to be approximately 1.644934066842264364; and from multiplying this number by six, and then taking the square root, the number 3.141592653589793238 is indeed produced, which expresses the perimeter of a circle whose diameter is 1. Following again the same steps by which I had arrived at this sum, I have discovered that the sum of the series 1 + 1/16 + 1/81 + 1/256 + 1/625 + etc. also depends on the quadrature of the circle. Namely, the sum of this multiplied by 90 gives the biquadrate (fourth power) of the circumference of the perimeter of a circle whose diameter is 1. And by similar reasoning I have likewise been able to determine the sums of the subsequent series in which the exponents are even numbers.
# [101, 120, 112]
