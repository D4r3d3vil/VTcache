from django.db import models

class Report(models.Model):
    TYPE_CHOICES = [
        ('url', 'URL'),
        ('ip', 'IP'),
        ('domain', 'Domain'),
    ]

    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    result = models.JSONField()

    def __str__(self):
        return f"{self.date} - {self.type}"

    class Meta:
        ordering = ['-date']
