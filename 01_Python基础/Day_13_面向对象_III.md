### 面向对象 III

#### 继承的简介
- 继承也是面向对象的三大特性之一。
  - 让类与类之间产生了关系，有了这层关系才有我们后续要说的多态。
  - 提高了代码的复用性。
  ```
  # 描述一个医生的类
  class Doctor():
      name = ''
      age = ''

      def study(self):
          print('治病救人')

  # 描述一个士兵的类
  class Soldier():
      name = ''
      age = ''

      def study(self):
          print('保家卫国')
  ```
  - 通过观察，我们可以发现，很多事物具有共同的属性，在这种情况下，我们可以对相同的属性单独描述。这就产生了类的继承。
  
- 继承的引入
  ```
  # 这是一个动物类
  class Animal:

      def sleep(self):
          print('动物可以睡觉...')

      def run(self):
          print('动物可以跑')
  ```
  - 定义一个具有相同特性的类有三个方法：
  - 第一个想法是在父类上修改，然后添加上子类所独有的功能。
    - 这样的方法比较繁琐，并且违反了OCP原则。
  - 第二个思路是重新创建一个类。
    - 创建一个新的类，创建和维护，都比较麻烦，会出现大量的重复代码。
  - 第三种思路就是直接从父类中**继承**他的属性和方法。
  ```
  class Dog(Animal):
      def watch_home(self):
          print('Woof....')

    d = Dog()
    d.run()          # 动物可以跑。 狗类中并没有run方法的代码，但依然可以调用Animal类中的方法。
    d.watch_home     # Woof...     在狗类中自定义的方法依然可以运行。
    r = isinstance(d, Dog)      # 检查d是否是Dog的实例
    r1 = isinstance(d, Animal)  # 检查d是否是Animal的实例
    print(r, r1)                # True True，说明， d既是Dog的实例，同时也是Animal的实例。
  ```
  - 在定义类的时候，可以在类的括号中指定类的父类（超类，基类）。
    - 通过继承，我们可以使一个类获得其他类的属性和方法。
  
  - 在创建类的时候，如果省略父类，则默认父类为object，object是所有类的父类。
    - 检查一个类是不是另外一个类的子类： `issubclass(子类，父类)`，返回 `True` 或者 `False`。
    ```
    r = issubclass(Dog, Animal)
    r1 = issubclass(Dog, object)
    r2 = issubclass(Animal, object)

    print(r, r1, r2)   # True True True
    ```
  
#### 方法重写
- 如果子类和父类出现同样（重名）的方法，子类实例调用类中的方法时会调用子类中的方法而不是父类中的方法。。
- 这个特点我们称之为方法重写（覆盖）。
```
class Animal:

    def sleep(self):
        print('动物可以睡觉...')

    def run(self):
        print('动物可以跑')


class Dog(Animal):

    def run(self):
        print('狗可以跑')


    def watch_home(self):
        print('Woof...')

d = Dog()
d.run()                # 狗可以跑... 说明调用了Dog()类里边的方法——找近的
```
- 当我们调用一个对象的方法时：
  - 会优先在当前对象中是否具有该方法，如果有则直接调用
  - 如果没有，则去当前类的父类中寻找，如果父类中有，则调用父类中的方法
  - 如果没有，继续向上寻找，直至`object`类，如果依然没有则报错。


