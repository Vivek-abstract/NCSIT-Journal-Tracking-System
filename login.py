from tkinter import *
import datetime
import csv

def Login():
    """This function creates the Login window and displays it"""

    def validate():
        """Validates the user_name and password"""

        user_name = user_name_entry.get()
        password = password_entry.get()

        if user_name == "admin" and password == "root":
            print("Hello Admin")
            login.destroy()
            Admin()
        elif user_name == "publisher" and password == "publisher":
            print("Hello Publisher")
            login.destroy()
            Publisher()
        else:
            label1 = Label(login, text="Invalid Credentials", fg="red")
            label1.place(relx=0.5, rely=0.7, anchor=CENTER)

    login = Tk()
    login.geometry("500x400")

    login_label = Label(login, text="Login", fg="black")
    login_label.config(font=("Courier", 22))
    user_name_label = Label(login, text="Username:", fg="black")
    password_label = Label(login, text="Password:", fg="black")

    user_name_entry = Entry(login)
    password_entry = Entry(login, show="*")
    submit_button = Button(login, text="Login", fg="blue", command=validate)

    login_label.place(relx=0.5, rely=0.3, anchor=CENTER)
    user_name_label.place(relx=0.4, rely=0.4, anchor=CENTER)
    user_name_entry.place(relx=0.6, rely=0.4, anchor=CENTER)
    password_label.place(relx=0.4, rely=0.5, anchor=CENTER)
    password_entry.place(relx=0.6, rely=0.5, anchor=CENTER)
    submit_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    login.mainloop()

def ArrivalDate():
    window = Tk()
    window.geometry("500x400")

    file = open("arrived_journals.csv", 'a', newline='')
    writer = csv.writer(file)

    def on_closing():
        file.close()
        file1.close()
        window.destroy()

    def add_arrival_date():
        journal_name = j_name.get()
        arrival_date = arrival_date_entry.get()

        writer.writerow([journal_name, arrival_date])

    heading = Label(window, text="Add arrival date")
    heading.config(font=("Courier", 20))
    heading.place(relx=0.5, rely=0.2, anchor=CENTER)

    select_label = Label(window, text="Select Journal:")
    select_label.place(relx=0.4, rely=0.4, anchor=CENTER)

    arrival_date_label = Label(window, text="Arrival Date:")
    arrival_date_label.place(relx=0.4,rely=0.5, anchor=CENTER)
    arrival_date_entry = Entry(window)
    arrival_date_entry.place(relx=0.62, rely=0.5, anchor=CENTER)

    file1 = open("booked_journals.csv", newline='')
    reader = csv.reader(file1)
    header = next(reader)

    booked_journal_names = []
    # row = Journalname, Publishdate, PublisherType
    for row in reader:
        journal_name = row[0]
        booked_journal_names.append(journal_name)

    journal_options = booked_journal_names
    j_name = StringVar(window)
    j_name.set(journal_options[0]) # default value

    journal_options_select = OptionMenu(window, j_name, *journal_options)
    journal_options_select.place(relx=0.6, rely=0.4, anchor=CENTER)
    submit_button = Button(window, text="Add", command=add_arrival_date)
    submit_button.place(relx=0.5,rely=0.6, anchor=CENTER)

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

