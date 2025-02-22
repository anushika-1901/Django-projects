"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first_app import views 
from vege import views 
from django.conf.urls.static import static 
from django.conf import settings 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
urlpatterns = [
    # path('home/',views.home,name='home'),
    # path('success-page/',views.success_page,name='success_page'),
    # path('index/',views.index,name='index'),
    # path('index1/',views.index1,name='index1'),
    # path('contact/',views.contact,name='contact'),
    # path('about/',views.about,name='about'),
    path('recipes/',views.recipes,name='recipes'),
    path('delete-recipes/<id>/',views.delete_recipes,name='delete_recipes'),
    path('update-recipes/<id>/',views.update_recipes,name='update_recipes'),
    path('login/',views.login_page,name='login_page'),
    path('logout/',views.logout_page,name='logout_page'),
    path('register/',views.register_page,name='register_page'),
    path('student/',views.get_students,name='get_students'),
    path('seemarks/<student_id>',views.see_marks,name='see_marks'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()
