#MLB_Teams

#pip install requests
import requests

#build the base of the api
mlbTeams = 'https://statsapi.mlb.com/api/v1/teams'

resp = requests.get(mlbTeams)
data = resp.json()


print(data)