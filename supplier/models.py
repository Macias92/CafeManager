from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator, MinLengthValidator


class Supplier(models.Model):
    name = models.CharField(max_length=64,
                            validators=[MinLengthValidator(4)],
                            null=False,
                            blank=False)
    phone_regex = RegexValidator(regex=r'^[\d+]{4,15}$',
                                 message=_("Phone number must be entered in format: '00000000000000.\nUp to 15 digits allowed"))
    phone_number = models.CharField(validators=[phone_regex],
                                    max_length=17,
                                    null=False,
                                    blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-name', )

    @property
    def custom_id(self):
        return f'{self.phone_number[1:3]}-{self.name[0:2]}-{self.created_date.year}'

    def __str__(self):
        return self.custom_id
