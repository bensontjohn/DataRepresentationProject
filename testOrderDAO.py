# Code adapated from https://github.com/andrewbeattycourseware/datarepresentation2021

# Calls the name of the file and NOT the class
from orderDAO import orderDao

order = {
    'id': 1,
    'name': 'John Doe',
    'item': 'Lenovo tablet',
    'price': 100
}

# order = {
#    'id': 2, #id auto increments
#   'name': 'Carl Rose',
#   'item': 'Iphone SE',
#  'price': 250
# }

# order = {
#    'id': 3,
#    'name': 'Steve Cook',
#    'item': 'Smartwatch',
#    'price': 300
# }

# order = {
#     'id': 4,
#    'name': 'Andy Roberts',
#    'item': 'Dell laptop',
#    'price': 400
# }


#check to see if create() works  
# returnValue = orderDao.create(order)
# print(returnValue) 

# returnValue = result = orderDao.getAll()
# print(returnValue) 

#returnValueCreate = orderDao.create(order)
#print("*Return from Create function is #id*:",(str(returnValueCreate)))

#returnValuegetAll = orderDao.getAll()
#print("*Return from getAll function*: \n",(str(returnValuegetAll)))

# returnValue = orderDao.findById(order['id'])
# print(returnValue)
# result = orderDao.findById(2)
# print("*Return from findById function*:",(str(result)))
# print(result)
# print(returnValue)

# returnValue = orderDao.update(order)
# print("*Return from update function*",(str(returnValue)))

# returnValue = orderDao.delete(order['id'])
# print("*After delete*",(str(returnValue)))