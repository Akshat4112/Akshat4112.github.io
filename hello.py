from knockknock import email_sender

@email_sender(recipient_emails=["akshat41121995@gmail.com", "garg.ridhima72@gmail.com"], sender_email="enyasharma0@gmail.com")

def knockknock():
    import time
    time.sleep(10)
    return {'loss': 0.9}

knockknock()