from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
urlpatterns=[
    path('', views.ProductView.as_view(), name="index"),


    path('product-detail/<int:pk>/',views.ProductDetailView.as_view(),name='product-detail'),

    path('base',views.base,name='base'),
    
    path('aboutus',views.aboutus,name='aboutus'),
    

    path('customerservice',views.customerservice,name='customerservice'),
    path('covid19andarmani',views.covid19andarmani,name='covid19andarmani'),
    path('settings',views.settings,name='settings'),
    path('countryandlanguage',views.countryandlanguage,name='countryandlanguage'),
    path('notifications',views.notifications,name='notifications'),
    path('alexa',views.alexa,name='alexa'),
    


    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    


    path('registration/', views.Registration.as_view(), name='registration'),
    path('welcome',views.welcome,name='welcome'),
    path('address/',views.address,name='address'),
    path('login_request',views.login_request,name='login_request'),
    
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'), name='passwordchangedone'),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=MySetPasswordForm), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),

    path('logout_request',views.logout_request,name='logout_request'),
    path('watch',views.watch,name='watch'),
    path('watch/<slug:data>',views.watch,name='watchdata'),
    path('sunglass',views.sunglass,name='sunglasses'),
    path('sunglass/<slug:data>',views.sunglass,name='sunglassdata'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)