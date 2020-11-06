import datetime
import pprint as pp

raidName = "1게임 - 커스텀 0P 사망 (thorax)w2게임 - 커스텀 3P2U 탈출w3게임 - 커스텀 6U 탈출w4게임 - 커스텀 2P 탈출w5게임 - 랩 1R 사망 (head, eyes) w6게임 - 랩 1R 사망 (head, eyes)w7게임 - 쇼어라인 맴몸넘 탈출w8게임 - 랩 1P 사망 (head, top)w9게임 - 랩 0P 사망 (head, top)w10게임 - 랩 0P 사망 (thorax)w11게임 - 랩 0P 사망 (thorax)w12게임 - 랩 2R 토즈런 탈출".split('w')
path = 'C:/Users/윤승재/Downloads/Logs'
logKey = '2020.11.02_9-06-01_0.12.8.9660'

# 첫번째 레이드 영상속 들어간 시간
# PS.1:00:00 되기 전에 게임 들어가야함 ㅋㅋㅋㅋ
firstTime = '18:00'

applicationLog = open(path + '/log_' + logKey + '/' + logKey + ' application.log')
notificationLog = open(path + '/log_' + logKey + '/' + logKey + ' notifications.log')

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
print(len(startTimes))
print(len(endTimes))
if len(startTimes) == len(endTimes):

    for i in range(0, len(startTimes)):
        s = datetime.datetime.strptime(startTimes[i], FMT)
        e = datetime.datetime.strptime(endTimes[i], FMT)
        _durationSec = abs((s - e).total_seconds())

        timeLine2 += raidName[i] + (secToTime((s - firstGame).total_seconds()) + ' ~ ' + secToTime((e - firstGame).total_seconds()) + '\n')
        # timeLine2 += (secToTime((s - firstGame).total_seconds()) + ' ~ ' + secToTime((e - firstGame).total_seconds()) + '\n')

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
            # "raidTitle": raidName[i]
        })

pp.pprint(timeLine, indent= 2, width=80, depth=10, compact= True, sort_dicts= False)
print('\n')

print(timeLine2)
