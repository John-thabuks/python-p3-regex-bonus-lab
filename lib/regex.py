import re

# my_pattern = r"[A-Za-z0-9_].*"
my_pattern = r"[A-Z][a-z]*'*[a-z]\s[a-z' ]*today'*[a-z, ]*[?\.]+"

my_regex = re.compile(my_pattern)

check = my_regex.fullmatch("It's such a lovely day today.")

text = [
    "It's such a lovely day today.",
    "Some weather we're having today, huh?",
    "Maybe today's just not my day.",
]
# convert_Tostring = " ".join(text)
# print(convert_Tostring)
check_findall = my_regex.findall(" ".join(text))
print(check_findall)
# print(check)

