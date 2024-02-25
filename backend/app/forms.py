from django import forms

class SearchForm(forms.Form):
    search_input = forms.CharField(
        label="Input",
        help_text="Enter what you want to search",
    )
    class Meta:
        fields = ["search_input",]