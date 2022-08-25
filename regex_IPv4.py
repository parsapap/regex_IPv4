import re

with open("sample_ip.txt") as f:
    var = f.readlines()
sample = r"([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.\
([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
pattern = re.compile(sample)
lst = [i.strip() for i in var]

for i in lst:
    if pattern.match(i):
        with open("valid_ip.txt", "a") as f:
            f.write(i + "\n")


