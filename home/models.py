from django.db import models

# Create your models here.
class Sermon(models.Model):
    topic =models.CharField(max_length=200)
    preacher = models.CharField(max_length=100)
    date = models.DateField()
    audio_file = models.FileField(upload_to='sermons/audio/', blank=True, null=True,max_length=200)
    video_file = models.FileField(upload_to='sermons/video/', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.topic} by {self.preacher} on {self.date}"
    
    def get_audio_url(self):
        if self.audio_file:
            return self.audio_file.url
        return None
    
    def get_video_url(self):
        if self.video_file:
            return self.video_file.url
        return None 
    
