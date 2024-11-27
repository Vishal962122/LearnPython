# MLB_team = {
#     'Colorado' : 'Rockies',
#     'Boston'   : 'Red Sox',
#     'Minnesota': 'Twins',
#     'Milwaukee': 'Brewers',
#     'Seattle'  : 'Mariners'
# }

# You can also construct a dictionary with the built-in dict() function. The argument to dict() should be a sequence of key-value pairs. A list of tuples works well for this:M

# MLB_team=dict([

#     ('colorado','Rockies'),
#     ('Boston', 'Red Sox'),
#     ('Minnesota','Twins'),
#     ('Milwaukee', 'Brewers'),
#     ('Seattle ', 'Mariners')

# ])
# If the key values are simple strings, they can be specified as keyword arguments. So here is yet another way to define MLB_team:
# MLB_team = dict(
#      Colorado='Rockies',
#      Boston='Red Sox',
#      Minnesota='Twins',
#      Milwaukee='Brewers',
#      Seattle='Mariners'
# )

# Python3 code to demonstrate
# to get key and value
# using in operator

# initializing dictionary
test_dict = {"Geeks": 1, "for": 2, "geeks": 3}

# Printing dictionary
# print("Original dictionary is : " + str(test_dict))
for value in test_dict.values():
    print("hhhhh" ,value,"efdefe",value)
 