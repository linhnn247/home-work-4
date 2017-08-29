stringinput = input("Nhập chuỗi cần đếm: ")
stringlower = stringinput.lower()
lettercount ={}
for letter in stringlower:
    if letter != ' ':
        lettercount[letter] = lettercount.get(letter,0)+1

## ---- sap xep theo alphabetical ---- output dua ra la dang string------
sortlettercount = sorted(lettercount.items())
#print(sortlettercount)
for letter,count in sortlettercount:
    print(letter,' ',count)



