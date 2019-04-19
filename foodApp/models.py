import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    YES = 'Y'
    NO = 'N'
    CHOICES = (
        (YES, 'Y'),
        (NO, 'N'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14, unique=True, null=False)
    address = models.TextField()
    volunter = models.CharField(max_length=1, choices=CHOICES,
                                default=NO)
    avaliable = models.CharField(max_length=1, choices=CHOICES,
                                 default=NO)

    def __str__(self):
        return self.user.username

    def get_profile_url(self):
        return reverse('profile_edit', kwargs={'pk': self.pk})


class FoodRequest(models.Model):

    REQUESTED = 'REQ'
    PROCESSING = 'PRO'
    RECEIVED = 'REC'
    FOOD_STATUS_CHOICES = (
        (REQUESTED, 'REQ'),
        (PROCESSING, 'PRO'),
        (RECEIVED, 'REC'),
    )
    # food_id = models.UUIDField(
    #     default=uuid.uuid1, primary_key=True, editable=False)
    donator = models.ForeignKey(
        Profile, on_delete=models.CASCADE, limit_choices_to={'volunter': 'N'})
    location = models.CharField(max_length=100)  # Where to pick up food
    quantity = models.PositiveSmallIntegerField(default=0)  # Amount of food
    expire_time = models.PositiveSmallIntegerField(default=0)
    food_desc = models.TextField()
    pick_up_time = models.TimeField()
    date_time = models.DateTimeField(
        auto_now_add=True)  # When the request is created
    food_status = models.CharField(max_length=3, choices=FOOD_STATUS_CHOICES,
                                   default=REQUESTED)
    # is_accepted will be added

    class Meta:
        ordering = ('-date_time', 'food_status', )

    def __str__(self):
        return str(self.donator.user)


class DonatedFood(models.Model):
    volunter = models.ForeignKey(
        Profile, on_delete=models.CASCADE, limit_choices_to={'volunter': 'Y'})
    donated_area = models.CharField(max_length=100, null=False)
    beneficent = models.PositiveSmallIntegerField(default=0)
    donated_by = models.ForeignKey(FoodRequest, on_delete=models.CASCADE)
    finished = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-finished', )

    def __str__(self):
        return self.donated_area + str(self.beneficent)
