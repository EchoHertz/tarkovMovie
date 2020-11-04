# 스폰 됐을때 로그
- application.log

2020-11-04 16:36:42.233 +09:00|0.12.8.9660|Info|application|GamePooled:61.57(21.27) real:90.96(24.26) diff:29.38
2020-11-04 16:36:42.462 +09:00|0.12.8.9660|Info|application|GameRunned:61.57(0) real:91.19(0.23) diff:29.62
2020-11-04 16:36:42.583 +09:00|0.12.8.9660|Info|application|GameSpawn:61.69(0.11) real:91.31(0.11) diff:29.61
2020-11-04 16:36:42.805 +09:00|0.12.8.9660|Info|application|PlayerSpawnEvent:61.98(0.29) real:91.54(0.23) diff:29.56
2020-11-04 16:36:44.976 +09:00|0.12.8.9660|Info|application|GameSpawned:63.6(1.61) real:93.71(2.16) diff:30.11
2020-11-04 16:36:45.685 +09:00|0.12.8.9660|Info|application|GameStarted:63.69(63.68) real:94.42(94.41) diff:30.72

- notification.log

2020-11-04 16:39:44.837 +09:00|Info|push-notifications|Got notification | UserConfirmed
{
  "profileid": "5f676bb99a6be16425687dbf",
  "status": "Busy",
  "ip": "92.38.165.134",
  "port": 17000,
  "sid": "92.38.165.134-17000_PID_04.11.20_07.05.42",
  "version": "live",
  "location": "Interchange",
  "mode": "deathmatch",
  "shortId": "0EY8",
  "additional_info": []
}

#죽어서 나왔을 때
- application.log

2020-11-04 16:41:26.100 +09:00|0.12.8.9660|Info|application|Disposing BEClient
2020-11-04 16:41:26.100 +09:00|0.12.8.9660|Info|application|BEClient exit
2020-11-04 16:41:26.202 +09:00|0.12.8.9660|Info|application|BEClient exit successfully

- notification.log

 2020-11-04 16:39:44.837 +09:00|Info|push-notifications|Got notification | UserMatchOver
{
  "profileid": "5f676bb99a6be16425687dbf",
  "status": "Free",
  "ip": "92.38.165.134",
  "port": 17000,
  "sid": "92.38.165.134-17000_PID_04.11.20_07.05.42",
  "version": "live",
  "location": "Interchange",
  "mode": "deathmatch",
  "shortId": "0EY8",
  "additional_info": []
}
