def convertdatetime(s):
    try:
        date, time = s.split()
        mm, dd, yyyy = map(int, date.split("/"))
        hh, mi, ss = map(int, time.split(":"))

        if not (1 <= mm <= 12 and 1 <= dd <= 31):
            print("Ошибка")
            return
        if not (0 <= hh <= 23 and 0 <= mi <= 59 and 0 <= ss <= 59):
            print("Ошибка")
            return

        period = "AM"
        if hh >= 12:
            period = "PM"
        hh = hh % 12
        if hh == 0:
            hh = 12

        print(f'{dd:02}.{mm:02}.{yyyy % 100:02} {hh:02}:{mi:02}:{ss:02} {period}')

    except:
        print("Ошибка")
