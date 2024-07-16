from roblox import Client
client = Client()
import asyncio

async def main():
   userName = input("Input a Username:")
   user = await client.get_user_by_username(userName)
   print ("User Created:", user.created)
   print ("Display:", user.display_name)
   print ("Description:", user.description)
   print("Is user banned:", user.is_banned)

asyncio.run(main())
