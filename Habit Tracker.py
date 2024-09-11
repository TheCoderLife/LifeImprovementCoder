import pandas as pd

MYDATA={
'Date':[1,2,3,4,5,6],
'LONG BAR CURLS(15)':[20,20,0,0,20,20],
'LONG BAR CURLS Total':[300,300,0,0,300,300],
'Inclined Pushups(10)':[0,0,0,2,0,2],
'Plank(1min)':[0,0,0,0,0,0],
'Squats(20)':[0,0,0,0,0,0],
'Novel : 100':[0,0,0,0,0,0],
'Novel : Rich Dad,Poor Dad':[0,0,0,0,0,0],
'Novel : Ichigo Ichie':[0,0,0,0,0,0],
'Education : CISI':[0,0,0,0,0,0],
'Intraday Trading':[0,0,0,0,0,0],
'Python Class':[0,0,0,0,0,0],
'Python Project':[0,0,0,0,0,0],
'Piano':[0,0,0,0,0,0],
'Da Vinci Resolve':[0,0,0,0,0,0],
'.Net Exam':[0,0,0,0,0,0],   
}
myinfo=(pd.DataFrame(MYDATA))
print(myinfo)
