all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
# given string
string = "devopsassessment"
  
# intialized value
total_letters = 0
  
# iterate through all characters
for s in string:  
    if s in all_letters:
       total_letters += 1
  
print("Number of letters in the word devopsassessment is ", total_letters)
