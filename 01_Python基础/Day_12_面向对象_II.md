### 面向对象 II
#### 特殊方法
  - 手动添加属性容易遗忘，创建实例时，希望能够自动添加必需的属性。
  ```
  class Ham:
      call_sign = 'bg2wma'
       def cq(self):

          print('Hello CQ, CQ, CQ, This is %s'%self.call_sign.upper())


  my = Ham()
  my.cq()         # Hello CQ, CQ, CQ, This is BG2WMA             

  you = Ham()
  you.cq()        # Hello CQ, CQ, CQ, This is BG2WMA, 与上边的实例显示了相同的call_sign，这不是我们希望看到的。
  ```  
  - 上边代码中的问题：
    - 此时如果将类代码中的`call_sign = 'bg2wma'`注释掉，则显示TB错误`call_sign`没有提供`cq`方法的实参。
    - 可以手动通过`my.call_sign = 'bg2wma'`的方式为当前实例添加属性。
    - 在此之后，如果又增加了一个`other = ham()`，而没有添加`other.call_sign=`为实例添加属性，则依然会TB错误。
    - 通过观察，我们发现，类`Ham()`中，`call_sign`属性是必须存在的，并且针对独立实例来讲，`call_sign`又是不同的。
    
  - 为了解决特殊问题，Python在类中可以定义一些特殊方法。
  - 特殊方法形如 `__方法名__()`
    - 特殊方法不需要我们自己调用  
    - 特殊方法是在特殊的时刻调用
  - 特殊方法之`__init__()`：
  ```
  class Ham:
      def __init__(self):
          print('hello')
      def cq(self):

          print('Hello CQ, CQ, CQ, This is %s' %self.call_sign.upper())

  my = Ham()                  # hello
  my.__init__()               # hello， 说明__init__()方法不经调用即可执行
  ```
  - `__init__()`方法在生成实例的时候即产生调用。每生成一个实例就调用一次。
  ```
  class Ham:
      def __init__(self):
          print('hello')
      def cq(self):

          print('Hello CQ, CQ, CQ, This is %s' %self.call_sign.upper())

  my = Ham()                  # hello
  you = Ham()                 # hello
  other = Ham()               # hello 只要生成一个实例，__init__()方法就会调用一次
  ```
  - `__init__(self, 属性1, 属性2...属性n)` 创建实例的时候自动调用。
  - 先执行类中的代码块**并且只执行一次**，后执行`__init__`中的代码块。
  ```
  class Ham:
      def __init__(self):
          print('hello')
      print('现在执行类中的代码...')
      def cq(self):
          print('Hello CQ, CQ, CQ, This is %s' %self.call_sign.upper())

  my = Ham()
  you = Ham()
  other = Ham()
  # 结果如下
  # 现在执行类中的代码...
  # hello
  # hello
  # hello
  # 说明Python先执行了类中的代码，并且只执行一次，然后才执行__init__()方法。
  ```
  - `__init__()`方法的作用：
  ```
  class Ham:
      def __init__(self, call_sign):
          self.call_sign = call_sign.upper()
      def cq(self):
          print('Hello CQ, CQ, CQ, This is %s' %self.call_sign)

  my = Ham('bg2wma')
  my.cq()              # Hello CQ, CQ, CQ, This is BG2WMA
  # 此时如果添加下列实例：
  # you = ham()          # 没有为实例添加属性，运行时出现TB错误：没有向`__init__()`方法提供实参'call_sign'
  you = ham('bh2sjs')
  you.cq()             #  Hello CQ, CQ, CQ, This is BH2SJS，显示了与my.cq()不同的结果，达到预期目的。
  ```
    
  - 类的基本结构
  ```
  class 类名([父类]):
      公共属性...
      # 对象的初始化方法
      def __init__(self, ...)
          pass
      # 其他的方法
      def method_1(self):
          pass
      def method_2(self):
          pass
      ...
  ```

#### 封装的引入
  - 尝试定义一个电台类
  ```
  class Radio():
      # 公共属性：
      is_speaker = True
      need_antenna = True
      need_grand = True
      public_name = 'radio'
      # 初始化实例私有属性：
      def __init__(self, model, brand, public_name= public_name):   # 这里public_name通过公共属性赋予
          self.public_name = public_name.upper()
          self.model = model.upper()
          self.brand = brand.upper()

      def power_on(self):
          print(self.public_name, self.model, 'Now Power ON.')

  y_991 = Radio('ft-991a', 'yaesu')
  y_991.power_on()        # RADIO FT-991A Now Power ON.
  ```
  - 这种方法出现的问题：
    - 首先，公共属性中的`public_name =`的值 `'RADIO'`可以通过`y_991a.public_name = ''`这种方式随意修改
    - 公共属性中的所有属性值都可以改成任意值，甚至是不合法的值。
    
  - 所以需要一种方式来增强数据的安全性。
    - 属性不能**随意修改**。
    - 属性不能改为**任意值**。


