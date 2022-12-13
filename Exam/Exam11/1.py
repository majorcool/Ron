# 1  Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
def longest_common_prefix(strs: list[str]) -> str:
    final = ""
    n = strs
    small_len = len(n[0])
    for i in range(1, len(n)-1):
        if len(n[i]) < small_len:
            small_len = len(n[i])
    for j in range(0, small_len):
        a = strs[0][j]
        for b in range(0, len(strs)):
            if a != strs[b][j]:
                if final == "":
                    print("一个都没有")
                return final
        final += a
    return final


with open("1.txt", "r") as m:
    for line in m.readlines():
        n = line.split(",")
        print(longest_common_prefix(n))
