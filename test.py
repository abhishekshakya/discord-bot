from phlib import PornHub
ph = PornHub()
# print(ph.categories)
a = (ph.search('boobs',max=5))
for i in a:
    print(i.url)