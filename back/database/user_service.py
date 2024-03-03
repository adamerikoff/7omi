from bson.objectid import ObjectId

import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.users

users_collection = database.get_collection("users_collection")


# helpers
def user_helper(user) -> dict:
  return {
    "id": str(user["_id"]),
    "fullname": user["fullname"],
    "email": user["email"],
    "password": user["password"],
  }

# Retrieve all students present in the database
async def retrieve_users():
  users = []
  async for user in users_collection.find():
    users.append(user_helper(user))
  return users


# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
  user = await users_collection.insert_one(user_data)
  new_user = await users_collection.find_one({"_id": user.inserted_id})
  return user_helper(new_user)


# Retrieve a user with a matching ID
async def retrieve_user(user_id: str) -> dict:
  user = await users_collection.find_one({"_id": ObjectId(user_id)})
  if user:
    return user_helper(user)


# # Update a user with a matching ID
# async def update_user(user_id: str, user_data: dict):
#   user = await users_collection.find_one({"_id": ObjectId(user_id)})
#   if user:
#     user = user_helper(user)
#     if user_data["fullname"]:
#       user["fullname"] = user_data["fullname"]
#     if user_data["email"]:
#       user["email"] = user_data["email"]
#     if user_data["password"]:
#       user["password"] = user_data["password"]
#     updated_student = await users_collection.update_one(
#       {"_id": ObjectId(id)}, {"$set": user})
#     return updated_student

# Delete a user from the database
async def delete_user(user_id: str):
  user = await users_collection.find_one({"_id": ObjectId(user_id)})
  if user:
    await users_collection.delete_one({"_id": ObjectId(user_id)})
    return True

