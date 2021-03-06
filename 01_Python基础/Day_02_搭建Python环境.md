## 第一天课程 搭建基础python环境

个人其实比较中意在Ubuntu/Debian的环境中使用Python。  
以前自学的时候也是在Linux的环境中，TUI的环境个人还是更喜欢Linux的Terminal  
Disk Operation System 的 command 用起来已经不习惯了，最近用的比较多的是PowerShell。  
  
**当然，学习还是要跟着老师走。**  

### Python 语言

  - 基本概念 Python是一种极少数能够兼具简单与功能强大的编程语言。你将惊异于发现你正在使用的这门编程语言是如此简单，
  它专注于如何解决问题，而非拘泥于语法与结构。  
  - 官方对Python的介绍：
    - Python是一款易于学习并且功能强大的编程语言。它具有高效率的数据结构，能够简单又有效地实现**面向对象**编程。
    Python简洁的语法与**动态输入**之特性，加之其解释性语言的本质，使得它称为一种在多种领域与绝大多数平台都能进行脚本编写
    与应用快速开发工作的理想语言。
    - Python的创造者吉多·范罗苏姆（Guido Van Rossum）采用BBC电视节目《蒙提·派森的飞行马戏团（Monty Python's Flying Circus，一译巨蟒剧团）》
    的名字来为这门编程语言名门。几乎所有介绍Python的书籍，以及Python官网，你都会发现一个蟒蛇的标志。
  - 希望简单但能够做比较多的事情（我个人认为他脑子中对简单的定义很诡异，这显然一点都不简单嘛！）  
  - 根据转换的时机不同，编程语言分为编译型语言和解释性语言。  
    - 编译型语言。 代表语言（C)语言。 `源码` --> `编译` --> `运行`（编译后的机器码）。优点：执行速度快。 缺点： 跨平台性能差。
    - 解释型语言。 代表语言 （Python）语言。 `源码` --> `解释器` --> `解释执行`。 优点：跨平台性好。 缺点：执行速度慢。
    
  - Python语言的特色
    - 简单易学，专注于解决问题，而并非语言本身。
    - 自由且开放。专有仓库方便安装 `pip install`
    - 跨平台。
    - 可嵌入。
    - 丰富的库。 标准库（自身携带），第三方库（比如`requests`），人生苦短，我用Python（Life is short, I use Python）。
      
  - Python的发展
    - 应用普遍性比较高，发展非常快。替Python吹牛并不是我的任务，下略......  
    
  - Python的应用
    - 常规软件开发
    - 科学计算
    - 自动化运维
    - 自动化测试
    - WEB开发
    - 网络爬虫
    - 数据分析
    - 人工智能
      
  - Python之禅
    - 在IDE中输入 import this
    - 美丽胜于丑陋（Python 以编写优美的代码为目标）
    - 明了胜于晦涩（优美的代码应该是明了的，命名规范，风格相似）
    - 简洁胜于复杂（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
    - 扁平胜于嵌套（优美的代码应该是扁平的，不能有**太多**的嵌套）
    - 间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
    - 可读性很重要（优美的代码是可读的）
    - 即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）
    - 不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写expert:pass风格地代码)
    - 当存在多种可能，不要尝试去猜测而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）
    - 虽然这并不容易，因为你不是Python之父（这里的Dutch是指Guido）
    - 做也许好过不做，但不假思索就动手还不如不做（动手之前要仔细思量）
    - 如果无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案评测标准）
    - 命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
  
#### 搭建Python环境 
  - Python解释器的种类
    - CPython （官方版本，使用C语言编写）
    - PYPY （使用Python语言编写）
    - JPython (使用Java编写）
      
  - Python的安装
    - [官方网站](https://python.org/)
    - 选择兼容性比较强的版本安装。比如3.6
    - 下载跟自己操作系统位数兼容的版本。
    - 安装的时候注意勾选add python目录到path。
    - 注意勾选pip
      
  - Python中`pip`的使用
    - 安装后使用 `python -m pip install --upgrade pip`命令升级pip  
    - 使用 `pip install ipython` 命令安装iPython
    - 使用 `pip install pandas` 命令安装pandas，快速便捷地处理结构化数据的大量数据结构和函数。
    - 使用 `pip install matplotlib` 命令安装 matplotlib，最流行的用于绘制数据图表地Python库。
    - 使用 `pip install scipy` 命令安装SciPy，一组专门解决科学计算中各种标准问题域的包的集合。
    - 使用 `pip install epd` 命令安装EPD, Enthought Python Distribution，来自Enthought的面向科学计算的安装包，包括EPDFree。
    - 使用 `pip install requests` 命令安装requests，获取网络资源必用的工具。
    - 使用 `pip install bs4` 安装Beautiful Soup，最流行的爬虫工具。  
      
  - 使用`wheel`文件安装（并不推荐）
    - 使用 `pip install wheel` 命令安装wheel。
    - 到[PythonWheel官网](https://pythonwheels.com/)下载所需的wheel文件。
    - 使用 `pip install filename.whl` 命令安装相应库。  
      
  - 换源安装
    - What ever，我们需要对某些东西保持应有的，尊重的态度。
    - 因为很多接口的原因，需要将安装源更换为国内源  
    [豆瓣](http://pypi.douban.com/simple/)  
    [阿里云](http://mirrors.aliyun.com/pypi/simple/)  
    [中科大](http://pypi.mirrors.ustc.edu.cn/simple)  
    [清华](https://pypi.tuna.tsinghua.edu.cn/simple)
      
    - 例如：`pip install packagename -i http://pypi.douban.com/simple`  
      
  - Pycharm的安装
    - 不建议使用交互模式编写程序。
    - 不要安装于过长的文件目录深度。推荐 `D:\PyCharm` 这样的目录。
    - File --> Settings --> Project : ProjectName --> Project Interpreter选择解释器，以及安装库。
    - File --> Settings --> Appearance & Behavior --> Appearance， 修改外观。
    - File --> Settings --> Appearance & Behavior --> System Settings --> Update设置自动更新。
    - File --> Settings --> Editor --> General --> Auto Import 设置自动导包。
    - File --> Settings --> Appearance & Behavior --> System Settings --> Reopen last project on Startup，设置是否自动打开上次关闭时的项目。  
    - File --> Settings --> Editor --> File and Code Templates --> Python Script， 设置头部文件。
    - File --> Settings --> Editor --> File Encodings, 将编码更改为UTF-8
    
    
  ## 本日课程结束
