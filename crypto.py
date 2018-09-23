from helpers import alphabet_position, rotate_character
def encrypt(text,rot):
    cipher = ''
    for i in text:
        if i.isalpha():             
            cipher += rotate_character(i,rot)
        else:
            cipher += i
    return cipher
def main():
    text = input("Type a message: \n")  
    rot = input("Rotate by: \n")
    rot = int(rot)      
    print(encrypt(text,rot))

if __name__ == '__main__':
    main()
   