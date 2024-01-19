def all_variants(string):
    n = len(string)
    for i in range(1 << n):
        yield "".join([string[j] for j in range(n) if (i & (1 << j))])


for variant in all_variants("abc"):
    print(variant)
