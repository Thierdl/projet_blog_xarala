from django.contrib import admin
from django.urls import include, path 
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include("blog.urls")),
    path('account/', include("account.urls")), 
    path('login/', auth_views.LoginView.as_view(template_name='account_e/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='page1'), name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)