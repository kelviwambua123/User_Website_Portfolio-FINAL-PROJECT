# portfolio/urls.py
from django.urls import path
from .views import project_list, project_detail, project_create, project_edit, project_delete, contact_view

from django.conf import settings
from django.conf.urls.static import static

app_name = 'portfolio'

urlpatterns = [
    path('', project_list, name='project_list'),
    path('project/<int:pk>/', project_detail, name='project_detail'),
    path('project/new/', project_create, name='project_create'),
    path('project/<int:pk>/edit/', project_edit, name='project_edit'),
    path('project/<int:pk>/delete/', project_delete, name='project_delete'),
    path('contact/<int:project_id>/', contact_view, name='contact'),
    path('contact/', contact_view, name='contact_general'),  # For general inquiries
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)