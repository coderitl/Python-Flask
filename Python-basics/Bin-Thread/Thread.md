### 线程

线程: 有时被称为轻量进程(Lightweight Process LWP)，是程序执行流的最小单位。一个标准的线程由线程
ID，当前指令指针(PC) 寄存器集合和堆栈组成,另外,线程是进程中的一个实体,是被系统独立调度和分排的基本单位，
线程自己不拥有系统资源,只拥有一点儿在运行中必不可少的资源,但它可与同属一个进程的其他线程共享进程所拥有的全部资源.
一个线程可以创建和撤销另一个线程,同一个进程中的多个线程之间可以并发执行。由于线程之间的相互制约,致使线程在运行中
呈现出间断性。线程也有就绪，阻塞和运行三种基本状态。

就绪状态是指线程具备运行的所有条件m逻辑上可以运行,在等待处理机；
运行状态是指线程占有处理机正在运行
阻塞状态: 阻塞状态是指线程在等待一个事件(如某个信号量),逻辑上不可执行。每一个程序都至少有一个线程，若程序
只有一个线程,那就是程序本身。


线程是程序中一个单一的顺序控制流程。程序内有一个相对独立的、可调度的执行单元.是系统独立调度和分派 CPU 的基本单位指令运行时的程序的调度
单位。在单个程序中同时运行多个线程完成不同的工作称为多线程

### 多线程:  
 多线程(multithreading) 是指从软件或者硬件上实现多个线程并发执行的技术。具有多线程能力的计算机因有硬件支持而能够
在同一时间执行多于一个线程,进而提升整体处理性能.具有这种能力的系统包括多对处理机,多核心处理器以及芯片级多处理或同时多线处理器。
在一个程序中,这些独立运行的程序片段就做 "线程"，利用它的编程的概念就叫做"多线程处理".

###  优点:
+ 使用线程可以把占据很长时间的程序中的任务放到后台去处理
+ 用户界面可以更加吸引人,这样比如用户点击了一个按钮去触发某些事件的处理,可以弹出一个进度条
来显示用户处理的进度
+ 程序的运行速度可能加快
+ 在一些等待的任务实现上如用户输入，文件读写和网络收发数据等,线程就比较有用了.这种情况下我们可以释放一些
珍贵的资源如内存占用等等