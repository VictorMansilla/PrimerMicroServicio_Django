from django.db import models

class File(models.Model):
    original_file = models.FileField(upload_to='uploads/originals/')
    optimized_file = models.FileField(upload_to='uploads/optimized/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[('PENDING', 'Pending'), ('PROCESSING', 'Processing'), ('COMPLETED', 'Completed')],
        default='PENDING'
    )

    def __str__(self):
        return f"File {self.id}: {self.status}"
