from django.db import models

class DANKMANAGER(models.Manager):
    def dank_validator(self, postData):
        dank_errors = {}
        if len(postData['first_name']) == 0 :
            dank_errors['first_name']= "First name can not be empty"
        if len(postData['first_name']) > 255 :
            dank_errors['first_name']= "First name can not be more than 255 letters"
            
        if len(postData['last_name']) == 0 :
            dank_errors['last_name']= "Last name can not be empty"
        if len(postData['last_name']) > 255 :
            dank_errors['last_name']= "Last name can not be more than 255 letters"
        
        if len(postData['email']) == 0 :
            dank_errors['email']= "Email can not be empty"
        if len(postData['email']) > 255 :
            dank_errors['email']= "Email can not be more than 255 letters"
        return dank_errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = DANKMANAGER()