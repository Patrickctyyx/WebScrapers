import smtplib
from email.mime.text import MIMEText


# 本地好像没有这个服务
# 运行了python３ -m smtpd -n -c DebuggingServer localhost:1025
# 终端可以看到邮件，收件箱看不到...
def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'Patrick'
    msg['To'] = '873948000@qq.com'

    sender = 'Patrick'
    receiver = ['873948000@qq.com']

    s = smtplib.SMTP(host='localhost', port=1025)
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()

sendMail('Patrick is handsome!', 'Patrick loves yyx!')
