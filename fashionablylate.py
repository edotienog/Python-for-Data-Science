def fashionably_late(arrivals, name):
   #Find the index of the guest with the given name 
    index = arrivals.index(name)
    #Find the number of guest who arrived before the half point
    half = len(arrivals)/2
    return index !=len(arrivals)-1 and index >= half
print(fashionably_late(['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], 'Mona'))