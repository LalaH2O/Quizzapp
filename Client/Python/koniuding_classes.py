import os
import json
import tkinter as tk
from tkinter import IntVar
import requests
from functs import save_to_file

class ui:
    def __init__(self, title) -> None:
        self.title = title

    def popup_main(self, message: str, time: int = 3000) -> None:
        root = tk.Tk()
        root.title(self.title)
        label = tk.Label(root, text=message)
        label.pack()
        root.after(time, root.destroy)
        root.mainloop()

    def multiple_choice(self, question: str, answers: list) -> int | None:
        window = tk.Tk()
        window.title(self.title)
        
        label = tk.Label(window, text=question)
        label.pack()
        
        v = IntVar()
        v.set(-1)
        
        for i in range(len(answers)):
            tk.Radiobutton(window, text=answers[i], padx=20, variable=v, value=i).pack(anchor=tk.W)

        def on_closing():
            window.quit()
            window.destroy()
        
        button = tk.Button(window, text="Submit", command=on_closing)
        button.pack()
        
        window.mainloop()
        
        return answers[v.get()] if v.get() >= 0 else None

    def input_question(self, question: str) -> str:
        window = tk.Tk()
        window.title(self.title)
        label = tk.Label(window, text=question)
        label.pack()
        
        entry = tk.Entry(window)
        entry.pack()

        def on_closing():
            window.quit()
            window.destroy()
        
        button = tk.Button(window, text="Submit", command=on_closing)
        button.pack()

        window.mainloop()
        return entry.get()
    
    def multiinputs(self, upperquestion: str, questions: list) -> list:
        window = tk.Tk()
        window.title(self.title)
        tk.Label(window, text=upperquestion).pack()

        entries = []
        for question in questions:
            tk.Label(window, text=question).pack()
            entry = tk.Entry(window)
            entry.pack()
            entries.append(entry)
        
        def on_closing():
            self.answers = [entry.get() for entry in entries]
            window.quit()
            window.destroy()
        
        button = tk.Button(window, text="Submit", command=on_closing)
        button.pack()
        
        window.mainloop()
        
        return self.answers

class uilogic:
    def __init__(self) -> None:
        pass

    def ask(self, verb: str, correct_answers: list) -> bool:
        ui_instance = ui(verb)
        pronouns = ['Je', 'Tu', 'Il/Elle', 'Nous', 'Vous', 'Ils/Elles']
        input_answers = ui_instance.multiinputs(f'Conjugate: {verb}', pronouns)
        
        return input_answers == correct_answers

class fs:
    def __init__(self, fdpath) -> None:
        self.folderpath = fdpath
    
    def getallchildren(self) -> list:
        return os.listdir(self.folderpath)
    
    def getchildpath(self, child) -> str:
        return os.path.join(self.folderpath, child)
        
    def loadfiletodict_json(self, file) -> dict:
        with open(file, 'r') as f:
            return json.load(f)

    def askwhatchildtouse(self) -> str:
        ui_instance = ui('Files')
        arr = self.getallchildren()
        arr.append('Download a new file')
        if len(arr) == 1:
            api = api('lassehelbling.ch/api/transalator/')
            return api.download_file()
        else:
            thing = ui_instance.multiple_choice('Please select a file', arr)
            if thing == len(arr) - 1:
                ...
            else:
                return self.getchildpath(arr[thing])

class api:
    def __init__(self, url) -> None:
        self.url = url

    def download_file(self, id_: str) -> str:
        return requests.get(url = self.url + 'transalator_app.php', params={'id':id_, 'json':'json'}).text

if __name__ == '__main__':
    uil = uilogic()
    result = uil.ask('aller', ['vais', 'vas', 'va', 'allons', 'allez', 'vont'])
    print(f'Correct answers: {result}')