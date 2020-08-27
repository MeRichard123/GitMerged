from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    TEXT_C = [
        ("Vim", "Vim"),
        ("EMACS", "EMACS")
    ]
    GENDER_C = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    ]
    OS_C = [
        ("Windows", "Windows"),
        ("Mac", "Mac"),
        ("Linux", "Linux")
    ]
    SPACES_C = [
        ("Tabs", "Tabs"),
        ("Spaces", "Spaces")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(
        max_length=50, blank=True, null=True, choices=GENDER_C)
    profile_image = models.ImageField(
        upload_to='profile_pic', default="default.jpg", null=True, blank=True)
    bio = models.TextField(null=True)
    tech_stack = models.CharField(max_length=500, null=True)

    editor = models.CharField(
        max_length=5, choices=TEXT_C, default=None, null=True, blank=True)
    os = models.CharField(
        max_length=10, choices=OS_C, default=None, null=True, blank=True)
    spacing = models.CharField(
        max_length=10, choices=SPACES_C, default=None, null=True, blank=True)

    likeability = models.ManyToManyField(
        User, related_name="likes", blank=True)
    blocked_by = models.ManyToManyField(
        User, related_name="blocked", blank=True)

    def __str__(self):
        return f"{self.full_name} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_image.path)

        if img.height > 200 or img.width > 200:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)

    @property
    def num_likes(self):
        return self.likeability.all().count()
