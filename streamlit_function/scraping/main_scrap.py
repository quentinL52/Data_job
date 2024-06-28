import sqlite3
from streamlit_function.scraping.apec_scrap import main_apec
from streamlit_function.scraping.wttj_scrap import main_wttj
from streamlit_function.scraping.cadreemploi_scrap import main_cadreemploi
from streamlit_function.scraping.hellowork_scrap import main_hellowork
from streamlit_function.scraping.freework_scrap import main_freework

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
        df_wttj = main_wttj()
        db_file_storage('wttj', 'df_clean', df_wttj)
    except:
        print("Error WTTJ")
        pass

    try:
        df_cadreemploi = main_cadreemploi()
        db_file_storage('cadreemploi', 'df_clean', df_cadreemploi)
    except:
        print("Error cadreemploi")
        pass

    try:
        df_hellowork = main_hellowork()
        db_file_storage('hellowork', 'df_clean', df_hellowork)
    except:
        print("Error hellowork")
        pass

    try:
        df_freework = main_freework()
        db_file_storage('freework', 'df_clean', df_freework)
    except:
        print("Error freework")
        pass





