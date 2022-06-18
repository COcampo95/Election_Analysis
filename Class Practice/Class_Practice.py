from pyparsing import countedArray


Title = "Frank"
years = 80 
expert_status = True


#printing variables
print("My name is" +Title)

print (f"Expert Status:{expert_status} and years ={years} and titles ={Title}")

summary = f'title:{Title}, years  = {years}'
print (summary)


myList = ["Andrew", "Jacob", "Lee", "Aliana", 100, 100, 100, 100, True, True, True, True]
myList.append("Christina") #add new item always  to end of list
print (myList)

len(myList)

myList[1] ="Jacob Kotcher" #editing list

print (myList)




grocery_list = ["Milk", "Bread","Eggs", "Peanut Butter", "Jelly"]

# Print the grocery list

print (grocery_list)

# Change "Peanut Butter" to "Almond Butter" and print out the updated list

grocery_list[3]= ("Almond Butter")

print (grocery_list)

# Remove "Jelly" from grocery list and print out the updated list

grocery_list.pop (3)


print (grocery_list)

# Add "Coffee" to grocery list and print the updated list

grocery_list.append("Coffee")

print (grocery_list)

# @TODO: Your code here
from unicodedata import name


pet_dict = {}
pet_dict ["name"] = "Duke"
pet_dict ["age"] = 7
pet_dict ["hobbies"] = ["fetch", "swimming", "cuddles"]

wakeup_dict = {}
wakeup_dict ["Monday"] = 8
wakeup_dict ["Tuesday"] = 7

pet_dict ["wakeup"] = wakeup_dict

print (pet_dict)

print (f'My name is {pet_dict["name"]} age = {pet_dict["age"]}')



