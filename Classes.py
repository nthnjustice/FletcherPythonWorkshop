class Apple:
  typeof = "Food"

  def __init__(self, kcal, col):
    self.calories = kcal
    self.color = col
class Pizza:
  typeof = "Food"

  def __init__(self, kcal):
    self.calories = kcal

class Soda:
  typeof = "Drink"

  def __init__(self, kcal):
    self.calories = kcal

myApple = Apple(70, 'red') #Declares an instance on an Apple wit 75 kcals

print myApple.typeof #Prints the typeof attribute of myApple

print myApple.calories #Prints the calories attribute of myApple
print myApple.color
myApple2 = Apple(80, 'green') #Declares an instance 

print myApple2

print myApple2.calories

myDay = [Apple(50, 'red')]

print myDay[0].typeof

print myDay[0].calories

myDay.append(Apple(90, 'yellow'))

myDay.append(Pizza(200))

myDay.append(Soda(150))

print myDay

for food in myDay:
  print food.typeof
  print food.calories

apple1 = Apple(50, 'green')
apple2 = Apple(60, 'red')
pizza1 = Pizza(168)
soda1 = Soda(75)

myDay2 = [apple1, apple2, pizza1, soda1]

for food in myDay2:
  print food

def countCalories(day):
  total = 0
  for i in day:
    total += i.calories

  return total

numCalories = countCalories(myDay2)

print numCalories
