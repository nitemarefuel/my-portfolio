import random
wordlist = ["fly","rhythm","gamer","pogchamp","squanch","kek","simp","poop","sexy","nipples","pewdiepie","anime","daboobymaster","Supercalifragilisticexpialidocious","pneumonoultramicroscopicsilicovolcanoconiosis","mitochondria","headshot","boop","chicken","buttcrack","rectum","spicy","dank","trippy","gucci","hypebeast","mudkip","teemo","thequickbrownfoxjumpedoverthelazydog"]
newword = random.choice(wordlist)
strike = 0
a= []
index = 0

for i in range(len(newword)):
  a.append("_")

while True:
  print(*a)
  x = input("Guess a letter: ")
  if (len(x) > 1):
    print("Please input more than one letter.")
    continue
  if x in newword:
    for i in range (len(newword)):
      if newword[i] == x:
        index = i
        a[i] = x
  else:
    print("")
    print("The secret word does not contain letter.")
    strike += 1
    print(str(strike))
  if "_" not in a:
    print("")
    print("you win!")
    print(*a)
    break
  if strike >= 6:
    print("")
    print("You lose")
    print("The secret word is " + newword)
    break



