from ExerciseInfo import ExerciseInfoClass

class WorkoutDayGen():
    def __init__(self, exerciseInfo, user_exp_lvl, workout_focus, session_type, workout_length):
        self.exerciseInfo = exerciseInfo
        self.user_exp_lvl = user_exp_lvl
        self.workout_focus = workout_focus
        self.session_type = session_type
        self.workout_length = workout_length
        self.difficulty_option_arr = ['Low', 'Mid', 'High']
        self.exercise_focus_rep_dict = {"Build Muscle" : "8 - 12", "Get Stronger" : "4 - 6", "Endurance" : "15 - 20"}
        self.exercise_set_ranges = {"Compound" : 4, "Isolation" : 3}
        self.workout_arr = []
        self.group_total = 0
    
    def run(self):
        #Look into db
        self.exerciseInfo.db_init()
        session_muscle_groups_trained_arr = self.exerciseInfo.get_unique_split_values(self.exerciseInfo.muscle_group.arr_of_dicts_with_all_data, self.session_type, 'Group')

        arr = self.gen_exercise_list_from_groups(session_muscle_groups_trained_arr, 60)
        print(arr)
        #Combine exercises into workout arr 
        self.exerciseInfo.db_close()


    def gen_exercise_list_from_groups(self, muscle_group_arr, workout_length):
        group_exercise_arr = []
        allocated_group_time = workout_length / len(muscle_group_arr)
        current_group_total_time = 0
        #Loop over each item of arr
        for group in muscle_group_arr:
            while current_group_total_time < allocated_group_time:
            #for each group select highest essential weighting exercise if not already in list 
                exercise = self.return_highest_weighting_exercise(group, group_exercise_arr)
                
            #for each exercise assign set / rep value 
                full_exercise_info = self.return_exercise_sets_reps(exercise)
                group_exercise_arr.append(full_exercise_info)
            #check if allocated time for group is not exceeded with set num 
                current_group_total_time = self.check_group_total_time(group_exercise_arr, group)
            current_group_total_time = 0
        return group_exercise_arr
    
    def return_highest_weighting_exercise(self, group, arr_of_exercises):
        highest_weight_exercise = 0
        exercise = None
        for dict in self.exerciseInfo.muscle_group.arr_of_dicts_with_all_data:
            if dict['Group'] == group:
                if self.check_exercise_in_list(arr_of_exercises, dict) == False:
                    if dict['Difficulty'] == self.difficulty_option_arr[self.user_exp_lvl]:
                        if dict['Essential_Weighting'] > highest_weight_exercise:
                            highest_weight_exercise = dict['Essential_Weighting']
                            exercise = dict
                    elif self.user_exp_lvl == 2:
                        if dict['Difficulty'] == self.difficulty_option_arr[self.user_exp_lvl-1]:
                            highest_weight_exercise = dict['Essential_Weighting']
                            exercise = dict
                    elif dict['Difficulty'] == self.difficulty_option_arr[self.user_exp_lvl+1]:
                        if dict['Essential_Weighting'] > highest_weight_exercise:
                            highest_weight_exercise = dict['Essential_Weighting']
                            exercise = dict
        return exercise
    
    def check_exercise_in_list(self, exercise_arr, exercise):
        count = 0
        for item in exercise_arr:
            if item['Exercise Info'] == exercise:
                return True
        
        return False


    def return_exercise_sets_reps(self, exercise):
        #Check what the workout focus is get rep ranges from it 
        current_exercise_length = 0
        rep_ranges = self.exercise_focus_rep_dict[self.workout_focus]
        current_set_amount = self.exercise_set_ranges[exercise['Type']]
        #Assign number of sets and get total exercise length 
        for i in range(0, current_set_amount):
            current_exercise_length += exercise['Set_Length'] + exercise['Rest_Time']

        #Combine sets, reps, exercise length and exercise info into new dict and return 
        full_exercise_info = {
            "Sets" : current_set_amount,
            "Reps" : rep_ranges,
            "Exercise Length" : current_exercise_length,
            "Exercise Info" : exercise
        }
        return full_exercise_info

    def check_group_total_time(self, group_arr, group):
        total_time = 0
        for item in group_arr:
            if group in item['Exercise Info'].values():
                total_time += item['Exercise Length']
        return total_time

inst = ExerciseInfoClass()
test = WorkoutDayGen(inst, 0, 'Build Muscle', "Push", 60)

test.run()

##### INPUT VARS #######
