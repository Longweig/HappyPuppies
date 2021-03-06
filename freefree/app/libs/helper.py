def is_isbn_or_key(word):
    """
    Return if the `word` is `isbn` number
    or `keyword`.

    :param word: query keywords to get HTTP response
    :type word: string
    :return: `isbn` or `key`
    :rtype: string
    """
    isbn_or_key = 'key'

    if '-' in word:
        short_word = word.replace('-', '')
    else:
        short_word = word

    if len(short_word) == 13 and short_word.isdigit():
        isbn_or_key = 'isbn'

    if len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
