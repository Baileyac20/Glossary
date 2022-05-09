import tkinter as tk
import tkinter.font as tkFont
SmartSearch = False
Glossary = [
    [
        "ram",
        "random access memory",
        "ram is a thing"
    ]
]


class App:
    def __init__(self, root):
        global Query
        global Output
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_91=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_91["font"] = ft
        GLabel_91["fg"] = "#333333"
        GLabel_91["justify"] = "center"
        GLabel_91["text"] = ""
        GLabel_91.place(x=0,y=0,width=185,height=30)

        GLabel_871=tk.Label(root)
        GLabel_871["anchor"] = "center"
        GLabel_871["cursor"] = "circle"
        ft = tkFont.Font(family='Times',size=18)
        GLabel_871["font"] = ft
        GLabel_871["fg"] = "#333333"
        GLabel_871["justify"] = "center"
        GLabel_871["text"] = "𝐆𝐥𝐨𝐬𝐬𝐚𝐫𝐲"
        GLabel_871["relief"] = "groove"
        GLabel_871.place(x=0,y=0,width=600,height=30)

        GLineEdit_647=tk.Entry(root)
        GLineEdit_647["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_647["font"] = ft
        GLineEdit_647["fg"] = "#333333"
        GLineEdit_647["justify"] = "center"
        GLineEdit_647["text"] = "Enter Query"
        GLineEdit_647.place(x=20,y=40,width=550,height=36)
        Query = GLineEdit_647

        GLineEdit_657=tk.Entry(root)
        GLineEdit_657["borderwidth"] = "3px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_657["font"] = ft
        GLineEdit_657["fg"] = "#333333"
        GLineEdit_657["justify"] = "center"
        GLineEdit_657["text"] = "Enter the query and submit to get a definition."
        GLineEdit_657.place(x=20,y=90,width=550,height=300)
        Output = GLineEdit_657

        GButton_520=tk.Button(root)
        GButton_520["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_520["font"] = ft
        GButton_520["fg"] = "#000000"
        GButton_520["justify"] = "center"
        GButton_520["text"] = "Submit"
        GButton_520.place(x=20,y=400,width=100,height=30)
        GButton_520["command"] = self.GButton_520_command

        GButton_335=tk.Button(root)
        GButton_335["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_335["font"] = ft
        GButton_335["fg"] = "#000000"
        GButton_335["justify"] = "center"
        GButton_335["text"] = "Define"
        GButton_335.place(x=130,y=400,width=100,height=30)
        GButton_335["command"] = self.GButton_335_command

        GButton_683=tk.Button(root)
        GButton_683["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_683["font"] = ft
        GButton_683["fg"] = "#000000"
        GButton_683["justify"] = "center"
        GButton_683["text"] = "Help"
        GButton_683.place(x=240,y=400,width=100,height=30)
        GButton_683["command"] = self.GButton_683_command

        GCheckBox_690=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_690["font"] = ft
        GCheckBox_690["fg"] = "#333333"
        GCheckBox_690["justify"] = "center"
        GCheckBox_690["text"] = "Smart Search"
        GCheckBox_690.place(x=0,y=460,width=104,height=39)
        GCheckBox_690["offvalue"] = "0"
        GCheckBox_690["onvalue"] = "1"
        GCheckBox_690["command"] = self.GCheckBox_690_command

        GMessage_664=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_664["font"] = ft
        GMessage_664["fg"] = "#333333"
        GMessage_664["justify"] = "center"
        GMessage_664["text"] = "Glossary v1.0 | Insert legal terminoligy here, lorum ispum."
        GMessage_664.place(x=170,y=450,width=249,height=30)

    # Submit
    def GButton_520_command(self):
        QueryText = Query.get().lower()
        if QueryText == "": return
        if SmartSearch:
            StripCharacters = ['"', "'", ",", ".", "!", "$", "[", "]", "@", "~", "(", ")", ":", ";"]
            for v in StripCharacters:
                QueryText = QueryText.strip(v)
            for v in Glossary:
                for vv in v: ## LOOP INSIDE LOOP
                    if (vv in QueryText) or (QueryText in vv):
                        Output.delete(0, tk.END)
                        Output.insert(tk.END, v[len(v)-1])
                        return
        else:
            for v in Glossary:
                if QueryText in v:
                    Output.delete(0, tk.END)
                    Output.insert(tk.END, v[len(v)-1])
                    return
        Output.delete(0, tk.END)
        Output.insert(tk.END, "No results found, check the spelling of your search and turn smart search on.")
                    

    # Define
    def GButton_335_command(self):
        QueryText = Query.get().lower()
        if QueryText == "": return
        OutputText = Output.get()
        if len(OutputText) > 3:
            Glossary.append([
                QueryText,
                OutputText
            ])
            Output.delete(0, tk.END)
            Output.insert(tk.END, "Stored your entry in the glossary.")

    # Help
    def GButton_683_command(self):
        Output.delete(0, tk.END)
        Output.insert(tk.END, """
𝗚𝗹𝗼𝘀𝘀𝗮𝗿𝘆 | 𝗩𝟭

- Get Entry
1) Type query into the box.
2) Turn smart search on - Optional.
3) Press "Submit".

- Write Entry
1) Write entry into the box.
2) Type defenition into the box.
3) Press "Define"
-- 09/05/2022
""")

    # Smart Search
    def GCheckBox_690_command(self):
        global SmartSearch
        SmartSearch = not SmartSearch

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

# DO THIS LATER
"""
# Buttons
def submitSearch():
    Query = entry.get()
    # Strip Query
    StripCharacters = ['"', "'", ",", ".", "!", "$", "[", "]", "@", "~", "(", ")", ":", ";"]
    Query = Query.lower()
    for v in StripCharacters:
        Query = Query.strip(v)

    # Get Response
    Response = "Failed to find a response."
    for v in Glossary:
        if Query in v:
            Response = v[len(v)-1]
    output.delete(0.0, END)
    output.insert(END, Response)
"""
