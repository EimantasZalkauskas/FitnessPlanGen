import psycopg2

class MuscleGroupClass():

    def __init__(self):
        self.exercise_id = None
        self.group = None
        self.split_category = None
        self.essential_weighting = None
        self.difficulty = None
        self.myConnection = None
        self.query_get_id = """SELECT "ExerciseID" FROM  "ExerciseInfo" WHERE "Difficulty" = 'Low' OR "Difficulty" = 'Mid'; """
        self.query_get_all_from_id = """SELECT * FROM  "ExerciseInfo" WHERE "ExerciseID" = '{}' """
    
    def db_connect(self):
        hostname = 'db.bit.io'
        username = 'EimantasZ'
        password = 'v2_3yLM5_pziuTrAAykrhRKCZeTWC7mS'
        database = 'EimantasZ/FitnessDb'

        self.myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
    
    def db_connection_close(self):
        self.myConnection.close()

        # Simple routine to run a query on a database and print the results:
    def queryReturnArrStringOfIds(self, conn, query) :
        arr = []
        string = ''
        cur = conn.cursor()
        cur.execute(query)
        
        for item in cur.fetchall() :
            string = ''.join(map(str,item)) 
            arr.append(string)

        #print(arr)
        return arr
    
    def queryReturnAllDataFromTable(self, conn, query, arr_id):
        cur = conn.cursor()

        for item in arr_id:
            cur.execute(query.format(item))
            for row in cur.fetchall():
                print(row)

inst = MuscleGroupClass()
inst.db_connect()
arr = inst.queryReturnArrStringOfIds(inst.myConnection, inst.query_get_id)
inst.queryReturnAllDataFromTable(inst.myConnection, inst.query_get_all_from_id, arr)
inst.db_connection_close()
#print(arr)