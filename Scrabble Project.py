# Below is a list of the letters of the alphabet and a list with Scrabble point values for each letter
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Creates a dictionary combining above lists so each letter corresponds to it's respective point value in Scrabble
letter_to_points = {key:value for key, value in zip(letters, points)}
# Adds blank Scrabble tile point value of 0 to the dictionary
letter_to_points[" "] = 0

# function that will take in a word and return how many points that word is worth
def score_word(word):
  point_total = 0
  for letter in word:
    if letter in letter_to_points:
      point_total += letter_to_points[letter]
    else:
      point_total += 0
  return point_total

# User Inputs
name = input("Type name here: ")
scrabbleword = input("Type your Scrabble word here: ")

# Setting any user word input to upper case so the function can correctly map it to the upper case alphabet dictionary
# Then running the user input word through our score_word function
scrabbleword_upper = scrabbleword.upper()
total_points = score_word(scrabbleword_upper)

# Print statement to display the point value for their word to the user
print("Hi {name}! Your Scrabble word, {scrabbleword}, is worth: {total_points} points!".format(name=name, scrabbleword=scrabbleword, total_points=total_points))
