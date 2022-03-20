from django.db import models

# Create your models here.


class One(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Classes(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Gender(models.Model):
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Qualification(models.Model):
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class SocioCultureCaste(models.Model):
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Minority(models.Model):
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class OrganisationCpm(models.Model):
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class NewsLetter(models.Model):
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class YesNo(models.Model):
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Member(models.Model):
    name = models.CharField(max_length=100)
    one = models.ForeignKey(One, on_delete=models.SET_NULL, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    age = models.DateField(null=True, blank=True)
    period_of_joining = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    classes = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True)
    qualification = models.ForeignKey(Qualification, on_delete=models.SET_NULL, null=True)
    income = models.IntegerField(default=1)
    levy_cash = models.IntegerField(default=1)
    socio_culture_caste = models.ForeignKey(SocioCultureCaste, on_delete=models.SET_NULL, null=True)
    minority = models.ForeignKey(Minority, on_delete=models.SET_NULL, null=True)
    organisation_cpm = models.ForeignKey(OrganisationCpm, on_delete=models.SET_NULL, null=True)
    disability = models.ForeignKey(YesNo, on_delete=models.SET_NULL, null=True)
    news_letter = models.ForeignKey(NewsLetter, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name