from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont
import tkmacosx
import os



class Application(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # creating a window
        self.window = Frame(self)
        self.window.pack()

        self.window.grid_rowconfigure(0, weight=1, minsize=1000)
        self.window.grid_columnconfigure(0, weight=1, minsize=800)
        self.window.config( padx = 20, pady= 20, bg='#F1E4C3')

        self.current_frame = None
        self.show_frame(FirstPage)

    def show_frame(self, page):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = page(self.window, controller=self)
        self.current_frame.config(bg='#F1E4C3')
        #self.current_frame.pack(side="top", fill="both", expand=True)
        self.current_frame.grid(row=0, column=0, sticky="N" )
        self.title("Add Watermark to Your Photo")

class FirstPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def upload_file():
            global filename, img
            f_types = [("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")]
            #f_types = [('Jpg Files', '*.jpg')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            img = Image.open(filename)
            max_width = 500
            if img.size[0] >= img.size[1]:
                pixels_x, pixels_y = tuple([int(max_width / img.size[0] * x) for x in img.size])
            elif img.size[0] < img.size[1]:
                pixels_x, pixels_y = tuple([int(max_width / img.size[1] * x) for x in img.size])
            self.img = img.resize((pixels_x, pixels_y))
            self.img = ImageTk.PhotoImage(self.img)
            b2 = Label(self, image=self.img, borderwidth =0, highlightthickness =0)
            b2.grid(row=2, column=0, pady=20, columnspan=2)

        def reset():
            global filename, img
            img = Image.open(filename)
            max_width = 500
            if img.size[0] >= img.size[1]:
                pixels_x, pixels_y = tuple([int(max_width / img.size[0] * x) for x in img.size])
            elif img.size[0] < img.size[1]:
                pixels_x, pixels_y = tuple([int(max_width / img.size[1] * x) for x in img.size])
            self.img = img.resize((pixels_x, pixels_y))
            self.img = ImageTk.PhotoImage(self.img)
            b2 = Label(self, image=self.img, borderwidth =0, highlightthickness =0)
            b2.grid(row=2, column=0, pady=20, columnspan=2)

        try:
            reset()
        except:
            pass

        top = Label(self, text="Please upload your image file using the button below", fg='#3C3633',bg='#F1E4C3',
                     font=('Ariel', 20, 'bold'))
        top.grid(row=0, column=0, pady=10, columnspan=2)

        upload_button = tkmacosx.Button(self, text='Upload Image',
                                        bg='#739072', fg='#ffffff',
                                        activebackground='#739072',
                                        font=('Ariel', 15, 'normal'),
                                        height=40, width=450, highlightthickness=0, command=upload_file, borderless=1,
                                        bd=0)
        upload_button.grid(row=1, column=0, pady=10, columnspan=2)

        op_text_watermark = tkmacosx.Button(self, text='Add Text Watermark',
                                            bg='#A25772', fg='#ffffff',
                                            activebackground='#A25772',
                                            font=('Ariel', 15, 'normal'),
                                            height=40, width=200, highlightthickness=0, command= lambda: controller.show_frame(SecondPage),
                                            borderless=1, bd=0)
        op_text_watermark.grid(row=3, column=0, pady=10)

        op_logo_watermark = tkmacosx.Button(self, text='Add Logo Watermark',
                                            bg='#A25772', fg='#ffffff',
                                            activebackground='#A25772',
                                            font=('Ariel', 15, 'normal'),
                                            height=40, width=200, highlightthickness=0, command=lambda: controller.show_frame(ThirdPage),
                                            borderless=1, bd=0)
        op_logo_watermark.grid(row=3, column=1, pady=10)


class SecondPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.watermark_text = StringVar()

        def add_watermark():
            global img
            width, height = img.size
            x = width / 2
            y = height / 2
            if x > y:
                font_size = y
            elif y > x:
                font_size = x
            else:
                font_size = x

            drawing = ImageDraw.Draw(img)
            path = os.path.dirname(__file__) + '/'
            font = ImageFont.truetype(path + "Arial.ttf", font_size/3)
            fill_color = (203, 201, 201)
            w_text = self.watermark_text.get()
            self.watermark_text.set("")

            position = (x, y)
            drawing.text(xy=position, text=w_text, font=font, fill=fill_color)
            max_width = 500
            if img.size[0] >= img.size[1]:
                pixels_x, pixels_y = tuple([int(max_width / img.size[0] * x) for x in img.size])
            elif img.size[0] < img.size[1]:
                pixels_x, pixels_y = tuple([int(max_width / img.size[1] * x) for x in img.size])
            self.img = ImageTk.PhotoImage(img.resize((pixels_x, pixels_y)))
            b2 = Label(self, image=self.img, borderwidth =0, highlightthickness =0)
            b2.grid(row=1, column=0, pady=20, columnspan = 2)

        def reset():
            global filename, img
            img = Image.open(filename)
            max_width = 500
            if img.size[0] >= img.size[1]:
                pixels_x, pixels_y = tuple([int(max_width / img.size[0] * x) for x in img.size])
            elif img.size[0] < img.size[1]:
                pixels_x, pixels_y = tuple([int(max_width / img.size[1] * x) for x in img.size])
            self.img = img.resize((pixels_x, pixels_y))
            self.img = ImageTk.PhotoImage(self.img)
            b2 = Label(self, image=self.img, borderwidth =0, highlightthickness =0)
            b2.grid(row=1, column=0, pady=20, columnspan = 2)

        def savefile():
            global img
            savefilename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
            if not savefilename:
                return
            img.save(savefilename)

        try:
            reset()
        except:
            pass

        watermark_text_label= Label(self, text = 'Watermark Text', font=('Ariel',15, 'normal'), bg = '#F1E4C3', fg = 'black')
        watermark_text_label.grid(row = 2, column = 0, pady = 10, sticky = 'N')
        watermark_text_entry = Entry(self, textvariable = self.watermark_text, font = ('Ariel',15,'normal'), bg = 'white', fg='black',borderwidth=0, highlightthickness=0)
        watermark_text_entry.grid(row=2,column=1, pady = 10, sticky = 'W')

        add_wm_button = tkmacosx.Button(self, text='Add Text Watermark',
                        bg='#6DA4AA', fg='#ffffff',
                        activebackground = '#6DA4AA',
                        font = ('Ariel', 15, 'normal'),
                        height=40, width=200, highlightthickness= 0, command=add_watermark, borderless=1, bd = 0)
        add_wm_button.grid(row = 3, column = 0, pady = 10, sticky = 'E')

        reset_button = tkmacosx.Button(self, text='Reset',
                        bg='#F3B95F', fg='#ffffff',
                        activebackground = '#F3B95F',
                        font = ('Ariel', 15, 'normal'),
                        height=40, width=200, highlightthickness= 0, command=reset, borderless=1, bd = 0)
        reset_button.grid(row = 3, column = 1, pady = 10, sticky = 'W')

        save_button = tkmacosx.Button(self, text='Save Image',
                                       bg='#50623A', fg='#ffffff',
                                       activebackground='#50623A',
                                       font=('Ariel', 15, 'normal'),
                                       height=40, width=405, highlightthickness=0, command=savefile, borderless=1, bd=0)
        save_button.grid(row=4, column=0, pady=10, columnspan = 2, sticky = 'N')

        button1 = tkmacosx.Button(self, text="Back to Main Page", highlightthickness=0, bd=0, borderless=1,
                                  font=('Ariel', 12, 'normal'),
                                  command=lambda: controller.show_frame(FirstPage))
        button2 = tkmacosx.Button(self, text="Add Logo Watermark", highlightthickness=0, bd=0, borderless=1,
                                  font=('Ariel', 12, 'normal'),
                                  command=lambda: controller.show_frame(ThirdPage))

        button1.grid(row=0, column=0, pady=10, sticky='E')
        button2.grid(row=0, column=1, pady=10, sticky='W')


class ThirdPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        def upload_logo():
            global img
            width, height = img.size
            x = width / 2
            y = height / 2
            if x > y:
                max_width_logo = y/3
            elif y > x:
                max_width_logo = x/3
            else:
                max_width_logo = x/3
            f_types = [("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")]
            logoname = filedialog.askopenfilename(filetypes=f_types)
            logo = Image.open(logoname).convert('RGBA')
            pixels_x, pixels_y = tuple([int(max_width_logo / logo.size[0] * x) for x in logo.size])
            logo = logo.resize((pixels_x, pixels_y))
            img.paste(logo, (50, 50), logo)
            max_width = 500
            if img.size[0] >= img.size[1]:
                pixels_x, pixels_y = tuple([int(max_width / img.size[0] * x) for x in img.size])
            elif img.size[0] < img.size[1]:
                pixels_x, pixels_y = tuple([int(max_width / img.size[1] * x) for x in img.size])
            self.img = img.resize((pixels_x, pixels_y))
            self.img = ImageTk.PhotoImage(self.img)
            b2 = Label(self, image=self.img, borderwidth =0, highlightthickness =0)
            b2.grid(row=1, column=0, pady=20, columnspan = 2)

        def reset():
            global filename, img
            img = Image.open(filename)
            max_width = 500
            if img.size[0] >= img.size[1]:
                pixels_x, pixels_y = tuple([int(max_width / img.size[0] * x) for x in img.size])
            elif img.size[0] < img.size[1]:
                pixels_x, pixels_y = tuple([int(max_width / img.size[1] * x) for x in img.size])
            self.img = img.resize((pixels_x, pixels_y))
            self.img = ImageTk.PhotoImage(self.img)
            b2 = Label(self, image=self.img, borderwidth =0, highlightthickness =0)
            b2.grid(row=1, column=0, pady=20, columnspan = 2)


        def savefile():
            global img
            savefilename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
            if not savefilename:
                return
            img.save(savefilename)

        try:
            reset()
        except:
            pass

        upload_logo_button = tkmacosx.Button(self, text='Add Logo Image',
                                        bg='#6DA4AA', fg='#ffffff',
                                        activebackground='#6DA4AA',
                                        font=('Ariel', 15, 'normal'),
                                        height=40, width=200, highlightthickness=0, command=upload_logo, borderless=1,
                                        bd=0)
        upload_logo_button.grid(row=2, column=0, pady=10, sticky = 'E')

        reset_button = tkmacosx.Button(self, text='Reset',
                                       bg='#F3B95F', fg='#ffffff',
                                       activebackground='#F3B95F',
                                       font=('Ariel', 15, 'normal'),
                                       height=40, width=200, highlightthickness=0, command=reset, borderless=1, bd=0)
        reset_button.grid(row=2, column=1, pady=10, sticky = 'W')

        save_button = tkmacosx.Button(self, text='Save Image',
                                      bg='#50623A', fg='#ffffff',
                                      activebackground='#50623A',
                                      font=('Ariel', 15, 'normal'),
                                      height=40, width=405, highlightthickness=0, command=savefile, borderless=1, bd=0)
        save_button.grid(row=3, column=0, pady=10, columnspan=2, sticky = 'N')

        # buttonframe = Frame(self)
        # buttonframe.grid(row = 0, column = 0, pady = 10, columnspan = 2)
        # buttonframe.config(highlightthickness=0, borderwidth=0, bd=0)

        button1 = tkmacosx.Button(self, text="Back to Main Page", highlightthickness=0, bd=0,borderless=1,
                         font=('Ariel', 12, 'normal'),
                         command= lambda: controller.show_frame(FirstPage))
        button2 = tkmacosx.Button(self, text="Add Text Watermark",highlightthickness=0, bd=0,borderless=1,
                         font=('Ariel', 12, 'normal'),
                         command=lambda: controller.show_frame(SecondPage))

        button1.grid(row=0, column=0, pady=10, sticky = 'E')
        button2.grid(row=0, column=1, pady=10, sticky='W')

        #
        # button1.pack(side="left")
        # button2.pack(side="left")


app = Application()
app.maxsize(2000, 2000)
#app.resizable(True, True)
app.mainloop()
