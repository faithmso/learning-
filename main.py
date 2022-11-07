for number in range(1,101):
  if number % 15 == 0:
    print("FizzBuzz")

  elif number % 3 == 0:
    print("Buzz")

  elif number % 15 == 0:
    print("Fizz")

  else:
    print(f"{number}")


for n in range(2,10):
  for x in range(2,n):
    if n % x == 0:
      print(f"{n} equals {x} * {n//x}")
      break
  else:
    print(f"{n} is a prime number.")


friend_ages = [22, 31, 35, 27]
age_string = [f"My friend is {age} years old." for age in friend_ages]

print(age_string)


friend = input("Enter your friend name: ")
friends = ["Rolf", "Anne", "Jen", "Charlie", "Bob"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
  friend_titlecased = friend.title()
  print(f"{friend_titlecased} is one of your friends.")