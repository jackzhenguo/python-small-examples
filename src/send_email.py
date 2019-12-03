import smtplib
from email import (header)
from email.mime import (text, application, multipart)
from datetime import date, datetime
import time


def sender_mail():
    smt_p = smtplib.SMTP()  # 创建对象
    smt_p.connect(host='smtp.qq.com', port=25)  # 设置smtp服务器
    sender = '113097485@qq.com'
    password = "**********"  # 在qq邮箱设置开启SMTP服务并复制授权码到password
    smt_p.login(sender, password)  # 进行邮箱登录一次，填写你本人的邮箱
    receiver_addresses, count_num = [
        'guozhennianhua@163.com', 'xiaoxiazi99@163.com'], 1
    for email_address in receiver_addresses:
        # 表格中邮箱格式不正确，如有空字符，在发邮件的时候会出现异常报错，捕获到这些异常就跳过
        try:
            msg = multipart.MIMEMultipart()
            msg['From'] = "zhenguo"  # 设置发邮件人
            msg['To'] = email_address  # 收件人
            # msg['Cc'] = 'guozhennianhua@163.com'
            msg['subject'] = header.Header('通知', 'utf-8')  # 主题名称
            msg.attach(text.MIMEText(
                '您好！\n这是一封测试邮件，使用Python实现自动发邮件，请勿回复本邮件功能~\n\n  祝您工作愉快！', 'plain', 'utf-8'))
            xlsxpart = application.MIMEApplication(
                open(r'./data/email_test.xlsx', 'rb').read())
            xlsxpart.add_header('Content-Disposition',
                                'attachment', filename='1.xlsx')
            msg.attach(xlsxpart)  # 添加邮件的附件
            smt_p.sendmail(sender, email_address, msg.as_string())  # 发送邮件
            time.sleep(10)  # sleep10秒避免发送频率过快，可能被判定垃圾邮件。
            print('第%d次发送给%s' % (count_num, email_address))
            count_num = count_num + 1
        except Exception as e:
            print('第%d次给%s发送邮件异常' % (count_num, email_address))
            continue
    smt_p.quit()


sender_mail()
