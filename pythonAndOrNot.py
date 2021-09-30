a = 10   # Variables - Değişkenler
b = 15   # Variables - Değişkenler

##############################################################################################################
# The AND operator works if it is provided in two conditions
# AND operatörü iki şartında sağlanması durumunda çalışır

if a == 10 and b == 15:
    print("Stable")
else:
    print("Not Stable")
##############################################################################################################

##############################################################################################################
# The OR operator works if one of two conditions is met.
# OR operatörü iki şarttan biri sağlanırsa çalışır.

if a == 8 or b == 15:
    print("Stable")
else:
    print("Not Stable")
##############################################################################################################

##############################################################################################################
# The NOT operator converts the true condition to false. As an example, twenty is not bigger than thirty.
# NOT operatörü True bir değeri False bir değere çevirir. 20 sayısı 30'dan büyük olmamasına rağmen çıktı aldık.

if (not (20>30)):
    print("This is not correct but function :)")
##############################################################################################################