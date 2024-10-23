def all_variants(text):
    i = 0
    __len = len(text) * 2
    while i <= __len:
        if i < 3:
            yield text[i]
        elif i == 4:
            yield text[0] + text[1]
        elif i == 5:
            yield text[1] + text[2]
        elif i == 6:
            yield text[0] + text[1] + text[2]
        i += 1

a = all_variants("abc")

for i in a:
    print(i)