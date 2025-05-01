# 字元數、單字數、行數

with open("mammoth.txt","r") as text:
    text = text.read()

# 字元數
char = len(text)
print(f"字元數:{char}")
# 單字數
word_List = text.split(" ")
words = len(word_List)
print(f"單字數:{words}")
# 行數
#line_count = text.readlines()  #.readlines() 是專門給「檔案物件」用的，不是給「字串」。 ---->text 是一個字串（你已經 text = f.read() 過了），
line_count = text.splitlines()
lines = len(line_count)
print(f"行數:{lines}")