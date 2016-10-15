### 概述
- 使用http请求后台数据返回json结果

### 一些门槛
- 设置验证：调用api时要用特定的api_key
- 上面的api_key一般是要注册之后才能生成
- 比较大型的网站的api则有更高的门槛:
- - 注册一个app用来获得token,api_key,甚至前面对应的secret

坑爹的是使用twitter的api不知为啥连接不上去...

### 联想
在官网www.jnugeek.cn项目中，就用REST的思路构造了一些api，而前端就是通过ajax请求来调用这些api
只不过上面这个api比较不同没有门槛

### Google大法好
Google有好多api！