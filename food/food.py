import json
import random

# Place where all your yummy dishes are stored!
FOODDOTJSON = "food.json"

# Read the list of food items
foodFile = open(FOODDOTJSON, "r")
foodData = json.load(foodFile)
foodFile.close()

breakFastPool = []
breakFastSelection = ""

# Loop thru the food items.
for foodItems in foodData:

    # Get the breakfast items
    breakFastItems = foodItems["breakfast"]

    for breakFastItem in breakFastItems:
        if breakFastItem["prepared"] == 0:
            breakFastPool.append(breakFastItem)

    # Make a random selection from unselected pool of breakfast items.
    # Toggle the "prepared" flag so that we dont get that item again.
    breakFastSelection = random.choice(breakFastPool)
    breakFastSelection["prepared"] = 1

    # Clear selection after everything selected at least once. If that is the
    # case then the pool count would be 1 on the final run after which we
    # need to do our reset.
    if len(breakFastPool) == 1:
        for breakFastItem in breakFastItems:
            breakFastItem["prepared"] = 0

    # Save the file
    foodFile = open(FOODDOTJSON, "w+")
    foodFile.write(json.dumps(foodData))
    foodFile.close()

# Mail selected
print("You can eat yummy " + breakFastSelection["name"])
