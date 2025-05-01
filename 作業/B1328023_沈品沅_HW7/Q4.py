import re

with open("mammoth.txt","r") as text:
    text = text.read()


#(a)
print("=====(a)=====")
c_letters = re.findall(r"\bc\w+",text)  # findall(搜尋模式（Pattern）,搜尋對象)  不能空格  #\b:單字的開始，c:小寫字母 c，\w*:後面可以接 0 個或多個英文、數字或底線
print(c_letters)
#(b)
print("=====(b)=====")
c_letters = re.findall(r"\bc\w{3}\b",text)  #單字邊界開始 \b...單字邊界結束 \b
print(c_letters)
#(c)
print("=====(c)=====")
r_letters = re.findall(r"\b\w*r\b",text)    #\w*r:任意多個字母或數字，單字最後一個字母是 r
print(r_letters)
#(d)
print("=====(d)=====")
#vow_letters = re.findall(r"\b\w[aeiou]{3}\b",text) ---> 這樣整個 pattern 只能找「長度剛好 4 個字母的單字」，而且只能第2~4個字是母音！
vow_letters = re.findall(r"\b\w*[aeiou]{3}\w*\b",text) # 單字可以在任何地方（前、中、後）出現連續三個母音
print(vow_letters)