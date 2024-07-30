from django.contrib import admin
from django.urls import include, path 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include("blog.urls")),
    path('account/', include("account.urls")), 
    #path('signup/', include("account.urls")),

]
