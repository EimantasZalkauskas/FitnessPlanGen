from MuscleGroup import MuscleGroupClass

class ExerciseInfoClass():

    def __init__(self):
        self.muscle_group = MuscleGroupClass()
    
    def db_init(self):
        self.muscle_group.db_connect()
        self.muscle_group.queryReturnArrStringOfVals(self.muscle_group.myConnection, self.muscle_group.query_get_id)
        self.muscle_group.queryReturnAllDataFromTable(self.muscle_group.myConnection, self.muscle_group.query_get_all_from_id, self.muscle_group.arr_of_ids)

        
        #arr = self.get_exercise_by_column_name(self.muscle_group.arr_of_dicts_with_all_data, 'Chest')
        #self.get_unique_split_values(self.muscle_group.arr_of_dicts_with_all_data, 'Push')

    def db_close(self):
        self.muscle_group.db_connection_close()
    
    def get_exercise_by_column_name(self, arr, type):
        output_arr = []
        for dict in arr:
            if type in dict.values():
                output_arr.append(dict)
        
        return output_arr
    
    def get_unique_split_values(self, arr, session_type, column_name):
        output_arr = []
        for dict in arr:
            if session_type in dict.values():                    
                if dict[column_name] not in output_arr:
                    output_arr.append(dict[column_name])
        #print(output_arr)
        return output_arr

    #TODO update db to include muscle trained and update make muscle groups the same 
    
    #load in arr of all the muscles trained that day 
    #set up workout length variable 
    #lopp over arr of muscles of a specific day 
    #loop over all exercises for specirfic muscle 
    #get exercises with highest weighting and store in arr
    #store set_length and rest_time in a workout length variable     


    

inst = ExerciseInfoClass()
inst.db_init()