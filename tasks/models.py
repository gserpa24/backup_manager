from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Backup(models.Model):
    vm_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    backup_date = models.DateTimeField(auto_now_add=True)
    execution_time = models.DurationField()
    vm_size = models.BigIntegerField()
    backup_file_path = models.CharField(max_length=500)
    success = models.BooleanField(default=True)
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Backup de {self.vm_name} - {self.backup_date.strftime('%Y-%m-%d %H:%M:%S')}"