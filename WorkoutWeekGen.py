from WorkoutDayGen import WorkoutDayGenClass
from ExerciseInfo import ExerciseInfoClass



class WorkoutWeekGenClass():

    def __init__(self,exerciseInfo, user_exp_lvl, workout_focus, weekly_sessions, workout_length, user_gender):
        self.exerciseInfo = exerciseInfo
        self.user_exp_lvl = user_exp_lvl
        self.workout_focus = workout_focus
        self.weekly_sessions = weekly_sessions
        self.workout_length = workout_length
        self.user_gender = user_gender
        self.sets_per_week = []

    def run(self):
        arr =self.gen_weekly_workout_play()


    def gen_weekly_workout_play(self):
        output_arr = []
        for item in self.weekly_sessions:
            wokroutDay = WorkoutDayGenClass(self.exerciseInfo, self.user_exp_lvl, self.workout_focus, item, self.workout_length, self.user_gender, self.sets_per_week)
            workout ,self.sets_per_week = wokroutDay.run()
            output_arr.append(workout)
        print(output_arr)
        print(self.sets_per_week)
        return output_arr



#input array of weekly sessions 

#loop over array of weekly sessions to run workoutDay for each session 

#Within workoutDay exercise selection check if exercise is already in weekly workout arr and only add it if the essential weighting is 9 or higher 



weekly_sessions = ['Push', 'Pull', 'Legs','Push', 'Pull', 'Legs']
inst_ex_info = ExerciseInfoClass()
inst = WorkoutWeekGenClass(inst_ex_info, 1, 'Build Muscle', weekly_sessions, 60, "Male")
inst.run()