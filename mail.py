# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

a='dkjdfknd'

body=str(a)

gmail_user=input("구글 계정 ID :")
gmail_pw=input('구글 계정 pass : ')
#gmail_user = 'wlsdndnjs@gmail.com'  # 실제 google 로그인할 때 쓰는 ID
#gmail_pw = 'wlsdndnjs12@'    # 실제 google 로그인할 때 쓰는 Password

from_addr = 'wlsdndnjs@gmail.com'   # 보내는 사람 주소
to_addr=input("상대방 이메일 주소")
# to_addr = 'wlsdndnjs12@naver.com'      # 받는 사람 주소

msg=MIMEMultipart('alternative')
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'Send email with Gmail'     # 제목
msg.attach(MIMEText(body, 'plain', 'utf-8')) # 내용 인코딩

    ########################
    # https://www.google.com/settings/security/lesssecureapps
    # Make sure less_secure_apps select 'use'
    ########################
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pw)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
    print('successfully sent the mail')

except BaseException as e:
    print("failed to send mail", str(e))
