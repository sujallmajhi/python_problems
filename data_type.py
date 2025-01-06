# list ordered and changeabble duplicate ok
# fruits=["banana","mango","litchi","litchi"]
# print(fruits)
# fruits[0]="kiwi"
# print(fruits)
# for fruit in fruits:
#     print(fruit)
# fruits.append("watermelon")
# print(fruits)
# print(len(fruits))
# fruits.remove("mango")
# print(fruits)
# fruits.insert(0,"Tomato")
# print(fruits)
# fruits.sort()
# print(fruits)
# print(fruits.index("litchi"))
# print(fruits.count("litchi"))
# fruits.pop(1) #pop is used to remove at specific index
# print(fruits)

# set unordered and immutable but add,remove,no duplicate

# fruits={"mango","banana","litchi","tomato","kiwi"}
# # fruits[0]="apple" immutable example
# fruits.add("pineaple")
# fruits.remove("banana")
# for fruit in fruits:
#     print(fruit)

#dictionary with key and values
user={"name":"sujal","age":20,"faculty":["science","EEC","Be cmp"]}
for value in user.values():
    print(value)
for key in user.keys():
    print(key)   
print(user["name"])
print(user["faculty"][1])
    