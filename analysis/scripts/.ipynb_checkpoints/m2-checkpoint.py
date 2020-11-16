import pandas as pd

def load_data(url):

    df = ( 
       pd.read_csv(url)
      .rename(columns={"Displ" : "Displacement", "Cyl" : "# of Cylinders", "Trans" : "Transmission", "Veh Class" : "Type", "Hwy MPG" : "Highway MPG", "Cmb MPG" : "Combined MPG"})
      .drop(["Cert Region", "Stnd", "Stnd Description", "Underhood ID", "Air Pollution Score", "Greenhouse Gas Score", "SmartWay", "Comb CO2"], axis=1)
      .reset_index(drop=True)
     )

    return df

def save_data(df, url):
    
    df.to_csv(url, index=False) 
    
    return