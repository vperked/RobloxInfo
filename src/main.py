from roblox import Client
import json
import asyncio

client = Client()

async def main():
   answer = input("Would you like to put your roblox token:")
   if answer.lower() == "y":
    await readToken()
   else: 
      print("Invalid.")

async def readToken():
   with open("config.json", "r") as file:
      config_data = json.load(file) 
      robloToken = config_data["token"]
   client.set_token(robloToken)
   user = await client.get_authenticated_user()
   print("Logged in as:", user.name)
   
   
asyncio.run(main())
