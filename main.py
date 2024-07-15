import robloxpy
import requests

def user(): 
    userID = input("Enter a Valid UserID:")
    print(robloxpy.User.External.CreationDate(userID))
    print(robloxpy.User.External.GetUserName(userID))

def server():
    print

def main():
    answer = input("User or Game: ")
    if answer == "u":
        user()
    elif answer == "g":
        server()
    else: 
        print("Invalid!")
main()