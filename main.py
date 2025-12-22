from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import tkinter as tk
import time
import threading

# GUI Setup
window = tk.Tk()
window.title("Cookie Clicker Bot")
window.geometry("400x400")
window.resizable(True, True)

bot_running_lbl = tk.Label(window, text="The clicker is currently off.", font=("Calibri", 12))
bot_running_lbl.grid()

logs_lbl = tk.Label(window, text="Logs:", font=("Calibri", 12))
logs_lbl.grid(column=0, row=6)

logs_text = tk.Text(window, height=10, width=40, font=("Calibri", 10))
logs_text.grid(column=0, row=7)

# Selenium Setup
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://ozh.github.io/cookieclicker/")
time.sleep(5)

langEn = driver.find_element(By.ID, "langSelect-EN")
langEn.click() # Select English
time.sleep(3)
cookie = driver.find_element(By.ID, "bigCookie")

bot_running = False
cycle = 0
current_keybind = '<Control-d>'
is_setting_keybind = False

def handle_new_keybind(event, modifier):
    global current_keybind, is_setting_keybind
    if is_setting_keybind:
        new_bind = f'<{modifier}-{event.keysym}>'
        window.unbind(current_keybind)
        window.bind(new_bind, switched)
        current_keybind = new_bind
        display_text = f'{"Cmd" if modifier == "Command" else "Ctrl"} + {event.keysym.upper()}'
        keybind_btn.config(text=display_text)
        is_setting_keybind = False
        window.unbind('<Control-Key>')
        window.unbind('<Command-Key>')

def botOn():
    global bot_running
    global cycle
    try:
        while bot_running:
            cycle += 1
            
            # Click the cookie 100 times per cycle
            for _ in range(100):
                cookie.click()
                time.sleep(0.01)
            
            # Try to buy upgrades
            upgrades = driver.find_elements(By.CLASS_NAME, "upgrade")
            for upgrade in reversed(upgrades):
                try:
                    upgrade.click()
                except:
                    pass

            # Try to buy buildings
            buildings = driver.find_elements(By.CLASS_NAME, "product")
            for building in reversed(buildings):
                try:
                    building.click()
                except:
                    pass

            log_message = f"Cycle {cycle} complete.\n"
            window.after(0, lambda: logs_text.insert(tk.END, log_message))
            window.after(0, lambda: logs_text.see(tk.END))
            time.sleep(0.5)  # Short pause before next cycle

    except Exception as e:
        error_message = f"Bot stopped due to error: {e}\n"
        window.after(0, lambda: logs_text.insert(tk.END, error_message))
        window.after(0, lambda: logs_text.see(tk.END))
    finally:
        exit_message = "Stopping bot...\n"
        window.after(0, lambda: logs_text.insert(tk.END, exit_message))
        window.after(0, lambda: logs_text.see(tk.END))

def on_closing():
    global bot_running
    bot_running = False
    time.sleep(0.1)
    driver.quit()
    window.destroy()

def switched(event=None):
    global bot_running
    if bot_running:
        bot_running = False
        botSwitch.config(text='Turn On')
        bot_running_lbl.config(text="The clicker is currently off.")
    else:
        bot_running = True
        botSwitch.config(text='Turn Off')
        bot_running_lbl.config(text="The clicker is currently on.")

        thread = threading.Thread(target=botOn)
        thread.start()

        start_message = "Bot starting...\n"
        window.after(0, lambda: logs_text.insert(tk.END, start_message))
        window.after(0, lambda: logs_text.see(tk.END))

def set_new_keybind(event=None):
    global is_setting_keybind
    is_setting_keybind = True
    keybind_btn.config(text="Press Ctrl or Cmd + letter...")
    window.unbind(current_keybind)  # Temporarily unbind current to avoid conflict
    window.bind('<Control-Key>', lambda e: handle_new_keybind(e, 'Control'))
    window.bind('<Command-Key>', lambda e: handle_new_keybind(e, 'Command'))
    
botSwitch = tk.Button(window, text="Turn On", font=("Calibri", 12), command=switched)
botSwitch.grid(column=0, row=1)
window.bind('<Control-d>', switched)

currentKeybind_lbl = tk.Label(window, text="Current Keybind:", font=("Calibri", 10))
currentKeybind_lbl.grid(column=0, row=3)
keybind_btn = tk.Button(window, text="Ctrl + D", font=("Calibri", 10))
keybind_btn.grid(column=0, row=4)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
