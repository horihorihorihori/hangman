import re

message = "HaHaHaHaHa"

greedy_Ha_regex = re.compile(r'(Ha){3,5}')

mo1 = greedy_Ha_regex.search(message)

print(mo1.group())

greedy_Ha_regex = re.compile(r'(Ha){3,5}?')

mo2 = greedy_Ha_regex.search(message)

print(mo2.group())


