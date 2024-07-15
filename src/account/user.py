from roblox import Client
client = Client()
import asyncio

async def main():
   userName = input("Input a Username:")
   user = await client.get_user_by_username(userName)
   print ("Display:", user.display_name)
   print("Is user banned:", user.is_banned)

asyncio.get_event_loop().run_until_complete(main())
