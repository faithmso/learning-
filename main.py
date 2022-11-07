lottery_numbers = {13,21,22,5,8}

players = [
  {
    "name":"joe",
    "numbers":{1,3,8,7,21}
  },
  {
    "name":"Hanna",
    "numbers":{4,9,10,12,15}
  }
]

name = players[0]["name"]
numbers = players[0]["numbers"].intersection(lottery_numbers)
print(f"player {name} got {len(numbers)} numbers right.")

name = players[1]["name"]
numbers = players[1]["numbers"].intersection(lottery_numbers)
print(f"player {name} got {len(numbers)} numbers right.")