def BookJournal():
    book_window = Tk()
    book_window.geometry("500x400")
    booked_journals = []

    file = open("booked_journals.csv", 'a', newline='')
    writer = csv.writer(file)

    def on_closing():
        file.close()
        file2.close()
        book_window.destroy()

    def book_journal():
        """Writes the journal_name, date_of_booking, publish_date, publisher_type in booked_journals.csv"""

        global expiry_date
        journal_name = j_names.get()
        date_of_booking = datetime.datetime.today()
        duration = dur.get()

        file2 = open("published_journals.csv", newline='')
        reader = csv.reader(file2)
        data = [row for row in reader]
        # Jounralname, publish_date, publisher_type
        for row in data:
            if row[0] == journal_name:
                pub_date = row[1]
                pub_type = row[2]
                break

        if duration == "Monthly":
            expiry_date = datetime.datetime.today() + datetime.timedelta(30)
        elif duration == "Bi-Monthly":
            expiry_date = datetime.datetime.today() + datetime.timedelta(15)
        elif duration == "Quarterly":
            expiry_date = datetime.datetime.today() + datetime.timedelta(120)
        elif duration == "Half Yearly":
            expiry_date = datetime.datetime.today() + datetime.timedelta(365)

        formatted_date_of_booking = datetime.datetime.strftime(date_of_booking, "%d/%m/%Y")
        formatted_expiry_date = datetime.datetime.strftime(expiry_date, "%d/%m/%Y")

        writer.writerow([journal_name, pub_date, pub_type, formatted_date_of_booking, duration, formatted_expiry_date])

    heading = Label(book_window, text="Book Journal")
    heading.config(font=("Courier", 20))
    heading.place(relx=0.5, rely=0.2, anchor=CENTER)

    select_label = Label(book_window, text="Select Journal:")
    select_label.place(relx=0.5, rely=0.4, anchor=E)

    duration_label = Label(book_window, text="Select Duration:")
    duration_label.place(relx=0.5, rely=0.5, anchor=E)

    duration_options = ["Monthly", "Bi-Monthly", "Quarterly", "Half Yearly"]
    dur = StringVar(book_window)
    dur.set(duration_options[0]) # default value
    duration_options_select = OptionMenu(book_window, dur, *duration_options)
    duration_options_select.place(relx=0.52, rely=0.5, anchor=W)

    file1 = open("published_journals.csv", newline='')
    reader = csv.reader(file1)
    header = next(reader)

    published_journal_names = []
    # row = Journalname, Publishdate, PublisherType
    for row in reader:
        journal_name = row[0]
        published_journal_names.append(journal_name)

    journal_options = published_journal_names
    j_names = StringVar(book_window)
    j_names.set(journal_options[0]) # default value
    journal_options_select = OptionMenu(book_window, j_names, *journal_options)
    journal_options_select.place(relx=0.52, rely=0.4, anchor=W)

    book_button = Button(book_window, text="Book Journal", command=book_journal)
    book_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    book_window.protocol("WM_DELETE_WINDOW", on_closing)
    book_window.mainloop()


def calculate_missing_journals():
    """Calculate all the missing journals and call the display_missing_journals function"""

    missing_journals = []

    file = open("booked_journals.csv", newline='')
    reader = csv.reader(file)
    header = next(reader)

    booked_journal = [row for row in reader]
    # Journal Name,Publish Date,Publisher Type,Date of Booking,Duration,Expiry Date
    journals_to_consider = []
    for journal in booked_journal:
        date_of_booking = datetime.datetime.strptime(journal[3],"%d/%m/%Y")
        if journal[2] == "Indian" and (datetime.datetime.today() - date_of_booking).days > 15:
            journals_to_consider.append(journal)
        elif journal[2] == "International" and (datetime.datetime.today() - date_of_booking).days > 30:
            journals_to_consider.append(journal)

    file = open("arrived_journals.csv", newline='')
    reader = csv.reader(file)
    header = next(reader)

    arrived_journal_names = [row[0] for row in reader]

    missing_journals = [journal for journal in journals_to_consider if journal[0] not in arrived_journal_names]
    display_missing_journals(missing_journals)

def display_missing_journals(missing_journals):
    """Displays all the missing journals in a new window"""

    missing = Tk()
    missing.geometry("500x400")
    missing_heading = Label(missing, text="The following Journals haven't arrived yet:")
    missing_heading.config(font=("Courier", 12))
    missing_heading.place(relx=0.5, rely=0.1, anchor=CENTER)
    y = 0.2
    count = 1
    for each in missing_journals:
        # Journal Name,Publish Date,Publisher Type,Date of Booking,Duration,Expiry Date
        missing_journal_label = Label(missing, text=str(count) + ". " + each[0] + ", booked on: " +  each[3])
        missing_journal_label.place(relx=0.5, rely=y, anchor=CENTER)
        y+=0.1
        count += 1

    missing.mainloop()

