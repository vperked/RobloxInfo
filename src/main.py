import json
import asyncio
from roblox import Client
client = Client()
from roblox.utilities.exceptions import UserNotFound
from roblox.utilities.exceptions import Unauthorized

async def main():
      answer = input("Would you like to check your roblox token:")
      if answer.lower() == "y":
        await readToken()
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
      print("Unauth")
   await question(robloToken)

async def question(robloToken):
   print("if you have no token but would like to enter, please put nt.")
   answer = input ("To enter the group section with this token, enter y:")
   if answer.lower() == "y":
      await groupReadingToken(robloToken)
   elif answer.lower() == "nt":
      await groupReading()
   else:
      print("Invalid!")


async def groupReading():
   groupID = input("Put a group ID:")
   group = await client.get_group(groupID)

async def groupReadingToken(robloToken):
   while True:
         client.set_token(robloToken)
         user = await client.get_authenticated_user()
         print(await user.get_group_roles())
         groupID = input("Put group ID:")
         group = await client.get_group(groupID)

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
