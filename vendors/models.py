from django.db import models
from .manager import UserManager
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser


from rest_framework.exceptions import ValidationError
from django.core.validators import MinLengthValidator


def validate_phone_number(value):
    if not str(value).isdigit() or len(str(value)) != 10:
        raise ValidationError('Phone number must be a 10-digit number.')


def validate_rating(value):
    if not isinstance(value, int) or value < 1 or value > 5:
        raise ValidationError('Rating must be between 1 and 5.')


def validate_pan_number(value):
    if not str(value).isdigit() or len(str(value)) != 10:
        raise ValidationError('Pan number must be a 10-digit number.')


def validate_zip_code(value):
    if not str(value).isdigit() or len(str(value)) != 5:
        raise ValidationError('Zip code must be a 5-digit number.')


phone_regex = RegexValidator(
    regex=r"^\d{10}", message="10 digits NTC or NCELL number only"
)


class CustomUser(AbstractUser):
    USER_TYPES = [
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
    ]
    username = None
    email = models.EmailField(max_length=200, unique=True, null=True)
    phone_number = models.CharField(unique=True, max_length=10,validators=[phone_regex])
    otp = models.CharField(max_length=4, null=True)
    last_otp_generated = models.DateTimeField(blank=True, null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='customer')
    otp_count = models.PositiveSmallIntegerField(default = 0)
    # token = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.phone_number)

    objects = UserManager()

    def save(self, *args, **kwargs):
        # Check if user has any details filled
        if not (self.email or self.phone_number or self.otp):
            raise ValidationError("User details are required.")

        # Call the original save method
        super().save(*args, **kwargs)



# class PhoneOTP(models.Model):
#     phone = models.CharField(validators=[phone_regex], max_length=17, unique=True)
#     otp = models.CharField(max_length = 9, blank = True, null= True)
#     count = models.PositiveSmallIntegerField(default = 0)
#     last_otp_generated = models.DateTimeField(blank=True, null=True)

from django.conf import settings

class MainCategory(models.Model):
    main_category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.main_category_name

    class Meta:
        ordering = ['id']


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    img = models.ImageField(upload_to='vendors/category/', null=True)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.category_name

    def img_url(self):
        if self.img:
            return settings.MEDIA_URL + self.img.name
        return None

    class Meta:
        ordering = ['category_name']


class ServiceType(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Facility(models.Model):
    facility_name = models.CharField(max_length=255)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, related_name='facility')

    def __str__(self):
        return self.facility_name


class Vendor(models.Model):
    STATUS = [
        ('New','New'),
        ('Pending','Pending'),
        ('Verified','Verified'),
    ]
    cover_photo = models.ImageField(blank=True, null=True)
    company_name = models.CharField(max_length=255, validators=[MinLengthValidator(3)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='vendors')
    contact_number = models.BigIntegerField(validators=[validate_phone_number], unique=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ratings = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    vendor_status = models.CharField(max_length=10, choices=STATUS, default='New')
    available = models.BooleanField(default=False, choices=[(True, 'Available'), (False, 'Not Available')])
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='vendor')
    website = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=200)
    email = models.EmailField(unique=True, max_length=100, null=True, blank=True)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    # location = PointField(blank=True, null=True)
    # service_types = models.ManyToManyField(ServiceType)
    # subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='vendors', null=True)
    # emergency_contact = models.BigIntegerField(validators=[validate_phone_number], null=True)
    # service_days = models.TextField(null=True)
    # service_start_time = models.TimeField(null=True)
    # service_end_time = models.TimeField(null=True)

    def __str__(self):
        return self.company_name
    
    def calculate_average_rating(self):
        total_rating = 0
        appointments_with_feedback = 0

        for appointment in self.appointments.all():
            try:
                feedback = appointment.feedback
                total_rating += feedback.user_rating
                appointments_with_feedback += 1
            # except Feedback.DoesNotExist:
            except:
                pass

        if appointments_with_feedback > 0:
            average_rating = total_rating / appointments_with_feedback
        else:
            average_rating = 0
        
        self.ratings = average_rating
        self.save()

    # def save(self, *args, **kwargs):
    #     if self.latitude and self.longitude:
    #         self.location = Point(self.longitude, self.latitude)
    #     super().save(*args, **kwargs)