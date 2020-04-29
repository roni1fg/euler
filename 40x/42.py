# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

def convert_letter_to_int(letter):
    return ord(letter) - ord('A') + 1

def find_triangle_numbers(threshold):
    return [(0.5 * i * (i + 1)) for i in range(threshold)]


def get_words(file_name):
    with open(file_name, 'rb') as f:
        data = f.read().decode('utf-8').split(',')
    return [word[1:-1] for word in data]


def is_triangle_word(word, triangles_list):
    word_val = sum([convert_letter_to_int(ch) for ch in word])
    return word_val in triangles_list

def main():
    file_name = 'p042_words.txt'
    threshold = 100
    word_count = 0
    words = get_words(file_name)
    triangles_list = find_triangle_numbers(threshold)
    print(is_triangle_word('SKY', triangles_list))
    print(triangles_list[-5:])
    for word in words:
        if is_triangle_word(word, triangles_list):
            word_count += 1
    print(word_count)


if __name__ == '__main__':
    main()
