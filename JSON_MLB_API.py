#fine the URL for the API

import urllib.parse #import the library so that python cand handle the calls

import requests     #import the requests module

import json

main_mlb_api = 'http://lookup-service-prod.mlb.com'  #build the base of the url

list_teams ='/json/named.team_all_season.bam?'

sport_code="'mlb'"
param_sport_code = {'sport_code': sport_code }      #the parameter and parameter value need to be in the tuple sytax

all_star = "'N'"                                    #all star value - 'Y' or 'N'
param_all_star= {'all_star_sw': all_star }        #build the all star parameter string

sort_order= 'name_asc'
param_sort_order = {'sort_order': sort_order}

season='2019'
param_season= {'season': season}

# Could the below statement be written more elagantly with a loop and a dictionary with key=value pairs?
#build the API parameters
url= main_mlb_api + list_teams + urllib.parse.urlencode(param_sport_code)  +'&' +urllib.parse.urlencode (param_all_star) +'&' +urllib.parse.urlencode(param_sort_order)+'&' +urllib.parse.urlencode(param_season)     #combine the base and parameters of the URL Individual key=value pairs are seperated by &

json_data=requests.get(url).json()                              #use the requests library to send a get request to the
                                                                #api url
                                                                #json_data is a 'dict' type
#print(json_data)
#print(type(json_data['team_all_season']))

#print(len(json_data))                                          #returns the number of data elements in the dict key
#print(json_data['team_all_season'])


for row in json_data['team_all_season']['queryResults']['row']:     #turn through the dict returned by api and fetch only one parameter

    print(row['name_display_long'])









#for row in json_data['team_all_season']['queryResults']:
 #   print(['name_display_long'])

#print(type(json_data[]))






