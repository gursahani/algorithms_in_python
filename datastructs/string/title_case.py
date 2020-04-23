def title_case(title, minor_words=''):
    title = title.split()
    output = ''
    for item in title:
        word = ''
        # if item != ' ':

        word += item[0].upper() + item[1:].lower()
        item = word
        output += item + ' '
    return output


print(title_case('a clash of kings'))


new_word = ' '.join([word.capitalize() for word in ['a', 'clash', 'of', 'kings']])


def rep(new_word, st):
    out = ''
    if st in new_word:
        st = st.lower()


# reduce(lambda a, b: a[0].upper + b[1:].lower, ['a', 'clash', 'of', 'kings'])