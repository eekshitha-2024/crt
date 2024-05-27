'''sp=int(input(" enter the price"))
p=int(input(" enter a discount"))
actual_price=sp*p/100
print(actual_price)
final_price=(sp-actual_price)
print(final_price)'''

sp,discount=int(input()),int(input())
print(sp-sp*(discount/100))
