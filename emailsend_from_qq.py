import smtplib
from email.mime.text import MIMEText
#登录服务器
mail_host='smtp.qq.com'
mail_user='779325519'

#开启pop3/smtp
# mail_pass='tgdscvfytvuhbchf'
#开启imap/smtp
mail_pass='qjxgfpdznszdbegb'

sender='779325519@qq.com'
receivers=['qipilangnudt@163.com']
#设置邮件内容
message=MIMEText('the future is created by what you do today not tomorrow','plain','utf-8')
message['Subject']='keep moving...'
message['From']=sender
message['To']=receivers[0]

#开始正式发送
try:
    # smtpObj=smtplib.SMTP()#设置一个SMTP对象（实例）
    # smtpObj.connect(mail_host,25)#25 为非ssl协议端口号；连接主机
    smtpObj=smtplib.SMTP_SSL(mail_host)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(
        sender,receivers,message.as_string()
        )
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print ('error',e)





