from django.http import JsonResponse
from django.shortcuts import render
from utils.Encryption.main import encryption, decoding
from Main.signals import is_logged_in
from utils.functions import process_pos_nev


# Create your views here.


def main_view(request):
    return render(request, 'Main/index.html')


@is_logged_in
def chat_with_pos_neg(request):
    return render(request, 'Main/chat_with_pos_neg.html')


@is_logged_in
def ml_process_pos_neg(request):
    text = request.POST.get('text')
    y_pred_to_str = process_pos_nev(text)
    return JsonResponse({
        'y_pred': y_pred_to_str,
    })


@is_logged_in
def chat_with_encryption(request):
    return render(request, 'Main/encryption.html')


@is_logged_in
def encryption_processing(request):
    text = request.POST.get('text')
    alphabet_dict = request.session.get('alphabet_dict', {})
    encryption_result = encryption(text=text, alphabet_dict=alphabet_dict)
    return JsonResponse({
        'y_pred': encryption_result,
    })


@is_logged_in
def chat_with_decoder(request):
    return render(request, 'Main/decoder.html')


@is_logged_in
def decoder_processing(request):
    numbers = request.POST.get('numbers')
    alphabet_dict = request.session.get('alphabet_dict', {})
    decoder_result = decoding(numbers=numbers, alphabet_dict=alphabet_dict)
    return JsonResponse({
        'y_pred': decoder_result if decoder_result else 'You cannot decode this text!',
    })
