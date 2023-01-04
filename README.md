# reoxxx

[TOC]

Building...

## TODO

### rex
1. 根据my-binaries修改techniques中部分，将例子中的4-5个demo的代码跑通
2. 通过checksec的内容，增加对ASLR,Canary,PIE,RELRO等保护的判断
3. Techniques部分中增加ARM Sepcify内容，例如ABI约定等，这部分也应该在archr中修改
4. 阅读CGC插件部分的相关实现，把CGC部分有用的代码或者思想留下，其余cgc部分全部删除
5. 写出一些其他漏洞Crash类型，(IP_OVERWRITE, PARTIAL_IP_OVERWRITE, BP_OVERWRITE,PARTIAL_BP_OVERWRITE, WRITE_WHAT_WHERE, WRITE_X_WHERE)的例子
6. 增加其他Crash类型
7. 增加新的Technique方法, 目前简单想到的，格式化字符串,GOT_Overwrite,ROP等
8. 增加部分启发式方法，当漏洞利用失败时，能够判定失败原因对payload进行部分调整，比如xmm调整栈等
9. 对Crash部分进行大范围重构
10. 对Exploit部分进行大范围重构
11. 增加绕过ASLR，Canary，PIE的部分，主要先增加通过leak进行交互，泄露，绕过ASLR，Canary等的方法

### angrop
11月：跑通单次ROP能够利用的Demo,例如`/my_binaries/httpd`

1. angrop中增加Gadget的分类:
  * 分成CallerGadget(已经大部分实现),JumpGadget,RetGadget(参考CallerGadgets实现,框架已OK)
  * `block_size`动态，最好就是angr的blocksize(找到最小的  棘手)
2. angrop中重构RegSetter中的部分
  * 增加RegGetter,MemSetter,MemGetter
  * 重构ROPchain部分
3. angrop.roputils中增加部分execution的部分
  * 目前roputils中是几个非常重要的符号执行函数，但是实现的都比较简陋，需要先封装成class
  * 增加对library/syscall/syscenter等的处理逻辑不够
  * 增加plthandler,syshandler,参考实现PLTHandler(这部分需要angr支持)
4. Ropchain部分大重构

### aflqemu
1. 增加aflqemu中的交互部分，能够读取leaked的信息，实现input-output的交互

### archr
1. 重写archr,重点添加arm相关的一些特定判断，例如Thumb之类的，在Technique中也加入架构相关的代码，比如传参r0,r1,r2之类

### povsim
1. 将rex中pov部分加入到这个项目中
2. 增加Pwntools模板的生成部分，在最终生成exp时候直接生成exp.py能够直接跑

### tracer
1. 充分利用execution的功能

### fuzzer
1. 对Crash的部分，增加fuzzing的输入支持，能够将fuzzing的部分喂给Crash
2. 参考Driller(AFL+angr)的部分实现


## 测试例子
1. netgear 7000P CVE- https://github.com/grimm-co/NotQuite0DayFriday/blob/trunk/2020.06.15-netgear/
2. Tenda ac15/18 mutiple vulerability
3. Netgear upnpd stack overflow CVE-2021-27329


