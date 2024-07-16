from roblox import Client
from roblox.utilities.exceptions import UserNotFound
import asyncio
client = Client()

async def main():
    while True:
        userName = input("Input a Username:")
        try:
            user = await client.get_user_by_username(userName)
            print("Is user banned:", user.is_banned)
            print ("User create date:", user.created)
        except UserNotFound:
            print("Username not found.")
asyncio.run(main())
