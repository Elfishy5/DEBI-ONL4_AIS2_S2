import random
def generate_password(length:int):
    characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password=""
    for _ in range(length):
      password+= random.choice(characters)
    return f"Generate_password:{password}" 