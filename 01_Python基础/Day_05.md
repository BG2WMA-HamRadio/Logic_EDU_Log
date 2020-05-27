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
  -[Python运算符的优先级](https://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/op_precedence.html）
  高优先级的在上，同级别优先级自左至右运算。
  |运算符|描述|
  |:---:|:---:|
  | `( )` | 括号 （分组） |
  | `f(args...)` | 函数调用 |
  | `x [index:index]` | 切片 |
  | `x [index]` | Subscription （订阅？） |
  | `x.attribute` | Attribute reference (属性参考）|
  | `**` | Exponentiation （幂） |
  | `~x` | Bitwise not （按位 否） |
  | `+x` `-x` | Positive, Negative （正，负） |
  | `*` `/` `%` | Mutilplication, division, remainder （乘，除，求余） |
  | `+` `-` | Addition, subtraction （加，减） |
  
  
