# _flower
index.html
```flow 
st=>start: 开始 
e=>end: 登录 
io1=>inputoutput: 输入用户名密码 
sub1=>subroutine: 数据库查询子类 
cond=>condition: 是否有此用户 
cond2=>condition: 密码是否正确 
op=>operation: 读入用户信息

st->io1->sub1->cond 
cond(yes,right)->cond2 
cond(no)->io1(right) 
cond2(yes,right)->op->e 
cond2(no)->io1 
```
<!-- ***
```flow
graph BT
st[注册印象笔记]-->a
a{是否已经购买马克飞象}
a-->|是|b1(您已购买马克飞象可以使用markdown语法)
a-->|否|b2(您还未能成功购买马克飞象但你可以免费试用10天)
b1-->c[欢迎使用马克飞象]
b2-->d{是否要购买马克飞象}
d-->|是|e1(您已成功购买马克飞象欢迎使用)
e1-->c[欢迎使用马克飞象]
d-->|否|e2(试用10天后将会到期欢迎购买)
``` -->