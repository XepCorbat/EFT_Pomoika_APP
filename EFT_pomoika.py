import requests
from tkinter import *
from tkinter import ttk


def run_query(aue=None):
    query = '''
    {
      items(lang: ru, name: "''' + entry.get() + '''") {
        avg24hPrice
        name
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
        subject_values = "o predmete\n"
        print(response.json())
        for i in response.json()['data']['items']:
            subject_values += f'\n{i["name"]}:\n Средняя цена на барахолке -> {i["avg24hPrice"]}\n'
            for j in i["sellFor"]:
                subject_values += f" {j['vendor']['name']} -> {j['price']} \n"
            subject_values += "--------------------"
        label['text'] = subject_values
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))


root = Tk()
root.title('Romapidor')
root.geometry('300x600')
entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
btn = ttk.Button(text="iwiMraz'", command=run_query)
btn.pack(anchor=NW, padx=6, pady=6)
entry.bind('<Return>', run_query)
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

root.mainloop()
