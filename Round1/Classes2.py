class Apple:
  def __init__(self, kcal):
    self.calories = kcal

class Basket:
  def __init__(self):
    self.allApples = []

  def addApple(self, newApple): #Remember, self is mybasket
    self.allApples.append(newApple)

  def countApples(self):
    return len(self.allApples)

  def countAppleCalories(self):
    total = 0
    for i in self.allApples:
      total += i.calories
    return total

#Declare an intance of an Apple object
apple1 = Apple(37)

#Declare an instance of a Basket
mybasket = Basket()

print "apple1 calories:",apple1.calories

mybasket.addApple(apple1)

print "apples in basket:",mybasket.countApples()

tempApple = 0

for i in range(0, 9): #Loop i from 0 to 8
  tempApple = Apple(25*((i%3)+1)) #Declare an instance of an Apple
  mybasket.addApple(tempApple) #Add tempApple to myBasket

print "apples in basket:",mybasket.countApples()

basket2 = Basket() #Declare an instance of a Basket

for i in range(0, 8): #Loop i from 0 to 7
  tempApple = Apple(50) #Create an instane of an Apple
  basket2.addApple(tempApple) #Add apple to basket2

print "apples in basket2:",basket2.countApples()
print "apples in basket:",mybasket.countApples()

print "calories in first basket:",mybasket.countAppleCalories()
print "calories in second basket:",basket2.countAppleCalories()

