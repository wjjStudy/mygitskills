import smtplib  # 用于建立smtp连接
from email.mime.text import MIMEText  # 邮件需要专门的MIME格式
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
from config import *


def send_email(report_file):
    # 1. 编写邮件内容（Email邮件需要专门的MIME格式）
    msg = MIMEMultipart()  # 混合MIME格式
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))  # 添加html格式邮件正文（会丢失css格式）

    # 2. 组装Email头（发件人，收件人，主题）
    msg['From'] = '1392637260@qq.com'  # 发件人
    msg['To'] = '13260597729@163.com'  # 收件人
    msg['Subject'] = Header('接口测试报告-邮件主题', 'utf-8')  # 中文邮件主题，指定utf-8编码

    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'  # filename为邮件中附件显示的名字
    msg.attach(att1)

    try:
        smtp= smtplib.SMTP('smtp.qq.com', 587)  # smtp服务器地址 使用SSL模式
        smtp.login('1392637260@qq.com', 'kffcwjnvddfjheff')  # 用户名和密码
        # smtp.login('jiaojiao_wan@126.com', 'BHBWMEZMMUPDNYST')  # 用户名和密码
        smtp.sendmail('1392637260@qq.com' , '13260597729@163.com', msg.as_string())
        # smtp.sendmail("test_results@sina.com", "superhin@126.com", msg.as_string())  # 发送给另一个邮箱
        logging.info("邮件发送完成！")
        print("邮件发送完成！")
    except Exception as e:
        print("邮件发送失败！")
        print(str(e))
        logging.error(str(e))
    finally:
        smtp.quit()

if __name__ == '__main__':
    send_email("report.html")