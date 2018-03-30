 ## 压缩指令和正规表达式

## 1. 压缩指令

| 后缀名   | 意义                              |
| -------- | --------------------------------- |
| *.Z      | compresss程序压缩的文件           |
| *.bz2    | bzip2程序压缩的文件               |
| *.gz     | gzip程序压缩的文件                |
| *.tar    | tar程序打包的数据，没有经过压缩   |
| *.tar.gz | tar程序打包的文件，且经过gzip压缩 |

### 1.1 compress

语法：

` compress [-d] filename `

参数说明：

-d  : 解压缩参数

compress -d 这个参数之外，也可以直接使用uncompress，意思相同

### 1.2 bzip2, bzcat

语法：

` bzip2 [-dz] filename`	<== 压缩解压缩指令

` bzcat filename.bz2`		<== 读取压缩文件内容

参数说明：

-d：解压缩指令

-z：压缩

当然，也可以使用bunzip2指令来取代bzip2 -d

### 1.3 gzip, zcat

语法：

` gzip [-d#] filename`		<==压缩解压缩指令

`zcat filename.gz `		<==读取压缩文件内容

参数说明：

-d：解压缩的参数

-#：压缩等级，1最不好，9最好，6为默认值

### 1.4 tar

语法：

` tar [-zxcvfpP] filename`

` tar -N 'yyyy/mm/dd' /path -zcvf target.tar.gz source`

参数说明：

-z：是否同时具有gzip

-x：解开一个压缩文件

-t：参看tarfile里面的文件

-c：建立一个压缩文件

-v：压缩过程中显示文件

-f：使用文件名

-p：使用原文件的原有属性

-P：可以使用绝对路径

-N：比后面接的日期（yyyy/mm/dd）还要新的文件才会被打包进新建的文件中

--exclude FILE：在压缩过程中，不要将FILE打包

## 2. 正规表示法

| 通配符     | 意义                             |
| ---------- | -------------------------------- |
| ^          | 句首字符相符                     |
| $          | 句尾相同的字符                   |
| ?          | 任何一个单一字符                 |
| *          | 随意几个任意字符                 |
| \          | 跳转符号，将特殊字符变成普通字符 |
| [list]     | 列表中的字符                     |
| [range]    | 列表中范围内的字符               |
| [^list]    | 反向选择，与[list]相反           |
| [^range]   | 反向选择，与[range]相反          |
| \\{n\\}    | 与前一个相同字连续n个            |
| \\{n, m\\} | 与前一个相同字连续n-m个          |

语法：

`grep "word" filename`

在这个文件中将关于"word"的相关的数据取出来



 







