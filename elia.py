import pandas as pd
df=pd.read_csv('https://opendata.elia.be/explore/dataset/ods039/download/?format=csv&timezone=Europe/Brussels&lang=en&use_labels_for_header=true&csv_separator=%3B', sep=';')
df.to_csv('Unplanned_unavailibilities.csv')
