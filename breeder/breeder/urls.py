from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name="signup"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('list-puppy', views.ListPuppy.as_view(), name="list_puppy"),
    path('puppy_detail/<slug:slug>', views.puppy_detail, name="puppy_detail"),
    path('blog', views.ListPost.as_view(), name="blog"),
    path('post_detail/<slug:slug>', views.post_detail, name="post_detail"),
    path('login/', auth_views.LoginView.as_view(template_name= 'app/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'app/login.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)