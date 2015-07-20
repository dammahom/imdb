from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, name=None, password=None):
        if not email:
            raise ValueError('Email Required')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='items', blank=True, null=True)
    total_rate = models.IntegerField(default=0)

    def __str__(self):
        return u'%s' % self.title


class UserProfile(AbstractBaseUser):
    name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    watch_list = models.ManyToManyField(Item, related_name='user_watch')
    wish_list = models.ManyToManyField(Item, related_name='user_wish')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Comment(models.Model):
    text = models.CharField(max_length=200)
    rate = models.FloatField(default=0)
    item = models.ForeignKey(Item)
    user = models.ForeignKey(UserProfile)

    def __str__(self):
        return self.text
