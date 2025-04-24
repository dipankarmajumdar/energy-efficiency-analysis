import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def load_data(filepath):
    df = pd.read_csv(filepath)
    df.columns = ['Relative_Compactness', 'Surface_Area', 'Wall_Area', 'Roof_Area',
                  'Overall_Height', 'Orientation', 'Glazing_Area', 'Glazing_Area_Distribution',
                  'Heating_Load', 'Cooling_Load']
    return df

def preprocess_data(df):
    df = pd.get_dummies(df, columns=['Orientation', 'Glazing_Area_Distribution'], drop_first=True)
    X = df.drop(['Heating_Load','Cooling_Load'], axis=1)
    y = df[['Heating_Load', 'Cooling_Load']]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return train_test_split(X_scaled,y,test_size=0.2, random_state=42), scaler
