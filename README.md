# TourSite
Django based touring site, using some Tencent cloud techs.
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
