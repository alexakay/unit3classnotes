# print("October 29th\n")
# temp_list = [6, 3, 4, 2, 10]
# for i in range(len(temp_list)):
#     temp_list[i] = 77 + i
#     print(temp_list[i])
#
# list = [1, 2, 3, 4, 5]
# print(list)
#
# list2 = [10, 20, 7, 6]
# list2[0] = 11
# list2[1] = 11
# list2[2] = 11
# list2[3] = 11
# print(list2[0])
# print(list2[1])
# print(list2[2])
# print(list2[3])
#
# list3 = [6, 2, 9, 4, 10, 7, 3, 8, 5, 1]
# list3.sort()
# print(list3)
#
# list41 = [1, 8, 24]
# list42 = [22, 3, 9]
# list4 = [(max(list41)), (max(list42))]
# print(max(list4))
#
# list5 = ["hello", "hi", "hola", "bonjour"]
# for x in list5:
#     print(x)
#
# list6 = [1, 2, 3, 4, 5, 6]
# for x in range(0,len(list6), 2):
#     print(list6[x])

# print("october 30th: \n")
# names = ["sarah", "jimmy", "matt", "alexa"]
# for name in names:
#     print(name)

# weekdays = ["sun", "tues", "wed", "thurs", "fri"]
# print(weekdays)
# del weekdays[0] #this removes based on index value
# print(weekdays)
# weekdays.remove("tues") #this removes based off the word/item in list
# print(weekdays)
# weekdays.insert(1, "mon") #inserts "mon" into index 1, original thing in index 1 moves to index 2
# print(weekdays)
#
# school = "greenwood college school"
# print(school)
# print(school[0]) #this will print the thing in index 0, so "g" in this case
#
# numbers = [2, 4, 3, 77, 12]
# print(numbers)
# numbers.insert(0,6) #inserts "6" into index 0
# print(numbers)
# del numbers[3] #deletes whatever is in index 3
# print(numbers)
# numbers.remove(2) #removes the 2 in the list, no matter the index
# print(numbers)
#
# exString = "hello world"
# for letter in exString:#prints every letter in "hello world" in different lines
#     print(letter)

print("\ntoday's tasks:\n")
task1 = ["hello", "my", "name", "is", "alexa"]
print(task1)
del task1[3]
print(task1)

import random
randLengthList = []
list_len = random.randint(5,10) #picks a random number of indexes between 5 and 10
for i in range(list_len):
    randLengthList.append(i)
print(randLengthList)
if len(randLengthList) % 2 == 0:
    randLengthList.insert(0, "even") #if the length of randlengthlist is divisble by 2, put "even" into idex 0
else:
    randLengthList.insert(0, "odd") #if the length of randlengthlist is not divisble by 2, put "odd" into idex 0
print(randLengthList)

task3 = ["435", "6587", "26862896", "akjsg", "216", "kjgsd"]
for x in task3:
    print(x)

task4 = ["y","o","u","r","e", "a", "w","i","z","a","r","d", "h","a","r","r","y"]
task4.insert(4,3)
task4.insert(1,0)
task4.insert(15,4)
task4.remove("e")
task4.remove("o")
task4.remove("h")
print(task4)

task5 = "reverse one"
task5 = task5.split(" ")
task5 = task5[::-1]
output = ' '.join(task5)
print(task5)

str = ""
for x in task5:
    str = x +str
print(task5)