#### 封装
  - 封装是面向对象的三大特性之一
  - 封装就是指隐藏对象中的一些不希望被外部访问到的属性或方法。
  - 实现的方法：将对象的属性名 修改为一个外部不知道的名字  
  ```
  class Radio():
      # 公共属性：
      is_speaker = True
      need_antenna = True
      need_grand = True
      public_name = 'radio'
      def __init__(self, model, brand, public_name = public_name):
          self.hidden_public_name = public_name    # 通过修改，实现隐藏该属性的目的。
          self.model = model.upper()
          self.brand = brand.upper()

      def power_on(self):
          print(self.hidden_public_name, self.model, 'Now Power ON.') # 在方法中调用隐藏的属性名，用以防止无意的修改。

  y_991 = Radio('ft-991a', 'yaesu')
  y_991.public_name = 'green'
  y_991.power_on()        # RADIO FT-991A Now Power ON.
  ```
  - 这是一种比较弱的封装方式，通常是用来提示其他编程者不要对相应属性进行修改。
    
  - 如果需要修改属性，我们要提供一个getter()和setter()方法，使外部可以访问到属性并修改。
  - getter(self)方法，用来获取对象的属性值
  - seeter(self, name)方法用来修改对象的属性值  
  ```
  class Radio():
      # 公共属性：
      is_speaker = True
      need_antenna = True
      need_grand = True
      public_name = 'radio'
      def __init__(self, model, brand, public_name = public_name):
          self.hidden_public_name = public_name    # 通过修改，实现隐藏该属性的目的。
          self.model = model.upper()
          self.brand = brand.upper()
      # 这个方法用来获取实例对象的public_name属性值。
      def get_public_name(self):
          return self.hidden_public_name
      # 这个方法用来修改实例对象的public_name属性值。
      def set_public_name(self, new_public_name):
          self.hidden_public_name = new_public_name

      def power_on(self):
          print(self.hidden_public_name, self.model, 'Now Power ON.') # 在方法中调用隐藏的属性名，用以防止无意的修改。
      def 
  y_991 = Radio('ft-991a', 'yaesu')
  print(y_991.get_public_name())    RADIO
  y_991.set_public_name('HF RADIO')
  y_991.power_on()        # HF RADIO FT-991A Now Power ON. 实例y_991的public_name被修改成‘HF RADIO’
  ```
  
  - 使用封装，确实增加了类的定义的复杂程度，但是它也确保了数据的安全
    - 隐藏属性名，使调用者无法随意的修改对象中的属性
    - 增加了getter()和setter()方法，很好的控制属性是否是只读的。
    - 使用setter()方法设置属性，可以增加数据的验证，确保数据是正确的
    ```
    class Radio():
        # 公共属性：
        is_speaker = True
        need_antenna = True
        need_grand = True
        public_name = 'radio'
        def __init__(self, model, brand, power, public_name = public_name):
            self.__public_name = public_name.upper()
            self.__power = power
            self.model = model.upper()
            self.brand = brand.upper()
        # 这个方法用来获取实例对象的public_name属性值。
        def get_public_name(self):
            return self.__public_name
        # 这个方法用来修改实例对象的public_name属性值。
        def set_public_name(self, public_name):
            self.__public_name = public_name

        def get_power(self):
            return self.__power

        def set_power(self, power):
            if power > 0:          # 增加了属性验证
                self.__power = power
        def power_on(self):
            print(self.__public_name, self.model, 'Now Power ON.', self.__power, 'Watt')

    y_991 = Radio('ft-991a', 'yaesu', 50)
    # print(y_991.get_public_name())
    # y_991.set_public_name('HF RADIO')
    y_991.set_power(-30)                     如果此时无意中输入了错误的值-30，则程序忽略该输入。
    y_991.power_on()
    ```
    - 使用getter()方法获取属性，使用setter（）方法修改属性的同时做一些逻辑操作。
    
  - 可以为对象的属性使用双下划线的方式来封装`__属性`来防止修改，而只能使用setter()方法进行修改。
  - 这种封装方式是一种隐藏属性。隐藏属性只能在类的内部访问，无法通过实例对象访问。
  - 隐藏属性是Python自动给属性取了另外一个名字
  - 这个名字叫`_类名__属性名`,使用这个名字可以依旧可以获取及修改。
  - 使用双下划线的属性，实际上依然可以在外部访问的，所以这种方式一般不用
  - 一般对属性进行封装都是使用`_属性`这种方式进行。
  ```
  class Radio():
      # 公共属性：
      is_speaker = True
      need_antenna = True
      need_grand = True
      public_name = 'radio'

      def __init__(self, model, brand, power, public_name=public_name):
          self._public_name = public_name.upper()
          self._power = power
          self.model = model.upper()
          self.brand = brand.upper()

      # 使用标准语法隐藏属性：'_attr'，单下划线。
      def public_name(self):
          return self._public_name

      # 这个方法用来修改实例对象的public_name属性值。
      def public_name(self, public_name):
          self._public_name = public_name

      def power(self):
          return self._power

      def power(self, power):
          if power > 0:                   
              self._power = power

      def power_on(self):
          print(self._public_name, self.model, 'Now Power ON.', self._power, 'Watt')

  y_991 = Radio('ft-991a', 'yaesu', 50)
  # print(y_991.get_public_name())
  # y_991.set_public_name('HF RADIO')
  y_991.power(30)
  y_991.power_on()
  ```
  
#### @property装饰器
  - 使用@property装饰器，来创建的只读属性，这个装饰器会将方法转换为同名的只读属性。
    ```
    class Ham:
        def __init__(self, call_sign):
            self._call_sign = call_sign


        def cq(self):
            print('Hello CQ, CQ, CQ, This is %s' % self._call_sign.upper())


    my = Ham('bg2wma')
    my.cq()
    ```
    - 使用`my.cq()`的方式不符合使用习惯，这时可以通过添加@property的装饰器，将`.cq()`方法转换为`.cq`**只读属性**
    ```
    class Ham:
        def __init__(self, call_sign):
            self._call_sign = call_sign

        @property
        def cq(self):
            print('Hello CQ, CQ, CQ, This is %s' % self._call_sign.upper())


    my = Ham('bg2wma')
    my.cq             # Hello CQ, CQ, CQ, This is BG2WMA，达到了预期目的
    ```
  
