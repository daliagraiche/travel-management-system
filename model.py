import mysql.connector 

class VoyageModel:
    def __init__(self):                 # le constructeur
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='voyage'
        )
        self.cursor = self.conn.cursor()


    def creer_table_consultations(self):    #creation de la table consultations
        query = """
        CREATE TABLE IF NOT EXISTS consultations (
            Id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,           
            Destination VARCHAR(100) NOT NULL,                    
            date_depart DATE NOT NULL,                           
            date_retour DATE NOT NULL,                           
            prix FLOAT NOT NULL,                                 
            places_disponibles INT NOT NULL,                     
            Descriptions TEXT
        )                            
        """
        self.cursor.execute(query)
        self.conn.commit()

    def ajouter_voyage(self, Destination, date_depart, date_retour, prix, places_disponibles, Descriptions):
        query = "INSERT INTO consultations (Destination, date_depart, date_retour, prix, places_disponibles, Descriptions) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (Destination, date_depart, date_retour, prix, places_disponibles, Descriptions))
        self.conn.commit()  

    def rechercher_voyage(self,Destination):
        query="SELECT * FROM consultations WHERE Destination LIKE %s"
        self.cursor.execute(query, (f"%{Destination}%",))
        return self.cursor.fetchall()

    def lire_voyages(self):
        self.cursor.execute("SELECT * FROM consultations")
        return self.cursor.fetchall()
    

    def __del__(self):          #fermeture
        self.cursor.close()
        self.conn.close()