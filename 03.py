data = []
while True:
    user = input ("ketikkan angka: ")
    if user == "n":
        break
    data.append(int(user))

total = sum(data)
rata = total/len(data)
print("rata-rata", rata)