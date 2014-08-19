from django.forms import ModelForm
from posts.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'link', 'lang', 'cat']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['lang'].label = "Language"
        self.fields['cat'].label = "Type"

