## 测试简介

测试对象是服务器后端，采用白盒测试，以达到高代码覆盖率。

## 测试环境与工具

nodejs+postman

## 测试方式

- 单元测试：针对各个用例的源代码，编写测试用例，分别在测试路径和生产环境路径下进行较为简略和较为详细的测试。
- 压力测试：针对每个测试单元进行短期内超量请求的测试，以探测系统的漏洞和极限。



## 测试流程

 - 在Postman中建立一个test-collection并在其中添加相应的request

![1](https://raw.githubusercontent.com/JohnsonLeeeee/SYSU-xiaoxin-catering/master/1.PNG)
 - 在Tests中，编写测试代码,因为测试路径只有简单的不带参数的查询命令，一次只需测试返回的response code值是否为200以及响应时间是否在200ms以内即可

![2](https://raw.githubusercontent.com/JohnsonLeeeee/SYSU-xiaoxin-catering/master/2.PNG)
 - 测试结果
 
![3](https://raw.githubusercontent.com/JohnsonLeeeee/SYSU-xiaoxin-catering/master/3.PNG)
 - 选择迭代次数为500，进行压力测试，结果如下

![4](https://raw.githubusercontent.com/JohnsonLeeeee/SYSU-xiaoxin-catering/master/4.PNG)
