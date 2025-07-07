from django.db import models

class Topic(models.Model):
    """My first ever model"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return the model in string format"""
        return self.text