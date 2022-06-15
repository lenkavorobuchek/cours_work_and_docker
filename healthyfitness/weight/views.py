from datetime import date, timedelta

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from calculator.models import Profile
from weight.models import Weight_trecker


def AddWeight(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.filter(user=request.user)[0]
        user_id = Profile.objects.get(user=request.user)
        current_weight = current_user.weight
        if request.POST.get('weight_inp'):
            new_weight = float(request.POST.get('weight_inp'))
            if 25 <= new_weight <= 210:
                if Weight_trecker.objects.filter(id_users=user_id, day_create=date.today()):
                    user_weight = Weight_trecker.objects.filter(id_users=user_id, day_create=date.today())[0]
                    user_weight.weight = new_weight
                    user_weight.save()
                else:
                    user_weight = Weight_trecker(id_users=user_id, weight=new_weight)
                    user_weight.save()
                if Profile.objects.filter(user=request.user)[0].needed_kkal:
                    user_info = Profile.objects.filter(user=request.user)[0]
                    data = {'weight': new_weight, 'growth': user_info.growth, 'age': user_info.age, 'gender': user_info.gender,
                            'activity': user_info.Activity_level, 'aim': user_info.user_aim}
                    data = calcUserData(getUserData(data))
                    Profile.objects.filter(user=request.user).update(needed_kkal=data['calories'], needed_proteins=data['proteins'],
                                                                     needed_fats=data['fats'], needed_carbohydrates=data['carbohydrates'])
            return HttpResponseRedirect('add_weight')
        cont = {'current_weight': current_weight}
        return render(request, 'weight/add_weight.html', cont)
    else:
        return redirect('login')


def getUserData(data):
    gender_dict = {"Мужчина": 1, "Женщина": 2}
    activity_dict = {"Отсутствие активности": 1, "Низкая активность": 2, "Средняя активность": 3,
                     "Высокая активность": 4, "Экстремальная активность": 5}
    aim_dict = {"Похудение": 1, "Поддержание веса": 2, "Набор мышечной массы": 3}
    data.update({'gender': gender_dict[data['gender']]})
    data.update({'activity': activity_dict[data['activity']]})
    data.update({'aim': aim_dict[data['aim']]})
    return data


def calcCalories(data):
    activity_index = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
    aim_index = {1: 0.9, 2: 1, 3: 1.1}
    if data["gender"] == 1:
        calories = round((10 * data["weight"] + 6.25 * data["growth"] - 5 * data["age"] + 5) *
                         activity_index[data["activity"]] * aim_index[data["aim"]])
    else:
        calories = round((10 * data["weight"] + 6.25 * data["growth"] - 5 * data["age"] - 161) *
                         activity_index[data["activity"]] * aim_index[data["aim"]])
    return calories


def calcUserData(data):
    indicators = {1: [0.4, 0.3, 0.3], 2: [0.3, 0.3, 0.4], 3: [0.35, 0.2, 0.45]}
    calories = calcCalories(data)
    proteins = round(calories * indicators[data["aim"]][0] / 4)
    fats = round(calories * indicators[data["aim"]][1] / 9)
    carbohydrates = round(calories * indicators[data["aim"]][2] / 4)
    result = {'calories': calories, 'proteins': proteins, 'fats': fats, 'carbohydrates': carbohydrates}
    return result


def WeightTracker(request):
    if request.user.is_authenticated:
        user_id = Profile.objects.get(user=request.user)
        values = []
        user_weight = Weight_trecker.objects.filter(id_users=user_id)
        if user_weight.count() == 1:
            values.append([user_weight[0].day_create - timedelta(days=1), user_weight[0].weight])
            values.append([user_weight[0].day_create, user_weight[0].weight])
        else:
            for i in range(0, 7):
                if i < user_weight.count():
                    values.append([user_weight[i].day_create, user_weight[i].weight])
        return render(request, 'weight/weight_tracker.html', {'values': values})
    else:
        return redirect('login')
