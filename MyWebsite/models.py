
from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import URLValidator
from django.utils import timezone

Criteria_Choices = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
)
Service_Choices = (
        ('0','0'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )
Intern_Choices = (
        ('Yes','Yes'),
        ('No','No'),
        ('Maybe','Maybe'),
    )
Offer_Choices = (
        ('JOB ONLY','JOB ONLY'),
         ('INTERNSHIP ONLY ', 'INTERNSHIP ONLY'),
         ('JOB+INTERNSHIP', 'JOB+INTERNSHIP'),
    )
# class SelectionProcess(models.Model):
#     choices = models.CharField(max_length=100,null=False,blank=False)

class Recruiter(models.Model):
    Organization_name = models.CharField(max_length=100,blank=False,null=False)
    Organization_website = models.CharField(max_length=1000,validators=[URLValidator()])
    Information_Technology = models.BooleanField()
    Analytics = models.BooleanField()
    E_Commerce = models.BooleanField()
    Telecom = models.BooleanField()
    Finance = models.BooleanField()
    Consulting = models.BooleanField()
    Other_field = models.CharField(max_length=400)
    Organization_profile = models.CharField(max_length = 250,blank=True,null=True)

    offer = models.CharField(max_length = 100,choices = Offer_Choices,default = 'JOB ONLY')

    Intern = models.CharField(max_length = 100,choices = Intern_Choices,default = 'No')
    Job_Profile  = models.CharField(max_length =300,blank=False,null=False)
    Job_Description = models.CharField(max_length = 500,blank=False,null=False)
    Locations = models.CharField(max_length = 100,blank=False,null=False)
    CTC  = models.IntegerField(blank=False,null=False)
    # Selection_Process = models.ManyToManyField(SelectionProcess)
    service = models.CharField(max_length=100,blank=False,choices = Service_Choices,default='0')
    Bond_Conditions = models.CharField(max_length = 200,blank=True,null=True)
    Tentative_Date = models.DateTimeField(blank = False, null = False,default = timezone.now())
    Other_details = models.CharField(max_length=1000,blank= True,null=True)
    Criteria = models.CharField(max_length=100, blank=False, null=False, choices=Criteria_Choices)
    Shortlisting_From_Resumes = models.BooleanField()
    Written_Test_Apptitute = models.BooleanField()
    Group_Discussion = models.BooleanField()
    Personal_Interview = models.BooleanField()
    Written_Test_Technical = models.BooleanField()
    Other = models.CharField(max_length=400)
    Offers_intend = models.IntegerField(blank = True,null=True)
    Officials_Visit = models.IntegerField(blank=True,null=True)
    Rooms_required = models.IntegerField(blank = True,null=True)
    Rooms_Type = models.CharField(blank = True,null=True,max_length = 100)
    Logistic_Support = models.CharField(blank = True,null = True,max_length = 100)
    Name = models.CharField(blank = False,null = False,max_length = 100)
    Designation = models.CharField(blank = False,null = False,max_length = 100)
    email = models.EmailField(max_length=50, null=False,blank = False)
    Contact_Number = models.IntegerField(blank = False,null = False)


    def get_absolute_url(self):
        return reverse("academic")

    def __str__(self):
        return self.Organization_name



class Gallery(models.Model):
    image = models.ImageField(blank = True)

    def get_absolue_url(self):
        return reverse("contact")
    
    
class PastRecruiter(models.Model):
    image = models.ImageField(blank = True)
    
    def get_absolute_url(self):
        return reverse("contact")
