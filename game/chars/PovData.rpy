# Here is the player's data

define PovStr = 10
define PovPer = 10
define PovEnd = 10
define PovCha = 10
define PovInt = 10
define PovAlg = 10
define PovLuc = 10

define Days = 0
define DaysOfWeekList = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Firday", "Saturday"]
define DayOfWeekNum = 0
define DayOfWeek = DaysOfWeekList[DayOfWeekNum]
define TimeOfDayList = ["Morning", "Noon", "Afternoon", "Evening", "Night"]
define TimeOfDayNum = 0
define TimeOfDay = TimeOfDayList[TimeOfDayNum]

define MGChance = PovLuc + renpy.random.randint(1, 100)

define MGDName = ""
define MGDColor = ""
define MGD = DynamicCharacter("MGName", color="MGColor")
define MGDS = MGStats(5, "", False, 0, 0, False, 10)
define MGDD = MGData(4, 3, False, False, False, False, False, False, False, False, False, False, False, False, False, False)

label TimeJump:
  if TimeOfDayNum > 4:
     $ TimeOfDayNum = 0
     $ DayOfWeekNum += 1
     $ Days += 1
  else:
     $ TimeOfDayNum += 1
     
  if DayOfWeekNum > 6:
     $ DayOfWeekNum = 0
     
  $ DayOfWeek = DaysOfWeekList[DayOfWeekNum]
  $ TimeOfDay = TimeOfDayList[TimeOfDayNum]
  return
