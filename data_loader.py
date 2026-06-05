import pandas as pd

def load_data():

    df = pd.read_csv(
        "data/HHS_Unaccompanied_Alien_Children_Program.csv"
    )

    return df