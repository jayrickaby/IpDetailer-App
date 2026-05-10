# IpDetailer App
Simple application to show select information about an IP and network.
Helped me learn about CustomTkinter.

## About this project
This was made after someone I know AI-generated some code which was: (a) Slow (b) Not working (c) Not functional. This is 1 of 3 repositories I have created that rewrote, fixed, and improved on the AI-generated slop.
Some challenges I faced:
- Using CustomTkinter. I had used normal Tkinter in class, but adapting the sloppy AI-produced CustomTkinter code to be feasible was also a challenge. Did you know the original couldn't fit every statistic onto the window without it cutting off, along with there being no titlebar to actually close the program?
- Environment Variables. I didn't want my api key to public for everyone to use. So, I figured out about .env and how to get it to work in Python.
- Updating a label dynamically. The transfer rates needed to be updating every second, but I figured out how to get it to change. Hackily, or not.

## Gallery
<img width="147.33" height="307.66" alt="image" src="https://github.com/user-attachments/assets/c6e82147-c46b-45c4-8d9d-02a9d5e44e22" />

## Features
- A sidebar widget displaying information about: Local IP, Public IP, Location, ISP and Network Traffic.
- A nice design that doesn't show the jarring design of normal Tkinter.
- API Key that relies on the user, not the creator.

## Requirements
- Python
- Python customtkinter package (included as a git submodule)
- My [ipdetails](https://github.com/jayrickaby/ipdetails) package

## Licence
Copyright © 2026 Jay Rickaby,
Licensed under the MIT License
