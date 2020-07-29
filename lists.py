pasta_dishes = ["Spaghetti", "Ramen", "Mac n Cheese", "Fettucini Alfredo", "Pad Thai", "Grilled Cheese"]

print("WHILE LOOP")

count = 0
while count < len(pasta_dishes):
    print(pasta_dishes[count])
    count += 1

print("FOR LOOP")
# FOR EVERY [ITEM] IN [LIST OF ITEMS]
for pasta in pasta_dishes:
    print(pasta)
    if pasta == "Mac n Cheese":
        break

# if "Grilled Cheese" in pasta_dishes:
#     pasta_dishes.remove("Grilled Cheese")
#     print("Grilled Cheese isn't pasta!")
# else:
#     print("This is all pasta!")