def main():
    print("generated_password")
    length=int(input("enter desired password length"))
    if length<8:
        print("password must be atleast eight letters")
    else:
        password=generate_password(length)
        print("generated_password:",password)
import random
import string
def generate_password(length):
    lowercase_letters=string.ascii_lowercase
    uppercase_letters=string.ascii_uppercase
    special_characters="@$&RDS123"
    characters=lowercase_letters+uppercase_letters+special_characters
    length=max(8,min(length,128))
    password= ''.join(random.choice(characters) for _ in range(length))
    return password
if __name__ == "__main__":
    main()