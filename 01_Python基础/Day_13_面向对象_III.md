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

    # 子类初始化属性的时候，会覆盖父类中的属性，所以需要将父类中的属性重新定义进来。
    # 子类属性初始化的时候，需要继承父类的哪些属性，就要初始化哪些属性，如果没有初始化，则不能调用
    def __init__(self, name, age, sex):            
        self._sex = sex
        # Animal.__init__(self, name, age)           # 调用父类中的初始化属性。但是这种方式当父类发生变化时需要进行修改。
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
- `类名.__bases__`：这个方法可以获取当前类的所有父类。
- Python是支持多继承的，我们可以为一个子类指定多个父类。
- 如无特殊需要，不要使用多重继承。


#### 多态
- 多态是面向对象的三大特性之一。
- 对象，也可以有不同的形态去呈现。
- len()函数的用法，就是多态类型的一种体验


#### 属性和方法
