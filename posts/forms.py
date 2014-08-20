from django.forms import ModelForm
from posts.models import Post, Language

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'link', 'lang', 'cat']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['lang'].label = "Language"
        self.fields['lang'].queryset = Language.objects.all().order_by('name')
        self.fields['cat'].label = "Type"

