import requests
import settings
import ui_tkinter as ui

def ids_download():
    ids = []
    names = []
    ct = []
    
    try:
        response = requests.get(settings.api_folder + 'transalator_app.php', params={'download_list': 'True'})
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        data = response.text
        lines = data.split('\n')
        
        # Remove the last element from the list
        if lines:
            lines = lines[:-1]

        print(lines)

        for line in lines:
            parts = line.split(';')
            print(parts)
            ids.append(parts[0])
            print(parts[0])
            ct.append(parts[1])
            print(parts[1])
            names.append(parts[2])
            print(parts[2])
    except requests.RequestException as e:
        print("Error fetching data:", e)
        # Handle the error gracefully, maybe retry or log it

    return ids, names, ct

def search(arr: list, term: str):
    out = []

    for i in range(len(arr)):
        if str(arr[i]) in str(term) or str(term) in str(arr[i]):
            out.append(i)

    return out

def mainearchforids():
    ids, names, ct = ids_download()
    arr = search(names, ui.input_question('Searching', 'Please enter a seachterm'))
    print(arr)
    arr2 = []
    for i in range(len(arr)):
        arr2.append(names[arr[i]])
    
    if len(arr2) == 0:
        ui.popup_main('Error', 'There are no results for your search and exiting', time=10000)
        exit('no search results error')
    elif len(arr2) == 1:
        ui.popup_main('Search', 'There was only one result for your search. \n Selecting The only option...')
        index = arr[0]
        print('Only one entry. ')
        print('Chosen one' + str(index))
    else:
        index = ui.multiple_choice('Please select a pack to use', arr2)
    
    out = ids[index]
    return out

if __name__ == '__main__':
    print('Debuging')

    ids, names, ct = ids_download()

    print('Data downloaded successfully.')
    print('IDs:', ids)
    print('Names:', names)
    print('Ct:', ct)

    #print(search(names, input('Searchterm: ', ids)))
    print(mainearchforids())