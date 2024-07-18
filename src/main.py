import json
import asyncio
from roblox import Client
client = Client()
from roblox.utilities.exceptions import UserNotFound
from roblox.utilities.exceptions import Unauthorized

async def main():
      answer = input("Would you like to check your roblox token:")
      if answer.lower() == "y":
         await groupReading()
      elif answer.lower() == "n":
         await noToken()
      else: 
         print("Invalid.")

async def readToken():
   # Reads token from config, then gets who the token is.
   with open("config.json", "r") as file:
      config_data = json.load(file) 
      robloToken = config_data["token"]
      client.set_token(robloToken)
      user = await client.get_authenticated_user()
      print("Logged in as:", user.name)
      print("Followers count:",  await user.get_follower_count())
      print ("Friend count:", await user.get_friend_count())
   try:
      premCheck = await user.has_premium()
      print ("Does user have Premium:", premCheck)
   except Unauthorized:
      print("Unauth Error!")


async def groupReading():
   groupID = input("Put a group ID:")
   group = await client.get_group(groupID)

async def groupReadingToken(robloToken):
   answer = input("Do you own this group:")
   if answer.lower == "y":
      client.set_token(robloToken)
      user = await client.get_authenticated_user()
      print(await user.get_group_roles())
      groupID = input("Put group ID.")
      group = await client.get_group(groupID)
   elif answer.lower == "n":
      await groupReading()


async def noToken():
   while True:
      data = input("Put a Username:")
      
      try:
         user = await client.get_user_by_username(data)
         print("Followers count:",  await user.get_follower_count())
         print ("Friend count:", await user.get_friend_count())

      except UserNotFound:
         print("Invalid Username!")

   
   
asyncio.run(main())
