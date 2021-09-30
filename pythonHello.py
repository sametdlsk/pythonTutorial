# The comment line starts with hashtag. This is a comment line examples
# yorum satırı hashtag ile başlar. Bu bir örnek yorumdur.
"""
We can show comments with three double quote if they have more than one line.
Birden fazla yorum satırı için üç adet çift tırnak işaretini kullanabilir
"""

print("Hello Python")  # Bu Python'da yazdırma komutudur.
                       # This is the command to write the text on the screen.


print("Hello Python", "I am a", 1, "person")
"""
String expressions, that is, textual expressions, must be specified in double quotation marks.
But there is no need for this for numbers, because the numbers are defined by Python.

String ifadeler yani Metinsel ifadeler çift tırnak işareti içerisinde belirtilmelidir.
Ancak sayılar için buna gerek yoktur çünkü sayılar Python tarafından tanımlanmıştır.
"""

print("Samet\nDlsk")    # Alt alta yazdırmak istediğimiz ifadeleri \n kullanarak yazdırırız.
print("1\n2")           # Bu satırdaki de sayılar için bir örnektir. Alt alta yazırabiliriz.
"""
\n we put it next to the expressions we want to print on the bottom line. Such as the above example.
We must specify with double quotes the numbers that we have customized and that are not variable. 


Alt alta yazdırmak istediğimiz ifadeleri \n kullanarak yazdırırız. Yukarıdaki örnekteki gibi alt alta yazırabiliriz.
Ancak spesifik ve değişken olarak tanımlamadığımız sayılarımızı print fonksiyonunda kullanırken çif tırnak ile
kullanmalıyız.
"""

print("01", "01", "2021")
print("01", "01", "2021", sep="/")

"""
We use the sep function to put a / between them dec. Such as the above example.
And we can also put any character instead of / (example: + - ? and more}. 


Tarihleri yazdırmak için sep fonskiyonu ile aralarında / bırakabiliriz. 
Yukardaki örneği bakınız sep ile + - ? gibi bir çok elemanı aralarda kullanabiliriz
"""