print("WELCOME TO SEOLING CAFE")
print(''' select_1 to order latte
 select_2 to order cookies
 select_3 to order cakes
 select_4 to order icecreams
 select_5 to order pizza''')
select_1={
    "Black seasame latte"      :   270,
    "Blue latte"               :   200,
    "Cafe latte"               :   170,
    "Condensed milk latte"     :   290,
    "Green tea latte"          :   150,
    "Ice cream mocha latte"    :   250,
    "Signature latte"          :   300,
    "Strawberry latte"         :   230,
    "Sweet potato latte"       :   170,
    "Toffee nut latte"         :   200,
    "Vanilla latte"            :   150,
    "Caramel cheese latte"     :   220,
} 
select_2={
    "Browny cookie"            :   70,
    "Butter cookie"            :   55,
    "Cereal cookie"            :   40,  
    "Chocolate cookie"         :   55, 
    "Molasses cookie"          :   60, 
    "Oatmeal raisin cookie"    :   35, 
    "Peanut butter cookie"     :   80, 
    "Pinwheel cookie"          :   75,
    "Shortbread cookie"        :   40,
    "Snowball cookie"          :   90,  
    "Sugar cookie"             :   30, 
    "Thumbprint cookie"        :   55,
    "Walnut chocolate cookie"  :   60,
}
select_3={
    "Black current cake"       :   500, 
    "Brownie cake"             :   450, 
    "Butterscotch cake"        :   350,
    "Chocolate cake"           :   400,
    "Ferrero rocher cake"      :   700, 
    "Kitkat cake"              :   650,
    "Oreo cake"                :   600, 
    "Pineapple cake"           :   450,
    "Plum cake"                :   350,
    "Rainbow cake"             :   500,
    "Redvelvet cake"           :   550,
    "Vanilla cake"             :   300,
    "White forest cake"        :   450,
}
select_4={
    "American nuts icecream"   :  70,
    "Cherry icecream"          :  60,
    "Chocolatechip icecream"   :  40,
    "Cookie and cream icecream":  45,
    "Kulfi"                    :  40,
    "Mango icecream"           :  30,
    "Mint chocolate icecream"  :  40,
    "Mochi icecream"           :  80,
    "Vanilla icecream"         :  40,
    "Raspberry icecream"       :  55,
    "Snowcream icecream"       :  50,
    "Strawberry icecream"      :  35,
}
select_5={
    "Capsicum pizza"           :  99,
    "Corn pizza"               :  99,
    "Greek pizza"              :  110,
    "Italian pizza"            :  175,
    "Margherita pizza"         :  150,
    "Onion pizza"              :  99,
    "Pan pizza"                :  75,
    "Pepperoni pizza"          :  115,
    "Roman pizza"              :  90,
    "Sandwich pizza"           :  70,
    "Stuffed crust pizza"      :  150,
}
order=int(input())
if order==1:
    print(select_1)
elif order==2:
    print(select_2)
elif order==3:
    print(select_3)
elif order==4:
    print(select_4)
else:
    print(select_5)
print("Order number:",end="")
order_number=int(input())
print("No.of.items to be ordered:",end="")
items=int(input())
list=[]
print("Your order:")
for i in range(items):
    order=input()
print("Price of each item:")
for j in range(items):
    price=int(input())
    list.append(price)
sum=0
for k in list:
    sum=sum+k
print("Total:",sum)
print("Thankyou for visiting SEOLING CAFE")
