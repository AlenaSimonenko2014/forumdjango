from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.datetime_safe import datetime
from django.views.generic import View

from forum.models import Section, Topic, Message
from forum.forms import TopicForm, MessageForm, UserForm  # UserProfileForm


def index(request):
    last_section_list = Section.objects.all()[:5]
    return render(request, 'forum/index.html', {'last_section_list': last_section_list})


def section(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    topics = Topic.objects.filter(section=section_id)
    return render(request, 'forum/section.html', {'section': section, 'topics': topics})


class TopicView(View):
    def get(self, request, topic_id, *args, **kwargs):
        topic = get_object_or_404(Topic, pk=topic_id)
        section = topic.section
        messages = topic.message_set.all()
        message_form = MessageForm(initial={'topic': topic})
        return render(request, 'forum/topic.html',
                      {'section': section, 'topic': topic, 'messages': messages,
                       'message_form': message_form})

    def post(self, request, topic_id, *args, **kwargs):
        message_form = MessageForm(request.POST)
        topic = get_object_or_404(Topic, pk=topic_id)
        section = topic.section
        messages = topic.message_set.all()
        if message_form.is_valid():
            message_form.instance.user = request.user
            message_form.instance.topic = topic
            message_form.save()

        return render(request, 'forum/topic.html',
                      {'section': section, 'topic': topic, 'messages': messages,
                       'message_form': message_form})



        # topic = get_object_or_404(Topic, pk=topic_id)
        # try:
        # m = Message(text=request.POST["msg_text"], topic=topic, user=request.user, date=datetime.now())
        # m.save()
        # # check correct msg_text
        # except (KeyError, Topic.DoesNotExist) as e:  # TODO CorrectMessageException
        #     # Redisplay the topic message addind form.
        #     print("FATAL PIZDAUSCASS", e)
        #     return render(request, 'forum/topic.html', {
        #         'error_message': "You didn't select a choice.",
        #     })
        # else:
        #     # Always return an HttpResponseRedirect after successfully dealing
        #     # with POST data. This prevents data from being posted twice if a
        #     # user hits the Back button.
        #     return HttpResponseRedirect(reverse('forum:topic', args=(topic.id,)))


def add_topic(request, section_id):
    context = RequestContext(request)

    if request.method == 'POST':
        form = TopicForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = TopicForm()

    return render_to_response('forum/add_topic.html', {'form': form, 'section_id': section_id}, context)


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        # user_form = UserForm(initial={'user': user})
        messages = Message.objects.filter(user=user)
        return render(request, 'forum/profile.html',
                      {'messages': messages,
                       'user_form': None})

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST)
        messages = Message.objects.filter(user=request.user)
        if user_form.is_valid():
            user_form.save()

        return render(request, 'forum/profile.html',
                      {'messages': messages,
                       'user_form': user_form})



