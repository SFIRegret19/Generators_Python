def all_variants(text):
    str_length = 1
    while str_length <= len(text):
        i = 0
        while i + str_length <= len(text):
            yield text[i : i + str_length]
            i += 1
        str_length += 1
a = all_variants("abc")

for i in a:
    print(i)