# OOP

# task-1

# init_name = input('Enter your name: ')
# init_color = input('Enter the color of your favorite fruit from the colors of the rainbow: ')
# class Fruit:
#     fruits = {
#         'orange':'orange',
#         'yellow':'lemon',
#         'green':'apple',
#         'red':'strawberry',
#         'pink':'raspberry',
#         'purple':'plum',
#         'blue':'currant'
#     }
#
# class Check_input:
#     def __init__(self, name, favo_color, obj):
#         self.name = name
#         self.favo_color = favo_color
#         self.obj = obj
#     def checking(self):
#         if self.favo_color in self.obj.keys():
#             check_l = input(f'{self.name}, do you like this {self.obj[self.favo_color]}? yes/no:  ')
#             if check_l == 'yes':
#                 return 'Great😊'
#             else:
#                 return 'Tragic😔'
#         else:
#             return 'Oh no, there is no fruit that you want'
#
# return_to_check = Check_input(init_name, init_color, Fruit.fruits)
#
# print(return_to_check.checking())








# task-2

# name = input('What\'s your name?: ')
# penpal = input('Enter the nationality: ')
#
# class Nationalities:
#
#     def __init__(self, name):
#         self.name = name.title()
#         self.hello_nation = {
#         'uzbek': f'Assalomu Aleykum, {self.name} keling do\'stlashamiz',
#         'russian': f'Здравствуйте, {self.name} давай подружимся',
#         'arabic':f'مرحبا،{self.name} دعونا نكون أصدقاء ',
#         'english': f'Hello, {self.name} let\'s be friends.',
#         'turkish': f'Merhaba {self.name} arkadaş olalım',
#         'italian': f'Ciao, {self.name} diventiamo amici',
#         'french': f'Bonjour, {self.name} soyons amis',
#         'korean': f'안녕, {self.name} 친구하자',
#         'chinese': f'你好，{self.name} 我們交朋友吧'
#         }
#
#
# class Response:
#     def __init__(self, name, penpal, dict):
#         self.name = name
#         self.penpal = penpal
#         self.dict = dict
#
#
#     def __res__(self):
#         if self.penpal in self.dict.keys():
#             return self.dict[self.penpal]
#         else:
#             return f'Not found a person of {self.penpal} nation'
#
# nat = Nationalities(name)
# res = Response(name, penpal, nat.hello_nation)
# print(res.__res__())