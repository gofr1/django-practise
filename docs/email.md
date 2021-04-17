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

## Sending Multiple Mails with send_mass_mail

The method returns the number of messages successfully delivered. This is same as send_mail but takes an extra parameter; datatuple, our `sendMassEmail` view will then be:

    from django.core.mail import send_mass_mail
    from django.http import HttpResponse
    
    def sendMassEmail(request,emailto):
       msg1 = ('subject 1', 'message 1', 'polo@polo.com', [emailto1])
       msg2 = ('subject 2', 'message 2', 'polo@polo.com', [emailto2])
       res = send_mass_mail((msg1, msg2), fail_silently = False)
       return HttpResponse('%s'%res)

Let's create a URL to access our view:

    urlpatterns = [
        re_path(r'^massEmail/(?P<emailto1>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/(?P<emailto2>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})', av.sendMassEmail),
    ]

Now run `python3 -m smtpd -n -c DebuggingServer localhost:1025` and try `massEmail` url. You will get:

    ---------- MESSAGE FOLLOWS ----------
    b'Content-Type: text/plain; charset="utf-8"'
    b'MIME-Version: 1.0'
    b'Content-Transfer-Encoding: 7bit'
    b'Subject: subject 1'
    b'From: email@example.com'
    b'To: email1@example.com'
    b'Date: Sat, 17 Apr 2021 11:06:18 -0000'
    b'Message-ID: <161865757819.36903.16506557644602428840@horcrux>'
    b'X-Peer: 127.0.0.1'
    b''
    b'message 1'
    ------------ END MESSAGE ------------
    ---------- MESSAGE FOLLOWS ----------
    b'Content-Type: text/plain; charset="utf-8"'
    b'MIME-Version: 1.0'
    b'Content-Transfer-Encoding: 7bit'
    b'Subject: subject 2'
    b'From: email@example.com'
    b'To: email2@example.com'
    b'Date: Sat, 17 Apr 2021 11:06:18 -0000'
    b'Message-ID: <161865757819.36903.3320877535659351789@horcrux>'
    b'X-Peer: 127.0.0.1'
    b''
    b'message 2'
    ------------ END MESSAGE ------------

`send_mass_mail` parameters details are:

- datatuples − A tuple where each element is like (subject, message, from_email, recipient_list).
- fail_silently − Bool, if false send_mail will raise an exception in case of error.
- auth_user − User login if not set in settings.py.
- auth_password − User password if not set in settings.py.
- connection − E-mail backend.
