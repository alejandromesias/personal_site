from django.test import TestCase

class HomePageTest(TestCase):

    def test_uses_home_template(self):
      response = self.client.get('/')
      self.assertTemplateUsed(response, 'projects/am_home.html')
      self.assertTemplateUsed(response, 'projects/base.html')
      self.assertTemplateUsed(response, 'projects/navigation.html')
      #self.assertTemplateUsed(response, 'projects/footer.html')
