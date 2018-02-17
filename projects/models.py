from django.db import models

# Create your models here.
class Project(object):

    def __init__(self,
                 title,
                 description,
                 picture = "",
                 repository = "",
                 published = "",
                 extra_link = "",
                 extra_text = ""):
        self.title = title
        self.description = description
        self.picture = picture
        self.repository = repository
        self.published = published
        self.extra_link = extra_link
        self.extra_text = extra_text
