def find_lus_length(a: str, b: str) -> int:
    if a == b:
        return -1
    else:
        if len(a) > len(b):
            return len(a)
        else:
            return len(b)


e = "phvfaedwkmmfinfxmws"
f = "yx"
print(find_lus_length(e, f))
