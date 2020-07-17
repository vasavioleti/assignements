list_1=[x for x in range(2000,3201) if x % 7 == 0 and x % 5 != 0]
print(list_1,"foo")
list_2=[x for x in range(2000,3201) if x % 7 != 0 and x % 5 == 0]
print(list_2,"bar")
list_3=[x for x in range(2000,3201) if x % 7 == 0 and x % 5 == 0]
print(list_3,"foobar")