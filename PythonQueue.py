# created a temporary list with all the people
people = ["Joe", "Sally", "Jim", "Betty", "Bill", "Sara", "Zak", "Anne", "Kate"]

#this is the list we want to the names in
names = []

for i in range(0,10):
    item = input("Enter name: ")
    names.append(item)
print(names)

#second loop, removing all elements in name
for b in range(len(names)):
    print(names.pop(0))

# names is empty so it worked
print(names)

