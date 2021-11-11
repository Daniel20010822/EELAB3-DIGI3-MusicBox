# EELAB3-DIGI3-MusicBox 樂譜轉換器

## 創作動機：
由於每輸入一個音就要對音長與音高的表，過程既無聊又繁瑣。藉此開發出簡單的樂譜對照表，可以以較直覺得方式來撰寫樂譜，不僅使用上方便許多，時間上也可以節省許多。

## 如何使用：
整份資料裡面有三份資料：
 - MusicSheetConverter.py (樂譜轉換的程式)
 - sheet.txt (轉換前的樂譜)
 - song.mif (轉換後的樂譜，一開始是不會出現的)

將這三份資料放進同一個資料夾裡，並且轉換前的樂譜命名為sheet.txt(這樣python才讀的到)
作曲完成後到創建的資料夾裡按住Shift並在視窗的任意空白處點擊右鍵，會出現"在這裡開啟PowerShell視窗"或"在這裡開啟命令視窗"
點擊完成後會出現終端機視窗，檢查目前的路徑對不對(>左邊的一大串)，確認後在指令列上輸入：
```
py MusicSheetConverter.py
```
這樣song.mif就順利做出來了。

## Sheet.txt如何撰寫：
音長 | 輸入時打
