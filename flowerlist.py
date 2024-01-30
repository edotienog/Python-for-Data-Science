flowers_list =["pink primrose", "hard leaved pocket orchid", "canterbury bells", "sweat pea", "english marigold", "tiger lily", "moon orchird", "bird of paradise", "monkshood", "globe thistle"]
#Check the type of list
print(type(flowers_list))
print(flowers_list)
#Returns the length of the list
print(len(flowers_list))
print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])
#The last entry is one less the count which is 9
print("Last entry:", flowers_list[9])
#Slicing 
print("First 3 entry:", flowers_list[:3])
print("Final 2 entries:", flowers_list[-2:])
#Removing an item from a list with .remove(), then add the item in parathesis
flowers_list.remove("globe thistle")
print(flowers_list)
#adding item we use .append() 
flowers_list.append('snapdragon')
print(flowers_list)
