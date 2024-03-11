from django.forms.widgets import MultiWidget, FileInput

class MultiFileInput(MultiWidget):
    template_name = 'multiple_file_input.html'

    def __init__(self, attrs=None):
        super().__init__([FileInput(attrs=attrs) for _ in range(5)], attrs)  # Adjust the number of file inputs as needed

    def deconstruct(self):
        return ('multiplefileuploadwidget.MultiFileInput', [], {})
