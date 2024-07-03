from tkinter import *
import mysql.connector
from tkinter import messagebox


def search():
    if rightsearch.get() == "":
        messagebox.showerror("Error!", "Please fill all the fields")
    else:
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="girir@123", database="student_record")
            curr = conn.cursor()
            rollno = rightsearch.get()
            curr.execute("SELECT * FROM record WHERE rollno = %s", (rollno,))
            result = curr.fetchone()
            if result:
                ser_ent.config(text=rollno)
                rightnameent.config(text=result[0])
                rightunit1ent.config(text=result[2])
                rightunit2ent.config(text=result[3])
                rightunit3ent.config(text=result[4])
                rightunit4ent.config(text=result[5])
                rightunit5ent.config(text=result[6])
                rightalltestent.config(text=result[7])
                rightrecent.config(text=result[8])
            else:
                messagebox.showinfo("Error", "Rollno entry not found")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"DATABASE ERROR FOUND! {e}")
        finally:
            conn.close()

def insert_funct():
    if rollno.get() == "" or name.get() == "":
        messagebox.showerror("Error!", "Please fill all the fields")
    else:
        conn = mysql.connector.connect(host="localhost", user="root", password="urpassword", database="student_record")
        curr = conn.cursor()
        curr.execute("INSERT INTO record VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", ( name.get(),rollno.get(),
                                                                               unit1.get(), unit2.get(), unit3.get(),
                                                                               unit4.get(), unit5.get(),unit_test.get(),choice.get()))
        try:
            conn.commit()
            messagebox.showinfo("Success", "Data entered successfully")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            conn.close()

win = Tk()
win.geometry("1370x700+0+0")
win.title("STUDENT INFORMATION APP")

mytitle = Label(win, text="STUDENT INFORMATION APP", font=("Arial", 25, "bold"), bg="#008080", fg="white")
mytitle.pack(side=TOP, fill='x',pady=40)

frame_style = {"bg": "lightgrey", "bd": 12, "relief": GROOVE}
entry_frame_style = {"font": ("Arial", 15), "bg": "lightgrey", "bd": 3}
submit_btn_style = {"font": ("Arial", 15), "bd": 5, "bg": "#008080", "fg": "white"}


fr = Frame(win, **frame_style)
fr.place(x=10, y=100, height=700, width=800)


name = StringVar()
rollno = StringVar()
unit1 = StringVar()
unit2 = StringVar()
unit3 = StringVar()
unit4 = StringVar()
unit5 = StringVar()
unit_test = BooleanVar()
choice = StringVar()
rightsearch = StringVar()



rollnolbl = Label(fr, text="Roll No : ", font=("Arial", 15), bg="lightgrey")
rollnolbl.grid(row=0, column=0, padx=12, pady=2)

rollnoent = Entry(fr, font=("Arial", 15), bg="lightgrey", bd=3, textvariable=rollno)
rollnoent.grid(row=0, column=1, padx=12, pady=2)

namelbl = Label(fr, text="NAME : ", font=("Arial", 15), bg="lightgrey")
namelbl.grid(row=1, column=0, padx=12, pady=2)
nameent = Entry(fr, font=("Arial", 15), bg="lightgrey", bd=3, textvariable=name)
nameent.grid(row=1, column=1, padx=12, pady=2)

unit1lbl = Label(fr, text="Unit test 1 : ", font=("Arial", 15), bg="lightgrey")
unit1lbl.grid(row=2, column=0, padx=12, pady=2)
unit1ent = Entry(fr, font=("Arial", 15), bg="lightgrey", bd=3, textvariable=unit1)
unit1ent.grid(row=2, column=1, padx=12, pady=2)

unit2lbl = Label(fr, text="Unit test 2 : ", font=("Arial", 15), bg="lightgrey")
unit2lbl.grid(row=3, column=0, padx=12, pady=2)
unit2ent = Entry(fr, font=("Arial", 15), bg="lightgrey", bd=3, textvariable=unit2)
unit2ent.grid(row=3, column=1, padx=12, pady=2)

unit3lbl = Label(fr, text="Unit test 3 : ", font=("Arial", 15), bg="lightgrey")
unit3lbl.grid(row=4, column=0, padx=12, pady=2)
unit3ent = Entry(fr, font=("Arial", 15), bg="lightgrey", bd=3, textvariable=unit3)
unit3ent.grid(row=4, column=1, padx=12, pady=2)

unit4lbl = Label(fr, text="Unit test 4 : ", font=("Arial", 15), bg="lightgrey")
unit4lbl.grid(row=5, column=0, padx=12, pady=2)
unit4ent = Entry(fr, font=("Arial", 15), bg="lightgrey", bd=3, textvariable=unit4)
unit4ent.grid(row=5, column=1, padx=12, pady=2)

unit5lbl = Label(fr, text="Unit test 5 : ", font=("Arial", 15), bg="lightgrey")
unit5lbl.grid(row=6, column=0, padx=12, pady=2)
unit5ent = Entry(fr, font=("Arial", 15), bg="lightgrey", bd=3, textvariable=unit5)
unit5ent.grid(row=6, column=1, padx=12, pady=2)

Submit_btn = Button(fr, text="Save Data",**submit_btn_style, command=insert_funct)
Submit_btn.place(x=100, y=350, height=50, width=200)

