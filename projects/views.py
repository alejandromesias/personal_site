
from django.http import HttpResponse
from django.views.generic import TemplateView
from projects.models import Project

# Create your views here.
class ProjectsView(TemplateView):
    template_name = 'projects/am_home.html'

    def get(self, request, *args, **kwargs):

        test_project1 = Project("titulo prueba1", "descripcion prueba1")
        test_project2 = Project("titulo prueba2", "descripcion prueba2")

        context = {
                'test_project': test_project1,
                }

        return self.render_to_response(context)
