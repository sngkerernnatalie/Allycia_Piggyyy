print("Piggy to the rescue!")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("Piggy will cheer you up! Will playing with giraffe and sheepy make you feel better?")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("Piggy's feeling happy too! Are you free to play some time soon?")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("Take a break and do something that makes you feel better")
      counter += 1
      if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("Piggy is bored too, would you like to spend the rest of the day with me?")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = encouragement_list[0] + ":)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
