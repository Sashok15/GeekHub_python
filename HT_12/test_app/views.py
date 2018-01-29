from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Message, Comment


class IndexView(generic.ListView):
    template_name = 'test_app/index.html'
    context_object_name = 'latest_message_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Message.objects.order_by('-pub_date')[:5]


# def index(request):
# latest_message_list = Message.objects.order_by('-pub_date')[:5]
# context = {
#     'latest_message_list': latest_message_list
# }
# return render(request, 'test_app/index.html', context)


class DetailView(generic.DetailView):
    model = Message
    template_name = 'test_app/detail.html'


# def detail(request, message_id):
#     message = get_object_or_404(Message, pk=message_id)
#     return render(request, 'test_app/detail.html', {'message': message})
class ResultView(generic.DetailView):
    model = Message
    template_name = 'test_app/result.html'


# def result(request, message_id):
#     message = get_object_or_404(Message, pk=message_id)
#     return render(request, 'test_app/result.html', {'message': message})


def vote(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    context = {
        'message': message,
        'error_message': 'You did not select a comment '
    }
    try:
        selected_comment = message.comment_set.get(pk=request.POST['comment'])
    except (KeyError, Comment.DoesNotExist):
        return render(request, 'test_app/detail.html', context)
    else:
        selected_comment.votes = 1
        selected_comment.save()
    return HttpResponseRedirect(reverse('test_app:result', args=(message.id,)))
