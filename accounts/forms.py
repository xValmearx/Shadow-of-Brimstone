from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationFrom(UserCreationForm):
    """Custome User Creaton Form"""

    class Meta:
        """This is the Meta class. it contains information"""

        # about how to get an instance of class created.
        # it is not common to se this, but Django dose for
        # certain things. Like this

        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age",)

class CustomUserChangeForm(UserChangeForm):
    """Custome User Change Form"""

    class Meta:
        """This is the Meta class. it contains information"""

        model = CustomUser
        fields = UserCreationForm.Meta.fields