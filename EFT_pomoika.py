import requests

def run_query(query):
    headers = {"Content-Type": "application/json"}
    response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))


new_query = """
{
   
  itemsByName(name: "AK-12 5.45x39 sound suppressor") {
    avg24hPrice
    sellFor {
      price,
      vendor{name}
    }
  }
}
"""

result = run_query(new_query)
print(result)