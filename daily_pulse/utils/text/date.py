from datetime import date, timedelta


def getSuffixOfDay(day):
    suffix = ""

    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]

    return suffix


def getTargetDate():
    today = date.today()
    is_monday = today.weekday() == 0
    date_delta = -3 if is_monday else -1

    return today + timedelta(days=date_delta)


def getFormattedTargetDate(format="%-d-%m-%Y", withSuffix=False):
    target_date = getTargetDate()
    suffix = getSuffixOfDay(target_date.day) if withSuffix else ""
    return target_date.strftime(format) + suffix
