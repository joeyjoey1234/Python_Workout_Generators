import random
ab_exer = [
   "AB-Wheel:",
   "Plank:",
   "Wieghted Situps:",
   "Standing Cable Crunch:",
   "Dumbbell Side Bend:",
   "Decline sit ups:",
   'Sit-up:',
   "Crunch:",
    "Bench-Press Sit-Up:",
    "Windmill:",
    "Resistance Band Frankenstein Twist:"
]

carryover = [
   "Farmer's Walks:",
   "Clean & Press:",
   "Jumping:",
   "Good Mornings:",
    "Bulgarian split squat:",
    "Step-ups:",
    "Kettlebell Swings:",
    "Pull-ups"
]
random_bodybuilding = [
     "Shrugs:",
     "Calf Raises:",
     "Neck Workout:",
     "Chest flys:",
    "Shoulder row:",
    "Machine PullDowns:",
    "Shoulder Press:",
    "Curls:",
    "Leg Extentions",
    "Leg Curls",
    "dumbbell rows",
    "Barbell Rows",
    "Back Extentions",
    "RDL",
    "Tricep Extention",
    "Skull crushers"

]

Cardio = [
    "Stationary bike:",
    "Extersize bike:",
    "Tredmil:",
    "Rowing Machine:",
    "Stair Stepper:",
    "Prowler Pushing:"
]
effort = ['Easy (Endurance)','Medium (Heart Rate)', "Hard (V02)"]
week = input('What difficulty did you want this week to be? Do not skip difficulty, Progress slowly (0-6) ')
week = int(week)

Main_lift_percentages = [.60,.65,.70,.75,.80,.85,.90]
acc_lift_percentages = [.60,.65,.70,.70,.70,.70,.75]

this_weeks_main_percentage = Main_lift_percentages[week]
this_weeks_acc_percentage = acc_lift_percentages[week]

Main_lift_Sets_reps = {.60:"5x12",.65:'5x10',.70:"5x10",.75:"5x8",.80:"5x5",.85:"5x4",.90:"5x3"}

acc_lift_Sets_reps = ['3x10','3x10','3x10','4x10','4x10','5x10','5x10']

ab_exer_sets_reps = ['3x10','4x10','5x11','5x12','5x13','5x14','5x15']



bench_max = 240
Squat_max = 305
Deadlift_max = 230
curl_max = 0
narrow_stance_squat_max = 0



workout1 = {
    ## Percentage based off week, Weight based off percentage, sets & reps based off Percentage
    '':'',
    random_bodybuilding[random.randrange(0, 16, 1)]: 'Percentage:{}%, Sets&Reps:{}'.format(this_weeks_acc_percentage,
                                                                                          acc_lift_Sets_reps[week]),
    ab_exer[random.randrange(0, 11, 1)]: 'Sets&Reps:{}'.format(ab_exer_sets_reps[week]),
    carryover[random.randrange(0, 8, 1)]: 'Percentage:{}%, Sets&Reps:{}'.format(this_weeks_acc_percentage,
                                                                                acc_lift_Sets_reps[week]),
    random_bodybuilding[random.randrange(0, 16, 1)]: 'Percentage:{}%, Sets&Reps:{}'.format(this_weeks_acc_percentage,
                                                                                          acc_lift_Sets_reps[week]),
    random_bodybuilding[random.randrange(0, 16, 1)]: 'Percentage:{}%, Sets&Reps:{}'.format(this_weeks_acc_percentage,
                                                                                          acc_lift_Sets_reps[week]),
    random_bodybuilding[random.randrange(0, 16, 1)]: 'Percentage:{}%, Sets&Reps:{}'.format(this_weeks_acc_percentage,
                                                                                          acc_lift_Sets_reps[week]),
    " ":""
}


workout_pick = [workout1]

This_weeks_workout = [workout_pick[0]]

for x in This_weeks_workout:
    for y in x:
        print(y,x[y])
        #print(y)
print("Anything extra done is up to user")
