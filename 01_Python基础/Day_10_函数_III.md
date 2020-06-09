### 函数 III
#### 高阶函数

  - 接收函数作为参数，或者将函数作为返回值返回的函数，都是高阶函数。
  - 定义一个函数将列表中所有的偶数保存到新的列表。
  - 当使用一个函数作为参数是，就是将一段代码作为目标函数。
  ```
  lst = [n for n in range(1, 101)]                          #利用列表解析创建一个列表
  # 找到可以被2整除的数
  def fn(lst):
      #创建一个新的列表
      new_list = []
      for i in lst:
          if i % 2 == 0:
              new_list.append(i)
      return(new_list)
  
  # 找到可以被3 整除的数
  def fn1(lst):
      # 创建一个新的列表
      new_list = list()
      for i in lst:
          if i % 3 == 0
              new_list.append(i)
      return(new_list)
      
  # 找到大于50的数
  def fn2(lst):
      new_list = list()                                     # 也可以用 new_list = []
      for i in lst:
          if i > 5:
              new_list.append(i)
      return new_list
             
  ```
  - 如果需要完成多个类似功能，则需要定义多个函数。
  ```
  a = [n for n in range(1, 101)]
  def fn(lst):
      # 在函数内部定义完成功能的函数：
      def fn1(i):
          if i % 2 == 0
              return True
          return False
      .
      .
      .
      def fnx(i)
          if i > 5:
              return True
          return False
          
      new_lst = []
      for n in lst:
          if fnx:                                #这里的x用1......x代替
              new_list.append(n)
      return new_list                             # 列表作为函数的返回值
      
  print(fn(a))                                    # 调用（执行）函数
  ```
  - 为达到更加便利的使用和维护的目的，将函数做如下修改：
  ```
  a = [n for n in range(1, 101)]
  # 将内部函数移到主函数外边：
  def fn1(i):
      if i % 2 == 0
          return True
      return False
  .
  .
  .
  def fnx(i)
      if i > 5:
          return True
      return False
  def fn(func, list):
      new_list = []
      for n in lst:
          if func(n):
              new_list.append(n)
      return new_list               # 将列表作为返回值
  
  print(fn(fn1, a))
  print(fn(fn2, a))
  .
  .
  .
  print(fn(fnx, a))
  ```
  - 将函数`fnx()`作为参数传递给函数，是高阶函数的一种。
  - 实际上是将一段代码作为参数传递给函数。  
  
#### 匿名函数
  - `filter()`可以从序列中过滤出符合条件的元素，并保存到一个新的序列中。
  - 参数一，函数，根据该函数来过滤序列
  - 参数二， 需要过滤的序列
  - 返回值：过滤后的序列。
  
  ```
  
  ```
  - 匿名函数就是lambda表达式。
    - lambda函数表达式专门创建一些简单的函数，他是函数的另一种创建方式
    - 语法：lambda 参数列表：返回值
    
#### 闭包
  - 高阶函数的另一种形式，将函数作为返回值返回，那么这种形式称之为闭包。
  - 可以访问函数内部的参数。
  - 可以通过闭包可以创建一些只有当前函数才能访问的变量
  - 可以将一些私有的数据隐藏在闭包中。
  - 形成闭包的条件：
    - 1. 函数嵌套
    - 2. 将内部函数作为返回值返回
    - 3. 内部函数必须要使用到外部函数的变量。


#### 装饰器的引入
  - 可以修改函数中的代码完成这个需求，但是会产生问题
    - 如果要修改的函数过多，修改起来会比较繁琐。
    - 不方便后期维护。
    - 违反开闭原则（OCP），程序的设计要求开发对程序的扩展，要求关闭对程序的修改。
  - 可以定义一个新函数对原函数扩展。

#### 装饰器的使用
  - 通过装饰器，可以在不修改原来函数的情况下来对函数进行扩展。
  - 在开发中，我们都是通过装饰器来扩展函数的功能。
  - 用`@装饰器` 可以直接调用装饰器。不带括号
  
