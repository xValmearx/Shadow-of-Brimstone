from django.shortcuts import redirect
from django.views.generic import TemplateView

class HomeView(TemplateView):
    
    template_name = "home.html"

    def dispatch(self, request, *args, **kwargs):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Redirect to another page (e.g., dashboard)
            return redirect('All_Characters')  # Replace 'dashboard' with your desired URL name
        # Otherwise, proceed as normal
        return super().dispatch(request, *args, **kwargs)