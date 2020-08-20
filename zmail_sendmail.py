# coding: utf-8

import zmail

MAIL = {

    'subject': 'sensecity_ui-master SC_UI自动化脚本',

    'content_text': 'Zmail发的邮件内容哈哈哈',

    # 'attachments': [r'D:\wjj\测试用的图片\无人脸图片\测试计划.doxc', r'D:\wjj\测试用的图片\无人脸图片\测试报告.doxc'],
    'attachments': r'D:\wjj\测试用的图片\无人脸图片\sensecity_ui-master.zip',

}

server = zmail.server('1392637260@qq.com', 'kffcwjnvddfjheff')

server.send_mail("jiaojiao_wan@126.com", MAIL)
