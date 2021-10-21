def dyvo_insert(sentence, flag):
    """
    Inserting word "диво" before every word that starts with flag.

    >>> dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті", "ки")
    'дивоКит кота по хвилях катав - дивокит у воді, кіт на дивокиті'
    """
    s = "диво"
    i = 0
    while i <= len(sentence) - len(flag) + 1:
        if sentence[i:i+2].lower() == flag:
            sentence = sentence[:i] + s + sentence[i:]
            i += len(s) + len(flag)
        else:
            i += 1
    return sentence
  