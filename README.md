# EELAB3-DIGI3-MusicBox 樂譜轉換器

## 創作動機：
由於每輸入一個音就要對音長與音高的表，過程既無聊又繁瑣。藉此開發出簡單的樂譜對照表，可以以較直覺得方式來撰寫樂譜，不僅使用上方便許多，時間上也可以節省許多。

## 如何使用：
整份資料裡面有四份資料：
 - MusicSheetConverter.py (樂譜轉換的程式)
 - sheet1.txt (轉換前的樂譜1)
 - sheet2.txt (轉換前的樂譜2)
 - MySong.mif (轉換後的樂譜，一開始是不會出現的)

0. 要先下載python
1. 將要轉換的兩份樂譜檔名打在MusicSheetConverter.py的第1、2行，輸出mif檔的檔名在第3行更改
2. 將MusicSheetConverter.py、sheet1.txt、sheet2.txt放入同一個資料夾裡
3. 當完成sheet1.txt與sheet2.txt的編輯後，到該資料夾的視窗按住Shift並在視窗的任意空白處點擊右鍵，會出現"在這裡開啟PowerShell視窗"或"在這裡開啟命令視窗"
4. 點擊完成後會出現終端機視窗，檢查目前的路徑對不對(>左邊的一大串)
5. 確認後在指令列上輸入：
```
py MusicSheetConverter.py
```
這樣轉換後的合併樂譜MySong.mif就順利做出來了！

## Sheet.txt如何撰寫：
### 音長對照表：
| 音長  | 輸入時打 |
| ------------- | -- |
| 32分音符      | 32 |
| 16分音符      | 16 |
| 8分音符       | 08 |
| 4分音符       | 04 |
| 2分音符       | 02 |
| 2分音符附點   | 2. |
| 全音符        | 01 |
| 結束          | 11 |

### 音高對照表：
| 音高 | 輸入時打 | 音高 | 輸入時打 | 
| ---- | ------- | ---- | ------- |
| 休止符  | p    | #La     | la+  |
| So(低)  | so<  | Si      | si   |
| #So(低) | so+< | Do(高)  | do>  |
| La(低)  | la<  | #Do(高) | do+> |
| #La(低) | la+< | Re(高)  | re>  |
| Si(低)  | si<  | #Re(高) | re+> |
| Do      | do  | Mi(高)   | mi>  |
| #Do     | do+ | Fa(高)   | fa>  |
| Re      | re  | #Fa(高)  | fa+> |
| #Re     | re+ | So(高)   | so>  |
| Mi      | mi  | #So(高)  | so+> |
| Fa      | fa  | La(高)   | la>  |
| #Fa     | fa+ | #La(高)  | la+> |
| So      | so  | Si(高)   | si>  |
| #So     | so+ | Do(高高) | do>> |
| La      | la  | 結束     | 11   |

### 單音舉例：
一個音的組合： 音長 + 音高
 * 4分音符Do：04do
 * 8分音符Mi(高)：08mi>
 * 16分音符休止：16p

### 規則：
1. 每一個音輸入一行，每個音的標註方式如上面舉例一樣
2. 檔案中除了音符外只允許留白(只有"\n"的意思)，和"#"來留言
3. 如有違反規定，程式便無法順利轉換樂譜
4. 如果樂譜超過256個音，在MusicSheetConverter.py的第4行自行更改數量即可
5. 整份樂譜結束後，輸入1111做為結束符號
6. 需留意音符後面不能有空白鍵，ex: 04do_(用底線表示空白)

sheet.txt範例可見此儲存庫
