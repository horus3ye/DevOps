from datetime import datetime as dt

print("Give us your goal and the deadline sparated by a colon :)")
goal_deadline = input().split(":")
    
goal_var = goal_deadline[0]
dealine = goal_deadline[1]
deadline = dt.strptime(dealine, "%d-%m-%Y")
tody_dte = dt.today()
time_rem = deadline - tody_dte
# validating values entered by user..
if time_rem.days <= 3
    print(f"You Still have {int(time_rem.total_seconds() / 60 / 60)} hours to {goal_var} deadline. Do Your best ^_^")
elif time_rem.days <= 30:
    print(f"You Still have {time_rem.days} days to {goal_var} deadline. Do Your best ^_^")
elif time_rem.days > 30:
    time_rem_mon = time_rem.days / 30
    time_rem_mod = time_rem.days % 30
    print(f"You Still have {int(time_rem_mon)} months and {time_rem_mod} days to make your {goal_var} deadline. Do Your best ^_^")
    
