##机器学习
http://www.cnblogs.com/yuxc/archive/2011/06/27/2091432.html
####nltk 自然语言处理
####scipy 算法库和数学工具包
####NumPy 几乎是一个无法回避的科学计算工具包，最常用的也许是它的N维数组对象，其他还包括一些成熟的函数库，用于整合C/C++和Fortran代码的工具包，线性代数、傅里叶变换和随机数生成函数等。NumPy提供了两种基本的对象：ndarray（N-dimensional array object）和 ufunc（universal function object）。ndarray是存储单一数据类型的多维数组，而ufunc则是能够对数组进行处理的函数。
####Matplotlib python最著名的绘图库，它提供了一整套和matlab相似的命令API
####scikit-learn 主要涵盖分类，回归和聚类算法，例如SVM， 逻辑回归，朴素贝叶斯，随机森林，k-means等算法,我们熟悉的NLTK中，分类器方面就有专门针对scikit-learn的接口，可以调用scikit-learn的分类算法以及训练数据来训练分类器模型
##[第三方库](https://github.com/vinta/awesome-python)
requests--- http请求
BeautifulSoup--- 解析网页(内容提取)
gevent--- 协程并发(greenlet)
multiprocessing--- 多线程/多进程
Tkinter———— Python默认的图形界面接口。
Pmw(Python megawidgets)Python超级GUI组件集
PyXML———— 用Python解析和处理XML文档的工具包
PyGame———— 用于多媒体开发和游戏软件开发的模块。
PyOpenGL———— 模块封装了“OpenGL应用程序编程接口”，可在程序中集成2D和3D的图形。
NumPy、NumArray和SAGE———— NumArray是Python的一个扩展库，主要用于处理任意维数的固定类型数组，简单说就是一个矩阵库
MySQLdb模块———— 用于连接MySQL数据库
PyGTK ———— 用于python GUI程序开发的GTK+库。gnome
PyQt ———— 用于python的Qt开发库。QT就是实现了KDE环境库
PyMedia ———— 用于多媒体操作的python模块
pypy ———— 一个Python代码加速度器
Python-ldap ———— 提供一组面向对象的API，可方便地在python中访问ldap目录服务，它基于OpenLDAP2.x。
smtplib模块 ———— 发送电子邮件。
ftplib模块 ———— 定义了FTP类和一些方法，用以进行客户端的ftp编程
xmpppy模块 ———— Jabber服务器采用开发的XMPP协议，Google Talk也是采用XMPP协议的IM系统。在Python中有一个xmpppy模块支持该协议。也就是说，我们可以通过该模块与Jabber服务器通信，是不是很Cool。
adodb ———— ADO数据库连接组件
bsddb3 ———— BerkeleyDB的连接组件
chardet ———— 编码检测
scons ———— 项目构建工具，写好了模板用起来还是很方便的
sendpkt ———— Python发包
setuptools ———— 一套python包管理机制
Cheetah ———— 构建和扩充任何种类的基于文本的内容
pycurl ———— URL处理工具
pydot ———— 画图的，graphiz
pyevent ———— Python的事件支持
pylint ———— 培养良好的编码习惯
pypcap ———— 抓包的
pysqlite2 ———— SQLite的连接组件
python-dnet ———— 控制网络安全的其他设备
pythonwin ———— Python的Windows扩展
pywmi ———— 省了好多折腾功夫
reportlab ———— Python操作PDF的Libary。
scapy ———— 网络包构建分析框架,可编程的wireshark,有兴趣的google “Silver Needle in the Skype”
simplejson ———— JSON的支持
sqlalchemy ———— SQL数据库连接池
SQLObject ———— 数据库连接池
cherrypy ———— 一个WEB framework
ctypes ———— 用来调用动态链接库
Cx-oracle ———— 连接oracle的工具
DBUtils ———— 数据库连接池
django ———— 一个WEB framework
DPKT ———— raw-scoket网络编程
docutils ———— 用来写文档的
dpkt ———— 数据包的解包和组包
feedparser ———— rss解析
Kodos ———— 正则表达式调试工具
Mechanize ———— 爬虫连接网站常用
pefile ———— windows pe文件解析器
py2exe ———— 用来生成windows可执行文件
twisted ———— 巨无霸的网络编程框架
winpdb ———— 自己的程序或者用别的库不太明白的时候就靠它了
wxPython ———— GUI编程框架,熟悉MFC的人会非常喜欢，简直是同一架构
PIL———— Python 的图像处理库
Pyro———— Python实现与JAVA RMI类似的技术
PLY———— 基于Python的LEX、YACC的语言工具
Corepy———— 使用Python开发编写x86汇编程序
LightCloud———— Python实现的分布式的键-值数据库
Parallel Python（PP）———— 轻松开发SMP、集群并行计算的库
####网络
Scapy: send, sniff and dissect and forge network packets. Usable interactively or as a library
pypcap, Pcapy and pylibpcap: several different Python bindings for libpcap
libdnet: low-level networking routines, including interface lookup and Ethernet frame transmission
dpkt: fast, simple packet creation/parsing, with definitions for the basic TCP/IP protocols
Impacket: craft and decode network packets. Includes support for higher-level protocols such as NMB and SMB
pynids: libnids wrapper offering sniffing, IP defragmentation, TCP stream reassembly and port scan detection
Dirtbags py-pcap: read pcap files without libpcap
flowgrep: grep through packet payloads using regular expressions
Knock Subdomain Scan, enumerate subdomains on a target domain through a wordlist
Mallory, extensible TCP/UDP man-in-the-middle proxy, supports modifying non-standard protocols on the fly
Pytbull: flexible IDS/IPS testing framework (shipped with more than 300 tests)
####调试和逆向工程
Paimei: reverse engineering framework, includes PyDBG, PIDA, pGRAPH
Immunity Debugger: scriptable GUI and command line debugger
mona.py: PyCommand for Immunity Debugger that replaces and improves on pvefindaddr
IDAPython: IDA Pro plugin that integrates the Python programming language, allowing scripts to run in IDA Pro
PyEMU: fully scriptable IA-32 emulator, useful for malware analysis
pefile: read and work with Portable Executable (aka PE) files
pydasm: Python interface to the libdasm x86 disassembling library
PyDbgEng: Python wrapper for the Microsoft Windows Debugging Engine
uhooker: intercept calls to API calls inside DLLs, and also arbitrary addresses within the executable file in memory
diStorm: disassembler library for AMD64, licensed under the BSD license
python-ptrace: debugger using ptrace (Linux, BSD and Darwin system call to trace processes) written in Python
vdb / vtrace: vtrace is a cross-platform process debugging API implemented in python, and vdb is a debugger which uses it
Androguard: reverse engineering and analysis of Android applications
Fuzzing
Sulley: fuzzer development and fuzz testing framework consisting of multiple extensible components
Peach Fuzzing Platform: extensible fuzzing framework for generation and mutation based fuzzing (v2 was written in Python)
antiparser: fuzz testing and fault injection API
TAOF, (The Art of Fuzzing) including ProxyFuzz, a man-in-the-middle non-deterministic network fuzzer
untidy: general purpose XML fuzzer
Powerfuzzer: highly automated and fully customizable web fuzzer (HTTP protocol based application fuzzer)
SMUDGE
Mistress: probe file formats on the fly and protocols with malformed data, based on pre-defined patterns
Fuzzbox: multi-codec media fuzzer
Forensic Fuzzing Tools: generate fuzzed files, fuzzed file systems, and file systems containing fuzzed files in order to test the robustness of forensics tools and examination systems
Windows IPC Fuzzing Tools: tools used to fuzz applications that use Windows Interprocess Communication mechanisms
WSBang: perform automated security testing of SOAP based web services
Construct: library for parsing and building of data structures (binary or textual). Define your data structures in a declarative manner
fuzzer.py (feliam): simple fuzzer by Felipe Andres Manzano
Fusil: Python library used to write fuzzing programs
Web
Requests: elegant and simple HTTP library, built for human beings
HTTPie: human-friendly cURL-like command line HTTP client
ProxMon: processes proxy logs and reports discovered issues
WSMap: find web service endpoints and discovery files
Twill: browse the Web from a command-line interface. Supports automated Web testing
Ghost.py: webkit web client written in Python
Windmill: web testing tool designed to let you painlessly automate and debug your web application
FunkLoad: functional and load web tester
spynner: Programmatic web browsing module for Python with Javascript/AJAX support
python-spidermonkey: bridge to the Mozilla SpiderMonkey JavaScript engine; allows for the evaluation and calling of Javascript scripts and functions
mitmproxy: SSL-capable, intercepting HTTP proxy. Console interface allows traffic flows to be inspected and edited on the fly
pathod / pathoc: pathological daemon/client for tormenting HTTP clients and servers
####取证
Volatility: extract digital artifacts from volatile memory (RAM) samples
LibForensics: library for developing digital forensics applications
TrIDLib, identify file types from their binary signatures. Now includes Python binding
aft: Android forensic toolkit
####恶意程序分析
pyew: command line hexadecimal editor and disassembler, mainly to analyze malware
Exefilter: filter file formats in e-mails, web pages or files. Detects many common file formats and can remove active content
pyClamAV: add virus detection capabilities to your Python software
jsunpack-n, generic JavaScript unpacker: emulates browser functionality to detect exploits that target browser and browser plug-in vulnerabilities
yara-python: identify and classify malware samples
phoneyc: pure Python honeyclient implementation
PDF
Didier Stevens' PDF tools: analyse, identify and create PDF files (includes PDFiD, pdf-parserand make-pdf and mPDF)
Opaf: Open PDF Analysis Framework. Converts PDF to an XML tree that can be analyzed and modified.
Origapy: Python wrapper for the Origami Ruby module which sanitizes PDF files
pyPDF: pure Python PDF toolkit: extract info, spilt, merge, crop, encrypt, decrypt…
PDFMiner: extract text from PDF files
python-poppler-qt4: Python binding for the Poppler PDF library, including Qt4 support
Misc
InlineEgg: toolbox of classes for writing small assembly programs in Python
Exomind: framework for building decorated graphs and developing open-source intelligence modules and ideas, centered on social network services, search engines and instant messaging
RevHosts: enumerate virtual hosts for a given IP address
simplejson: JSON encoder/decoder, e.g. to use Google's AJAX API
PyMangle: command line tool and a python library used to create word lists for use with other penetration testing tools
Hachoir: view and edit a binary stream field by field
py-mangle: command line tool and a python library used to create word lists for use with other penetration testing tools
####其他有用的Py库和工具
IPython: enhanced interactive Python shell with many features for object introspection, system shell access, and its own special command system
Beautiful Soup: HTML parser optimized for screen-scraping
matplotlib: make 2D plots of arrays
Mayavi: 3D scientific data visualization and plotting
RTGraph3D: create dynamic graphs in 3D
Twisted: event-driven networking engine
Suds: lightweight SOAP client for consuming Web Services
M2Crypto: most complete OpenSSL wrapper
NetworkX: graph library (edges, nodes)
Pandas: library providing high-performance, easy-to-use data structures and data analysis tools
pyparsing: general parsing module
lxml: most feature-rich and easy-to-use library for working with XML and HTML in the Python language
Whoosh: fast, featureful full-text indexing and searching library implemented in pure Python
Pexpect: control and automate other programs, similar to Don Libes `Expect` system
Sikuli, visual technology to search and automate GUIs using screenshots. Scriptable inJython
PyQt and PySide: Python bindings for the Qt application framework and GUI library
