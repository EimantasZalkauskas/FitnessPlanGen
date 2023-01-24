

class MuscleGroupClass():

    def __init__(self):
        self.exercise_id = None
        self.group = None
        self.split_category = None
        self.essential_weighting = None
        self.difficulty = None
    
    def db_connect(self):
        hostname = 'db.bit.io'
        username = 'EimantasZ'
        password = 'v2_3yLM5_pziuTrAAykrhRKCZeTWC7mS'
        database = 'EimantasZ/FitnessDb'

        print( "Using psycopg2:" )
        import psycopg2
        myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
        self.doQuery( myConnection )
        myConnection.close()

        # Simple routine to run a query on a database and print the results:
    def doQuery(self, conn ) :
        cur = conn.cursor()

        cur.execute("""SELECT * FROM  "MuscleGroup"; """)

        for item in cur.fetchall() :
            print( item )


inst = MuscleGroupClass()
inst.db_connect()