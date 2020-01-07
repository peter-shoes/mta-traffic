import pandas as pd
import numpy as np

# maybe make this like, wifi coverage by station?
# and then who covers?
# maybe customer feedback vs wifi?

entrances = 'DOITT_SUBWAY_ENTRANCE_01_13SEPT2010.csv'
arts = 'Arts_For_Transit_-_Metropolitan_Transportation_Authority__MTA__Permanent_Art_Catalogue.csv'
feedback = 'MTA_Customer_Feedback_Data__Beginning_2014.csv'
wifi = 'MTA_Wi-Fi_Locations.csv'

wifi_df = pd.read_csv(wifi)
fb_df = pd.read_csv(feedback)
entr_df = pd.read_csv(entrances)

# these might be the ones
print(wifi_df['Lines'])
print(entr_df['LINE'])
