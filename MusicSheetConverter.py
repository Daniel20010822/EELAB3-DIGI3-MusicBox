# 音高對照表
pitch = {
    "p" : "00000",
    "so<"  : "00001",
    "so+<" : "00010",
    "la<"  : "00011",
    "la+<" : "00100",
    "si<"  : "00101",
    "do"   : "00110",
    "do+"  : "00111",
    "re"   : "01000",
    "re+"  : "01001",
    "mi"   : "01010",
    "fa"   : "01011",
    "fa+"  : "01100",
    "so"   : "01101",
    "so+"  : "01110",
    "la"   : "01111",
    "la+"  : "10000",
    "si"   : "10001",
    "do>"  : "10010",
    "do+>" : "10011",
    "re>"  : "10100",
    "re+>" : "10101",
    "mi>"  : "10110",
    "fa>"  : "10111",
    "fa+>" : "11000",
    "so>"  : "11001",
    "so+>" : "11010",
    "la>"  : "11011",
    "la+>" : "11100",
    "si>"  : "11101",
    "do>>" : "11110",
    "11"   : "11111",
    # "1"    : "11111",
}

# 音長對照表
length = {
    "32": "000",
    "16": "001",
    "08": "010",
    "04": "011",
    "02": "100",
    "2.": "101",
    "01": "110",
    "11": "111",
}


with open("sheet.txt", "r") as sheet:
    notes = []
    try:
        for note in sheet.readlines():
            if note == "\n" or "#" in note: continue
            else: notes.append(length[note[0:2]] + pitch[note[2:-1]])
    except KeyError:
        print("讀取樂譜時發生錯誤！")
        print("請確定樂譜裡：")
        print("1. 音符是否輸入正確(對照音高與音長對照表)")
        print("2. 換行符號(or Enter鍵)")
        print("3. 含 # 的留言")


with open("song.mif", mode="w") as song:
    song.write("WIDTH=8;\n")
    song.write("DEPTH=256;\n")
    song.write("\n")
    song.write("ADDRESS_RADIX=UNS;\n")
    song.write("DATA_RADIX=BIN;\n")
    song.write("\n")
    song.write("CONTENT BEGIN\n")

    for i in range(len(notes)):
        song.write("    {addr}    :    {value};\n".format(addr=i, value=notes[i]))

    if len(notes) < 255:
        song.write("    [{num}..255]    :    00000000;\n".format(num=len(notes)))
        song.write("END;")
    else:
        song.write("END;")

