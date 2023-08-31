import requests
from tkinter import*
from tkinter import ttk


def run_query():
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
        label["text"]=str(response.json())
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))


root=Tk()
root.title('Romapidor')
root.geometry('300x600')
entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
btn = ttk.Button(text="iwiMraz'", command=run_query)
btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
root.mainloop()
