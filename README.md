技术文档

仓库地址：

https://se.jisuanke.com/edustar/super-mario

环境部署：

本项目采取 django+vue+uni—app 分别部署后端、管理 web 端、用户微信小程序端

备注：相当于大礼包+uni-app，大家如果以前用过大礼包的话强烈建议在 docker 运行之后，

进入 powershell 执行 docker rmi mariadb，即将 mariadb 镜像删除，以免数据库发生冲突，导致部署失败

进入仓库地址后，点击 project dockerenv，进行 git clone，然后在 clone 下来的文件目录中的 dockerenv 下打开 powershell 或 CMD 进行如下操作：

2.1. docker-compose build

完成后执行第二步

2.2. docker-compose run backend django-admin createsuperuser,建立超级管理员，此处须记住用户名和密码

完成后执行第三步

2.3.docker-compose run backend migrate,完成数据库表的迁移

2.4.docker-compose up 操作

 备注：如果报出 npm error 则在 powershell 里进入 dockerenv/src/frontend/frontendforh5

（和dockerenv/src/frontend/frontendforweixin） 文件目录下，分别进行

(1). npm install

(2). npm install axios

(3). npm install qs

(4). npm install vuex

（共计四步操作）

打开浏览器

输入 localhost:8080 进入管理 web 端，如见登录界面则 web 端部署成功

输入 localhost:8081 进入用户微信小程序端,如见登录界面则微信小程序端部署成功

输入 localhost:8002 进入后端，如见登录界面则后端部署成功。输入刚才注册的超级管理员的用户名密码即可进入后端。

部署脚本：

dockerfiles 文件夹里的四个文件