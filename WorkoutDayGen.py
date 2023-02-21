from ExerciseInfo import ExerciseInfoClass

class WorkoutDayGenClass():
    def __init__(self, exerciseInfo, user_exp_lvl, workout_focus, session_type, workout_length, user_gender):
        self.exerciseInfo = exerciseInfo
        self.user_exp_lvl = user_exp_lvl
        self.workout_focus = workout_focus
        self.session_type = session_type
        self.workout_length = workout_length
        self.user_gender = user_gender
        self.difficulty_option_arr = ['Low', 'Mid', 'High']
        self.exercise_focus_rep_dict = {"Build Muscle" : "8 - 12", "Get Stronger" : "4 - 6", "Endurance" : "15 - 20"}
        self.exercise_set_ranges = {"Compound" : 4, "Isolation" : 3}
        self.workout_arr = []
        self.group_total = 0
    
    def run(self):
        #Look into db
        self.exerciseInfo.db_init()
        session_muscle_groups_trained_arr = self.exerciseInfo.get_unique_split_values(self.exerciseInfo.muscle_group.arr_of_dicts_with_all_data, self.session_type, 'Group')

        arr = self.gen_exercise_list_from_groups(session_muscle_groups_trained_arr, self.workout_length)
        #Combine exercises into workout arr 
        self.exerciseInfo.db_close()
        return arr


    def gen_exercise_list_from_groups(self, muscle_group_arr, workout_length):
        group_exercise_arr = []
        allocated_group_time = workout_length / len(muscle_group_arr)
        current_group_total_time = 0
        #Loop over each item of arr
        for group in muscle_group_arr:
            if self.get_group_from_muscle_trained(muscle_group_arr, group_exercise_arr):
                group_weighting = self.get_group_weighting(group)
                current_allocated_time = self.get_allocated_time_from_group_weighting(group_weighting, allocated_group_time)
                while current_group_total_time < current_allocated_time:
                #for each group select highest essential weighting exercise if not already in list 
                    exercise = self.return_highest_weighting_exercise(group, group_exercise_arr)
                    
                #for each exercise assign set / rep value 
                    full_exercise_info = self.return_exercise_sets_reps(exercise)
                    group_exercise_arr.append(full_exercise_info)
                #check if allocated time for group is not exceeded with set num 
                    current_group_total_time = self.check_group_total_time(group_exercise_arr, group)
                current_group_total_time = 0
        return group_exercise_arr
    
    def get_group_from_muscle_trained(self, muscle_group, exercise_arr):
        for item in exercise_arr:
            item['Exercise Info']['Muscle_Trained']
        # for item in muscle_group:
        #     if item == 'Glutes':
        return True
                

    def get_group_weighting(self, group):
        group_weight = 0
        for item in self.exerciseInfo.muscle_group.arr_of_dicts_with_all_data:
            if item['Group'] == group:
                group_weight = item['Group_Weight']
                return group_weight
    
    def get_allocated_time_from_group_weighting(self, weighting, allocated_time):
        if weighting == str(50):
            return allocated_time/2
        elif weighting == str(100):
            return allocated_time
        elif weighting == str(25):
            return allocated_time/4



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
                    elif self.user_exp_lvl == 1: 
                        if dict['Difficulty'] == self.difficulty_option_arr[self.user_exp_lvl-1] or dict['Difficulty'] == self.difficulty_option_arr[self.user_exp_lvl+1]:
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
    
    def check_compound_exercise_in_list(self, exercise_arr, exercise):
        count = 0
        for item in exercise_arr:
            if exercise['Type'] == "Compound" and exercise in item['Exercise Info'].values():
                return True
        
        return False


    def return_exercise_sets_reps(self, exercise):
        #Check what the workout focus is get rep ranges from it 
        current_exercise_length = 0
        current_set_amount = self.exercise_set_ranges[exercise['Type']]
        #Assign number of sets and get total exercise length 
        for i in range(0, current_set_amount):
            current_exercise_length += exercise['Set_Length'] + exercise['Rest_Time']
        
        if self.workout_focus == 'Get Stronger' and exercise['Type'] == 'Compound':
            rep_ranges = self.exercise_focus_rep_dict["Get Stronger"]
        elif exercise['Type'] == 'Isolation' or exercise['Type'] == 'Compound' and self.workout_focus == 'Get Stronger' or self.workout_focus == 'Build Muscle':
            rep_ranges = self.exercise_focus_rep_dict["Build Muscle"]
        elif self.workout_focus == 'Endurance':
            rep_ranges = self.exercise_focus_rep_dict[self.workout_focus]

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
test = WorkoutDayGenClass(inst, 1, 'Build Muscle', "Legs", 60, 'Male')

va = test.run()
print(va)
##### INPUT VARS #######
