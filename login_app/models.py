from django.db import models
# from material_supply_app.models import Line, Department
import re
# from . import views

class UserManager(models.Manager):
    def validator(self, postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    # FIRST NAME
        #  at least 2 characters
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        # Letters only
        if (postData['first_name']).isalpha() == False :
            errors['first_name'] = "First name must be letters only"
        # Required

    # LAST NAME
        # at least 2 characters
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        # letters only
        if postData['last_name'].isalpha() == False :
            errors['last_name'] = "Last name must be letters only"
        # Required
        if len(postData['last_name']) == 0:
            errors['last_name'] = "Last name required"

    # EMAIL
        # valid format
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        # Required
        if len(postData['email']) == 0:
            errors['email'] = "Account must have an email"

    #Registered email is unique
        try: 
            self.get(email= postData['email'])
            errors['email_unique'] = "An account is already associated with that email"
        except:
            pass

    # PASSWORD:
        # at least 8 Chars
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        # Required
        if postData['password'] == "":
            errors['password'] = "Account must have a password"
        # Matches Confirmation
        if postData['password'] != postData['confirm_password']:
            errors['password'] = "Password and password confirmation must match"
        if postData['password'] == "password":
            # what about all the other colors of the rainbow?...
            errors['password'] = "Try a more complex password"


        return errors

    def update_validator(self, postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    # FIRST NAME
        #  at least 2 characters
        if len(postData['first_name']) == 1:
            errors['first_name'] = "First name must be at least 2 characters"
        # If letters, letters only
        if len(postData['first_name']) > 0 and postData['first_name'].isalpha() == False :
            errors['first_name'] = "First name must be letters only"

    # LAST NAME
        # at least 2 characters
        if len(postData['last_name']) == 1:
            errors['last_name'] = "Last name must be at least 2 characters"
        # If letters, letters only
        if len(postData['last_name']) > 0 and postData['last_name'].isalpha() == False :
            errors['last_name'] = "Last name must be letters only"

    # EMAIL
        # valid format
        if len(postData['email']) > 0 and not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"

        return errors

class ManagerManager(models.Manager):
    def validator(self, postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    # FIRST NAME
        #  at least 2 characters
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        # Letters only
        if (postData['first_name']).isalpha() == False :
            errors['first_name'] = "First name must be letters only"
        # Required

    # LAST NAME
        # at least 2 characters
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        # letters only
        if postData['last_name'].isalpha() == False :
            errors['last_name'] = "Last name must be letters only"
        # Required
        if len(postData['last_name']) == 0:
            errors['last_name'] = "Last name required"

    # EMAIL
        # valid format
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        # Required
        if len(postData['email']) == 0:
            errors['email'] = "Account must have an email"

    #Registered email is unique
        try: 
            self.get(email= postData['email'])
            errors['email_unique'] = "An account is already associated with that email"
        except:
            pass

    # PASSWORD:
        # at least 8 Chars
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        # Required
        if postData['password'] == "":
            errors['password'] = "Account must have a password"
        # Matches Confirmation
        if postData['password'] != postData['confirm_password']:
            errors['password'] = "Password and password confirmation must match"
        if postData['password'] == "password":
            # what about all the other colors of the rainbow?...
            errors['password'] = "Try a more complex password"


        return errors

    def update_validator(self, postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    # FIRST NAME
        #  at least 2 characters
        if len(postData['first_name']) == 1:
            errors['first_name'] = "First name must be at least 2 characters"
        # If letters, letters only
        if len(postData['first_name']) > 0 and postData['first_name'].isalpha() == False :
            errors['first_name'] = "First name must be letters only"

    # LAST NAME
        # at least 2 characters
        if len(postData['last_name']) == 1:
            errors['last_name'] = "Last name must be at least 2 characters"
        # If letters, letters only
        if len(postData['last_name']) > 0 and postData['last_name'].isalpha() == False :
            errors['last_name'] = "Last name must be letters only"

    # EMAIL
        # valid format
        if len(postData['email']) > 0 and not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    level = models.IntegerField()
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    def serialize(self):
        return {
            'id':self.id,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'level':self.level,
            'email':self.email,
            'created_at':self.created_at,
            'updated_at':self.updated_at,
        }
    def __str__(self):
        return f'{self.full_name} - ({self.created_at})'
    def __repr__(self) -> str:
        return super().__repr__()
    def __str__(self):
        return str(self.full_name)

# class Manager(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     level = models.IntegerField()
#     # staff = models.ForeignKey(User, related_name="manager", on_delete=models.CASCADE)
#     department = models.ForeignKey(Department, related_name="manager", on_delete=models.CASCADE)
#     line = models.ForeignKey(Line, related_name="manager", on_delete=models.CASCADE)
#     email = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=60)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = ManagerManager()