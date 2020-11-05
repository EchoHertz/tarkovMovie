import datetime
import pprint as pp


# 첫번째 레이드 영상속 들어간 시간
# PS.1:00:00 되기 전에 게임 들어가야함 ㅋㅋㅋㅋ
firstTime = '17:35'

applicationLog = open('log_2020.11.04_12-55-42_0.12.8.9660/2020.11.04_12-55-42_0.12.8.9660 application.log')
notificationLog = open('log_2020.11.04_12-55-42_0.12.8.9660/2020.11.04_12-55-42_0.12.8.9660 notifications.log')

startLogs = list(filter(lambda x: 'GameStarted' in x, applicationLog.readlines()))
endLogs = list(filter(lambda x: 'UserMatchOver' in x, notificationLog.readlines()))

startTimes = list(map(lambda x: x.split('|')[0], startLogs))
endTimes = list(map(lambda x: x.split('|')[0], endLogs))

def deleteTimezone(x:str):
    _temp = x.split(' ')
    _temp.pop()
    return ' '.join(_temp)

def minToSec(x:str):
    _x = x.split(':')
    return (int(_x[0]) * 60 + int(_x[1]))

def secToTime(x:str):
    return str(datetime.timedelta(seconds=int(x)))


startTimes = list(map(lambda x:deleteTimezone(x), startTimes))
endTimes = list(map(lambda x:deleteTimezone(x), endTimes))

FMT = '%Y-%m-%d %H:%M:%S.%f'
FMT2 = '%M:%S'

firstGame = datetime.datetime.strptime(startTimes[0], FMT) - datetime.timedelta(seconds=minToSec(firstTime))

timeLine2 = ''
timeLine = []
if len(startTimes) == len(endTimes):

    for i in range(0, len(startTimes)):
        s = datetime.datetime.strptime(startTimes[i], FMT)
        e = datetime.datetime.strptime(endTimes[i], FMT)
        _durationSec = abs((s - e).total_seconds())

        timeLine2 += (secToTime((s - firstGame).total_seconds()) + ' ~ ' + secToTime((e - firstGame).total_seconds()) + '\n')

        timeLine.append({
            "start": {
              "original": s.strftime('%Y-%m-%d %H:%M:%S'),
              "inTimeLine": secToTime((s - firstGame).total_seconds())
            },
            "end": {
              "original": e.strftime('%Y-%m-%d %H:%M:%S'),
              "inTimeLine": secToTime((e - firstGame).total_seconds())
            },
            "durationSec": _durationSec.__trunc__(),
            "durationMin": _durationSec // 60,
            "nthGame": i + 1
        })

pp.pprint(timeLine, indent= 2, width=80, depth=10, compact= True, sort_dicts= False)
print('\n')

print(timeLine2)
