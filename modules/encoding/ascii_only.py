import unicodedata


def ascii_only(text):
    ascii_only = unicodedata.normalize("NFKD", text) \
        .encode('ascii', 'ignore') \
        .decode('ascii')
    return ascii_only


text = 'The éclairs and crème brûlée were served at the café, creating a '\
    'délicieux experience.'

print(ascii_only(text))