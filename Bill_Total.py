s = {
    "pepsi": 190.23,
    "popcorn": 150.55,
    "fries": 140.25,
    "cake": 100.55,
    "tea": 25.00 
}
total = 0
cart = []
print("------MENU------")
for i,j in s.items():
  print(f"{i:10}:{j:.2f}")
while True:
    w=input("select the items").lower()
    if w =="q":
        break
    else:
        cart.append(w)
        total+=s[w]
        print(f"your order:{cart}")
print(f"your bill:{total}")