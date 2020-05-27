### 条件运算符  
  - 三元运算符  
  **注意：三元运算符并非 if - else语句**  
  **语法：**运算结果为True的返回值 `if` 运算语句 `else` 运算结果如果为False返回值  
  **例如：**
  ```
  m = float(input('输入一个数M: '))
  n = float(input('输入一个数N: '))
  
  big = ('M: ' + str(m) + ' 更大') if m > n else ('N: ' + str(n) + ' 更大')
  print(big)
  ```  
  
  **运算结果：** 如果 m>n，输出`M 更大`，反之输出为`N 更大`。  
  
### Python 运算符的优先级
    
  高优先级的在上，同级别优先级自左至右运算。
  |运算符|描述|中文描述
  |:---:|:---:|:---:|
  | `( )` |---| 括号 （分组） |
  | `f(args...)` |---| 函数调用 |
  | `x [index:index]` |---| 切片 |
  | `x [index]` | Subscription |（订阅？） |
  | `x.attribute` | Attribute reference | (属性参考）|
  | `**` | Exponentiation | （幂） |
  | `~x` | Bitwise not | （按位 否） |
  | `+x` `-x` | Positive, Negative | （正，负） |
  | `*` `/` `%` | Mutilplication, division, remainder | （乘，除，求余） |
  | `+` `-` | Addition, subtraction | （加，减） |
  | `<<` `>>` | Bitwise shifts |（移位） |
  | `&` | Bitwise AND | (按位 与） |
  | `^` | Bitwise XOR | (按位异或） |
  | `\|` | Bitwise OR  | (按位 非） |
  | `in` `not in` `is` `is not` `<` `<=` `>` `>=` `<>` `!=` `==` | Compairsons, membership, identity | 比较  成员？ 身份？ |
  | `not x` | Boolean NOT | 布尔非 |
  | `and` | Boolean AND | 布尔与 |
  | `or` | Bollean OR | 布尔或 |
  | `lambda` | Lambda expression | Lambda表达式 |
  
## 第五日 正式内容  
### 5.1 if语句
  - 定义：判断语句，条件测试，Python 根据条件测试的值为`True`或者`Flase`来决定是否执行随后的代码块，如果条件测试值为`True`则执行代码块中所有的语句。否则代码块中所有的语句都不执行。

  
  
  
