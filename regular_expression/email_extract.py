import re

source = "To get assistance please contact at baponkar_123@gmail.com"
print(source)



pattern = r"[a-z].*com$"

res = re.match(pattern,source)

print(res)
print(res.group())
