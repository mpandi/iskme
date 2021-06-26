from django.db import models

class Iskme(models.Model):
    """
    Iskme Model
    """
    standard = models.TextField()
    grade = models.CharField(max_length=50)
    end_grade = models.CharField(max_length=50,blank=True)
    learning_domain = models.CharField(max_length=100)
    full_code = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.standard

    def __repr__(self):
        return self.standard + ' added.'
