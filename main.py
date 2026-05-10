import customtkinter as ctk
import psutil
import os
from ipdetails import ipdetails as ipd
from dotenv import load_dotenv

load_dotenv()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SidebarWidget(ctk.CTk):
    def __init__(self):
        super().__init__()

        API_KEY = os.getenv("IPINFO_API_KEY")

        self.details = ipd.IPDetails(API_KEY)
        self.title(self.details.getHostname())
        self.geometry("340x680")
        self.resizable(False, False)
        self.lastIo = psutil.net_io_counters()

        self.__build_ui();
        self.__updateSpeeds()

    def __build_ui(self):
        self.__createHeader()
        self.__createMainframe()


    def __createHeader(self):
        f_header = ctk.CTkFrame(self, fg_color="#1B1B1B", corner_radius=24)
        f_header.pack(fill="x", padx=12, pady=12)

        l_title = ctk.CTkLabel(
            f_header,
            text="🌐 Network Sidebar",
            font=("Segoe UI", 24, "bold")
        )
        l_title.pack(pady=18)

    def __createMainframe(self):
        f_main = ctk.CTkFrame(self, fg_color="#1A1A1A", corner_radius=24)
        
        self.__labelPairMaker(f_main, "Local IP:", self.details.getLocalIP())
        self.__labelPairMaker(f_main, "Public IP:", self.details.getPublicIP())
        self.__labelPairMaker(f_main, "Location:", self.details.getLocation())
        self.__labelPairMaker(f_main, "ISP:", self.details.getISP())

        self.l_speed = self.__labelPairMaker(f_main, "Transfer Rate:", "0 KB/s  | 0 KB/s Download")

        f_main.pack(fill="both", expand=True, padx=12, pady=(0,12))

        
    def __labelPairMaker(self, parent, text1, text2):
        f_Labels = ctk.CTkFrame(parent, fg_color="#222222", corner_radius=18)
        f_Labels.pack(fill="x", padx=18, pady=8)
        
        label1 = ctk.CTkLabel(f_Labels, text=text1, font=("Segoe UI", 13), text_color="#aaaaaa")
        label1.pack(anchor="w", padx=14, pady=(10,0))

        label2 = ctk.CTkLabel(f_Labels, text=text2, font=("Segoe UI", 18, "bold"), text_color="#FFFFFF")
        label2.pack(anchor="w", padx=14, pady=(0,10))

        return label2

    def __updateSpeeds(self):
        currentIo = psutil.net_io_counters();
        
        upSpeed, downSpeed = self.details.getTransferRates(previousStats=self.lastIo, currentStats=currentIo)

        self.l_speed.configure(text=f"{upSpeed:.1f} KB/s ↑ | {downSpeed:.1f} KB/s ↓")

        self.lastIo = currentIo

        self.after(1000, self.__updateSpeeds)
        

    


app = SidebarWidget()
app.mainloop()

