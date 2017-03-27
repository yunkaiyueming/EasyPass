# coding=utf8

import smtplib
import ConfigParser
import utils

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
from email.utils import formataddr


def send_mail_with_snapshot(content, subject='WarnNotice', snapshot_imgs='', attach_file=''):
        cf = ConfigParser.ConfigParser()
        cf.read('config.ini.bk')
        send_from = cf.get('email_account', 'send_from')
        send_pwd = cf.get('email_account', 'send_pwd')
        send_to = cf.get('email_account', 'send_to')
        send_ccs = cf.get('email_account', 'send_cc')
        send_smtp_server = cf.get('email_account', 'smtp_server')
        send_port = cf.get('email_account', 'smtp_port')
        send_tos = send_to.split(';')

        message = MIMEMultipart()
        message['From'] = Header("EasyPass机器人", 'utf-8')
        #message['To'] = Header(''接收组, 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        message.attach(MIMEText(content, 'html', 'utf-8'))

        if attach_file:
                att = MIMEText(open(attach_file, 'rb').read(), 'base64', 'utf-8')
                att["Content-Type"] = 'application/octet-stream'
                att["Content-Disposition"] = 'attachment; filename="'+attach_file+'"'
                message.attach(att)

        message = __add_snapshot_img(message, snapshot_imgs)
        try:
                server = smtplib.SMTP(send_smtp_server, send_port)
                server.login(send_from, send_pwd)
                server.sendmail(send_from, send_tos, message.as_string())
                server.quit()

                utils.record_log("send email success")
                return True
        except smtplib.SMTPException,e:
                utils.record_log("send email failed "+e.message)
                return False


def __add_snapshot_img(total_msg, snapshot_imgs):
        view_mail_msg = '<p>报警截图如下：</p>'
        i = 0
        for img_path in snapshot_imgs:
                i += 1
                view_mail_msg += '<p><img src ="cid:image' + ("%d" % i) + '"></p>'

                fp = open(img_path, 'rb')
                msgImage = MIMEImage(fp.read())
                fp.close()
                msgImage.add_header('Content-ID', '<image' + ("%d" % i) + '>')
                total_msg.attach(msgImage)

        msgAlternative = MIMEMultipart('snapshot')
        msgAlternative.attach(MIMEText(view_mail_msg, 'html', 'utf-8'))
        total_msg.attach(msgAlternative)
        return total_msg