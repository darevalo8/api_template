from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


# Create your models here.


class User(AbstractUser):
    email = models.EmailField(
        _("Email Address"),
        unique=True,
        blank=True,
        null=True,
        error_messages={"unique": _("A user with that email already exist")},
    )

    def clean(self):
        super().clean()
        if self.email == "":
            self.email = None
        elif (
            self.email
            and User.objects.filter(email=self.email).exclude(pk=self.pk).exists()
        ):
            raise ValidationError(
                {"email": _("A user with that email already exists.")}
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BaseUser(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_pro")
    # phone_regex = RegexValidator(
    #     regex=r"\+?1?\d{9,15}$",
    #     message=_(
    #         "Phone number must be entered in the format: +9999999. Up to 10-15 digits allowed"
    #     ),
    # )
    # phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    # profile_image = models.URLField(_("Your profile photo"), blank=True)
    # birthday = models.DateField(_("Day of Birthday"), null=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = self.user.username
        super(BaseUser, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True
