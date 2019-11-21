list_a = ["a","b","c"]
for e in list_a:
	print("e:" + e)

p_list = list_a[1:]
print("===========")
for e in p_list:
	print("e:" + e)
print("======end=====")

print("======start... sort=====")
list_a.sort();
for e in list_a:
	print("e:" + e)
	
print("======start... reverse sort=====")
list_a.sort( reverse = True );
for e in list_a:
	print("e:" + e)

print("======start... reverse sorted=====")
sorted(list_a);
for e in list_a:
	print("e:" + e)
print("======start... reverse sorted=====")
list_b = sorted(list_a);
for e in list_b:
	print("e:" + e)
for e in list_a:
	print("e:" + e)
