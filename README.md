# python-cloudmusic

### V1.0 项目开始

有些网易云用户喜欢并要求网友关注自己的网易云从而增长关注度，一旦对方取关了，自己也会取关。
但是手动查找会比较繁琐，所以本人使用Python获取网易云CloudMusic所关注的和被关注的对象，查找出关注的对象不再被关注中。

本人也喜欢做这种事(偷笑)。

使用前需要先把account.ini文件里的两个值填好之后，使用python官网的idle或者eclipse，pycharm等运行main.py即可。

由于现在网易云对音乐的版权管控比较严，所以才会出现后续的功能小迭代。



#### 前提

* python3+
* idle，eclipse，pycharm
* 需要安装requests模块，pycryptodome模块
  * pip install requests
  * pip install pycryptodome [pycryptodome](https://pypi.org/project/pycryptodome/)， **pycryptodome**对Python的版本有要求：
    * It supports Python `2.6` and `2.7`, Python `3.4` and `newer`, and `PyPy`。



--------

### V2.0 重构

按照不同功能或模块进行包管理，包括登录，获取关注对象以及获取未被关注的对象。



#### V2.1 私有歌单（未整理）去重歌曲功能

收藏别人歌曲，添加到私有歌单（未整理歌单）中，然后通过该功能可以将私有歌单中已经被整理到其他公有歌单中的歌曲删除掉，避免重复整理。



#### V2.2 注销退出功能

添加注销退出网易云音乐的功能。



#### V2.3 修复bug

修复私有歌单相互去重的bug。



#### V2.4 增加自动循环删除私有歌单中的歌曲

在之前的版本中，必须手动输入两个歌单的id，进行去重，该功能过于繁琐，所以特意在V2.4版本中增加了自动的功能，原来的手动功能还是保留，用于简单的两个歌单之间的去重



#### V2.5 增加删除下架歌曲和试听歌曲

在一些未整理的私有歌单中，存在着大量的下架歌曲和试听歌曲，非会员的一般都不需要这些，所以增加了删除这些歌曲的功能。



#### V2.6 新增签到功能和刷歌功能，并修复部分bug

1、已知存留着签到功能的bug，正在修复中；

2、刷歌功能完美公布，可以适用；

3、获取粉丝接口升级，原来接口已经无效，但是该接口返回的值与实际值不一致，百思不得其解；

4、加密方式调整，原来的加密方式导致登录失败，后续操作一度阻塞；

---

### 问题：

* 使用该程序，不能长时间调用，否则会出现**高频**访问，导致查找不到，需要用动态代理才行。
* 该网易云所实现的功能并不能完全适用于所有网友，必须定制，如果有需求，可以联系我。

### core.js
```js
function d(d, e, f, g) {
        var h = {},
            i = a(16);
        console.log("1=====> " + d);
		console.log("2=====> " + e);
		console.log("3=====> " + f);
		console.log("4=====> " + g);
        return h.encText = b(d, g), h.encText = b(h.encText, i), h.encSecKey = c(i, e, f), h
    }

``

---



**打个广告：如果有人也喜欢网易云，可以关注我**

*  网易云帐号：412425870@qq.com

*  网易云地址：[木石前盟Caychen](https://music.163.com/#/user/home?id=137378260)

|                           **QQ:**                            |                        **412425870**                         |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                   **微信公众号：Cay课堂**                    | ![](https://github.com/caychen/readme/raw/master/img/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7.jpg) |
|                        **csdn博客：**                        | [http://blog.csdn.net/caychen](http://blog.csdn.net/caychen) |
|                          **码云：**                          |   [https://gitee.com/caychen/](https://gitee.com/caychen/)   |
|                         **github：**                         |   [https://github.com/caychen](https://github.com/caychen)   |
| **点击群号或者扫描二维码即可加入QQ群:[328243383(1群)](https://jq.qq.com/?_wv=1027&k=5wfhR5N)** | ![](https://github.com/caychen/readme/raw/master/img/1%E7%BE%A4.png) |
| **点击群号或者扫描二维码即可加入QQ群:[180479701(2群)](https://jq.qq.com/?_wv=1027&k=5DFkoIm)** | ![](https://github.com/caychen/readme/raw/master/img/2%E7%BE%A4.png) |