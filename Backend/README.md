# 注意：
#### 使用虚拟环境pipenv安装所有库（pipfile文件记录）
#### 使用pycharm IDE（可能需要https://www.jianshu.com/p/1d9c78efa39a修改设置）
### 暂时使用sqlite，待开发到尾声再改用mysql

## To be notice: 
图片上传后存储的目录写在了" /static/upload/{{ info.main_image  }}" 中，测试数据一并上传。方便调试与体验。
不要将idea中的workspace文件也commit了


# 当下工作(TODO)：
### 完成api post (comment order) get(dish comment) by 杨元昊。
（菜单）Item:[
 {
 "itemId":(int),
 "Name":(string),
 "Type":(string),
 "Price":(float),
 "Img_url":(string)
 },
 
### 完成web目录中，管理员的各个界面和对应的路由函数
+ index页面 （yyh）
+ Food页面 （yyh）
+ 登录页面 （yyh）
+ 订单页面 （zxx）
+ 评论页面 （zxx）


# 待完善工作：
### 自动化部署与多线程