import sqlite3
from apec_scrap import main_apec
from wttj_scrap import main_wttj

def db_file_storage(db_name, table_name, df):

    # Connexion à la base de données SQLite
    conn = sqlite3.connect(f"../data/{db_name}.db")
    
    # Enregistrer le DataFrame dans la base de données
    df.to_sql(name=table_name, con=conn, if_exists='append', index=False)
    
    # Fermer la connexion
    conn.close()

def update():

    try:
        df_apec = main_apec()
        db_file_storage('apec', 'df_clean', df_apec)
    except:
        print("Error APEC")
        pass

    try:
        df_wttj = main_wttj
        db_file_storage('wttj', 'df_clean', df_wttj)
    except:
        print("Error WTTJ")
        pass





