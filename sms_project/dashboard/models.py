from django.db import models
from twilio.rest import Client
import os  # For accessing environment variables

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):  # Corrected method name
        return self.name

    def save(self, *args, **kwargs):  
        account_sid = "ACd50c52da4b7f4746435ab14f098012d1"
        auth_token = "1bfdd882d093f937fd6adc995b31f6ff"

        client = Client(account_sid, auth_token)

        if self.score >= 70:
            message = client.messages.create(
            body=f"Congratulations!",
            from_="+16814323893",
            to="+639911738803",
            )

        else:
            message = client.messages.create(
            body=f"Sorry! Try again",
            from_="+16814323893",
            to="+639911738803",
            )

        print(f"Message sent: {message.sid}")
        

        # Call the parent save method
        super().save(*args, **kwargs)
