import pandas as pd
import numpy as np

# clean entries so they all match and can be indexed
# other stuff

entrances = 'DOITT_SUBWAY_ENTRANCE_01_13SEPT2010.csv'
arts = 'Arts_For_Transit_-_Metropolitan_Transportation_Authority__MTA__Permanent_Art_Catalogue.csv'
wifi = 'MTA_Wi-Fi_Locations.csv'

entr_df_raw = pd.read_csv(entrances)
arts_df_raw = pd.read_csv(arts)
wifi_df_raw = pd.read_csv(wifi)

# function to replace a column in the raw df with cleaned data
def replace_col(data_raw, col_name, clean_list):
    # create df from clean list
    data_CLEAN = pd.DataFrame({col_name:clean_list})
    # update old df with clean list
    data_raw.update(data_CLEAN)
    return data_raw[col_name]


# function to split up strings containing train lines, containing function to update the column in the raw df
def lineclean(data_raw, col_name, sep):
    # list on lines from entrances csv
    data_line = data_raw[col_name]
    # create clean list of lines
    line_list = []
    for i in data_line.index:
        line_list.append(data_line[i].split(sep))
    return replace_col(data_raw, col_name, line_list)


def main():
    entr_line = lineclean(entr_df_raw, 'LINE', '-')
    # combine entries where the names are the same before 'at' [...]
    # the problem is that some of these entries refer to the same station but have different cross streets
    entr_station = entr_df_raw['NAME']
    # # entr_station_list = []
    # for i in entr_station.index:
    #     temp = str(entr_station[i]).split(' at ')[0]
    #     entr_station_list.append(temp)
    # entr_station = replace_col(entr_df_raw, 'NAME', entr_station_list)
    entr_df = pd.concat([entr_station, entr_line], axis = 1)
    print(entr_df)


    arts_line = lineclean(arts_df_raw, 'Line', ',')
    # clean up names so they match a standard format
    arts_station = arts_df_raw['Station Name']
    arts_df = pd.concat([arts_station, arts_line], axis = 1)
    # print(arts_df)


    wifi_station = wifi_df_raw['Station Name']
    wifi_line = wifi_df_raw['Lines']
    wifi_df = pd.concat([wifi_station, wifi_line], axis = 1)
    # print(wifi_df)


if __name__ == '__main__':
    main()
