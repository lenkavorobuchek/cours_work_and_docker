from datetime import date

from django.shortcuts import render, redirect
from calculator.forms import CalculatorForm
from calculator.models import Profile
from weight.models import Weight_trecker


def calcIMT(growth, weight):
    return str(round(weight / (0.0001 * growth * growth), 1))


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def getUserData(data):
    gender_dict = {1: "Мужчина", 2: "Женщина"}
    activity_dict = {1: "Отсутствие активности", 2: "Низкая активность", 3: "Средняя активность",
                     4: "Высокая активность", 5: "Экстремальная активность"}
    aim_dict = {1: "Похудение", 2: "Поддержание веса", 3: "Набор мышечной массы"}
    dbUserData["gender"] = gender_dict[data["gender"]]
    dbUserData["activity_level"] = activity_dict[data["activity"]]
    dbUserData["user_aim"] = aim_dict[data["aim"]]
    return dbUserData


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


dbUserData = {'age': 0, 'weight': 0, 'gender': "", 'growth': 0, 'activity_level': "", 'user_aim': "",
              'calories': 0, 'proteins': 0, 'fats': 0, 'carbohydrates': 0}


def calculator(request):
    global dbUserData
    is_valid = error_info = False
    form = CalculatorForm(request.POST)
    userInfo = {'calories': '', 'proteins': '', 'fats': '', 'carbohydrates': '', 'IMT': 0}
    if request.method == 'POST':
        if form.is_valid():
            temp = request.POST
            error_info = True
            if isfloat(temp["weight"]) and temp["growth"].isnumeric() and temp["age"].isnumeric():
                userDataNumbers = {'age': int(temp["age"]), 'growth': int(temp["growth"]),
                                   'weight': float(temp["weight"]),
                                   'activity': int(temp["user_activity"]), 'aim': int(temp["user_aim"]),
                                   'gender': int(temp["gender"])}
                if 59 < userDataNumbers['growth'] < 231 and 9 < userDataNumbers['age'] < 101 and 25 < userDataNumbers['weight'] < 210:
                    dbUserData = {'age': userDataNumbers['age'], 'growth': userDataNumbers['growth'],
                                  'weight': userDataNumbers['weight']}
                    userDataResults = calcUserData(userDataNumbers)
                    dbUserData.update(getUserData(userDataNumbers))
                    dbUserData['calories'] = userDataResults['calories']
                    dbUserData['proteins'] = userDataResults['proteins']
                    dbUserData['fats'] = userDataResults['fats']
                    dbUserData['carbohydrates'] = userDataResults['carbohydrates']
                    userInfo = {'calories': str(dbUserData['calories']), 'proteins': str(dbUserData['proteins']),
                                'fats': str(dbUserData['fats']), 'carbohydrates': str(dbUserData['carbohydrates']),
                                'IMT': calcIMT(dbUserData['growth'], dbUserData['weight'])}
                    is_valid = True
    if "save_data" in request.POST:
        user_photo = Profile.objects.filter(user=request.user)[0].photo
        user_info = Profile(user=request.user, age=dbUserData["age"], weight=dbUserData["weight"],
                            gender=dbUserData["gender"], growth=dbUserData["growth"],
                            user_aim=dbUserData["user_aim"],
                            Activity_level=dbUserData["activity_level"], needed_kkal=dbUserData["calories"],
                            needed_proteins=dbUserData["proteins"], needed_fats=dbUserData["fats"],
                            needed_carbohydrates=dbUserData["carbohydrates"], photo=user_photo)
        user_info.save()
        return redirect('personalArea')
    cont = {'res': is_valid,
            'error': error_info,
            'form': form,
            'imt': userInfo['IMT'],
            'calories': userInfo['calories'],
            'proteins': userInfo['proteins'],
            'fats': userInfo['fats'],
            'carbohydrates': userInfo['carbohydrates'], }
    return render(request, 'calculator/calculator.html', cont)
