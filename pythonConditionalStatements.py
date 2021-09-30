"""
Conditions      EN Description;             TR Açıklamaları;
>               Greater than                Büyüktür
<               Less than                   Küçüktür
<=              Less than or equal          Küçük eşit
>=              Greater Than or Equal       Büyük eşit
==              Equality                    Eşitse
!=              Inequality                  Eşit değilse
"""

# The bottom line is that we defined our variable and asked our question as a string expression
# Alt satırda değişkenimizi tanımladık ve string veri tipiyle sorumuzu sorduk
learn = str(input("What software language are you learning right now :"))

if learn == "Python":  # if the input is python / eğer girdi "Python" ise yani eşitse
    print("Yes !, never give up !")  # print this / bunu yazdır

else:  # Print this if the condition in the if block does not apply / if bloğu geçerli değilse bunu uygula
    print("Think again !")  # if the input is not python write this / eğer girdi python değilse yazdır.

# if we have more than one condition, you can use bottom line
# birden fazla şartımız var ise alttaki örnekteki gibi tanımlayabilirsiniz
operator = int(input("Select 1 or 2 or 3 or 4 :"))

if operator == 1:
    print("You are selected 1")
elif operator == 2:
    print("You are selected 2")
elif operator == 3:
    print("You are selected 3")
elif operator == 4:
    print("You are selected 4")
else:
    print("You are not selected anything")