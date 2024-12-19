from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    technologies = models.CharField(max_length=200)
    link = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(help_text="Niveau de compétence sur 100")

    def __str__(self):
        return self.name
    

#cERTIFICAT OBTE
class Certification(models.Model):
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    date_obtained = models.DateField()
    badgeImage = models.ImageField(upload_to='certifications_badges/')

    def __str__(self):
        return f"{self.title} - {self.institution}"
#Experience
class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.CharField(max_length=10)  
    end_date = models.CharField(max_length=10, default= 'En cours')  
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, default="No Subject") 
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
    
#Stat experience
class ExperienceStats(models.Model):
    years_of_experience = models.IntegerField(default=0)
    happy_clients = models.IntegerField(default=0)
    completed_projects = models.IntegerField(default=0)

    def __str__(self):
        return f"Stats: {self.years_of_experience} years, {self.happy_clients} clients, {self.completed_projects} projects"

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=100)

    def __str__(self):
        return self.title
#Temoignage client
class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    testimonial = models.TextField()
    image = models.ImageField(upload_to='testimonial_images/')

    def __str__(self):
        return self.client_name
#partie Blog    
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(max_length=200,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def __str__(self):
        return self.title
