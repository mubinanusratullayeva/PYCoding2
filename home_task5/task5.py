import random

cousin = input('harf kiriting: ')

word_list = ['bear', 'tiger', 'fox', 'wolf', 'rabbit', 'dolphin', 'kit', 'panda']

class Checking_cousin:
    def __init__(self, cousin, list):
        self.foo = cousin
        self.listy = list
    def checking(self):
        word_random = random.choice(self.listy)

        char = ''

        if self.foo in word_random:
            for i in word_random:
                if self.foo != i:
                    char += '*'
                elif self.foo == i:
                    char += i
        else:
            return f'there isn\'t {self.foo} in {self.listy}'
        return f'randomized word: {word_random}, result: {char}'

check_cousin = Checking_cousin(cousin, word_list)
print(check_cousin.checking())