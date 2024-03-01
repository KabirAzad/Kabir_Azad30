import tkinter as tk
import openai
from PIL import Image, ImageTk

openai.api_key = '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'


def scroll_text(*args):
    entry.yview(*args)

def input_text():
    entry.config(state="normal")
    entry.delete(1.0 , tk.END)  # Clear any existing text
    prompt = entry_input.get()

    def get_completion(prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]

        response = openai.ChatCompletion.create(

            model=model,

            messages=messages,

            temperature=0,

        )

        return response.choices[0].message["content"]
    response = get_completion(prompt)
    entry.insert( float(len(response)), response)  # Printing the text on the output textbox
    entry.config(state="disabled")

#MAIN WINDOW
root = tk.Tk()
root.geometry('1920x1080')
root.title("TOUR PLANNER")

#IMAGE INSERTION

image = Image.open("background_template.jpg")  # Path to your image file
photo = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Text_Input
label = tk.Label(root, text="INPUT :-", font=("Arial", 16))
label.place(x = 470 , y = 242 )

#EntryWidget_Input
custom_font = ('Helvetica', 16)
entry_input = tk.Entry(root, font=custom_font ,width=61 , borderwidth=1 , border=2 , background='lemonchiffon', relief="solid")
entry_input.place(x=470 , y=275)


#Button
button_input = tk.Button(root,width= 15 ,height=1 ,text="CONTINUE", command=input_text , border=5 , bg='pink' )
button_input.place(x=790 , y = 310)

#Text_Output
label_out = tk.Label(root, text="OUTPUT :-", font=("Arial", 16))
label_out.place(x = 470 , y = 340 )

#TextBoxWidget_Output

custom_font = ('Helvetica', 16)
entry = tk.Text(root , width=60 , height=16.5 , font=custom_font , relief="solid" , background='antiquewhite' , border=2, wrap="word" , borderwidth=2)
entry.place(x = 470 , y = 370 )


scrollbar = tk.Scrollbar(root, command=scroll_text)
scrollbar.place(x=1197, y=370, height=414 , width=11)  # Position the Scrollbar widget using place
entry.config(yscrollcommand=scrollbar.set)


# Start the main event loop
root.mainloop()
