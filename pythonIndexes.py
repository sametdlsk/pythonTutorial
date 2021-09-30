########################################################################################################
a = "Hello"
print(a[0])
print(a[2])
print(len(a))
# We have a word consisting of 5 letters in the "a" variable.
# The first print function takes the first letter of variable. Where 0 is the first letter
# The second print function takes the third letter of variable
# With the "len" function, we can see how many letters our variable consists of

# Yukarıda a değişkenimizde string ifadenin içerisinde 5 harften oluşan bir kelimemiz var.
# ilk print fonksiyonu a değişkenimize tanımlı string ifadenin ilk harfini alır.
# ilk print fonksiyonu a değişkenimize tanımlı string ifadenin üçüncü harfini alır.
# "len" fonksiyonu ile de tüm string ifadenin kaç harften oluştuğunu gösterir.
########################################################################################################

########################################################################################################
a = "Hello"
print(a[len(a)-1])
# The len function does not just indicate how many letters it consists of
# In the example above, we know that our word consists of 5 letters together with len(a).
# We can also reach our last element with the len(a)-1 command

# len fonksiyonu sadece kaç harften oluştuğunu göstermez.
# Yukarıda ki örnekte len(a) ile birlikte 5 harften kelimemizin oluştuğunu biliyoruz.
# len(a)-1 ile de sonuncu elamanımıza ulaşabiliriz.
########################################################################################################

########################################################################################################
b = [1, 2, 3, 4, 5]
print(b[0])
print(b[2])
print(len(b))
print(b[len(b)-1])
# All methods apply to numeric operators
# Yukarıda String ifadeler için yaptığımız tüm işlemler sayısal operatörler içinde geçerlidir.
########################################################################################################

########################################################################################################
print(a[0:2]) # Write from the zero to the second / Sıfırıncı elemandan ikinci elemana kadar yazdır.
print(b[2:4]) # Write from the second to the fourth / İkinci elemandan dördüncü elemana kadar yaz.
print(a[:4])  # Go to the fourth element and finish / Dördüncü elemana kadar yazdır.
print(b[2:])  # Go to the second and start writing / İkinci elemandan başlayarak yazdır.
print(a[::2]) # Print by skipping two from start to finish / Baştan sona yazdır ancak ikişer atla.
print(b[0:5:2]) # Print between zero and five, but skip two two / 0 ile 5 arası yazdır ancak 2'şer atla.
########################################################################################################

########################################################################################################
x = {"first": 15, "second": 17, "third": 21}

print(x["first"])
# using with dict data types
# dict veri tipi ile yani sözlük dizimi ile kullanımı
########################################################################################################