def Admin():
    """Admin Panel which displays all commands for admin"""

    admin_panel = Tk()
    admin_panel.geometry("500x400")

    welcome_label = Label(admin_panel, text="Welcome, Admin")
    welcome_label.config(font=("Courier", 18))
    welcome_label.place(relx=0.5, rely=0.2, anchor=CENTER)

    review = Button(admin_panel, text="Review Missing Journals", command=calculate_missing_journals)
    review.place(relx=0.35, rely=0.4, anchor=CENTER)

    arrival_date_button = Button(admin_panel, text="Add arrival date", command=ArrivalDate)
    arrival_date_button.place(relx=0.65, rely=0.4, anchor=CENTER)

    book_journal_button = Button(admin_panel, text="Book Journal", command=BookJournal)
    book_journal_button.place(relx=0.35, rely=0.5, anchor=CENTER)

    admin_panel.mainloop()

def Publisher():
    """Publisher window which contains publish journal, logout"""

    publisher_panel = Tk()
    publisher_panel.geometry("500x400")

    welcome_label = Label(publisher_panel, text="Welcome, Publisher")
    welcome_label.config(font=("Courier", 18))
    welcome_label.place(relx=0.5, rely=0.2, anchor=CENTER)

    publish_journal = Button(publisher_panel, text="Publish Journal", command=PublishJournal)
    publish_journal.place(relx=0.4, rely=0.4, anchor=CENTER)
    logout = Button(publisher_panel, text="Logout", command=publisher_panel.destroy)
    logout.place(relx=0.6, rely=0.4, anchor=CENTER)
    publisher_panel.mainloop()

def PublishJournal():
    """Publish Journal window which takes journal name, publish_date and publisher_type from user
    and stores them in published_journals"""

    file = open("published_journals.csv", 'a', newline='')
    writer = csv.writer(file)

    def publish_journal():
        """Publishes the journal and adds it in a csv file published_journals"""

        journal_name = journal_name_entry.get()
        publish_date = publish_date_entry.get()
        publisher_type = btn.get()
        writer.writerow([journal_name, publish_date, publisher_type])

    published_journals = []
    # Tk doesn't work here so we use Tk()
    publish_window = Toplevel()
    btn = StringVar()
    publish_window.geometry("500x400")

    welcome_label = Label(publish_window, text="Enter Journal Details")
    welcome_label.config(font=("Courier", 18))
    welcome_label.place(relx=0.5, rely=0.2, anchor=CENTER)

    journal_name_label = Label(publish_window, text="Journal Name: ")
    publish_date_label = Label(publish_window, text="Publishing date: ")
    publisher_type_label = Label(publish_window, text="Publisher type: ")

    journal_name_entry = Entry(publish_window)
    publish_date_entry = Entry(publish_window)
    journal_name_label.place(relx = 0.35, rely=0.3, anchor=CENTER)
    journal_name_entry.place(relx = 0.6, rely=0.3, anchor=CENTER)
    publish_date_label.place(relx= 0.35, rely= 0.4, anchor=CENTER)
    publish_date_entry.place(relx = 0.6, rely=0.4, anchor=CENTER)
    publisher_type_label.place(relx=0.35, rely=0.5, anchor=CENTER)

    indian_radio_button = Radiobutton(publish_window, text="Indian", variable=btn, value="Indian")
    international_radio_button = Radiobutton(publish_window, text="International", variable=btn, value="International")
    indian_radio_button.place(relx=0.46, rely=0.5, anchor=W)
    international_radio_button.place(relx=0.46, rely=0.6, anchor=W)

    publish_button = Button(publish_window, text="Publish Journal", command=publish_journal)
    publish_button.place(relx=0.5, rely=0.7, anchor=CENTER)

    publish_window.mainloop()

Login()
# Admin()
# Publisher()
