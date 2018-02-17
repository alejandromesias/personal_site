
from django.http import HttpResponse
from django.views.generic import TemplateView
from projects.models import Project

# Create your views here.
class ProjectsView(TemplateView):
    template_name = 'projects/am_home.html'

    def get(self, request, *args, **kwargs):

        test_project1 = Project("titulo prueba1", "descripcion prueba1")
        test_project2 = Project("titulo prueba2", "descripcion prueba2")

        projects_list = [test_project1,
                        test_project2]

        context = {
                'projects_list': projects_list,
                }

        return self.render_to_response(context)
