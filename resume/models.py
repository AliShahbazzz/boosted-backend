from django.db import models

# local import  here..

# ========================================================================================================


class ResumeThumbnails(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    user = models.CharField(max_length=80,
                            null=True,
                            blank=True,
                            help_text="Full Name of the User")

    resume_number = models.PositiveIntegerField(null=False,
                                                blank=True,
                                                help_text='Resume number')

    path = models.CharField(max_length=800,
                            null=False,
                            blank=True,
                            help_text='Thumbnail path')

    def __str__(self):
        return str(self.user)


class UserResume(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    user = models.CharField(max_length=80,
                            null=True,
                            blank=True,
                            help_text='UserId')

    resume_number = models.PositiveIntegerField(null=False,
                                                blank=True,
                                                help_text='Resume number')

    resume_image = models.ImageField(upload_to='user_resume_image',
                                     default='default.jpg',
                                     null=True,
                                     blank=True)

    name = models.CharField(max_length=80,
                            null=True,
                            blank=True,
                            help_text="Full Name of the User")

    age = models.IntegerField(null=True,
                              blank=True,
                              help_text="Age of the User")

    position = models.CharField(max_length=100,
                                null=True,
                                blank=True,
                                help_text="Position of the User")

    profile = models.TextField(null=True,
                               blank=True,
                               help_text="Profile/ description of the User")

    achievements = models.TextField(max_length=250, null=True, blank=True)

    skills = models.TextField(max_length=250, null=True, blank=True)

    interests = models.TextField(max_length=250, null=True, blank=True)

    email = models.EmailField(max_length=80,
                              null=True,
                              blank=True,
                              help_text="Email of the User")

    phone = models.CharField(max_length=20,
                             null=True,
                             blank=True,
                             help_text="Phone no of the User")

    url = models.CharField(max_length=50,
                           null=True,
                           blank=True,
                           help_text="Portfolio Url")

    address = models.TextField(null=True,
                               blank=True,
                               help_text="Address of the User")

    education_institute = models.CharField(max_length=80,
                                           null=True,
                                           blank=True,
                                           help_text="Name of the Institute.")

    education_degree = models.CharField(max_length=80,
                                        null=True,
                                        blank=True,
                                        help_text="Name of the degree.")

    education_course = models.CharField(max_length=80,
                                        null=True,
                                        blank=True,
                                        help_text="Name of the course.")

    education_start = models.CharField(max_length=10,
                                       null=True,
                                       blank=True,
                                       help_text="give it a  start date.")

    education_end = models.CharField(max_length=10,
                                     null=True,
                                     blank=True,
                                     help_text="give it a end date.")

    education_score = models.IntegerField(null=True,
                                          blank=True,
                                          help_text="GPA/SCORE.")

    intern_company = models.CharField(max_length=80,
                                      null=True,
                                      blank=True,
                                      help_text="Name of the Company")

    intern_position = models.CharField(max_length=80,
                                       null=True,
                                       blank=True,
                                       help_text="Position of the User")

    intern_start = models.CharField(max_length=10,
                                    null=True,
                                    blank=True,
                                    help_text="give it a  start date.")

    intern_end = models.CharField(max_length=10,
                                  null=True,
                                  blank=True,
                                  help_text="give it a end date.")

    intern_description = models.TextField(max_length=800,
                                          null=True,
                                          blank=True,
                                          help_text="give it a description.")

    experience_company_1 = models.CharField(max_length=80,
                                            null=True,
                                            blank=True,
                                            help_text="Name of the Company")

    experience_position_1 = models.CharField(max_length=100,
                                             null=True,
                                             blank=True,
                                             help_text="Position of the User")

    experience_start_1 = models.CharField(max_length=10,
                                          null=True,
                                          blank=True,
                                          help_text="give it a  start date.")

    experience_end_1 = models.CharField(max_length=10,
                                        null=True,
                                        blank=True,
                                        help_text="give it a end date.")

    experience_description_1 = models.TextField(max_length=800,
                                                null=True,
                                                blank=True,
                                                help_text="give it a description.")

    experience_company_2 = models.CharField(max_length=80,
                                            null=True,
                                            blank=True,
                                            help_text="Name of the Company")

    experience_position_2 = models.CharField(max_length=100,
                                             null=True,
                                             blank=True,
                                             help_text="Position of the User")

    experience_start_2 = models.CharField(max_length=10,
                                          null=True,
                                          blank=True,
                                          help_text="give it a  start date.")

    experience_end_2 = models.CharField(max_length=10,
                                        null=True,
                                        blank=True,
                                        help_text="give it a end date.")

    experience_description_2 = models.TextField(max_length=800,
                                                null=True,
                                                blank=True,
                                                help_text="give it a description.")

    experience_company_3 = models.CharField(max_length=80,
                                            null=True,
                                            blank=True,
                                            help_text="Name of the Company")

    experience_position_3 = models.CharField(max_length=100,
                                             null=True,
                                             blank=True,
                                             help_text="Position of the User")

    experience_start_3 = models.CharField(max_length=10,
                                          null=True,
                                          blank=True,
                                          help_text="give it a  start date.")

    experience_end_3 = models.CharField(max_length=10,
                                        null=True,
                                        blank=True,
                                        help_text="give it a end date.")

    experience_description_3 = models.TextField(max_length=800,
                                                null=True,
                                                blank=True,
                                                help_text="give it a description.")

    experience_company_4 = models.CharField(max_length=80,
                                            null=True,
                                            blank=True,
                                            help_text="Name of the Company")

    experience_position_4 = models.CharField(max_length=100,
                                             null=True,
                                             blank=True,
                                             help_text="Position of the User")

    experience_start_4 = models.CharField(max_length=10,
                                          null=True,
                                          blank=True,
                                          help_text="give it a  start date.")

    experience_end_4 = models.CharField(max_length=10,
                                        null=True,
                                        blank=True,
                                        help_text="give it a end date.")

    experience_description_4 = models.TextField(max_length=800,
                                                null=True,
                                                blank=True,
                                                help_text="give it a description.")

    project_name_1 = models.CharField(max_length=80,
                                      null=True,
                                      blank=True,
                                      help_text="Name of the Project")

    project_start_1 = models.CharField(max_length=10,
                                       null=True,
                                       blank=True,
                                       help_text="give it a  start date.")

    project_end_1 = models.CharField(max_length=10,
                                     null=True,
                                     blank=True,
                                     help_text="give it a end date.")

    project_description_1 = models.TextField(max_length=800,
                                             null=True,
                                             blank=True,
                                             help_text="Decsribe Project")

    project_name_2 = models.CharField(max_length=80,
                                      null=True,
                                      blank=True,
                                      help_text="Name of the Project")

    project_start_2 = models.CharField(max_length=10,
                                       null=True,
                                       blank=True,
                                       help_text="give it a  start date.")

    project_end_2 = models.CharField(max_length=10,
                                     null=True,
                                     blank=True,
                                     help_text="give it a end date.")

    project_description_2 = models.TextField(max_length=800,
                                             null=True,
                                             blank=True,
                                             help_text="Describe Project")

    project_name_3 = models.CharField(max_length=100,
                                      null=True,
                                      blank=True,
                                      help_text="Name of the Project")

    project_start_3 = models.CharField(max_length=10,
                                       null=True,
                                       blank=True,
                                       help_text="give it a  start date.")

    project_end_3 = models.CharField(max_length=10,
                                     null=True,
                                     blank=True,
                                     help_text="give it a end date.")

    project_description_3 = models.TextField(max_length=800,
                                             null=True,
                                             blank=True,
                                             help_text="Describe Project")

    certificate_name_1 = models.CharField(max_length=80,
                                          null=True,
                                          blank=True,
                                          help_text="Name of the Certificate")
    certifying_center_1 = models.CharField(max_length=80,
                                           null=True,
                                           blank=True,
                                           help_text="Name of the Cerifying Center")
    certificate_description_1 = models.TextField(max_length=300,
                                                 null=True,
                                                 blank=True,
                                                 help_text="Describe your certification")
    certificate_obtainment_date_1 = models.CharField(max_length=10,
                                                     null=True,
                                                     blank=True,
                                                     help_text="Date of obtainment")

    certificate_name_2 = models.CharField(max_length=80,
                                          null=True,
                                          blank=True,
                                          help_text="Name of the Certificate")
    certifying_center_2 = models.CharField(max_length=80,
                                           null=True,
                                           blank=True,
                                           help_text="Name of the Cerifying Center")
    certificate_description_2 = models.TextField(max_length=300,
                                                 null=True,
                                                 blank=True,
                                                 help_text="Describe your certification")
    certificate_obtainment_date_2 = models.CharField(max_length=10,
                                                     null=True,
                                                     blank=True,
                                                     help_text="Date of obtainment")

    certificate_name_3 = models.CharField(max_length=80,
                                          null=True,
                                          blank=True,
                                          help_text="Name of the Certificate")
    certifying_center_3 = models.CharField(max_length=80,
                                           null=True,
                                           blank=True,
                                           help_text="Name of the Cerifying Center")
    certificate_description_3 = models.TextField(max_length=300,
                                                 null=True,
                                                 blank=True,
                                                 help_text="Describe your certification")
    certificate_obtainment_date_3 = models.CharField(max_length=10,
                                                     null=True,
                                                     blank=True,
                                                     help_text="Date of obtainment")

    recommendation_1 = models.TextField(max_length=150,
                                        null=True,
                                        blank=True)

    recommendation_2 = models.TextField(max_length=150,
                                        null=True,
                                        blank=True)

    recommendation_3 = models.TextField(max_length=150,
                                        null=True,
                                        blank=True)

    recommendation_4 = models.TextField(max_length=150,
                                        null=True,
                                        blank=True)

    recommendation_5 = models.TextField(max_length=150,
                                        null=True,
                                        blank=True)

    def __str__(self):
        return str(self.name)
