import requests
from tkinter import*
from tkinter import ttk


def run_query(aue=None):
    query = '''
    {
      itemsByName(name: "''' + entry.get() + '''") {
        avg24hPrice
        sellFor {
          price,
          vendor{name}
        }
      }
    }
    '''
    headers = {"Content-Type": "application/json"}
    response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
    if response.status_code == 200:
        kot = "o predmete\n"
        for i in response.json()['data']['itemsByName']:
            kot+=f'\navg: {i["avg24hPrice"]}\nsellFor:\n'
            for j in i["sellFor"]:
                kot+=f"   цена: {j['price']} vender:{j['vendor']['name']}\n"
            kot+="--------------------"
        label['text']=kot
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))


root=Tk()
root.title('Romapidor')
root.geometry('300x600')
entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
btn = ttk.Button(text="iwiMraz'", command=run_query)
btn.pack(anchor=NW, padx=6, pady=6)
entry.bind('<Return>',run_query)
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

root.mainloop()
