class Car():

    def __init__(self, brand,color,tires):
        self.__brand = brand
        self.__color = color
        self.__tires = tires
    
    def __str__(self):
        return f'This is a {self.__color} {self.__brand} with {self.__tires} tires'

    def __repr__(self):
        return 'Car({self.__brand},{self.__color},{self.__tires})'


    @property
    def color(self):
        return self.__color

    @color.setter 
    def color(self,color):
        self.__color = color

audi = Car('Audi', 'red', '4')

print (audi)
print (audi.color)
audi.color = 'Black'
print(audi)

    