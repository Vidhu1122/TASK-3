from django.conf import settings
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    video = models.FileField(upload_to='course_videos/', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='instructed_courses'
    )
    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='enrolled_courses',
        blank=True
    )

    def __str__(self):
        return self.title
