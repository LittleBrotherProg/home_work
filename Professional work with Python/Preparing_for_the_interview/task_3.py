import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pwinput import pwinput

class work_email():

    def __init__(self, my_email, password):
        # SMTP - Simple Mail Transfer Protocol
        self.smtp = "smtp.gmail.com"
        # IMAP - Internet Message Access Protocol
        self.imap = "imap.gmail.com"
        self.msg = MIMEMultipart()
        self.my_email = my_email
        self.password = password

        

    def send(self, recipients, subject, message):
        self.msg["From"], self.msg['To'], self.msg['Subject'] = self.my_email, ', '.join(recipients), subject
        self.msg.attach(MIMEText(message))
        ms = smtplib.SMTP(self.smtp, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.my_email, self.password)
        ms.sendmail(self.my_email, recipients, self.msg.as_string())
        ms.quit()


    def accept(self, header):
        mail = imaplib.IMAP4_SSL(self.imap)
        mail.login(self.my_email, password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        email_message = email.message_from_string(str(data[0][1]))
        mail.logout()

    def check_email(you_email):
        if ("@" not in list(you_email)) or ( you_email.split("@")[1] not in ["gmail.com", "mail.ru", "yandex.ru"]):
            return False




if __name__ == "__main__":
    while True:
        print("Доброго времени суток. Перед началом работы с модулем потребуется ввести в консоль данные для работы с почтой")
        you_email = input('email ')
        chek_emai = work_email.check_email(you_email)
        if chek_emai == False:
            print("Не вернно введён почта.")
            continue
        password = pwinput(prompt='email password ', mask='*')
        we = work_email(you_email, password)
        while True:
            print('send or accept')
            metod = input('')
            if metod == 'send':
                text_recipients = 'Введите почту получателей письма через запятую '
                text_message = 'Введите сообщение '
                text_subject = 'Введите тему сообщения '
                recipients, subject, message = input(text_recipients), input(text_subject), input(text_message)
                we.send(recipients.split(","), subject, message)
            elif metod == 'accept':
                header = input("Введите заголовок сообщения ")
                we.accept(header)
                