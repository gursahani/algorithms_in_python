#codewars https://www.codewars.com/kata/5848565e273af816fb000449/train/python


def encrypt_word(word):
    new = ""
    for j in range(len(word)):
        if j == 0:
            new += str(ord(word[j]))
        elif j == 1:
            temp = word[j]
            new += word[-1]
        elif j == len(word) - 1:
            new += temp

        else:
            new += word[j]

    return new




    # if len(word) >= 2:
    #     second = word[1]
    #     last = word[len(word) - 1]
    #     rest = word[2:len(word)]
    #     newword = firstletter + str(last) + str(rest) + str(second)
    #     return newword
    # else:
    #     return firstletter





def encrypt_this(text):
    result = []
    text_arr = text.split(" ")
    print(encrypt_word(text_arr[2]))
    for item in text_arr:
        result.append(encrypt_word(item))


    return " ".join(result)




tests = [
    ("", ""),
    ("A wise old owl lived in an oak", "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"),
    ("The more he saw the less he spoke", "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"),
    ("The less he spoke the more he heard", "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"),
    ("Why can we not all be like that wise old bird", "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"),
    ("Thank you Piotr for all your help", "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"),
]

# for t in tests:
#     inp, exp = t
#     print(encrypt_this(inp))
#



print(encrypt_this("The more he saw the less he spoke"))