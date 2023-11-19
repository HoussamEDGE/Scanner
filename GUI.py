import tkinter as tk
from nmap_port_scanner import NmapScanner
from ipadd_finder import url_to_ipadd
from urllib.parse import urlparse
from sql_injection_scanner import sql_injection_scan
from tkinter import messagebox
from Xss_scanner import XSScanner
from bruteforce import bruteforce2



def navigate_to_page1():
    url = url_entry.get()
    mes=bruteforce2(url,'admin')
    print("MMMMMMMMMMMMMMMMMMMMMMMMMM\n"+mes)

    root = tk.Tk()
    root.title("Brute Force")
    root.geometry("600x200")

    title_label = tk.Label(root, text="Scanning...", font=("Helvetica", 20))
    title_label.pack(pady=10)

    title_label.configure(text=mes)
    window.update_idletasks()


    root.mainloop()
    

def navigate_to_page2():
    url = url_entry.get()
    mes=XSScanner(url)
    print("MMMMMMMMMMMMMMMMMMMMMMMMMM\n"+mes)

    root = tk.Tk()
    root.title("scan Xss vulnerabilities")
    root.geometry("600x200")

    title_label = tk.Label(root, text="Scanning...", font=("Helvetica", 20))
    title_label.pack(pady=10)

    title_label.configure(text=mes)
    window.update_idletasks()


    root.mainloop()


def navigate_to_page3():

    url = url_entry.get()
    mes=sql_injection_scan(url)
    print("MMMMMMMMMMMMMMMMMMMMMMMMMM\n"+mes)

    root = tk.Tk()
    root.title("Scan Sql Injections ")
    root.geometry("600x200")

    title_label = tk.Label(root, text="Scanning...", font=("Helvetica", 20))
    title_label.pack(pady=10)

    title_label.configure(text=mes)
    window.update_idletasks()




    root.mainloop()

    


def extract_domain_from_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain




def scan_button_clicked():
    
    url = url_entry.get()
    domain = extract_domain_from_url(url)
    print(domain)
    port_range = port_entry.get()
    
    
    output_text = f"Scanning domain : {domain} ...."  
    output_label.configure(text=output_text)
    window.update_idletasks()

    ip_add = url_to_ipadd(domain)
    print(ip_add)
    output_text2 = f"The IP add is : {ip_add}"  
    output_label2.configure(text=output_text2)
    window.update_idletasks()
    
    mes=NmapScanner(ip_add,port_range)
    output_text3 = mes 
    output_label3.configure(text=mes)
    window.update_idletasks()









# Create the main window
window = tk.Tk()
window.title("Scanning GUI")
window.geometry("800x800")

# Create the title label
title_label = tk.Label(window, text="Scanning GUI", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

# Create the URL form
url_label = tk.Label(window, text="Enter the URL", font=("Arial", 12))
url_label.pack(pady=10)

url_entry = tk.Entry(window, width=50)
url_entry.pack(pady=10)

port_range_label = tk.Label(window, text="Enter a port range (e.g., 80-100)", font=("Arial", 12))
port_range_label.pack(pady=10)
# Create the port entry and align it to the left
port_entry = tk.Entry(window, width=50)
port_entry.pack(pady=10)

# Create the Scan button
scan_button = tk.Button(window, text="Scan", command=scan_button_clicked, font=("Arial", 16), padx=20, pady=10)
scan_button.pack()

# Create the label to display the output
output_label = tk.Label(window, text="", font=("Arial", 14))
output_label.pack(pady=20)

# Create the label to display the output
output_label2 = tk.Label(window, text="", font=("Arial", 14))
output_label2.pack(pady=20)

# Create the label to display the output
output_label3 = tk.Label(window, text="", font=("Arial", 14))
output_label3.pack(pady=30)

# frame to hold the buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

# buttons
button1 = tk.Button(button_frame, text="Brute Force", command=navigate_to_page1, font=("Arial", 16), width=15, height=3)
button1.pack(side=tk.LEFT, padx=10)

button2 = tk.Button(button_frame, text="XSS", command=navigate_to_page2, font=("Arial", 16), width=15, height=3)
button2.pack(side=tk.LEFT, padx=10)

button3 = tk.Button(button_frame, text="Sql Injection", command=navigate_to_page3, font=("Arial", 16), width=15, height=3)
button3.pack(side=tk.LEFT, padx=10)
# footer message
footer_message = tk.Label(window, text="Powered By Houssam ED", font=("Arial", 12), fg="gray")
footer_message.pack(side=tk.BOTTOM)

# Start the GUI event loop
window.mainloop()
