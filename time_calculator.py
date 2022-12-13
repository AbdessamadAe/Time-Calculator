def add_time(start, duration, day=False):

  wdays =  [
        'monday', 'tuesday',
        'wednesday', 'thursday',
        'friday', 'saturday',
        'sunday'
      ]
  
  scoords = start.split(':')
  scoords2 = scoords[1].split()
  sh = int(scoords[0])
  sm = int(scoords2[0])
  AP = scoords2[1]
  dcoords = duration.split(":")
  dh = int(dcoords[0])
  dm = int(dcoords[1])
  rh = sh + dh
  rm = sm + dm

  addindex =0
  rdays = rh/24
  if rdays>=1:
    addindex=int(rdays)
    rh=rh%24
    
  if rm>=60:
    rh=rh+1
    rm=rm%60
    
  if rh>=12:
    if AP=="AM":
      AP="PM"
    elif AP=="PM":
      AP="AM"
      addindex+=1
      
    rh = rh%12
    if rh==0:
      rh=12
  
  if day:
    rday = wdays[(wdays.index(day.lower())+addindex)%7]

  if day==False and addindex==0:
    new_time = f'{rh}:{rm:02} {AP.upper()}'
    
  if day!=False and addindex==0:
    new_time = f'{rh}:{rm:02} {AP.upper()}, {rday.title()}'
  
  elif day==False and addindex==1:
    new_time = f'{rh}:{rm:02} {AP.upper()} (next day)'
  elif day==False and addindex>1:
    new_time = f'{rh}:{rm:02} {AP.upper()} ({addindex} days later)'
  elif day!=False and addindex==1:
    new_time = f'{rh}:{rm:02} {AP.upper()}, {rday.title()} (next day)'
  elif day!=False and addindex>1:
    new_time = f'{rh}:{rm:02} {AP.upper()}, {rday.title()} ({addindex} days later)'
    
  
  return new_time