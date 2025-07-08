from django.db import models

class Topic(models.Model):
    """Learning topic the user created"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return the model in string format"""
        return self.text
    
class Entry(models.Model):
    """Something specific about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # topic 是 ForeignKey 的实例
    text = models.TextField() # text 是 TextField 的实例，不限制条目的长度
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta: # Meta class is used to define metadata for the model
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Return the model in string format"""
        return f"{self.text[:50]}..." if len(self.text) > 50 else self.text