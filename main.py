import os    
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, shift_num, msg_direction):
    # msg_direction determines whether message is encrypted/decrypted
    new_message = ''
    new_index = 0
    for letter in message:
        if letter.isalpha():
            lst_index = alphabet.index(letter)
            if msg_direction.lower() == 'encode':
                new_index = lst_index + shift_num
                if new_index > 25:
                    new_index -= 26
            elif msg_direction.lower() == 'decode':
                new_index = lst_index - shift_num
                if new_index < 0:
                    new_index += 26
            new_message += alphabet[new_index]
        else:
            new_message += letter
    
    print(f'The {msg_direction}d text is {new_message}')

def get_input():
    # get user inputs for message, shift number, direction
    # do not accept invalid inputs
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == 'encode' or direction == 'decode':
            break
        else:
            print('Please enter a valid selection!')
    text = input("Type your message:\n").lower()
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            if shift > 26:
                print('Invalid choice, shift must be <= 26.  Try again.\n')
            else:
                break
        except ValueError:
            print('Please enter a valid number!\n')
    caesar(text, shift, direction)

# Execute the program
go_again = True
while go_again:
    os.system('clear')
    print(logo) # prints Caesar Cipher logo at program start
    get_input() # calls function to get user inputs
    while True:
        ask_user = input('Enter \'yes\' to go again, \'no\' to quit.\n').lower()
        if ask_user == 'no':
            go_again = False
            break
        elif ask_user == 'yes':
            break
        else:
            print('Invalid selection, please enter valid response.\n\n')
        
print('Thanks for using our Caesar Cipher, goodbye!')
