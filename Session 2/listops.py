wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing',
                        'slug butter', 'snake dandruff']

#Adding items to a list
wizard_list.insert(6, "bear burp")
print(wizard_list)

wizard_list.insert(3, "mandrake")
wizard_list.insert(0, "hemlock")
wizard_list.insert(9, "swamp gas")

print(wizard_list)

#Removing items from a list
del wizard_list[5]
print(wizard_list)

del wizard_list[2]
del wizard_list[4]
del wizard_list[0]
print(wizard_list)

#Replacing items in a list
wizard_list[0] = 'bear legs'
wizard_list[4] = 'spider burp'
print(wizard_list)

#Get length of array
print(len(wizard_list))

