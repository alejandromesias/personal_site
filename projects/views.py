
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class ProjectsView(TemplateView):
    template_name = 'projects/am_home.html'

    def get(self, request, *args, **kwargs):

        testvar = "testeando"

        context = {
                'testvar': testvar,
                }

        return self.render_to_response(context)
