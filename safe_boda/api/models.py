from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group


class CustomUser(AbstractUser):
    USER_TYPES = (
        ('Rider', 'Rider'),
        ('Driver', 'Driver'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='Rider')

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f"{self.username} ({self.user_type})"


class Trip(models.Model):
    STATUS_CHOICES = (
        ('REQUESTED', 'Requested'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    )

    rider = models.ForeignKey(
        'CustomUser', 
        on_delete=models.CASCADE, 
        related_name='rider_trips'
    )
    driver = models.ForeignKey(
        'CustomUser', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='driver_trips'
    )
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='REQUESTED')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rider.username} → {self.dropoff_location} ({self.status})"
