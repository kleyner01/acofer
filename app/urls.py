from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('api/v1/', include('authentication.urls')),

    # Defina a home antes das outras rotas de '' para evitar conflitos
    path('', views.home, name='home'),

    # As outras rotas que usam o caminho '' devem ter um prefixo claro
    path('brands/', include('brands.urls')),
    path('categories/', include('categories.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('inflows/', include('inflows.urls')),
    path('outflows/', include('outflows.urls')),
    path('products/', include('products.urls')),
    path('candidatos/', include('candidatos.urls')),

    path('quem-somos/', views.quem_somos, name='quem_somos'),
    path('parceiros/', views.parceiros, name='parceiros'),
    path('lojas/', include('lojas.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
