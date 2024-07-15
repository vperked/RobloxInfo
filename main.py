from roblox import Client
client = Client()
import asyncio

async def main():
   userID = input("Input a userID:")
   user = await client.get_user(userID)
   print ("Display:", user.display_name)
   
asyncio.get_event_loop().run_until_complete(main())
