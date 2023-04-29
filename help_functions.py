import datetime

import requests


def is_t_ok(l1, l2) -> bool:
    # format HH:MM - HH:MM
    time = [0] * 1441
    # print(list(l1) + list(l2))
    for h in list(l1) + list(l2):
        t = h.hours
        b1, b2 = t.split('-')
        a = b1.split(':')
        a = int(a[0]) * 60 + int(a[1])
        b = b2.split(':')
        b = int(b[0]) * 60 + int(b[1])
        time[a] += 1
        time[b + 1] -= 1
        # print(t, b1, b2, a, b, time[a], time[b + 1])
    # print('---------------------------')
    balance = 0
    for i in time:
        balance += i
        if balance >= 2:
            return True
    return False


def get_coordinates(address: str) -> (int, int):
    coords = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b" \
             f"&geocode={address}&format=json"

    print(coords)
    response = requests.get(coords)
    if response:
        json_response = response.json()
        xy = toponym = \
            json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]['Point']['pos']
        xy = f'{xy.replace(" ", ",")}'


def check_address():
    pass


def choose_orders(ords: list, maxw: int) -> list:
    try:
        n, w = len(ords), maxw * 100
        a = list(map(lambda x: int(x * 100), ords))
        c = list(map(lambda x: int(x * 100), ords))
        dp = [[(0, [])] + [(-1, [])] * w for i in range(n)]
        dp[0][0] = (0, [])
        dp[0][a[0]] = (c[0], [1])
        for i in range(1, n):
            for j in range(1, w + 1):
                dp[i][j] = dp[i - 1][j]
                if j - a[i] >= 0 and dp[i - 1][j - a[i]][0] != - 1:
                    if dp[i][j][0] < dp[i - 1][j - a[i]][0] + c[i]:
                        dp[i][j] = (dp[i - 1][j - a[i]][0] + c[i], dp[i - 1][j - a[i]][1] + [i + 1])
        ans = max(dp[-1])[1]
        return list(map(lambda x: x - 1, ans))
    except IndexError:
        return []


def from_few_fields_to_json(t, rs, whs):
    d = {
        'courier_type': t,
        'regions': list(map(int, rs.split(','))),
        'working_hours': whs.split(',')
    }
    return d


def parse_time(raw_time: datetime.time) -> str:
    h = raw_time.hour
    m = raw_time.minute
    return ('0' if (h < 10) else '') + str(h) + ":" + ('0' if (m < 10) else '') + str(m)


def parse_to_about(type_of_courier: str, region: int, start_time: datetime.time, end_time: datetime.time) -> str:
    return type_of_courier + ';' + str(region) + ';' + parse_time(start_time) + '-' + parse_time(end_time)


def parse_from_about(about: str) -> (str, int, datetime.time, datetime.time):
    if about == "":
        return None
    data = about.split(";")
    type_of_courier = data[0]
    region = int(data[1])
    start_time, end_time = data[2].split('-')
    h1, m1 = map(int, start_time.split(':'))
    start_time = datetime.time(h1, m1)
    h2, m2 = map(int, end_time.split(':'))
    end_time = datetime.time(h2, m2)
    return type_of_courier, region, start_time, end_time
