# allows subclasses to have the same method but act differently
# SO"L"ID, Liskov Substitution Principle: superclass objects must be replaceble objects of a superclass
# should be replaceable with objects of its subclasses without breaking the application

from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, message):
        self.message = message

    @abstractmethod
    def send(self) -> bool: ...  # Type Hinting


class EmailNotification(Notification):
    def send(self):
        print(f'Email: sending "{self.message}"')
        return True


class SMSNotification(Notification):
    def send(self):
        print(f'SMS: sending "{self.message}"')
        return False


def notify(notification: Notification):
    notification_sent = notification.send()
    if notification_sent:
        print("Notification sent!")
    else:
        print("Notification not sent")


email_notification = EmailNotification("Hello")
notify(email_notification)
print()

sms_notification = SMSNotification("Hello")
notify(sms_notification)
