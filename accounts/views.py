from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView as LoginViewBase
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'


class LoginView(LoginViewBase):
    extra_context = {'title': 'ログイン'}


class UserLogoutView(LogoutView):
    pass


class UserPasswordChangeView(PasswordChangeView):
    pass


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    pass


class UserPasswordResetView(PasswordResetView):
    pass


class UserPasswordResetDoneView(PasswordResetDoneView):
    pass


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    pass


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    pass
