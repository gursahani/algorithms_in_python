import copy
warmtones = ['blue',
             'green',
             'red',
             'blue',
             'white'
             ]

pallette = list(warmtones)



deep_pallette = copy.deepcopy(warmtones)
print(deep_pallette)
pallette.pop(1)

pallette[0] = 'grey'

print(pallette)
print(warmtones)