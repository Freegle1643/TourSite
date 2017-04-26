# 途尔旅行 一路有你
[欢迎作客！途尔，一路有你！](http://minewtour.com/)
这是一个基于Django的小众行程和游记旅行网站，用于参加[云计算应用创新大赛(Cloud Computing Application Innovation Contest)](https://cloud.seu.edu.cn/contest/index)，目前已进入全国总决赛并获得一等奖，将前往上海参加“ACM图灵奖50周年庆祝大会”颁奖典礼。
## 基本信息
本项目主要用于参加 [云计算应用创新大赛(Cloud Computing Application Innovation Contest)](https://cloud.seu.edu.cn/contest/index).
我们参加的是腾讯云命题组，作为要求，我们使用了不少腾讯云的服务，包括云虚拟机CVM，云数据库（MySQL），对象存储（COS）以及腾讯的大数据AI产品云搜，这些都是我们项目完善的关键所在。
我们做这个项目的初衷在于去创建一个让人们更深入的去体验旅途的乐趣的平台，同时方便人们互相交流，并提供了完善的交互界面方便人们去找到适合自己的行程和游记。
## 我们的团队
这些卓越的成果都要归功于我们 *候鸟* 团队的辛勤努力。我们分别是 [Freegle](https://github.com/Freegle1643)， [Chanki](https://github.com/ChankiWu)， [Hypnos](https://github.com/Hypnosx) 和 [Zhixiang](https://github.com/wuzhixiang)。
### Tech specs
Django 1.9.6
Python 2.7.9
MySQL 5.6/5.7

[Tencent Cloud(腾讯云)](https://www.qcloud.com/) 产品:
云主机 CVM Debian 3.16,
云数据库 MySQL 5.6,
对象存储 COS
云搜 Cloud Search
#### 联系我们
pearl1643@live.com
#### 使用须知
出于安全考虑，我们对数据库信息部分留空，你可以使用我们的代码来创建你的项目，但是请记得告诉我们。使用方法如下：
```Python
python manage.py migrate
python manage.py makemigrations
```
你就可以享用你的途尔了！
如果你要使用途尔作比赛或商用，请联系我们！

# TourSite
Django based touring site, using some Tencent cloud techs. We, as a team, has won the first prize in the competition mentioned below !
## Basic info
This is a project mainly used for a competition called [云计算应用创新大赛(Cloud Computing Application Innovation Contest)](https://cloud.seu.edu.cn/contest/index).
The contest is partly supported by Tencent, so we would like to use many of their cloud service including CVM, Cloud Database, COS and other AI products like 云搜(Cloud Search) to optimize the experience of our site.
Our ultimate goal is to create a website that people who enjoy traveling themselves can discover spots and routes just to fit their needs.
## Our group
All these outcomes are the fabulous results of hardworking of our group 候鸟(Passagird:meaning bird of passage). We are [Freegle](https://github.com/Freegle1643), [Chanki](https://github.com/ChankiWu), [Hypnos](https://github.com/Hypnosx) and [Zhixiang](https://github.com/wuzhixiang).
### Tech specs
Django 1.9.6
Python 2.7.9
MySQL 5.6/5.7

[Tencent Cloud(腾讯云)](https://www.qcloud.com/) Product:
CVM Debian 3.16,
Cloud Database MySQL 5.6,
COS Cloud Search (云搜)
#### Contact
pearl1643@live.com
#### Usage
For security reasons, we leave the code to connect DB blank, you can definitly use your own MySQL DB or any other compatible database to run the project. After you configure the database connection code, just by typing:
```Python
python manage.py migrate
python manage.py makemigrations
```
Then you can run your own project!
But do tell us when you use it!
