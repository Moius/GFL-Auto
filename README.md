# GFL-Auto : 基于Python的自动化实现 #

## 注意: 本自动化目前不适用于当前版本。 以下为历史更新 ##

## 更新说明 ##

无

## 概述 ##

首先感谢GitHub上各位大佬的脚本案例为我提供了思路和方法。
脚本架构和思路来自于这个库：[少女前线8-1n双zas炸狗与收后勤脚本](https://github.com/fyypll/GirlsFrontLine)。我根据这个脚本和基于后勤计算器的自定义后勤形式对原来脚本逻辑进行了重新编写。
脚本框架基于Airtest,基本原理就是在不停的检测窗口内是否有相对应的图片。如果你不会使用AIRtest无所谓，会一点PYthon基础就行，本身脚本基于PYthon编写。
可以使用python本地环境运行，需要安装第三方库，如果你嫌麻烦，或者仅仅只是想用这个脚本可以看如下概述：

**纯新手/电脑小白？**：

新手没关系，你可以在[Airtest](https://airtest.netease.com/index.html "AIRtest使用的官方IDE")官网下载官方的IDE,里面有配置好的环境,基本够用.我在调试的时候，没用自己本地PATH运行也是可以的.

如果你对IDE的操作不甚熟悉，这里有非常亲民的[官方教程/文档](https://airtest.doc.io.netease.com/tutorial/1_quick_start_guide/)可以帮助你快速上手。

~~AIRtest真的好用~~

## 使用说明 ##

这个脚本使用起来很简单，只需要先使用IDE进行一次链接配置就可以直接使用命令行后台运行了,这里默认你至少已经阅读过airtest上手教程。个人还是建议使用命令行运行,这样可以节省一点内存.

我在每个程序中都附上了示例bat,如果还是不明白可以自己看示例bat.

目前没搞完全脱离IDE的纯py脚本.如果有这方面需求请自己查阅AIRtest文档.里面有较为详细的说明.

但是你自己要用得按照以下步骤:

1. 先使用IDE打开本程序 ****.py,同时IDE内先连接上模拟器(模拟器端口啥的在AIRtest文档里都有，如果实在没办法连上你的模拟器，可以尝试使用windows窗口捕获。)

2. 进行调试运行，可以从log日志窗口行第一行获得命令行启动代码.（你得先连接上你自己的模拟器）

3. 把代码复制到txt文件里,然后改后缀为.bat,**记得换行加个cmd** 用**管理员!!!管理员!!!**运行.

4. 这时你就会发现cmd窗口会显示“校准中，当前时间>>****”，说明脚本已经正在执行了。如果弹一直校准不要慌，他需要一个基准点进行循环统一收菜。

---

如果你使用的是后勤计算模拟器，在代码最后一行的sleep（）中的秒数改为后勤计算器中的最短收后勤时间，然后所有模拟器和命令行都可以最小化放置了。

如果你觉得两次后勤之间间隔太长，可以把倒数第二个sleep（）中的秒数适当缩短，如果太短会导致判断出错重新校准（其实问题也不大，就是会延时更长罢了）

代码简单易懂，有时间会写个注释进去，方便大家看懂，自己进行DIY RUA！~

## 免责声明 ##

本程序发布与更新等一切行为均基于学习和参考这一目的.使用者使用后对自己账号造成的任何后果均与作者无关,本程序完全开源,免费,且可任意修改与增添并发布自己的版本.

下载后使用本程序皆视为你已经阅读并接受该免责声明且愿意自行承担一切后果.

本程序基于GNU General Public License v3.0协议分发.如果你想单独发布也请基于本协议.