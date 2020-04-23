def compare(word1, word2):
    alphabet = 'abcdxyz'
        # this should return True if value 1 is alphabetically before value 2, false otherwise
    letter_index = 0
    while letter_index < len(word1):
        letter_index += 1
        letter1 = word1[letter_index]
        letter2 = word2[letter_index]
        if alphabet.index(letter1) > alphabet.index(letter2):
            return True
        elif alphabet.index(letter2) > alphabet.index(letter1):
            return False
         # if they’re the same word, we’ll exit the loop and it doesn’t matter what we return
    return True

print(compare('fgh','fghi'))
