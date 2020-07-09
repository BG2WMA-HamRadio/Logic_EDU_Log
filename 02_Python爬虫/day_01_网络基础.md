## 网络传输
文中内容多来自于**中文维基**（摘抄）

## 网络传输协议
### 通信协议（Communications Protocol，也称**传输协议**）：
-在**电信**领域中指的是：在任何物理介质中允许**两个**或**多个**在传输系统中的**终端**之间传播信息的**系统标准**。  
- 也是指计算机通信或网络设备的共同语言。
- 通信协议定义了通信中的**语法学**、**语义学**和**同步规则**以及可能存在的**错误检测与纠正**。
- 通信协议在**硬件**，**软件**以及两者之间皆可实现。
- 编程语言是为了模式化的**计算**，而传输协议为了更畅通的**交流**。

### 网络传输协议（Internet Communication Protocol）
#### 网络模型
##### 开放式系统互联模型（Open System Interconnection Model, 缩写OSI，简称为**OSI模型**）
- 层次划分：
- 第七层：应用层（Application Layer）与爬虫息息相关的**HTTP/HTTPS**协议即在这一层。
  - 提供为应用软件而设置的接口，以设置与另一应用软件之间的通信。例如：HTTP, HTTPS, FTP, Telnet, SSH, SMTP, POP3等
- 第六层：表达层（Presentation Layer）（弃用）
  - 把数据转换为能与接收者的系统格式兼容并适合传输的格式。
- 第五层：会话层（Session Layer）（弃用）
  - 负责在数据传输中设置和维护计算机网络中两台计算机之间的通信连接。
- 第四层：传输层（Transport Layer）爬虫常用的TCP协议在这一层。
  - 把传输表头（HT）加至数据已形成数据包，传输表头包含了所使用的协议等发送信息。例如传输控制协议（Transport Control Protocol，简称TCP）等。
- 第三层：网络层（Network Layer）爬虫常用的IP协议在这一层。
  - 决定数据的路径选择和转寄，将网络表头（NH）加至数据包，已形成报文。网络表头包含了网络数据。例如互联网协议（Internet Protocol，简称IP）等。
- 第二层：数据链路层（Data Link Layer）
  - 负责寻址，错误侦测和改错。当表头和表尾被添加至数据包时，会形成信息框（Data Frame）
  - 数据链表头（Data Link Header, DLH）是包含了物理地址和错误侦测及改错的方法。
  - 数据链表尾（Data Link Tail, DLT）是一串指示数据包末端的字符串。
  - 例如以太网，无线局域网（Wi-Fi）和通用分组无线服务（GPRS）等。
  - 数据链路层分为两个子层：逻辑链路控制（Logical Link Control, LLC）子层和介质访问控制（Media Access Control, MAC）子层
- 第一层：物理层（Physical Layer）
  - 在局部局域网上传送数据帧（Data Frame），它负责管理电脑通信设备和网络媒体之间的互通。
  - 包括了针脚、电压、线缆规范、集线器、中继器、网卡、主机接口卡等。
    
##### TCP/IP网络模型
- 通常，人们认为OSI模型最上边的三层（应用程，表达层和会话层）在TCP/IP组中是一个**应用层**。由于TCP/IP有一个相对较弱的会话层，由TCP和RTP（实时传输协议Real-Time Transport Protocol）下打开和关闭连接组成，并且在TCP和UDP下的各种应用提供不同的端口号，这些功能能够被单个的应用程序（或者那些应用程序所使用的库）增加。
- 与此相似的是，IP是按照将它下面的网络当作一个**“黑盒子”**的思想设计的，这样在讨论TCP/IP的时候，就可以把它当作一个独立的层。  
  
