### 异常和文件
#### 异常
- 在程序的运行过程中，不可避免会出现错误。
- 这些错误，我们称之为异常
- 异常以后的代码，都不会执行。避免后面的程序出现连锁反应。
- `try:`
  代码块（可能出现错误的语句）
- `except:`
  代码块（出现错误的处理方式）
- `else:`
  代码块（没有出现错误的处理方式）

#### 异常的传播（抛异常）
- 当在**函数**中出现了异常，如果对异常进行了处理，则异常不再继续传播。
- 如果**函数**中没有处理异常，则异常会继续向函数调用处继续传播。
- 直到异常传递到**全局作用域**，如果依然没有处理，则程序终止，并且显示异常信息。
```
def fn():

    print('我是fn')
    print(100 / 0)         #在这里故意制造了一个除0异常


def fn2():
    print('我是fn2')
    fn()

def fn3():
    print('我是fn3')
    fn2()

fn3()
```
运行时出现如下结果：
```
我是fn3         # 代码正常运行
我是fn2         # 代码正常运行
我是fn          # 代码正常运行
Traceback (most recent call last):                          # 程序出现了异常：Traceback
  File "D:/GitHub/exercies/turtle.py", line 28, in <module> # 出现异常的位置
    fn3()                                                   # 异常来源于执行fn3()
  File "D:/GitHub/exercies/turtle.py", line 26, in fn3      # 出现异常的位置fn3()
    fn2()                                                   # 异常对象来源于fn2()，并将抛给fn3()
  File "D:/GitHub/exercies/turtle.py", line 22, in fn2      # 出现异常的位置fn2()
    fn()                                                    # 异常对象来源于fn()，并抛给fn2()
  File "D:/GitHub/exercies/turtle.py", line 17, in fn       # 异常对象初始来源。
    print(100 / 0)                                          # 产生异常对象的语句
ZeroDivisionError: division by zero                         # 异常对象（通常是产生异常的原因）

Process finished with exit code 1
```

- 当程序的运行过程中出现异常，所有异常信息会被保存（封装）到一个专门的**异常对象**中
- 异常传播，实际上就是异常对象抛给调用处。
- 通常，异常对象是一个类（class）


#### 异常对象
- 如果在`except`中，不添加任何内容，则`except`会捕获所有异常 。
- 如果在`except`中，对异常对象进行处理，则只会捕获该类型的异常。
- 所有异常类的父类是`Exception()` 类
```
print('异常出现前...')

try:
    # print(b)
    print(100 / 0 )

except Exception as e:
    print('出现了异常...', e)

print('异常出现后...')
```
代码将出现的第一个异常命名,并且将异常输出。
- `finally:`无论是否出现异常，都会执行。
```
print('异常出现前...')

try:
    print('666', 666)
    # print(b)
    print(100 / 0 )

except Exception as e:
    print('出现了异常...', e)

finally:
    print('无论是否出现异常，都会执行的代码...')
    print(888)


print('异常出现后...')
```
运行后得到的结果
```
异常出现前...
666 666                           # 代码正常运行
出现了异常... division by zero     # 出现异常执行except中的代码
无论是否出现异常，都会执行的代码...  # finally: 后边的代码，不管是否出现异常，都会执行。 
888
异常出现后...
```
- 异常的整体代码块：
  ```
  try:
      代码块  # 可能出现的错误
  except ExceptionA:
      代码块  # 出现A错误给出的提示
  except ExceptionB:
      代码块  # 出现B错误给出的提示。
  except ExceptionC:
      代码块  # 出现C错误给出的提示。
      .
      .
      .
  else:
      代码块  # try语句没有出现错误时运行的语句
      
   finally:
       代码块  # 无论是否出现异常，都会执行。
  ```

#### 打开文件
- 文件（File）（Input/Output）
- 在编程里，通过Python程序来对计算机中的各种文件进行增删改查的操作。
  1. 打开文件： `open('filename.ext')`，参数为文件名或者文件所在路径。返回当前**文件对象**
  2. 对文件进行读写操作（保存）
    - `read()`**函数**将读取到的文件保存到一个**字符串**中
  3. 关闭文件`close()`。
