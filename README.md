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
7. 增加新的Technique方法
8. 增加部分启发式方法，当漏洞利用失败时，能够判定失败原因对payload进行部分调整，比如xmm调整栈等
9. 对Crash部分进行大范围重构
10. 对Exploit部分进行大范围重构
11. 增加绕过ASLR，Canary，PIE的部分，主要先增加通过leak进行交互，泄露，绕过ASLR，Canary等的方法

### angrop
1. angrop中重构Gadget的分类(CallerGadget,JumpGadget,RetGadget)
2. angrop中重构RegSetter中的部分，重构RegGetter,MemSetter,MemGetter
3. angrop.roputils中增加部分execution的部分
4. 增加plthandler,syshandler等部分
5. Ropchain 部分大重构

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




