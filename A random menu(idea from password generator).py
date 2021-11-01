from random import choice, randint, shuffle
import random
import datetime
#-------------------------------------------food list-----------------------------------------------#
grain = {"Rice(1cup)":232, "Bread(1slice)":60, "Hotdog(1)":119, "HamburgerBun(1)":120, "Pizza(1slice)":290,"Spaghetti(1cup)":159}
fruits_vege = {"Apple(1)":81, "Banana(1)":90, "Orange(1)":65, "Grapes(1cup)":114, "Pear(1)":98, "Carrot(1)":31, "Potato(1)":220,"Corn(1/2)":89, "Three-bean salad(1/2cup)":90}
meat = {"Steak(164g)":407, "Pork(185g)":363, "Ham": 236, "Chicken Leg(199g)":346, "Chicken Wing(3wing)":240, "Chicken Breast(200g)": 344}
drinks = {"beer":153, "Soda":150, "Orange juice":160, "Apple juice":170, "vegetable juice":180, "Soy milk":170,
         "Whole milk":220, "Unsweetened tea":4, "Gin":97 }
#--------------------------------------to select random item, even random the frequent--------------#
random_integer = random.randint(2,3)#from 1 - 10

today_list = []
def new_item(import_list):
    import_list = list(import_list.items())
    for _ in range(random_integer):
        random_entry = random.choice(import_list)
        today_list.append(random_entry)

new_item(grain)
new_item(fruits_vege)
new_item(meat)
new_item(drinks)
#--------------------------------------use for loop to sum the calories and append food list------------------------#
sum_of_calories = 0
food_list =[]
time = 0
for _ in today_list:
    food_list.append(today_list[time][0])
    sum_of_calories = sum_of_calories + int(today_list[time][1])
    time = time + 1
print(sum_of_calories)
print(food_list)
#----------------------------------------to save a record in csv ---------------------------------------------#
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
raw_today = datetime.datetime(year, month, day)
today = raw_today.strftime('%Y-%m-%d')

string = f'{today},{sum_of_calories},{food_list}'
with open("data.csv", "a") as file:
    file.write(f"\n{string}")


####this idea come from password generator but i dun need that tool in my life
####So i try to use the core function(append, random) to write other codes