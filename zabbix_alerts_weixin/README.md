### alerts
(1)You need to turn off selinux
### usage
使用Python调用微信API可以先查阅一下官方文档，主要看“建立连接”和“发送信息”即可。

大致的通过自己企业号的CorpID和Secret来换取AccessToken，然后通过AccessToken和发送的内容（JSON）格式来发送信息。

Configure the weixin.py
```bash
    corpid = ''
    corpsecret = ''
``` 
run the weixin.py

Just run: 
```bash
python weixin.py "@all" "service" "server down"
```
