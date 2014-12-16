from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.utils.datetime_safe import datetime
from forum.models import Section, Topic, Message


def index(request):
    last_section_list = Section.objects.all()[:5]
    return render(request, 'forum/index.html', {'last_section_list': last_section_list})


def section(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    topics = Topic.objects.filter(section=section_id)
    return render(request, 'forum/section.html', {'section': section, 'topics': topics})


def topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    section = Section.objects.filter(pk=topic.section_id)
    messages = Message.objects.filter(topic=topic_id)
    return render(request, 'forum/topic.html',
                  {'section': section[0], 'topic': topic, 'messages': messages, 'user': request.user})


@login_required
def send_message(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    try:
        # selected_choice = p.choice_set.get(pk=request.POST['choice'])
        m = Message(text=request.POST["msg_text"], topic=topic, user=request.user, date=datetime.now())
        m.save()
        # check correct msg_text
    except (KeyError, Topic.DoesNotExist) as e:
        # Redisplay the question voting form.
        # return render(request, 'polls/detail.html', {
        # # 'question': p,
        #     #'error_message': "You didn't select a choice.",
        # })
        print("FATAL PIZDAUSCASS", e)
    else:
        # selected_choice.votes += 1
        # selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('forum:topic', args=(topic.id,)))