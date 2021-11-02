#!/usr/bin/env python3
# Minecraft Launcher for many 
from tkinter import Tk, Label, Entry, Button, mainloop
from tkinter.ttk import Combobox
import minecraft_launcher_lib
import os
import subprocess
import sys


def main():
    def launch():
        window.withdraw()

        print("Downloading game...")

        minecraft_launcher_lib.install.install_minecraft_version(version_select.get(), minecraft_directory)

        #login_data = minecraft_launcher_lib.account.login_user(username_input.get(), password_input.get())

        options = {
            "username": username_input.get(),
            "uuid": "0",
            "token": "0",
            "launcherName": "PowerCraft PPC Launcher",
            "launcherVersion": "0.1.1",
            "nativesDirectory": "./natives"
        }
        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version_select.get(), minecraft_directory, options)

        print("Starting game...")

        subprocess.call(minecraft_command)

        sys.exit(0)
        
    def settings():
        print("E: Function not implemented yet.")

    def ownlaunch():
        window.withdraw()

        minecraft_launcher_lib.install.install_minecraft_version(version_select.get(), minecraft_directory)

        print("Downloading game...")

        login_data = minecraft_launcher_lib.account.login_user(username_input.get(), password_input.get())

        options = {
            "username": login_data["selectedProfile"]["name"],
            "uuid": login_data["selectedProfile"]["id"],
            "token": login_data["accessToken"],
            "launcherName": "mpl-dev-test",
            "launcherVersion": "a0.1",
            "nativesDirectory": "./natives-current"
        }
        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version_select.get(), minecraft_directory, options)

        print("Starting game...")
        os.system("rm natives-current/*")
        os.system("cp own-natives/* natives-current/")
        print(minecraft_command)
        subprocess.call(minecraft_command)
        sys.exit(0)

    window = Tk()
    window.title("PowerCraft Launcher - linux release 0.1.1")

    Label(window, text="PowerCraft Laucher").grid(row=0, column=1)
    Label(window, text="Username/E-mail:").grid(row=1, column=0)
    username_input = Entry(window)
    username_input.grid(row=1, column=2)
    Label(window, text="Password:").grid(row=2, column=0)
    password_input = Entry(window)
    password_input.grid(row=2, column=2)

    minecraft_directory = "./gamedir"
    version_list = ['1.5.2', '1.2.5', '1.7.10', '1.12.2', '1.12.1', '1.12', '1.11.2', '1.11.1', '1.11', '1.10.2', '1.10.1', '1.10', '1.9.4', '1.9.3', '1.9.2', '1.9.1', '1.9', '1.8.9', '1.8.8', '1.8.7', '1.8.6', '1.8.5', '1.8.4', '1.8.3', '1.8.2', '1.8.1', '1.8', '1.7.10', '1.7.9', '1.7.8', '1.7.7', '1.7.6', '1.7.5', '1.7.4', '1.7.3', '1.7.2', '1.7.1', '1.7', '1.6.4', '1.6.3', '1.6.2', '1.6.1', '1.6', '1.5.2', '1.5.1', '1.5', '1.4.7', '1.4.6', '1.4.5', '1.4.4', '1.4.3', '1.4.2', '1.4.1', '1.4', '1.3.2', '1.3.1', '1.3', '1.2.5', '1.2.4', '1.2.3', '1.2.2', '1.2.1', '1.1', '1.0']

    Label(window, text="Version:").grid(row=3, column=0)
    version_select = Combobox(window, values=version_list)
    version_select.grid(row=3, column=2)
    version_select.current(0)

    Button(window, text="Launch", command=launch).grid(row=4, column=1)
    
    print("Launcher initialised.")

    mainloop()


if __name__ == "__main__":
    main()
