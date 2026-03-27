def count(sentence):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    
    vowelcount = 0
    consonantcount = 0
    
    for ch in sentence:
        if ch in vowels:
            vowelcount += 1
        elif ch in consonants:
            consonantcount += 1
    
    print("Гласных:", vowelcount)
    print("Согласных:", consonantcount)

'''text = input()
count(text)'''
