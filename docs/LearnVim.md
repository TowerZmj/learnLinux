# vim 相关操作记录

## 1. 一般模式

### 1.1 光标移动

#### 1.1.1 前后左右键

* h或左箭头键——光标向左移动一个字符
* j或下箭头键——光标向下移动一个字符
* k或上箭头键——光标向上移动一个字符
* l或右箭头键——光标向右移动一个字符

#### 1.1.2 页移动

* [ctrl] + [f] ——屏幕向下移动一页，相当于 [Page Down]键
* [ctrl] + [b] ——屏幕向上移动一页，相当于 [Page Up]键
* [ctrl] + [d] ——屏幕向下移动半页
* [ctrl] + [u] ——屏幕向上移动半页

#### 1.1.3 其余移动

* +——光标移动到非空格符的下一行
* -——光标移动到非空格符的上一行
* n<sapce> ——光标向右移动这一行的n个字符
* 0或功能键 [Home] ——移动到这一行的最前面字符处
* $或功能键 [End] ——移动到这一行的最后面字符处
* H ——光标移动到这个屏幕的最上方的那一行的第一个字符
* M ——光标移动到这个屏幕的中央那一行的第一个字符
* L ——光标移动到这个屏幕的最下方那一行的第一个字符
* G ——移动到这个文件的最后一行
* nG ——移动这个文件的第n行
* gg ——移动到这个文件的第一行
* N[enter] ——光标向下移动n行

### 1.2 整行删除

* dd ——删除光标所在的那一整行
* ndd ——删除光标所在的向下n行（包含光标所在行）
* d1G ——删除光标所在行到第一行的所有数据（包含光标所在行）
* dG ——删除光标所在行到最后一行的所有数据
* d$ ——删除光标所在处到该行的最后一个字符
* d0 ——删除光标所在处到该行的最前面的一个字符
* *配合光标移动相关的字符，可进行删除操作

### 1.3 整行复制

* yy ——复制光标所在的那一整行
* nyy ——复制光标所在的向下n行（包含光标所在行）
* y1G ——复制光标所在行到第一行的所有数据（包含光标所在行）
* yG ——复制光标所在行到最后一行的所有数据
* y$ ——复制光标所在处到该行的最后一个字符
* y0 ——复制光标所在处到该行的最前面的一个字符

### 1.4 整行粘贴

* p ——将已复制的数据在光标下一行粘贴
* P ——将已复制的数据在光标上一行粘贴

### 1.5 两行合并

* J ——将光标所在行与下一行的数据结合成同一行

### 1.6 单一字体、字符串的删除

* x ——向后删除一个字符
* X ——向前删除一个字符
* nx ——向后删除n个字符

### 1.7 搜索、重复搜索

#### 1.7.1 搜索

* /word ——向下寻找一个名称为word的字符串
* ?word ——向上寻找一个名称为word的字符串

#### 1.7.2 重复搜索

* n ——向下重复搜索前一个查找的操作
* N ——向上重复搜索前一个查找的操作

#### 1.7.3 替换

* n1,n2s/word1/word2/g[c] ——在n1, n2行之间寻找word1这个字符串，并将该字符串替换为word2.

### 1.8 还原、继续

* u ——复原前一个操作
* [ctrl] + [r] ——重做上一个操作
* . ——重复前一个操作

### 1.9 块的选择、复制与粘贴

* v ——字符选择，会将光标经过的地方反白选择
* V ——行选择，会将光标经过的行反白选择
* [ctrl] + [v] ——块选择，可以用长方形的形式选择数据
* y ——将反白的地方复制起来
* d ——将反白的地方删除

### 1.10 保存后退出

* ZZ ——若文件没有改变，则不保存离开，若文件发生变动，则保存后离开

### 1.11 窗口分割

#### 1.11.1 多文件编辑

使用vim filename1,filename2,...可以同时打开多个文件

* :n ——编辑下一个文件
* :N ——编辑上一个文件
* :files ——列出目前这个vim的打开的所有文件

#### 1.11.2 多窗口功能

* :sp [filename] ——打开一个新窗口，如果有加filename，表示在新窗口中打开一个新文件，否则表示两个窗口为同一文件内容 
* [ctrl] + w + j或下方向键 ——按键的方法是：先按下[ctrl] 不放，再按下w后松开所有的按键，然后再按下方向键或j，则光标移动到下方的窗口
* [ctrl] + w + k或上方向键 ——同上，光标移动到上方的窗口
* [ctrl] + w + q ——同上，结束离开

## 2. 编辑模式

* i, I ——进入插入模式：i为从目前光标所在处插入；I为在目前所在行的第一个非空格符处开始插入
* a, A ——进入插入模式：a为从目前光标所在处的下一个字符处开始插入；A为从光标所在行的最后一个字符处开始插入
* o, O ——进入插入模式：o为在目前光标所在处的下一行处插入新的一行；O为在目前光标所在处的上一行插入新的一行
* r, R ——进入替换模式：r只会替换光标所在的那一个字符一次；R会一直替换光标所在的文字，直到按下[Esc]键为止

## 3. 命令行模式

* :w ——将编辑的数据写入硬盘文件中
* :w! ——若文件属性为“只读”时，强制写入该文件。
* :q ——离开vim
* :q! ——若曾修改过文件，又不想存储，使用 “!” 为强制离开不保存文件
* :wq ——将文件保存后离开
* :w [filename] ——将编辑的数据保存成另一个文件
* :r [filename] ——在编辑的数据中，读入另一个文件的数据，即将 "filename" 这个文件的内容加到光标所在行后面
* :n1,n2 w [filename]——将n1到n2的内容保存成filename这个文件
* :! command ——暂时离开vim到命令行中执行command的显示结果
* :set nu ——显示行号
* :set nonu ——取消行号