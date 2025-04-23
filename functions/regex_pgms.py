import re

x = "transmitted in any form or by any means electronic, mechanical, photocopying,"

y = re.findall("photocopying", x)
if y[0] == 'photocopying':  # ['photocopying'] != 'photocopying'
    print("found")
else:
    print("not found")

'''re.search("photocopying",x)
re.match("photocopying",x)
re.sub("photocopying","copying",x)
re.split("photocopying",x)
re.fullmatch("photocopying",x)
re.compile("photocopying")'''
re.escape("photocopying")
print(re.escape("photocopying"))
print(re.finditer("photocopying",x))
get=re.search("photocopying",x)
print(get)
print(get.start())
print(get.end())
print(get.group())

date = '08-09-1996'
pattern = re.compile(r'([\d]{2})-([\d]{2})-([\d]{2})')
print(pattern.search(date))



y= pattern.sub(r'\1.\2.\3',date)
print(y)