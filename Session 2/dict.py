'''
shopping_list = {'bear legs': 100,
                 'eye of newt': 200,
                 'mandrake': 50,
                 'snake dandruff': 200,
                 'spider burp': 750,
                 'swamp gas': 750}

print(shopping_list)
print(shopping_list['spider burp'])
'''
#A Dictionary can store a Dictionary within itself!

nested_shopping_list = {'bear legs': {'price': 100, 'store': 'Shop BL'},
                        'eye of newt': {'price': 200, 'store': 'Shop EON'},
                        'mandrake': {'price': 50, 'store': 'Shop M'},
                        'snake dandruff': {'price': 200, 'store': 'Shop SD'},
                        'spider burp': {'price': 750, 'store': 'Shop SB'},
                        'swamp gas': {'price': 750, 'store': 'Shop SG'}}

print(nested_shopping_list['bear legs'])
print(nested_shopping_list['bear legs']['price'])