#### super()
- 父类中所有的方法都会被继承，包括特殊方法。
- 在子类中希望直接调用父类的特殊方法。
```
# 定义一个动物父类
class Animal(object):
    def __init__(self, name, age):
         self._name = name
         self._age = age

    def sleep(self):
        print('动物可以睡觉...')

    def run(self):
        print('动物可以跑')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > 0:
            self._name = name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if age > 0:
            self._age = age


class Dog(Animal):

    # 初始化子类属性，相当于重写了父类的初始化属性（__init__()）。
    # 需要继承父类的哪些属性，就要初始化哪些属性，如果没有初始化，则不能调用
    def __init__(self, name, age, sex):            
        self._sex = sex
        # 调用父类中的初始化属性。但是这种方式当父类发生变化时需要进行修改。
        # 比如，class Dog(Animal)修改为 class Dog(Canis)，那么下边的语句就需要进行相应的修改。
        # Animal.__init__(self, name, age)           
        # 使用super直接指代父类，无论父类修改成什么都会去继承当前父类的属性。注意super后边跟括号。
        super().__init__(name, age)
   
    def run(self):
        print('狗可以跑')

    def watch_home(self):
        print('Woof...')

    @property
    def sex(self):
        return self._sex.upper()

    @sex.setter
    def sex(self, sex):
        if len(sex) > 0:
            self._sex = sex

d = Dog('胡来', 6, 'male')
print(d.name)                 # 通过super调用了父类的方法
d.name = 'Love Me'            # 通过super调用了父类中的setter
print(d.name)            
print(d.age)                  # 通过super调用父类的方法
print(d.sex)                  # 调用子类的方法
```
- 用法`super.__init__(父类中的属性1, 父类中的属性2...)`直接在子类中初始化父类包含的属性。
- 通过`super`不需要传递`self`。
- `super`代表当前类的父类。

#### 多重继承
```
# 一个多重继承的例子
class A(object):
    def test1(self):
        print('A...')

class B(object):
    def test2(self):
        print('B...')


class C(A, B):     # C 先继承A，再继承B
    pass

c = C()
c.test1()       # A... 继承了A中的方法。
c.test2()       # B... 继承了B中的方法。
```
- `类名.__bases__`：这个属性可以获取当前类的所有父类。
```
r = C.__bases__     # 注意区分实例和类，这里是获取类的属性，并非获取实例的属性。
print(r)            # (<class '__main__.A'>, <class '__main__.B'>)，返回一个元组，列出当前类的所有父类（不包括object）
```
- Python是支持多继承的，我们可以为一个子类指定多个父类。
- 如果多个父类中出现同名的方法，则会先在第一个父类中寻找，然后再到第二个父类中寻找，以此类推。
- 逻辑关系比较复杂的时候，这种继承方法会产生混乱和错误。
- 如无特殊需要，不要使用多重继承。


#### 多态
- 多态是面向对象的三大特性之一。
- 在Python中， 一个对象，也可以有不同的形态去呈现。
```
class A(object):

    def __init__(self, name):
        self._name = name


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > 0:
            self._name = name


class B(object):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > 0:
            self._name = name

wma = A('BG2WMA')
sjs = B('BH2SJS')

def cq(ham):
    print('%s Now Calling CQ...'%ham.name)

cq(wma)       # BG2WMA Now Calling CQ...
cq(sjs)       # BH2SJS Now Calling CQ...

# 这里，cq这个函数，可以同时对wma，sjs两个参数进行操作，我们称这种现象就是多态
```
- 只要实例中有`name`这个属性，`cq()`函数就可以对实例进行操作。这种形式或者说现象，就是多态。
- `len()`函数的用法，就是多态类型的一种体验。
  - 支持`len()`函数操作的对象的源码中，都会包含一个`__len__()`这个特殊方法。
  - 我们可以在自己编写的代码中添加一个`len()`方法，用来输出一个自定义的`len()`
  ```
  class B(object):

      def __init__(self, name):
          self._name = name

      def __len__(self):
          return 120
   
      @property
      def name(self):
          return self._name

      @name.setter
      def name(self, name):
          if len(name) > 0:
              self._name = name

  b = B('bg2wma')
  print(b.name)
  print(len(b))            # 120 正确的输出了我们在类中定义的__len__()方法的返回值
  ```
  - 这也就是说，多态，也是我们在程序中定义的。  
    
    
  - 不用多态的好处是，代码的`健壮性`更好，但是`通用性`较差。
  - 计算机科学中，健壮性，鲁棒性，稳健性（英语：Robustness）是指一个计算机系统在执行过程中处理错误，以及算法在遭遇输入、运算等异常时继续正常运行的能力。 诸如模糊测试之类的形式化方法中，必须通过制造错误的或不可预期的输入来验证程序的稳健性。很多商业产品都可用来测试软件系统的稳健性。稳健性也是失效评定分析中的一个方面。


#### 属性和方法
