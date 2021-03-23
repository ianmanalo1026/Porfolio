from django.urls import path
from .views import UserSignInView, CreateContentView, home 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
    path('sign-in', UserSignInView.as_view(), name='sign-in'),
    # path('create-content', CreateContentView.as_view(), name='create-content'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
urlpatterns += staticfiles_urlpatterns()