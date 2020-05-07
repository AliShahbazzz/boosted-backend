from django.db import models
from django.contrib.contenttypes.models import ContentType 
from django.contrib.contenttypes.fields import GenericForeignKey

# local import  here..

# ========================================================================================================
# Abstract Classes

class TimeStampBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Input Base
class InputBase(models.Model):
    title = models.CharField(max_length=100, 
                                        null=True, 
                                            blank=True, 
                                                help_text="give it a name.")

    class Meta:
        abstract = True                                            

# TextField Base
class TextFieldBase(models.Model):
    description = models.CharField(max_length=100, 
                                        null=True, 
                                            blank=True, 
                                                help_text="give it a description.")

    class Meta:
        abstract = True   

# Date Field Base
class DateFieldBase(models.Model):
    date = models.DateField(max_length=100, 
                                        null=True, 
                                            blank=True, 
                                                help_text="give it a date.")

    class Meta:
        abstract = True 

# Start End Date Field Base
class StartEndDateFieldBase(models.Model):
    start = models.DateField(max_length=100, 
                                        null=True, 
                                            blank=True, 
                                                help_text="give it a  start date.")
    end = models.DateField(max_length=100, 
                                    null=True, 
                                        blank=True, 
                                            help_text="give it a end date.")                                            

    class Meta:
        abstract = True 


# ===================================================================================================
class UserResume(TimeStampBase):
    name = models.CharField(max_length=80, 
                                        null=True, 
                                            blank=True, 
                                                help_text="Full Name of the User")
    age = models.DateField(null=True, 
                                    blank=True, 
                                            help_text="Age of the User")                                            


    position = models.CharField(max_length=100, 
                                        null=True, 
                                            blank=True, 
                                                help_text="Position of the User")

    profile = models.TextField(null=True, 
                                            blank=True, 
                                                help_text="Profile/ description of the User")  


    def __str__(self):
        return self.name    


class Content(TimeStampBase):
    resume = models.ForeignKey(UserResume, null=True, 
                                                    blank=True, 
                                                        on_delete=models.CASCADE, 
                                                            related_name='option')
    # order = OrderField(blank=True, for_fields=['resume'], help_text='Leave this field empty.')                                                         
    content_type = models.ForeignKey(ContentType, 
                                                null=True,
                                                        blank=True,
                                                            on_delete=models.CASCADE,
                                                                limit_choices_to={'model__in':(
                                                                                        'contactdetail',
                                                                                        'achievement',
                                                                                        'skill',
                                                                                        'interest',
                                                                                        'internship',
                                                                                        'education',
                                                                                        'experience',
                                                                                        'project',
                                                                                        'certification',
                                                                                        'recommendation'
                                                                                        )})
    object_id = models.PositiveIntegerField(null=True,
                                                        blank=True)
    item = GenericForeignKey('content_type', 'object_id')   
                                                                                          
                                                        
    # class Meta:
    #     ordering = ['order']

    def __str__(self):
        return '{}'.format(self.item)


# =====================================================================================================
# Content type Models

# contact details
class ContactDetail(models.Model):
    email = models.EmailField(max_length=80, 
                                    null=True, 
                                        blank=True, 
                                            help_text="Email of the User")
    phone = models.PositiveIntegerField(null=True, 
                                                blank=True, 
                                                    help_text="Phone no of the User")   
    url = models.URLField(null=True, 
                                    blank=True, 
                                                help_text="Portfolio Url")
    address = models.TextField(null=True, 
                                        blank=True, 
                                                help_text="Address of the User") 


    def __str__(self):
        return self.email                                                    


 
# Achievement
class Achievement(InputBase):
    pass

    def __str__(self):
        return self.title 


# skills
class Skill(InputBase):
    pass

    def __str__(self):
        return self.title 


#  hobbies/Interest
class Interest(InputBase):
    pass

    def __str__(self):
        return self.title 


# Internship
class Internship(InputBase, StartEndDateFieldBase):
    position = models.CharField(max_length=100, 
                                        null=True, 
                                            blank=True, 
                                                help_text="Position of the User")

    description = models.CharField(max_length=100, 
                                        null=True, 
                                            blank=True, 
                                                help_text="give it a description.")

    def __str__(self):
        return self.title 

# Education
class Education(InputBase, StartEndDateFieldBase):
    course = models.CharField(max_length=100, 
                                        null=True, 
                                            blank=True, 
                                                help_text="Name of the course.")
    score = models.IntegerField(
                                        null=True, 
                                            blank=True, 
                                                help_text="GPA/SCORE.")

    def __str__(self):
        return self.title 

# experience
class Experience(InputBase, StartEndDateFieldBase):
    position = models.CharField(max_length=100, 
                                        null=True, 
                                            blank=True, 
                                                help_text="Position of the User")

    description = models.CharField(max_length=100, 
                                        null=True, 
                                            blank=True, 
                                                help_text="give it a description.")
    def __str__(self):
        return self.title 

# projects
class Project(InputBase, DateFieldBase):
    role = models.CharField(max_length=100, 
                                        null=True, 
                                            blank=True, 
                                                help_text="Describe the role in the project.")

    def __str__(self):
        return self.title 

# Certification
class Certification(InputBase):
    center = models.CharField(max_length=80, 
                                        null=True, 
                                            blank=True, 
                                                help_text="Name of the Certifying Center")
    description = models.TextField(
                                        null=True, 
                                            blank=True, 
                                                help_text="Description of the certificate.")
    date = models.DateField(null=True, 
                                    blank=True, 
                                            help_text="Date of obtainment")                                                                                                  


    def __str__(self):
        return self.title 

# Recommendation
class Recommendation(TextFieldBase):
    pass

#====================================================================================================== 

