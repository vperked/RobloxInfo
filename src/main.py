from roblox import Client
client = Client()
import json
import asyncio

async def main():
   answer = input("Would you like to put your roblox token:")
   if answer == "y":
      readToken()
   else: 
      print("Invalid.")

async def readToken():
   with open("config.json", "r") as file:
      config_data = json.load(file) 
      robloToken = config_data["token"]
   robloToken = await client.set_token(robloToken)
   
asyncio.get_event_loop().run_until_complete(main())
