# 2.2  Capitalize the Title
# You are given a string title consisting of one or more words separated by a single space, where each word consists
# of English letters. Capitalize the string by changing the capitalization of each word such that:
# - If the length of the word is 1 or 2 letters, change all letters to lowercase.
# - Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
# Return the capitalized title.
def capitalize_title(title: str) -> str:
    list_title = title.split(" ")
    title_new = ""
    for i in range(0, len(list_title)):
        if len(list_title[i]) <= 2:
            list_title[i] = list_title[i].lower()
            title_new = title_new + " " + list_title[i]
        else:
            list_title[i] = list_title[i][0].upper() + list_title[i][1::]
            title_new = title_new + " " + list_title[i]
    return title_new[1::]


print(capitalize_title("about something to"))




