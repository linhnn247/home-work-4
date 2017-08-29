alicefile = open('alice.txt', 'r')
##'r' : use for reading
##'w' : use for writing
##'x' : use for creating and writing to a new file
##'a' : use for appending to a file
##'r+' : use for reading and writing to the same file

count = {}

for line in alicefile:
    for word in line.split():
        # replace các thể loại dấu má
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", '')
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')

        # replace các thể loại in hoa
        word = word.lower()

        # bỏ qua số má
        if word.isalpha():
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

# sắp xếp theo chiều alphabet
keysorted = sorted(count.keys())


# lưu file dưới dạng text và có quyền viết
alicewords = open('alice_words.txt', 'w')

for word in keysorted:
    width = 20
    alicewords.write('{0: <{1}} {2}'.format(word,width,count[word])) # câu lệnh in ra 2 cột cách nhau 1 khoảng cố định
    alicewords.write('\n')

noofalice = count['alice']

print("Chữ 'alice' xuất hiện {0} cmn lần trong file text".format(noofalice))


