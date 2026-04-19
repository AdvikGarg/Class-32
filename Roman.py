class Roman:
    def roman_numeral(self, number):
        
        val=[
           (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),

           (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),

           (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),

           (1, 'I'),
            ]

        rom = ""
        num=number
        
        for (n, roman) in val:
            (x, num) = divnod(num,n)
            rom+=roman*x
        
        return rom

convert=Roman()

user= int(input("Enter a whole number: "))

print(f"{user}: is {convert.roman_numeral(user)}")