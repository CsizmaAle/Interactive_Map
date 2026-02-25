import customtkinter as ctk
from PIL import Image, ImageTk
import os

# Cale relativă către folderele cu resurse
BASE_PATH = os.path.join(os.path.dirname(__file__), "assets")
LANDS_PATH = os.path.join(BASE_PATH, "lands")
#CITY_PATH= 

# Mapare culori către țări (nivelul hărții mamă)
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

# Mapare culori pentru regiuni/orășe (nivel 1)
region_color_maps = {
    "AI_si_robotica": {
        (246, 50, 0): "Oras1",
        (87, 77, 150): "Oras2",
    },
    "Arhitectura_calculatoarelor": {
        (109, 178, 0): "Oras1",
        (238, 31, 0): "Oras2",
    }
}

# Mapare culori pentru clădiri (nivel 2)
city_color_maps = {
    "AI_si_robotica/Oras1": {
        (254, 106, 0): "Cladire1",
        (87, 77, 150): "Cladire2",
    },
    "Arhitectura_calculatoarelor/Oras1": {
        (109, 178, 0): "Cladire1",
        (238, 31, 0): "Cladire2",
    }
}

class MapExplorer:
    def __init__(self):
        # Istoricul stărilor: (folder, nume_imagine, nume_overlay, level, current_country, current_region, current_building)
        self.history = []  
        self.current_level = 0  # 0: harta mamă, 1: țară, 2: regiune/orăș, 3: clădire
        self.current_country = None
        self.current_region = None
        self.current_building = None

        self.root = ctk.CTk()
        self.root.title("Map Explorer")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}")
        self.root.state("zoomed")

        self.canvas = ctk.CTkCanvas(self.root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor="nw")
        self.canvas.image_tk = None

        # Butoanele Back și Exit (stilizate: light blue cu text negru,
        # fără chenar; la hover, fundalul devine alb)
        self.back_button = ctk.CTkButton(
            self.root,
            text="Back",
            command=self.go_back,
            fg_color="light blue",
            hover_color="white",
            text_color="black",
            border_width=0,
            border_color="light blue",
            corner_radius=0
        )
        self.back_button.place(x=20, y=20)

        self.exit_button = ctk.CTkButton(
            self.root,
            text="Exit",
            command=self.root.quit,
            fg_color="light blue",
            hover_color="white",
            text_color="black",
            border_width=0,
            border_color="light blue",
            corner_radius=0
        )
        # Vom plasa butonul.EXIT doar pe harta mamă (nivel 0)
        if self.current_level == 0:
            self.exit_button.place(x=20, y=70)
        else:
            self.exit_button.place_forget()

        self.root.bind("<Escape>", lambda e: self.root.quit())
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Configure>", self.update_image)

        # Încarcă harta mamă (nivel 0)
        self.load_map(BASE_PATH, "map.jpg", "map_cc.jpg")
        self.root.mainloop()

    def load_map(self, folder, image_file, overlay_file):
        """Încarcă imaginea și overlay-ul din folderul specificat."""
        self.current_folder = folder
        self.image_path = os.path.join(folder, image_file)
        self.overlay_path = os.path.join(folder, overlay_file)
        try:
            print(f"[INFO] Încărc harta: {self.image_path}")
            print(f"[INFO] Încărc overlay: {self.overlay_path}")
            self.original_map = Image.open(self.image_path)
            self.original_overlay = Image.open(self.overlay_path).convert("RGB")
            self.update_image()
            # Manipulează vizibilitatea butonului de exit: apare doar la nivelul 0 (harta mamă)
            if self.current_level == 0:
                self.exit_button.place(x=20, y=70)
            else:
                self.exit_button.place_forget()
        except FileNotFoundError as e:
            print(f"[EROARE] Fișierul nu a fost găsit: {e}")

    def update_image(self, event=None):
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        if w < 2 or h < 2:
            return
        print(f"[DEBUG] Redimensionare la: {w}x{h}")
        self.resized_map = self.original_map.resize((w, h), Image.Resampling.LANCZOS)
        self.resized_overlay = self.original_overlay.resize((w, h), Image.Resampling.NEAREST)
        self.canvas.image_tk = ImageTk.PhotoImage(self.resized_map)
        self.canvas.itemconfig(self.image_on_canvas, image=self.canvas.image_tk)

    def on_click(self, event):
        try:
            x, y = event.x, event.y
            print(f"[DEBUG] Click detectat la: ({x}, {y})")
            color = self.resized_overlay.getpixel((x, y))[:3]
            print(f"[DEBUG] Culoare detectată: {color}")

            if self.current_level == 0:
                # Nivel 0: Se selectează țara din harta mamă
                selected_country = country_map.get(color)
                if selected_country:
                    print(f"[INFO] Țara selectată: {selected_country}")
                    self.history.append((self.current_folder,
                                         os.path.basename(self.image_path),
                                         os.path.basename(self.overlay_path),
                                         self.current_level,
                                         self.current_country,
                                         self.current_region,
                                         self.current_building))
                    self.current_level = 1
                    self.current_country = selected_country
                    self.load_map(LANDS_PATH, f"{selected_country}.jpg", f"{selected_country}_cc.jpg")
                else:
                    print("[WARN] Nicio țară identificată pentru această culoare.")
            elif self.current_level == 1:
                # Nivel 1: Se selectează regiunea/orășul (folosim region_color_maps)
                mapping = region_color_maps.get(self.current_country, {})
                selected_region = mapping.get(color)
                if selected_region:
                    print(f"[INFO] Regiunea/Orășul selectat: {selected_region}")
                    self.history.append((self.current_folder,
                                         os.path.basename(self.image_path),
                                         os.path.basename(self.overlay_path),
                                         self.current_level,
                                         self.current_country,
                                         self.current_region,
                                         self.current_building))
                    self.current_level = 2
                    self.current_region = selected_region
                    # Se presupune ca hărțile regiunilor se găsesc în folderul cu numele regiunii în cadrul LANDS_PATH
                    self.load_map(os.path.join(LANDS_PATH, selected_region), f"{selected_region}.jpg", f"{selected_region}_cc.jpg")
                else:
                    print("[WARN] Nicio regiune identificată pentru această culoare.")
            elif self.current_level == 2:
                # Nivel 2: Se selectează clădirea (folosim city_color_maps)
                key = f"{self.current_country}/{self.current_region}"
                mapping = city_color_maps.get(key, {})
                selected_building = mapping.get(color)
                if selected_building:
                    print(f"[INFO] Clădirea selectată: {selected_building}")
                    self.history.append((self.current_folder,
                                         os.path.basename(self.image_path),
                                         os.path.basename(self.overlay_path),
                                         self.current_level,
                                         self.current_country,
                                         self.current_region,
                                         self.current_building))
                    self.current_level = 3
                    self.current_building = selected_building
                    # Se presupune că hărțile clădirilor se găsesc în folderul clădirii, în interiorul folderului regiunii
                    self.load_map(os.path.join(LANDS_PATH, self.current_region, selected_building), f"{selected_building}.jpg", f"{selected_building}_cc.jpg")
                else:
                    print("[WARN] Nicio clădire identificată pentru această culoare.")
            else:
                print("[INFO] La nivelul maxim – nu există alte hărți.")
        except Exception as e:
            print(f"[EROARE] La click: {e}")

    def go_back(self):
        if self.history:
            (last_folder, last_image, last_overlay, last_level,
             last_country, last_region, last_building) = self.history.pop()
            self.current_folder = last_folder
            self.current_level = last_level
            self.current_country = last_country
            self.current_region = last_region
            self.current_building = last_building
            print(f"[INFO] Revenire la: {last_image} cu overlay {last_overlay}")
            self.load_map(last_folder, last_image, last_overlay)

if __name__ == "__main__":
    MapExplorer()
