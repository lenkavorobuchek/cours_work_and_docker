from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime
from calculator.models import Profile
from food_diary.views import valid_data
from sport.models import Type_of_training, Training_trecker


def calculate_training_data(info):
    info['kkal'] = round(info['training_time'] / 60 * info['kkal'], 1)
    return info


def AddSport(request):
    if request.user.is_authenticated:
        search_query = request.GET.get('search', '')
        error = "К сожалению, по Вашему запросу ничего не найдено..."
        if request.POST.get('training_time'):
            training_time = request.POST.get('training_time')
            if 0 < int(training_time) < 721:
                training = request.POST.get('id')
                info = Type_of_training.objects.filter(id=training)
                training_info = {'id': training, 'type_training': info[0].type_training, 'kkal': info[0].kkal_in_hour,
                                 'training_time': int(training_time), }
                training_info = calculate_training_data(training_info)
                user_id = Profile.objects.get(user=request.user)
                training_id = Type_of_training.objects.get(id=training_info["id"])
                user_choice = Training_trecker(id_users=user_id, id_training=training_id,
                                               duration_training_min=training_info['training_time'], burned_kkal=training_info['kkal'],)
                user_choice.save()
                return HttpResponseRedirect('add_sport')
    else:
        return redirect('login')

    if search_query and '*' not in search_query:
        data = Type_of_training.objects.filter(type_training__iregex=search_query)
        return render(request, 'sport/add_sport.html', {'data': data, 'error': error, 'value': search_query})
    elif search_query and '*' in search_query:
        return render(request, 'sport/add_sport.html', {'error': error, 'value': search_query})
    elif not search_query:
        data = Type_of_training.objects.all()
        return render(request, 'sport/add_sport.html', {'data': data, })


def SportDiary(request):
    if request.user.is_authenticated:
        error = "У Вас нет записей по выбранной дате!"
        totalAmount = {'training_time': 0, 'kkal': 0,}
        user_id = Profile.objects.get(user=request.user)
        if request.POST.get('id'):
            record_id = request.POST.get('id')
            record = Training_trecker.objects.get(id=record_id)
            record.delete()
        search_query = request.GET.get('search', '')
        flag = 0
        if search_query and valid_data(search_query):
            TrainedToday = Training_trecker.objects.filter(day_create=search_query, id_users=user_id)
            flag = 1
        elif search_query and not valid_data(search_query):
            error = "Некорректно указана дата!"
        elif not search_query:
            today = datetime.date.today()
            TrainedToday = Training_trecker.objects.filter(day_create=today, id_users=user_id)
            flag = 1
        if flag == 1:
            for i in range(len(TrainedToday)):
                totalAmount['training_time'] += TrainedToday[i].duration_training_min
                totalAmount['kkal'] += TrainedToday[i].burned_kkal
            return render(request, 'sport/sport_diary.html',
                          {'data': TrainedToday, 'value': search_query, 'total': totalAmount, 'error': error})
        return render(request, 'sport/sport_diary.html', {'value': search_query, 'error': error})
    else:
        return redirect('login')
