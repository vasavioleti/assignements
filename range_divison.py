list_1=[x for x in range(2000,3201) if x % 7 == 0 and x % 5 != 0]
print("foo")
list_2=[x for x in range(2000,3201) if x % 7 != 0 and x % 5 == 0]
print("bar")
list_3=[x for x in range(2000,3201) if x % 7 == 0 and x % 5 == 0]
print("foobar")
