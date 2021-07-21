#列表里放5个想去的城市
places = ['shanghai','xizang','yunnan','hainan','taiwan']
print(places)


#使用sorted()按字母顺序打印这个列表，同时不要修改它
print(sorted(places))


#再次打印核实排列顺序未变
print(places)


#使用sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它
print(sorted(places,reverse=True))


#再次打印核实排列顺序未变
print(places)


#用reverse()修改列表元素的排列顺序，打印并核实确实改变了
places.reverse()
print(places)


#用reverse()再次修改列表元素的排列顺序，打印并核实确实恢复到原来的排列顺序
places.reverse()
print(places)


#用sort()修改列表，使其元素按照字母顺序排列，打印并核实排列顺序确实改变了。
places.sort()
print(places)


#用sort()修改列表，使其元素按照字母顺序相反的顺序排列，打印并核实排列顺序确实改变了。
places.sort(reverse=True)
print(places)