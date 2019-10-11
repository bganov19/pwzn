def count_letters(msg):
    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    """
    s = []

    for elem in msg:
        if elem not in s:
            s.append(elem)

    chars = [msg.count(elem) for elem in s]

    if chars.count(max(chars)) == 1:
        return s[chars.index(max(chars))], max(chars)
    else:
        for elem in chars:
            if elem != max(chars):
                chars.pop(chars.index(elem))
                s.pop(chars.index(elem))
        return min(s), max(chars)


if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ('a', 4)
    assert count_letters('za') == ('a', 1)