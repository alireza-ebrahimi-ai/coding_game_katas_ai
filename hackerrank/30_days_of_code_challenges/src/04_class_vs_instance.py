class Person(object):

    age = 0

    def __init__(self, initial_age):
        if initial_age >= 0:
            self.age = initial_age
        else:
            print('Age is not valid, setting age to 0.')

    def year_passes(self):
        self.age += 1

    def am_i_old(self):
        if self.age < 13:
            print('You are young.')
        elif ((self.age >= 13) and (self.age < 18)):
            print('You are a teenager.')
        else:
            print('You are old.')




