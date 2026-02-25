import customtkinter as ctk
from PIL import Image, ImageTk
import os

# Cale relativă către folderul cu resurse
BASE_PATH = os.path.join(os.path.dirname(__file__), "assets")
LANDS_PATH = os.path.join(BASE_PATH, "lands")

# Mapare culori către regiuni
country_map = {
    (255, 242, 21): "AI_si_robotica",
    (87, 77, 150): "Arhitectura_calculatoarelor",
    (109, 178, 0): "ASD",
    (238, 31, 0): "Baze_de_date_si_regasire_de_informatii",
    (97, 20, 255): "Bioinformatica",
    (61, 148, 254): "Grafica",
    (125, 125, 1): "Inginerie_software",
    (255, 118, 213): "Interactiune_om_computer",
    (255, 20, 128): "Limbaje_de_programare",
    (0, 231, 237): "Sisteme_de_operare_si_retele",
    (60, 237, 0): "Stiinta_computationala",
    (255, 136, 20): "Informatica_organizatoriala"
}

def get_region_name(color, tolerance=20):
    """
    Caută un match dintre culoarea dată și cheile din country_map folosind o toleranță.
    Dacă diferența pentru fiecare componentă este mai mică sau egală cu pragul dat,
    se consideră că a fost găsit un match.
    """
    for key in country_map:
        if all(abs(color[i] - key[i]) <= tolerance for i in range(3)):
            return country_map[key]
    return None

class MapExplorer:
    def __init__(self):
        self.history = []

        self.root = ctk.CTk()
        self.root.title("Map Explorer")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}")
        self.root.state("zoomed")  # Sau poți folosi self.root.attributes("-fullscreen", True)

        self.canvas = ctk.CTkCanvas(self.root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.image_on_canvas = self.canvas.create_image(0, 0, anchor="nw")
        self.canvas.image_tk = None

        # Butonul Back fără chenar negru, cu aspect alb și text negru.
        self.back_button = ctk.CTkButton(
            self.root, 
            text="Back", 
            command=self.go_back, 
            fg_color="light blue", 
            text_color="black", 
            border_width=0,
            border_color="white",
            hover_color="white",
            corner_radius=0
        )
        self.back_button.place(x=20, y=20)

        # Butonul Exit fără chenar negru, alb cu text negru.
        self.exit_button = ctk.CTkButton(
            self.root, 
            text="Exit", 
            command=self.root.quit, 
            fg_color="light blue", 
            text_color="black",
            border_width=0,
            border_color="white",
            hover_color="white",
            corner_radius=0
        )
        # Butonul Exit se va afișa doar pe harta principală, plasat imediat sub butonul Back.

        self.root.bind("<Escape>", lambda e: self.root.quit())
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Configure>", self.update_image)

        self.load_map(BASE_PATH, "map.jpg", "map_cc.jpg")
        self.root.mainloop()

    def load_map(self, folder, image_file, overlay_file):
        self.current_folder = folder
        self.image_path = os.path.join(folder, image_file)
        self.overlay_path = os.path.join(folder, overlay_file)
        try:
            print(f"[INFO] Încărc harta: {self.image_path}")
            print(f"[INFO] Încărc overlay: {self.overlay_path}")
            self.original_map = Image.open(self.image_path)
            # Convertim overlay-ul la modul RGB pentru a asigura corectitudinea culorilor
            self.original_overlay = Image.open(self.overlay_path).convert("RGB")
            self.update_image()

            # Afișăm butonul Exit doar dacă suntem pe harta principală.
            if self.current_folder == BASE_PATH:
                # Calculăm poziția butonului Exit imediat sub butonul Back.
                back_y = 20
                back_height = self.back_button.winfo_reqheight()
                margin = 10  # spațiu între butoane
                self.exit_button.place(x=20, y=back_y + back_height + margin)
            else:
                self.exit_button.place_forget()

        except FileNotFoundError as e:
            print(f"[EROARE] Nu s-a găsit fișierul: {e}")

    def update_image(self, event=None):
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        if w < 2 or h < 2:
            return
        print(f"[DEBUG] Redimensionare la: {w}x{h}")
        self.resized_map = self.original_map.resize((w, h), Image.Resampling.LANCZOS)
        # Folosim NEAREST pentru overlay, astfel încât culorile să nu fie interpolate.
        self.resized_overlay = self.original_overlay.resize((w, h), Image.Resampling.NEAREST)
        self.canvas.image_tk = ImageTk.PhotoImage(self.resized_map)
        self.canvas.itemconfig(self.image_on_canvas, image=self.canvas.image_tk)

    def on_click(self, event):
        try:
            x, y = event.x, event.y
            print(f"[DEBUG] Click detectat la: ({x}, {y})")
            # Obținem culoarea pixelului din overlay.
            color = self.resized_overlay.getpixel((x, y))[:3]
            print(f"[DEBUG] Culoare detectată: {color}")
            region_name = get_region_name(color, tolerance=20)
            if region_name:
                print(f"[INFO] Navigare către: {region_name}")
                self.history.append((self.current_folder, os.path.basename(self.image_path), os.path.basename(self.overlay_path)))
                self.load_map(LANDS_PATH, f"{region_name}.jpg", f"{region_name}_cc.jpg")
            else:
                print(f"[WARN] Zona selectată nu este recunoscută. Culoare: {color}")
        except Exception as e:
            print(f"[EROARE] la click: {e}")

    def go_back(self):
        if self.history:
            folder, img, overlay = self.history.pop()
            print(f"[INFO] Revenire la: {img} cu overlay {overlay}")
            self.load_map(folder, img, overlay)

if __name__ == "__main__":
    MapExplorer()
