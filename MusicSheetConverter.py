import_filename1 = "sheet1"
import_filename2 = "sheet2"
export_filename  = "song"
number_of_notes = 256

# ----------------------------------------
import_file1 = import_filename1 + ".txt"
import_file2 = import_filename2 + ".txt"
export_file  = export_filename  + ".mif"

# Pitch table
pitch = {
    "p"    : "00000",
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
    "1"    : "11111",
}

# Length table
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


notes1 = []
current_line1 = 1
error_line1 = []

notes2 = []
current_line2 = 1
error_line2 = []

try:
    with open(import_file1, "r") as sheet1:
        for note in sheet1.readlines():
            if note == "\n" or "#" in note:
                current_line1 += 1
            elif note[0:2] not in length or note[2:-1] not in pitch:
                error_line1.append(current_line1)
                current_line1 += 1
            else:
                notes1.append(length[note[0:2]] + pitch[note[2:-1]])
                current_line1 += 1
except FileNotFoundError:
    print(f"無法找到{import_file1}，請確定第1行檔名")

try:
    with open(import_file2, "r") as sheet2:
        for note in sheet2.readlines():
            if note == "\n" or "#" in note:
                current_line2 += 1
            elif note[0:2] not in length or note[2:-1] not in pitch:
                error_line2.append(current_line2)
                current_line2 += 1
            else:
                notes2.append(length[note[0:2]] + pitch[note[2:-1]])
                current_line2 += 1
except FileNotFoundError:
    print(f"無法找到{import_file2}，請確定第2行檔名")



if not error_line1 or not error_line2:
    with open(export_file, mode="w") as song:

        # Informations
        song.write("WIDTH=8;\n")
        song.write(f"DEPTH={number_of_notes};\n")
        song.write("\n")
        song.write("ADDRESS_RADIX=UNS;\n")
        song.write("DATA_RADIX=BIN;\n")
        song.write("\n")
        song.write("CONTENT BEGIN\n")

        # For sheet1
        for i in range(len(notes1)):
            song.write(f"    {i : <5}:{notes1[i] : >11};\n")
        if len(notes1) < number_of_notes - 1:
            song.write(f"    [{len(notes1)}..{number_of_notes//2 - 1}]  :   00000000;\n")

        # For sheet2
        for i in range(len(notes2)):
            song.write(f"    {i + number_of_notes//2 : <5}:{notes2[i] : >11};\n")
        if len(notes2) < number_of_notes - 1:
            song.write(f"    [{len(notes2) + number_of_notes//2}..{number_of_notes - 1}]  :   00000000;\n")
            song.write("END;")
        else:
            song.write("END;")
else:
    print(f"請檢察{import_file1}的以下行數：")
    print(*error_line1, sep='\n')
    print(f"請檢察{import_file2}的以下行數：")
    print(*error_line2, sep='\n')
    print("請確定樂譜裡：")
    print("1. 音符是否輸入正確(對照音高與音長對照表)")
    print("2. 只有換行符號(or Enter鍵)或含 # 的留言")
