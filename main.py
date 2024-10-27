#You will need to install the requests library to run this code. You can do this by opening a terminal window and typing the following command
#AND, if it doesn't work on replit, copy paste the code onto VS code. 

import cv2
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

#function to open and process the image
def open_and_process_image():
    #get the JPG file path from files on your desktop
    #press button to open up your files on the computer
    image_path = filedialog.askopenfilename(filetypes=[("JPG files", "*.jpg")])

    #only .jpg files will work with this.
    if image_path.endswith('.jpg'):

        #load the image
        image = cv2.imread(image_path)

        #Converts the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        #apply Gaussian Blur to the grayscale image
        blur_image = cv2.GaussianBlur(gray_image, (3, 3), cv2.BORDER_DEFAULT)

        #apply edge detection
        edges = cv2.Canny(blur_image, threshold1=125, threshold2=175)

        #convert the processed image to RGB
        impil = Image.fromarray(cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB))
        im_tk = ImageTk.PhotoImage(image=impil)

        #display the processed image in the tkinter label
        label_img.config(image = im_tk)
        label_img.image = im_tk

#the rest is tkinter stuff!

window = Tk()
window.geometry("800x600")
window.title("Computer Vision Edge Detection")

#Labelsssss
label_title = Label(window,
                    text="COMPUTER VISION RESULT",
                    font=('Times New Roman', 20, "bold"),
                    fg='blue',
                    bg='black',
                    relief=RAISED,
                    bd=10,
                    padx=20,
                    pady=10)

label_title.pack()

label_img = Label(window)
label_img.pack()

btn_open = Button(window, text="Open Image", command=open_and_process_image, font=('Times New Roman', 16))
btn_open.pack(pady=20)
#Makes button useable

window.mainloop()

#REFERENCES: https://www.youtube.com/watch?v=oXlwWbU8l2o&t=2541s, https://www.youtube.com/watch?v=TuLxsvK4svQ&t=923s