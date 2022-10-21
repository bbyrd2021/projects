# Brandon L. Byrd
# COMP 163/004
# March 29, 2022
# This project uses the concept of inheritance to create multiple instances of Animal objects that each have their own subclasses. This allows the user to print multiple instances of each sub-class of animals.


#Superclass Animal
class Animal:
  # I could've saved space by using constructors to take in argument values for my classes, but I wanted to experiment with setters and getters. I know there's a more Pythonic way to do it, but this is entirely intentional.

  def __init__(self):
    self.name = 'None'
    self.species = 'None'
    self.gender = 'None'
    self.qty = 0

  #setters and getters
  def setName(self, nomen='none'):
    self.name = nomen
    
  def getName(self):
    return self.name

  def setGender(self, gen='none'):
    self.gender = gen

  def getGender(self):
    return self.gender

  def setSpecies(self, species='none'):
    self.species = species

  def getSpecies(self):
    return self.species

  def display(self):
    print(f'Species: {self.getSpecies()}\n Name: {self.getName()}\n Gender: {self.getGender()} ')

#The class for Swine
class Swine(Animal):
  def __init__(self):
    self.setName(input('Enter the name of your Swine: '))
    self.setSpecies('Swine')
    self.setCurl()

  #this method creates an attribute unique to the Swine class
  def setCurl(self, curl=0):
    #used exception handling to take an interger from 1-10. It loops until it gets a valid number.
    while True:
        try:
          curl = int(input("On an scale from 1-10 how curly is your Swine's tail? "))
          if 1 <= curl <= 10:
            self.tailCurliness = curl
            break
          else:
            print('Out of range, try again')
        except ValueError:
          print('ValueError: Please enter an interger from 1-10')

  def getCurl(self):
    return self.tailCurliness
  
  #display2 uses display() from the Animal Super class and adds the unique class attribute to it. I do this for every subsequent class.
  def display2(self):
    self.display()
    print(f' Tail curliness: {self.getCurl()}\n')

#class for chicken
class Chicken(Animal):
  def __init__(self):
    self.setName(input('Enter the name of this Chicken: '))
    self.setSpecies('Chicken')
    self.setFeatherColor()

  def setFeatherColor(self, color='None'):
    color = input("Enter this chicken's feather color: ")
    self.featherColor = color

  def getFeatherColor(self):
    return self.featherColor
  
  def display2(self):
    self.display()
    print(f' Feather color: {self.getFeatherColor()}\n')

#class for sheep
class Sheep(Animal):
  def __init__(self):
    self.setName(input('Enter the name of this Sheep: '))
    self.setSpecies('Sheep')
    self.setWoolThickness()
  
  def setWoolThickness(self, woolfactor=0):
    while True:
        try:
          woolfactor = int(input("On an scale from 1-10 how thick is this Sheep's wool? "))
          if 1 <= woolfactor <= 10:
            self.woolThickness = woolfactor
            break
          else:
            print('Out of range, try again')
        except ValueError:
          print('ValueError: Please enter an interger from 1-10')

  def getWoolThickness(self):
    return self.woolThickness

  def display2(self):
    self.display()
    print(f' Wool Thickness: {self.getWoolThickness()}\n')

#class for donkey
class Donkey(Animal):
  def __init__(self):
    self.setName(input("Enter the name of this Donkey: "))
    self.setSpecies('Donkey')
    self.setStrength()

  def setStrength(self, strength=0):
    while True:
        try:
          strength = int(input("On an scale from 1-10 how strong is this Donkey? "))
          if 1 <= strength <= 10:
            self.strength = strength
            break
          else:
            print('Out of range, try again')
        except ValueError:
          print('ValueError: Please enter an interger from 1-10')
  
  def getStrength(self):
    return self.strength

  def display2(self):
    self.display()
    print(f' Strength: {self.getStrength()}\n')

