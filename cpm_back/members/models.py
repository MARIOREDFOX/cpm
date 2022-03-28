from django.db import models
import datetime
from django.core.validators import MaxValueValidator

# Create your models here.



class Member(models.Model):

    def year_choices():
        return [(r,r) for r in range(1984, datetime.date.today().year+1)]

    def current_year():
        return datetime.date.today().year

    # models.CharField(max_length=20, choices=GENDER, null=True)


    GENDER = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('Others', 'others')
    )
    DISABLITLITY = (
        ('Yes', 'yes'),
        ('No', 'no')
    )
    MINORITY = (
        ('Hindu','hindu'),
        ('Christian','christian'),
        ('Muslim','muslim'),
        ('Jain','jain')
    )
    ORGCPM = (
        ('DYFI','dyfi'),
        ('SFI','sfi'),
        ('AIDWA','aidwa'),
        ('AIAWU','aiawu')
    )
    ONE = (
        ('PM', 'pm'),
        ('CM', 'cm'),
        ('AM', 'am')
    )
    CATEGORYOFWORK = (
        ('Daily Wages','dailywages'),
        ('Driver','driver'),
        ('Fisher Man','fisherman'),
        ('Shop Keeper','shopeeper'),
        ('Barber','barber'),
        ('Watchman','watchman')
    )
    CLASSES = (
        ('SC','sc'),
        ('ST','st'),
        ('MBC','mbc'),
        ('BC','bc')
    )
    QUALIFICATION = (
        ('10th', '10'),
        ('12th', '12'),
        ('Graduate', 'graduate')
    )
    SOCIOCULTURECASTE = (
        ('SC','sc'),
        ('ST', 'st'),
        ('MBC', 'mbc'),
        ('BC', 'bc')
    )
    NEWSLETTER = (
        ('மார்க்சியம்', 'marxist'),
        ('தீக்கதிர்', 'theek'),
        ('PD', 'pd')
    )

    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    name = models.CharField(max_length=100)
    one = models.CharField(max_length=20, choices=ONE, null=True)
    gender = models.CharField(max_length=20, choices=GENDER, null=True)
    age = models.DateField(null=True, blank=True)

    period_of_joining = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    
    category = models.CharField(max_length=20, choices=CATEGORYOFWORK, null=True)
    classes = models.CharField(max_length=20, choices=CLASSES, null=True)
    qualification = models.CharField(max_length=20, choices=QUALIFICATION, null=True)
    income = models.IntegerField(default=1)
    levy_cash = models.IntegerField(default=1)
    socio_culture_caste = models.CharField(max_length=20, choices=SOCIOCULTURECASTE, null=True)
    minority = models.CharField(max_length=20, choices=MINORITY, null=True)
    organisation_cpm = models.CharField(max_length=20, choices=ORGCPM, null=True)
    disability = models.CharField(max_length=20, choices=DISABLITLITY, null=True)
    news_letter = models.CharField(max_length=20, choices=NEWSLETTER, null=True)
    
    def __str__(self):
        return self.name