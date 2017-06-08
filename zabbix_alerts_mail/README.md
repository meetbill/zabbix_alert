<p align="center">
	<img 
		style="margin-bottom: -30px"
		align="center" 
		height="70" 
		src="http://img.labnol.org/images/2008/04/gif-animation.gif">
</p>
### alerts
(1)You need to turn off selinux

### usage

#### download

```
#mkdir -p /usr/lib/zabbix/alertscripts/
#curl -o alerts.py "https://raw.githubusercontent.com/BillWang139967/zabbix_alert/master/zabbix_alerts_mail/alerts/alerts.py"
#cp alerts.py /usr/lib/zabbix/alertscripts/ 
```

#### config

配置文件已放到 /etc/zabbix/alert/alert.ini
```
[default]
# 邮件服务器地址
smtp_server = 'smtp.exmail.qq.com' 
# 邮件服务器端口(25/465)
smtp_port = 465 
smtp_user = 'xxxxx@qq.com'
smtp_pass = '*********'
# 是否开启SMTP_SSL
smtp_tls = True
# 提示信息,当接受多个报警服务器报警时，可以通过下面信息区分
smtp_info = "sc:"
```

#### test

```
#python alerts.py "test@example.com" "this is subject" "this is message"
```

#### 说明

发送邮件后，会将日志记录在 /var/log/zabbix/alert/alert.log
