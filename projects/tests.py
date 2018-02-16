from django.test import TestCase
from projects.models import Project

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'projects/am_home.html')
        self.assertTemplateUsed(response, 'projects/base.html')
        self.assertTemplateUsed(response, 'projects/navigation.html')

    def test_project_object(self):
        test_project = Project("title test",
                               "description test",
                               "picture_url_test",
                               "repository_link_test",
                               "published_link_test",
                               "extra_link_test",
                               "extra text test")

        self.assertEqual(test_project.title, "title test")
        self.assertEqual(test_project.description, "description test")
        self.assertEqual(test_project.picture, "picture_url_test")
        self.assertEqual(test_project.repository, "repository_link_test")
        self.assertEqual(test_project.published, "published_link_test")
        self.assertEqual(test_project.extra_link, "extra_link_test")
        self.assertEqual(test_project.extra_text, "extra text test")


    #def test_view_has_project_title(self):
    #    response = self.client.get('/')
    #    self.assertContains(response,'titulo prueba1')
