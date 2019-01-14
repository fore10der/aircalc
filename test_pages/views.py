from django.views.generic.edit import FormView
from .forms import TestFileForm
from .specials import preprocess_xlsx#, fill_db

class TestFileView(FormView):
    template_name = 'upload.html'
    form_class = TestFileForm
    success_url = '/'
    
    def form_valid(self, form):
        data = preprocess_xlsx(self.request.FILES['file_input'])
        print(data)
        return super().form_valid(form)