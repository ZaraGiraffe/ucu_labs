def caesar_encode(message, key):
    """
    >>> caesar_encode('abwz', 3)
    'dezc'
    >>> caesar_encode('computer', 3)
    'frpsxwhu'
    """
    key = key % 26
    newm = ''
    for i in message:
        if i == ' ':
            newm += ' '
            continue
        x = ord(i)
        x += key
        if x > ord('z'):
            x = ord('a') + x - ord('z') - 1
        newm += chr(x)
    return newm

def caesar_decode(message, key):
    """
    >>> caesar_decode('dezc', 3)
    'abwz'
    >>> caesar_decode('frpsxwhu', 3)
    'computer'
    """
    return caesar_encode(message, 26-key)
