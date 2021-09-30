# sets of string, tuple, dict, list data types can also be navigated with the for loop
# string, tuple, dict, list veri tipindeki kümelerde for döngüsüyle gezinebiliriz.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # list type

for element in a:   # 6
    print(element)

# 6 We say just this to the Python "we want to navigate the list in the variable a"
# 6 Kısaca "a" değişkenindeki listede gezinmek istiyoruz dedik.
################################################################################################################

################################################################################################################
b = ("Hello")

for element in b:
    print(element)

# We can also navigate in string expressions
# String ifadeler içinde de gezebiliriz
################################################################################################################

for anything in range(0, 12):   # with the range function, we can navigate through specific sections
    print(anything)             # range fonksiyonu ile belirli bölümlerde gezinebiliriz

################################################################################################################
