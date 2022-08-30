import tkinter
# import customtkinter
from PIL import Image, ImageTk
import whatsapp

# customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()
#
#         self.title("Carsafey")
#         self.geometry("400x450")
#         self.resizable(0, 0)
#         self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
#
#         self.label_frame = customtkinter.CTkFrame(master=self)
#         self.label_frame.pack(pady=20, padx=60, fill="both", expand=True)
#
#         self.image = Image.open("logo2.png").resize((200, 150))
#         self.bg_image = ImageTk.PhotoImage(self.image)
#         self.image_label = tkinter.Label(master=self.label_frame, image=self.bg_image, highlightthickness=0, bd=0)
#         self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#         self.image_label.grid(row=2, column=0, padx=60, pady=0.5)
#
#         self.label_Welcome = customtkinter.CTkLabel(master=self.label_frame, justify=tkinter.CENTER,
#                                                     text='\nWelcome to Carsafey!\n Please enter your information:')
#         self.label_Welcome.grid(row=3, column=0)
#
#         self.nameEntry = customtkinter.CTkEntry(master=self.label_frame, placeholder_text="Name")
#         self.nameEntry.grid(row=4, column=0, padx=80, pady=12)
#
#         self.emailEntry = customtkinter.CTkEntry(master=self.label_frame, placeholder_text="Email")
#         self.emailEntry.grid(row=5, column=0, padx=80, pady=10)
#
#         self.phoneEntry = customtkinter.CTkEntry(master=self.label_frame, placeholder_text="Phone")
#         self.phoneEntry.grid(row=6, column=0, padx=80, pady=10)
#
#         self.submit_btn = customtkinter.CTkButton(master=self.label_frame, text="Submit", command=self.btn_clicked)
#         self.submit_btn.grid(row=7, column=0, padx=80, pady=10)
#
#     def on_closing(self, event=0):
#         self.destroy()
#
#     def btn_clicked(self):
#         print("Button click")
#         name = self.nameEntry.get()
#         email = self.emailEntry.get()
#         phone = self.phoneEntry.get()
#         user = User(name, email, phone)
#         label_join = customtkinter.CTkLabel(master=self.label_frame, justify=tkinter.CENTER, text_color="red",
#                                             text='Your info was submitted succefully!\nPlease send the following\n '
#                                                  'whatsapp message to +14155238886\n "join team-evidence"')
#         label_join.grid(row=7, column=0)


class User:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


# if __name__ == "__main__":
#     # app = App()
#     # app.mainloop()
#     # whatsapp.sendEmergencyWhatsapp()
