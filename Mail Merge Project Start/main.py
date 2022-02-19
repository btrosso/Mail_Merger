# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# open the letter template and read all the lines, each line becomes a string item in a list
with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_contents = letter_file.readlines()
    print(letter_contents)

# open the list of names (invited_names) and read all the lines, each line becomes a string item in a list
with open("./Input/Names/invited_names.txt", mode="r") as recipients_file:
    recipient_contents = recipients_file.readlines()
    for i in range(len(recipient_contents)-1):
        recipient_contents[i] = recipient_contents[i].strip("\n")
    print(recipient_contents)

# testing something out
# temp = letter_contents[0][5:11]
# recipient_var = temp
# print(recipient_var)

# writing all the new files and logic to replace the recipient name with each name in the recipient list
previous_recip = ""
for recipient in recipient_contents:
    with open(f"./Output/ReadyToSend/{recipient}_letter.txt", mode="w") as new_letter:
        if letter_contents[0][5:11] == "[name]":
            temp = letter_contents[0][5:11]
            letter_contents[0] = letter_contents[0].replace(f"{temp}", f"{recipient}")
            new_letter_contents = ''.join(letter_contents)
            new_letter.write(new_letter_contents)
            previous_recip = recipient
        else:
            letter_contents[0] = letter_contents[0].replace(f"{previous_recip}", f"{recipient}")
            new_letter_contents = ''.join(letter_contents)
            new_letter.write(new_letter_contents)
            previous_recip = recipient
