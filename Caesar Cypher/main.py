from art import logo


symbols= ["1","2","3","4","5","6","7","8","9","0",'~', '`', '!','@',"#","$", "%", "^", "&", '*', '(', ")", "_", "-", "+", "=", "{", "}", "|", "[", ']', ":", ';', "\' ", "<", ",", ">", ".", "?", "/", " "]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def encrypt(original_text, shift_amount):
    encoded_message= ""
    for letter in original_text:
        if letter in symbols:
            encoded_message+= letter
        elif letter in alphabet:
            count= alphabet.index(letter) + shift_amount
            if count >25:
                encoded_message+= alphabet[count-26]
            else:
                encoded_message += alphabet[alphabet.index(letter)+shift_amount]

    print(f"Here is the encoded result: {encoded_message}")

def decrypt(original_text, shift_amount):
    decoded_message= ""
    for letter in original_text:
        if letter in symbols:
            decoded_message+= letter
        elif letter in alphabet:
            count= alphabet.index(letter) - shift_amount
            if count >0:
                decoded_message+= alphabet[count-26]
            else:
                decoded_message += alphabet[alphabet.index(letter)-shift_amount]
    print(f"Here is the decoded result: {decoded_message}")

def caesar(direction_chosen,original_text,shift_amount):
    if direction_chosen=='encode':
        encrypt(original_text,shift_amount)
    elif direction=='decode':
        decrypt(original_text,shift_amount)
        
i= True
while i != False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction,text,shift)
    conti= input("Type 'Yes' if you want to go again. Otherwise type 'No'.\n").lower()
    if conti== 'no':
        i= False





