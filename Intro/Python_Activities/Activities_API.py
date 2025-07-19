import requests 
import pandas as pd

# Step 1: API credentials and endpoint
api_key = "b7c50ab"

base_url = "https://www.omdbapi.com/"
params = {"apikey": api_key, "s":"star wars"}

# Step 2: Send GET request
response = requests.get(base_url, params = params)

# Step 3: Check for successful response
if response.status_code == 200:
    results = response.json()["Search"]
else:
    print("Error",response.status_code)

# Step 4: Parse JSON into structured list
movies_list = []
for result in results:
    movies_details  = {
        "Title": result["Title"],
        "Year": result["Year"],
        "ID": result["imdbID"],
        "Type": result["Type"]
    }
    movies_list.append(movies_details)

movie_df = pd.DataFrame(movies_list)
print(movie_df)



