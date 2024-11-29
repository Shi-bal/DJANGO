from django.db import models
from twilio.rest import Client
from decouple import config

# Load credentials from .env
account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
print(f"Account SID length: {len(account_sid)}")  # Should be 34 characters
print(f"Auth token length: {len(auth_token)}")    # Should be 32 characters

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Example: Sending a message
message = client.messages.create(
    body="Hello from Django!",
    from_='+17753209120',  # Replace with your Twilio number
    to='+639489625940'      # Replace with the recipient's number
)

print(f"Message sent! SID: {message.sid}")

import os  # For accessing environment variables

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):  # Corrected method name
        return self.name

    def save(self, *args, **kwargs):  
        account_sid = "ACa038f99ab18470ef3b8f44012ec6cfe1"
        auth_token = "8efdbbb6f6666cfd30fa9071a6ba35fc"

        client = Client(account_sid, auth_token)

        if self.score >= 70:
            message = client.messages.create(
                body="Congratulations!",
                from_="+17753209120",
                to="+639489625940",
            )
        else:
            message = client.messages.create(
                body="Sorry! Try again",
                from_="+17753209120",
                to="+639489625940",
            )

        print(f"Message sent: {message.sid}")
        super().save(*args, **kwargs)