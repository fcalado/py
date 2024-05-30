# Version 1.0

# Send e-mails

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

from os.path import basename
from email.message import EmailMessage
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.utils import formatdate

class EmailUtils:
    def __init__(self, 
                 recipient_list = None,
                 subject = None):
        msg = EmailMessage()

        # Configure smtp connection
        sender = 'contato@fcalado.com'
        server_ip = 'check'
        server_port = '25'

        # Instance connection
        self.server = smtplib.SMTP(server_ip, server_port)
        self.msgRoot = MIMEMultipart('related')
        self.msgRoot['Date'] = formatdate(localtime=True)
        self.msgRoot.preamble = 'E-mail sent by DSToolBox Library'
        self.msgAlternative = MIMEMultipart('alternative')
        self.msgRoot.attach(self.msgAlternative)

        # Configure the e-mail body
        self._msg = ''
        self._image_id = 1
        self._recipient_list = recipient_list
        self._subject = subject
        self._sender = sender

    def set_subject(self, recipient_list):
        self._subject = recipient_list
        return self
    
    def set_to(self, recipient_list):
        self._recipient_list = recipient_list
        return self
    
    def add_text(self, text, convert_break_like = True):
        text = text.replace('\n','<br>') if convert_break_like else text
        self._msg = "%s%s" % (self._msg, text)
        return self
    
    def add_image(self, image):
        fp = open(image, 'rb')
        msgImage = MIMEImage(fp.read())
        msgImage.add_header('Content-ID', '<image%d>' % self._image_id)
        fp.close()
        self._msg = '%s<img src="cid:image%d>' % (self._msg, self._image_id)
        self.msgRoot.attach(msgImage)
        self._image_id = self._image_id + 1
        return self
    
    def add_table(self, df):
        self.add_text(df.to_html(index=False), convert_break_like=False)
        return self
    
    def add_attach(self, file):
        with open(file, "rb") as fil:
            part = MIMEApplication(fil.read(), Name = basename(file))
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file)
            self.msgRoot.attach(part)
            return self
    
    def send(self):
        # Set parameters to send e-mail
        self.msgRoot['Subject'] = self._subject
        self.msgRoot['From'] = self._sender
        self.msgRoot['To'] = ",".join(self._recipient_list)
        msgText = MIMEText(self._msg, 'html', "utf-8")
        self.msgAlternative.attach(msgText)

        # Send the e-mail
        self.server.sendmail(
            self._sender,
            self._recipient_list,
            self.msgRoot.as_string()
        )
        self.server.quit()