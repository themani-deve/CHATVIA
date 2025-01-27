from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from Main.models import Messages, MlMessages
import joblib


# Create your views here.


def main_view(request):
    if request.user.is_authenticated:
        user_messages = Messages.objects.filter(user_id=request.user.id)
        ml_messages = MlMessages.objects.filter(user_id=request.user.id)
        list_messages = sorted(list(user_messages) + list(ml_messages), key=lambda message: message.datetime)
        context = {
            'messages': list_messages,
        }
        return render(request, 'Main/index.html', context)
    else:
        return redirect(reverse('login'))


def ml_process(request):
    if request.user.is_authenticated:
        model = joblib.load('Comprehenc.pkl')
        vectorizer = joblib.load('vectorizer.pkl')
        text = request.GET.get('text')
        user_id = request.GET.get('user_id')
        message: Messages = Messages(user_id=user_id, message=text)
        message.save()
        x = vectorizer.transform([text]).toarray()
        y_pred = model.predict(x)
        if y_pred == 0:
            y_pred_to_str = 'Negative'
        else:
            y_pred_to_str = 'Positive'
        ml_message: MlMessages = MlMessages(user_id=user_id, message=y_pred_to_str)
        ml_message.save()

        return JsonResponse({
            'y_pred': y_pred_to_str,
        })
    else:
        return redirect(reverse('login'))
