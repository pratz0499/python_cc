alphabet="abcdefghijklmnopqrstuvwxyz"
key=2
new_message=""
message=input("write your message:")
for character in message:
    if character in alphabet:
        position=alphabet.find(character)
        new_position=(key+position)%26
        new_character=alphabet[new_position]
        new_message+=new_character

print("the new message is:",new_message)
