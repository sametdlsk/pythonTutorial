i = 0  # Declared variable / Değişkenimizi tanımladık

while i < 10:
    if i == 5:          # condition is if it comes to cycle 5 / eğer i = 5 olursa
        break           # break the loop / döngüyü durdur.
    print("i :", i)
    i = i + 1

# so break is used to terminate a cycle
# and if have the code here, system resume to the this area
##################################################################################################################

##################################################################################################################
while i < 10:
    if i == 4 or i == 8:  # Condition is if it comes to loop 5 / eğer i = 5 olursa
        i += 1            # When it's time for the 4. element, is a ignored. Döngü 4. elemana geldiğinde bir atlar.
        continue          # Break the loop / döngüyü durdur.
    print("i :", i)
    i = i + 1
# continue allows the cycle to return again
# continue bir döngünün devam etmesini sağlar
##################################################################################################################

##################################################################################################################
"""
while i < 10:
    if i == 4 or i == 8:   # burada iki koşul atadık ancak continue işlevine her hangi bir girdi vermedik
        continue           # we have assigned two conditions here, but we have not given any input to the continue function     
    print("i :", i)
    i = i + 1
"""
# continuous rotation of the loop due to its improper use
##################################################################################################################