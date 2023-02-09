import psycopg2
import json

class MuscleGroupClass():

    def __init__(self):
        self.myConnection = None

        self.arr_of_ids = None
        self.query_get_id = """SELECT "ExerciseID" FROM  "ExerciseInfo" WHERE "Difficulty" = 'Low' OR "Difficulty" = 'Mid'; """
        self.arr_of_dicts_with_all_data = None
        self.query_get_all_from_id = """SELECT * FROM  "ExerciseInfo" WHERE "ExerciseID" = '{}' """
        self.select_from_group_column_query = """SELECT Group FROM  "ExerciseInfo" WHERE "Base_Category" = {} """


    
    def db_connect(self):
        hostname = 'db.bit.io'
        username = 'EimantasZ'
        password = 'v2_3yLM5_pziuTrAAykrhRKCZeTWC7mS'
        database = 'EimantasZ/FitnessDb'

        self.myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
    
    def db_connection_close(self):
        self.myConnection.close()

        # Simple routine to run a query on a database and print the results:
    def queryReturnArrStringOfVals(self, conn, query) :
        arr = []
        string = ''
        cur = conn.cursor()
        cur.execute(query)
        
        for item in cur.fetchall() :
            string = ''.join(map(str,item)) 
            arr.append(string)

        #print(arr)
        self.arr_of_ids = arr
        # return arr
    
    def queryReturnAllDataFromTable(self, conn, query, arr_id):
        cur = conn.cursor() 
        output_arr = []

        for item in arr_id:
            new_dict = {}
            cur.execute(query.format(item))
            row_vals = cur.fetchall()
            for row in row_vals:
                new_dict = {
                    "ExerciseID" : row[0],
                    "Group" : row[1], 
                    "Split_Category" : row[2], 
                    "Essential_Weighting" : row[3], 
                    "Difficulty" : row[4], 
                    "Name" : row[5], 
                    "Type" : row[6], 
                    "Set_Length" : row[7], 
                    "Rest_Time" : row[8],
                    "Muscle_Trained": row[9],
                    "Base_Category": row[10]
                }
                output_arr.append(new_dict)

        self.arr_of_dicts_with_all_data = output_arr
        # return output_arr





# inst = MuscleGroupClass()
# inst.db_connect()
# arr = inst.queryReturnArrStringOfIds(inst.myConnection, inst.query_get_id)
# all_value_dicts_in_arr =inst.queryReturnAllDataFromTable(inst.myConnection, inst.query_get_all_from_id, arr)
# inst.db_connection_close()
# print(all_value_dicts_in_arr)

