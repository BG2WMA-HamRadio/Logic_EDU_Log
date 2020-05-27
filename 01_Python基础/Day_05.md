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
  **运算结果：**如果 m>n，输出`M 更大`，反之输出为`N 更大`。

