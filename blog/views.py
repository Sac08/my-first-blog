from django.shortcuts import render
#view = models.ManyToManyField('view.View',through='ItemView',blank=True)
# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
