"""
rada 0       *    - 3 mezery
rada 1      ***   - 2 mezery
rada 2     *****  - 1 mezera
rada 3    ******* - 0 mezer
"""


#1,3,5,7

hvezdy = "*"


radku = int(input("kolik radku bude mit piramida "))


for i in range(radku):
    mezery = (radku - 1) - i 
    print((mezery * " ") + ((2*i )+1) * "*" + (mezery * " "))
