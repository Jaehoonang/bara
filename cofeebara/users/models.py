import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserManager(BaseUserManager):
    def create_user(self, user_email, user_nickname, password=None):
        if not user_email:
            raise ValueError("Users must have an email address")
        user = self.model(user_email=self.normalize_email(user_email), user_nickname=user_nickname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_email, user_nickname, password=None):
        user = self.create_user(user_email, user_nickname, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), unique=True)
    user_email = models.EmailField(unique=True)
    profile_image = models.ImageField(blank=True, null=True)

    user_nickname = models.CharField(max_length=32, unique=True)
    user_firstname = models.CharField(max_length=32, blank=True)
    user_lastname = models.CharField(max_length=32, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "user_email"
    REQUIRED_FIELDS = ["user_nickname"]

    def __str__(self):
        return f"{self.user_nickname} ({self.user_email})"

class Follow(TimeStampedModel):
    follow_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")

    class Meta:
        unique_together = ('follower', 'following')  # 중복 팔로우 방지

    def __str__(self):
        return f"{self.follower} → {self.following}"