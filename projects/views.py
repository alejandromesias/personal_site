
from django.http import HttpResponse
from django.views.generic import TemplateView
from projects.models import Project

# Create your views here.
class ProjectsView(TemplateView):
    template_name = 'projects/am_home.html'

    def get(self, request, *args, **kwargs):

        tesis_project  =  Project("Companion Robot",
                                   "The Companion Robot based on Kinect Sensor is my Bachelor’s degree project. Together with my mate we built a wheeled robot  capable of visually following a person around, while carrying a 5Kg payload. The people tracking system was made possible thanks to Microsoft’s Kinect sensor and the Kinect SDK. The developed human shape recognition program ran on a on-board laptop computer and the main control program on a Microcontroller chip. The setup process and remote control was available through an android mobile app. (2012)",
                                   "https://drive.google.com/uc?export=view&id=1zBm0xsbjL5vDqrEA40hW4-rUJY_DKWcg",
                                   "",
                                   "https://www.youtube.com/watch?v=0gv6BbJWOB8",
                                   "http://bibdigital.epn.edu.ec/handle/15000/17140",)

        celebrar_project = Project("celebrar.vip",
                                   "Celebrar.vip is a Django based site meant to host web pages for events, such as weddings or anniversaries. The current functionalities of an event web page is to display further information about it in a aesthetic manner and to offer a RSVP channel for the guests. The site is structured as a Django project with Django apps for each event web page. Although each event is particular, work is being done to build the apps in a way that can be easily customizable for each single event. (2018)",
                                   "https://drive.google.com/uc?export=view&id=1bIm204RsBTYn-4vqwY7ASJaKT_TSNiez",
                                   "https://github.com/alejandromesias/celebrar_py",
                                   "http://www.celebrar.vip/modelapp_a",)

        sspot_project  =  Project("SSPOT Parking app",
                                   "Sspot is a young start-up that strives to help Quito with its car parking issues. Sspot Parking is a mobile app that can tell drivers where parking places are based on their location or destination. I have been responsible for the development of the native Front-End apps for both Android and iOS, and I have also been involved in integrating them to the Node.js backend through the REST API. (2017)",
                                   "https://drive.google.com/uc?export=view&id=1k4Wf66crtk8oWqHn_7_pxayAzfhYqDyF",
                                   "",
                                   "https://play.google.com/store/apps/details?id=com.sspot.www.sspotparkin&hl=en",
                                   "http://www.sspot-app.com/conductores",)

        personal_project = Project("alejandromesias.com",
                                   "This very same site. It has been built using Django and introducing first steps in TDD through python’s unittest library and functional testing with selenium. (2018)",
                                   "https://drive.google.com/uc?export=view&id=1s8_qee09spgnfBfYkLVUNDPh48fT9-9a",
                                   "https://github.com/alejandromesias/personal_site",
                                   "http://www.alejandromesias.com",)

        engtranslator_project = Project("engineering translators",
                                   "Engineering translators is a web app developed for a group of translators freelancers who had a glossary of technical terms translated to spanish and wanted to display it on the internet. It was developed as a Django project. Of special interest are the relationships between terms, themes, chapters, related terms, synonyms, etc, that needed to be addressed when defining the models for the Database.(2017)",
                                   "https://drive.google.com/uc?export=view&id=1NYKOoIfKtA6SBjDrj1SSnZAfYD3w6rTk",
                                   "https://github.com/alejandromesias/engtranslators",
                                   "http://amesias.pythonanywhere.com/",)



        projects_list = [tesis_project,
                        celebrar_project,
                        sspot_project,
                        personal_project,
                        engtranslator_project,]

        context = {
                'projects_list': projects_list,
                }

        return self.render_to_response(context)
