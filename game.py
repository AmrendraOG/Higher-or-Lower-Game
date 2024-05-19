from replit import clear
import random

score = 0

person_set = [["Cristiano Ronaldo", 629], ["Lionel Messi", 502],
              ["Selena Gomez", 428], ["Kylie Jenner", 399],
              ["Dwayne Johnson", 397], ["Ariana Grande", 379],
              ["Kim Kardashian", 363], ["Beyonce", 319],
              ["Khloe Kardashian", 309], ["Kendall Jenner", 293]]

person1 = random.choice(person_set)
person_set.remove(person1)
person2 = random.choice(person_set)


def present(a, b):
  '''Prints two person a and b'''
  print(f"Compare A: {a[0]}")
  print("VS")
  print(f"Compare B: {b[0]}")


def game(a, b):
  global person_set, score
  if len(person_set) > 1:
    if score > 0:
      print(f"Correct Answer! Your score: {score}\n")
    present(a, b)
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if (answer == 'a' and a[1] > b[1]) or (answer == 'b' and b[1] > a[1]):
      clear()
      score += 1
      a = b
      person_set.remove(b)
      b = random.choice(person_set)
      game(a, b)
    else:
      clear()
      print(f"You lose!!! Your final score = {score}")
  else:
    clear()
    print(f"You won!!! Your final score = {score}")


game(person1, person2)
