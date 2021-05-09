import re_ex1

source = str(re_ex1.main.__doc__)

print(source)

import re

data_list = re.findall('^c.*$',source)
print(data_list)


m = re.sub('a', '*',source)

print(m)
