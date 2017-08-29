#d = {"apples": 15, "bananas": 35, "grapes": 12}
#print(d["bananas"]) #output tra ra la 35
#d["oranges"] = 20 # nhập thêm 1 key là orange với value = 20
#print(len(d)) #output đưa ra là 4, 4 keys
#print("grapes" in d) # output = True
#print(d["pears"]) # error do không có key 'pears' trong d
#print(d.get("pears", 0)) # output = 0 do không có key 'pears' trong d
#fruits = list(d.keys())
#fruits.sort()
#print(fruits) # đưa ra 1 mảng bao gồm các key của d nhưng sắp xếp theo alphabet
#del d["apples"] # xóa key apples trong d
#print("apples" in d) # False

def add_fruit(inventory, fruit, quantity=0):
    # phần thêm vào theo yêu cầu đề bài
    if fruit not in inventory.keys():
        inventory[fruit] = quantity
    else:
        inventory[fruit] += quantity
    return

new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)

print("strawberries" in new_inventory)

print(new_inventory["strawberries"] == 10)

add_fruit(new_inventory, "strawberries", 25)

print(new_inventory["strawberries"] == 35)
#print(new_inventory)

