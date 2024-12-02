def all_variants(text):
    for j in range(len(text)):
        yield text[j]

    for j in range(2, len(text) + 1):
        for n in range(len(text) - j + 1):
            k = n + j
            yield text[n:k]


a = all_variants("abc")
for i in a:
    print(i)
