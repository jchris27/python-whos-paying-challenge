# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

# Angela Ben Jenny Michael
# name is going to buy the meal today!


tag = len(names)
a = tag - 1
it = random.randint(0, a)
print(names[it])

