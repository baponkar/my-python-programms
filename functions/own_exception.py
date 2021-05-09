class UppercaseException(Exception):

    pass


words = ['enee', 'meene', 'miny', 'MO']

for word in words:
    if word.isupper():
        raise UppercaseException(word)