- `with...as` 上下文处理器，可以用在很多函数，并非绑定在open()函数上。
- `with open('filename.ext') as file_object` 
  - 在`with`语句中直接使用file_object来操作文件
 
  - 退出`with`代码块后文件自动关闭，不用再写`close()`语句

#### 关闭文件
- 当获取文件对象之后，所有操作都是通过文件对象操作的。
- 通过`close()`函数关闭文件。


#### 读取文件
- 通过`read()`函数进行读取，将读取到的内容保存到一个**字符串**当中
- 通过`open()`函数打开的文件有两种：
  - 纯文本文件
  - 二进制文件（图片，音频，视频...）
- 打开**非ASCII编码**文件的时候，需要在`open()`函数中传递`encode=`编码。
```
# demo2.txt
凉州词（二首）
王之涣
黄河远上白云间，
一片孤城万仞山。
羌笛何须怨杨柳，
春风不度玉门关。


单于北望拂云堆，
杀马登坛祭几回。
汉家天子今神武，
不肯和亲归去来
```
打开demo2.txt文件需要使用如下命令：
```
try:
    with open('demo2.txt', encoding='utf-8') as f_name:
        content = f_name.read()
        print(content)
except FileNotFoundError:
    print(f'{f_name}'文件不存在)
```

- 操作文件的基本代码：

```
try:
    with open(file_name, 'a/r/w/r+') as obj:
        ...
except FileXXX:
    print(f'{file_name}' XXX)  
```


#### 较大文件的读取
- 读取较大文件的时候，不要直接使用`.read()`文件，容易出现内存溢出等错误。
- `read()`可以接收一个`size`作为参数，默认值为`-1`，会读取所有字符。
- 该参数用来指定读取的字符的数量。**每个中文字符是一个字符。**
- 可以为`size`指定一个数值，`read()`会读取指定数量的字符。
- 每一次读取的时候，都是从上一次读取结束的位置开始读取。
- 如果剩余字符的数量小于`size`，则**一次性**将剩余内容读取完毕。
```
try:
    with open(filename, encoding='utf-8') as f_name:
        # 定义一个变量保存读取结果
        file_content = ''
        # 定义一个变量指定读取的大小
        chunk = 100
        while True:
            content = f_name.read(chunk)           # 每次读取100个字符
            # 定义跳出死循环的条件
            if not content:
                break
            # print(content)
            file_content += content

except FileNotFoundError:
    print(f'{f_name}文件不存在')
else:
    print(file_content)
```
- `readline()`函数，每次读取一行文件。
- `readlines()`函数，每次读取一行文件，并将读取到的文件封装到一个列表中，类似于`file_content.append(file.readline())`
```
try:
    with open('demo2.txt', encoding='utf-8') as f_name:
        file_content = ''
        for line in f_name.readlines():          # 每次从列表中提取一行
            file_content += line

except FileNotFoundError:
    print(f'{f_name}文件不存在')

else:
    print(file_content)
```

#### 文件的写入
- write()，向文件写入内容
- 如果操作的是一个文本文件，write()文件需要传递一个**字符串**，如果需要写入其他类型的数据，需要进行类型转换。
- 打开文件的时候，要指定一个操作类型。open(file_name, 'w/w+/r/r+/a')
- 参数`r`表示已只读方式打开文件
  - 如果需要在读取的前提下进行写操作，使用`r+`作为参数。
- 参数`w`表示文件可以进行写操作。
  - 如果文件不存在会创建一个文件。
  - 如果文件存在会**覆盖**文件内容。
  - `w`不会对文件进行读取，如果需要读取，需要使用`w+`参数
- 参数`a`表示以追加的方式写入。
  - 如果文件不存在会创建一个文件
  - 如果文件存在，则在文件的结尾追加写入的文件
- `write()`函数是有返回值的，返回的是写了多少个字符。

#### 二进制文件写入
- 操作二进制文件 `open(file_name, 'rb/wb/ab')`
