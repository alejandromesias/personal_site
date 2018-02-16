from django.db import models

# Create your models here.
class Project(object):

    def __init__(self, title, description):
        self.title = title
        self.description = description