#class for dog
class Dog(Animal):
  def __init__(self):
    self.setName(input('Enter the name of this Dog: '))
    self.setSpecies('Dog')
    self.setHerding()

  def setHerding(self, instinct=0):
      while True:
        try:
          instinct = int(input("On an scale from 1-10 how capable is this dog at herding? "))
          if 1 <= instinct <= 10:
            self.herding = instinct
            break
          else:
            print('Out of range, try again')
        except ValueError:
          print('ValueError: Please enter an interger from 1-10')

  def getHerding(self):
    return self.herding

  def display2(self):
    self.display()
    print(f' Hearding Capability: {self.getHerding()}\n')

print('\nWelcome to the Farm App!')
print('Please choose an animal below!\n')
print('(1) Swine (Sow)')
print('(2) Swine (Boar)')
print('(3) Chicken (Hen)')
print('(4) Chicken (Cock)')
print('(5) Sheep (Ewe)')
print('(6) Sheep (Ram)')
print('(7) Donkey (Ass)')
print('(8) Donkey (Jenny)')
print('(9) Dog (Sire)')
print('(10) Dog (Dam)')
print('(11) Exit & Print Inventory')


animalList = [] #this list will contain all of the objects to be printed out.

#these are for keeping track of the number of animals to print later
swine = 0
chicken = 0
sheep = 0
donkeys = 0
dogs = 0

n=0 #used the same concept of exception handling for a valid input integer 1-11
while n != 11:
  try:
    n = int(input('\nChoose your animal here (or Enter 11 to exit): '))

    if n == 1:
      print('You choose a Sow\n')
      sow = Swine()
      sow.setGender('Sow') #I define gender down here instead of in the class because I wanted the object's gender to automatically be updated based on what the user chooses the gender to be.
      animalList.append(sow) #adds object to animal list. If you were to print the list you would get each objects address.
      swine += 1

    elif n == 2:
      print('You choose a Boar\n')
      boar = Swine()
      boar.setGender('Boar')
      animalList.append(boar)
      swine += 1

    elif n == 3:
      print('You choose a Hen\n')
      hen = Chicken()
      hen.setGender('Hen')
      animalList.append(hen)
      chicken += 1

    elif n == 4:
      print('You choose a Cock\n')
      cock = Chicken()
      cock.setGender('Cock')
      animalList.append(cock)
      chicken += 1

    elif n == 5:
      print('You choose an Ewe\n')
      ewe = Sheep()
      ewe.setGender('Ewe')
      animalList.append(ewe)
      sheep += 1

    elif n == 6:
      print('You choose a Ram\n')
      ram = Sheep()
      ram.setGender('Ram')
      animalList.append(ram)
      sheep += 1

    elif n == 7:
      print('You choose an Ass\n')
      ass = Donkey()
      ass.setGender('Ass')
      animalList.append(ass)
      donkeys += 1

    elif n == 8:
      print('You choose a Jenny\n')
      jenny = Donkey()
      jenny.setGender('Jenny')
      animalList.append(jenny)
      donkeys += 1

    elif n == 9:
      print('You choose a Sire\n')
      sire = Dog()
      sire.setGender('Sire')
      animalList.append(sire)
      dogs += 1

    elif n == 10:
      print('You choose a Dam\n')
      dam = Dog()
      dam.setGender('Dam')
      animalList.append(dam)
      dogs += 1

    elif n == 11:
      print('Exiting and printing your list of animals!\n')
      print('Here is your animal inventory!..\n')
      print(f'Number of... Swine: {swine}, Chicken: {chicken}, Sheep: {sheep}, Donkeys: {donkeys},  Dogs: {dogs}.\n')
      print(f'Detail List:\n')
      for animal in animalList: #printing out the list of objects 
        animal.display2()
      break
    elif n > 11:
      print('Out of range, try again')
  except ValueError:
    print('ValueError: Choose an integer from 1-11, please try again')

 