|名称|English Name|主要协议| 
|:---:|:---:|:---:|  
|应用层|Application Layer|HTTP FTP DNS（如BGP和RIP这样的路由协议，尽管由于各种各样的原因它们分别运行在TCP和UDP上，仍然可以将他们看作网络层的一部分）|  
|传输层|Transport Layer|TCP UDP RTP SCTP（如OSPF这样的路由协议，尽管运行在IP上也可以看作是网络层的一部分）|  
|网络互连层|Internet Layer|对于TCP/IP来说，这是互联网协议（IP）（如ICMP和IGMP这样的协议尽管必须运行在IP上，也仍然可以看作是网络互连层的一部分；ARP不运行在IP上）|  
|网络访问（链接）层|Network Access (Link) Layer|例如以太网（Enternet）,Wi-Fi，MPLS等|  
   
- 应用层
  - 该层包括所有和应用程序协同工作，利用基础网络交换应用程序专用的数据的协议。 应用层是大多数普通与网络相关的程序为了通过网络与其他程序通信所使用的层。
  - 这个层的处理过程是**应用特有的**；数据从网络相关的程序以这种应用内部使用的格式进行传送，然后被编码成标准协议的格式。
  - 一些特定的程序被认为运行在这个层上。它们提供服务直接支持用户应用。
  - 这些程序和它们对应的协议包括HTTP（万维网服务）、FTP（文件传输）、SMTP（电子邮件）、SSH（安全远程登录）、DNS（名称<-> IP地址寻找）以及许多其他协议。
  - 一旦从应用程序来的数据被编码成一个标准的应用层协议，它将被传送到IP栈的下一层。
  - 在传输层，应用程序最常用的是TCP或者UDP，并且服务器应用程序经常与一个**公开的端口号**相联系。服务器应用程序的端口由互联网号码分配局（IANA）正式地分配。
  - 链接外部的客户端程序通常使用系统分配的一个随机端口号。监听一个端口并且通过服务器将那个端口发送到应用的另外一个副本以创建对等链接（如IRC上的dcc文件传输）的应用也可以使用一个随机端口，但是应用程序通常允许定义一个特定的端口范围的规范以允许端口能够通过实现网络地址转换（NAT）的路由器映射到内部。
  - 每一个应用层（TCP/IP参考模型的最高层）协议一般都会使用到两个传输层协议之一： 面向连接的TCP传输控制协议和无连接的包传输的UDP用户数据报文协议。 常用的应用层协议有：
  - 运行在TCP协议上的协议：  
  |协议名称|English Name|功能|
  |:---|:---:|---:|
  |HTTP|Hypertext Transfer Protocol|超文本传输协议，主要用于普通浏览。|
  |HTTPS|Hypertext Transfer Protocol over Secure Socket Layer, or HTTP over SSL|安全超文本传输协议，HTTP协议的安全版本。|
  |FTP|File Transfer Protocol|文件传输协议，用于文件传输。|
  |POP3|Post Office Protocol, version 3，|邮局协议，收邮件用。|
  |SMTP|Simple Mail Transfer Protocol|简单邮件传输协议，用来发送电子邮件。|
  |TELNET|Teletype over the Network|网络电传，通过一个终端（terminal）登陆到网络。|
  |SSH|Secure Shell|用于替代安全性差的TELNET，用于加密安全登陆用。|
  - 运行在UDP协议上的协议：  
  |协议名称|English Name|功能|
  |:---|:---:|---:|
  |BOOTP|Boot Protocol|启动协议，应用于无盘设备。|
  |NTP|Network Time Protocol|网络时间协议，用于网络同步时间。|
  |DHCP|Dynamic Host Configuration Protocol|动态主机配置协议，动态配置IP地址。|
  - 其他：  
  |协议名称|English Name|功能|
  |:---|:---:|---:|
  |DNS|Domain Name Service|域名服务，用于完成地址查找，邮件转发等工作（运行在TCP和UDP协议上）。|
  |ECHO|Echo Protocol|回绕协议，用于查错及测量应答时间（运行在TCP和UDP协议上）。|
  |SNMP|Simple Network Management Protocol|简单网络管理协议，用于网络信息的收集和网络管理。|
  |ARP|Address Resolution Protocol|地址解析协议，用于动态解析以太网硬件的地址。|
    
