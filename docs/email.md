# Sending E-mails

Django comes with a ready and easy-to-use light engine to send e-mail. Similar to Python you just need an import of `smtplib`. In Django you just need to import `django.core.mail`. To start sending e-mail, edit your project `settings.py` file and set the following options:

- EMAIL_HOST − smtp server.
- EMAIL_HOST_USER − Login credential for the smtp server.
- EMAIL_HOST_PASSWORD − Password credential for the smtp server.
- EMAIL_PORT − smtp server port.
- EMAIL_USE_TLS or _SSL − True if secure connection.

F.e. for developing purpose:

    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025

Start server from terminal:

    python3 -m smtpd -n -c DebuggingServer localhost:1025

## Sending a simple E-mail

Now add view and url to appropriate files, start server and try: http://127.0.0.1:8000/simpleemail/email@example.com/. In a teminal window where you started SMTP server you will see:

    ---------- MESSAGE FOLLOWS ----------
    b'Content-Type: text/plain; charset="utf-8"'
    b'MIME-Version: 1.0'
    b'Content-Transfer-Encoding: 7bit'
    b'Subject: hello'
    b'From: email@example.com'
    b'To: email@example.com'
    b'Date: Fri, 16 Apr 2021 12:39:32 -0000'
    b'Message-ID: <165328777206.40302.8775665874151254581@machinename>'
    b'X-Peer: 127.0.0.1'
    b''
    b'world'
    ------------ END MESSAGE ------------

Here is the details of the parameters of send_mail −

- subject − E-mail subject.
- message − E-mail body.
- from_email − E-mail from.
- recipient_list − List of receivers’ e-mail address.
- fail_silently − Bool, if false send_mail will raise an exception incase - of error.
- auth_user − User login if not set in settings.py.
- auth_password − User password if not set in settings.py.
- connection − E-mail backend.
- html_message − (new in Django 1.7) if present, the e-mail will be multipart/alternative.