submit_checkbox = Checkbutton(fr, text="All unit test completed ", font=("ARIAL", 16), bg="lightgrey",
                              variable=unit_test)
submit_checkbox.grid(row=7, column=1, padx=12, pady=2)

record_label = Label(fr,text="Record : ",font=("Arial", 15), bg="lightgrey")
record_label.grid(row=8,column =0,padx=12,pady=2)

choice.set("Not-Submitted")  # Default selection

radio_button1 = Radiobutton(fr, text="Not-Submitted", variable=choice, value="Not-Submitted")
radio_button1.grid(row=8, column=1, padx=12, pady=2)
radio_button2 = Radiobutton(fr, text="Submitted", variable=choice, value="Submitted")
radio_button2.grid(row=8, column=2, padx=12, pady=2)
radio_button3 = Radiobutton(fr, text="Not Yet started", variable=choice, value="Not Yet started")
radio_button3.grid(row=8, column=3, padx=12, pady=2)


#right side
rightfr = Frame(win,border =12,bg="lightgrey",relief=SUNKEN)
rightfr.place(x=820,y=100,height=700,width=700)

search_frame = Frame(rightfr,bg="red",bd=12,relief=GROOVE)
search_frame.pack(side=TOP,fill='x')
#search label
Search_btn = Button(search_frame,text="Search : ",**submit_btn_style,command=search)
Search_btn.grid(row=0,column=0,padx=12,pady=2)
#search entry
Search_entry = Entry(search_frame,**entry_frame_style,textvariable=rightsearch)
Search_entry.grid(row=0,column=1,padx=12,pady=2)

# results frame
result_frame = Frame(rightfr,border=12,bg="white",relief=SUNKEN)
result_frame.pack(fill=BOTH,expand=True)

result_label = Label(result_frame,text = "Showing results for : ",font=("Arial 15 bold"),bg="white")
result_label.grid(row=0,column=1,padx=2,pady=12)
ser_ent =  Label(result_frame,text="",font=("Arial 15 bold"),bg="white",bd=12,relief=GROOVE)
ser_ent.grid(row=0,column=2,padx=2,pady=12)

# results storing
rightnamelbl = Label(result_frame, text="NAME : ", font=("Arial", 15), bg="white")
rightnamelbl.grid(row=1, column=1, padx=12, pady=2)
rightnameent = Label(result_frame, text="",font=("Arial", 15), bg="white", bd=3,relief=SUNKEN)
rightnameent.grid(row=1, column=2, padx=2, pady=12)

rightunit1lbl = Label(result_frame, text="Unit-Test-1 : ", font=("Arial", 15), bg="white")
rightunit1lbl.grid(row=2, column=1, padx=12, pady=2)
rightunit1ent = Label(result_frame, text="",font=("Arial", 15), bg="white", bd=3,relief=SUNKEN)
rightunit1ent.grid(row=2, column=2, padx=2, pady=12)

rightunit2lbl = Label(result_frame, text="Unit-Test-2 : ", font=("Arial", 15), bg="white")
rightunit2lbl.grid(row=3, column=1, padx=12, pady=2)
rightunit2ent = Label(result_frame, text="",font=("Arial", 15), bg="white", bd=3,relief=SUNKEN)
rightunit2ent.grid(row=3, column=2, padx=2, pady=12)

rightunit3lbl = Label(result_frame, text="Unit-Test-3 : ", font=("Arial", 15), bg="white")
rightunit3lbl.grid(row=4, column=1, padx=12, pady=2)
rightunit3ent = Label(result_frame, text="",font=("Arial", 15), bg="white", bd=3,relief=SUNKEN)
rightunit3ent.grid(row=4, column=2, padx=2, pady=12)

rightunit4lbl = Label(result_frame, text="Unit-Test-4 : ", font=("Arial", 15), bg="white")
rightunit4lbl.grid(row=5, column=1, padx=12, pady=2)
rightunit4ent = Label(result_frame, text="",font=("Arial", 15), bg="white", bd=3,relief=SUNKEN)
rightunit4ent.grid(row=5, column=2, padx=2, pady=12)


rightunit5lbl = Label(result_frame, text="Unit-Test-5 : ", font=("Arial", 15), bg="white")
rightunit5lbl.grid(row=6, column=1, padx=12, pady=2)
rightunit5ent = Label(result_frame, text="",font=("Arial", 15), bg="white", bd=3,relief=SUNKEN)
rightunit5ent.grid(row=6, column=2, padx=2, pady=12)

rightalltestlbl = Label(result_frame, text="ALL unit test completed : ", font=("Arial", 15), bg="white")
rightalltestlbl.grid(row=7, column=1, padx=12, pady=2)
rightalltestent = Label(result_frame, text="",font=("Arial", 15), bg="white", bd=3,relief=SUNKEN)
rightalltestent.grid(row=7, column=2, padx=2, pady=12)

rightrecordlbl = Label(result_frame, text="Record : ", font=("Arial", 15), bg="white")
rightrecordlbl.grid(row=8, column=1, padx=12, pady=2)
rightrecent = Label(result_frame, text="",font=("Arial", 15), bg="white", bd=3,relief=SUNKEN)
rightrecent.grid(row=8, column=2, padx=2, pady=12)

win.mainloop()