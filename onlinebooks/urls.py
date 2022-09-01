from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'onlinebooks'

urlpatterns = [
	path("", views.home, name="home"),
	path("<int:pk>/<slug:slug_text>/", views.detail, name="book-detail"),
	path('register/', views.UserRegister, name="register"),
	path('login/', views.UserLogin, name="login"),
	path('logout/', views.UserLogout, name="logout"),
	path('upload/<int:pk>/', views.content_form, name="upload"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.urls import path
# from . import views
# from django.conf import settings
# from django.conf.urls.static import static


# app_name = "shop"

# urlpatterns = [
# 	path('', views.home, name="home"),
# 	path('detail/<int:item_id>/', views.item_detail, name="detail"),
# ]


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
