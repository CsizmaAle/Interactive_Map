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
        (246, 50, 0): "Invatare_automata_si_deeplearning",
        (246, 139, 1): "Procesarea_limbajului_natural_si_viziune_computerizata",
        (246, 203, 0): "AI_explicabil_si_sisteme_multiagent",
        (144, 246, 0): "Simulare_si_realitate_virtuala",
        (0, 246, 181): "Robotica_cognitiva_si_sisteme_de_control_inteligente",
        (0, 134, 247): "Roboti_autonomi_si_industriali",
        (192, 0, 246): "Roboti_umanoizi_si_colaborativi",
        (62, 0, 247): "Robotica_medicala_si_soft_robotics",
        (246, 0, 187): "Robotica_de_tip_roi",
    },
    
    "Arhitectura_calculatoarelor": {
        (255, 102, 6): "Arhitectura_hardware",
        (254, 200, 4): "Arhitectura_software",
        (170, 255, 4):"Arhitectura_sistemelor_distribuite",
        (4, 233, 254): "Arhitectura_bazei_de_date",
        (5, 255, 121): "Arhitectura_retelelor_si_comunicatiilo",
        (255, 6, 234): "Arhitectura_securitatii_informatice",
        (24, 5, 255) : "Arhitectura_cloud_si_devops",
    },
    
    "ASD":{
        (235, 131, 8): "Teoria_algoritmilor",
        (234, 217, 5): "Structuri_de_date_clasice",
        (227, 44, 0): "Algoritmi_fundamentali",
        (134, 235, 7): "Structuri_de_date_avansate",
        (235, 7, 182): "Algoritmi_pe_grafuri",
        (6, 235, 153): "Algoritmi_probabilistici_si_randomizati",
        (148, 7, 236): "Algoritmi_geometrici",
        (5, 119, 234): "Algoritmi_paraleli_si_distribuiti",
        
    },
    
     "Baze_de_date_si_regasire_de_informatii":{
         (255, 0, 94): "Securitate_si_confidentialitate",
         (205, 0, 255): "Mecanisme_de_stocare_si_indexare",
         (37, 0, 254): "Concurrency_control_and_transaction_management",
         (0, 153, 255): "Acces_la_date_si_optimizarea_interogarilor",
         (0, 255, 207): "Recuperarea_si_integritatea",
         (68, 255, 0): "Big_data_si_bd_distribuite",
         (249, 255, 1): "Reprezentari_avansate_ale_datelor_si_vm",
         (255, 176, 1): "Depozitarea_datelor_si_analiza",
         (255, 112, 0): "Modele_logice_de_date",
         (255, 32, 0): "Heterogenous_data_si_multimedia_interogation",
         
    },
     
     "Bioinformatica":{
         (203, 104, 0):"Analiza_secventelor_biologice",
         (194, 203, 0): "Bioinformatica_structurala",
         (203, 152, 0): "Biotehnologie",
         (0, 203, 150): "Bioinformatica_sistemelor",
         (26, 203, 0): "Bioinformatica_evolutionista",
         (120, 0, 160): "Bioinformatica_medicala",
         (203, 0, 188): "Proteomica",
         (176, 72, 97): "Genomica",
         (202, 43, 1): "Bioinformatica_aplicata_in_farmacologie"
         
    },
     
    "Grafica":{
        (0, 254, 114): "Vizualizarea_datelor",
        (153, 254, 0): "GUI",
        (0, 254, 254): "CGI",
        (1, 126, 254): "Grafica_pentru_jocuri_video",
        (46, 1, 254): "AR",
        (155, 0, 254): "VR",
        (253, 0, 179): "3d",
        (254, 55, 0): "2d"
    
    },
    
    "Inginerie_software":{
        (230, 4, 254): "Dezvoltare_software",
        (4, 116, 254): "Ingineria_securitatii_software",
        (3, 255, 168): "Arhitectura_software",
        (255, 201, 4): "Ingineria_sistemelor_software",
        (160, 255, 5):"Testarea_si_asigurarea_calitatii",
        (255, 96, 4): "Devops_si_automatizarea_software",
        
    },
    
    "Interactiune_om_computer":{
        (255, 92, 13): "Securitate_si_etica_in_HCI",
        (255, 201, 13): "Interactiunea_bazata_pe_ai",
        (152, 255, 13): "UI/UX_design",
        (13, 255, 169): "Interactiunea_in_medii_colaborative",
        (205, 13, 255): "Factori_umani_si_psihologia_interactiunii",
        (13, 85, 255): "Interactiunea_in_contexte_specifice",
        
    },
    
    "Limbaje_de_programare":{
        (255, 241, 0): "Programare_logica",
        (255, 151, 0): "Programare_functionala",
        (75, 255, 0): "Programare_declarativa",
        (255, 35, 0): "Programare_orientata_pe_obiect",
        (0, 75, 255): "Metaprogramming",
        (1, 255, 231): "Programare_reactiva_si_event_based",
        (187, 0, 255): "Programare_concurenta_si_paralela",
        (254, 0, 212): "Programare_imperativa",
    },
    
    "Sisteme_de_operare_si_retele":{
        (235, 144, 1): "Sisteme_de_fisiere",
        (233, 212, 0): "Programare_concurenta",
        (0, 234, 145): "Analiza_comportamentelor_programelor",
        (0, 197, 234): "Teoria_concurentei",
        (0, 81, 233): "Gestiunea_memoriei",
        (184, 0, 234): "Teoria_planificarii_proceselor",
        (234, 1, 93): "Retele_de_calculatoare",
    
    },
    
    "Stiinta_computationala":{
        (254, 41, 1): "Analiza_numerica",
        (254, 155, 0): "Calcul_de_inalta_performanta",
        (253, 236, 0): "Aplicatii_fizica_computationala",
        (83, 254, 0): "Aplicatii_biologia_computationala",
        (0, 254, 254): "Aplicatii_chimia_computationala",
        (0, 69, 253): "Aplicatii_economia_computationala",
        (201, 0, 254): "Aplicatii_ingineria_computationala"
    },
    
    "Informatica_organizatoriala":{
        (100, 255, 3): "Bd_si_gestionarea_informatiilor",
        (2, 255, 224): "MIS",
        (2, 132, 255): "Guvernanta_it_si_managementul_strategic_al_tehnologiilor",
        (209, 2, 254): "Interactiunea_oc_in_mediul_organizational",
        (252, 231, 0): "Srhitectura_sistemelor_informatice_pt_organizatii",
        (251, 133, 1): "Retele_si_securitatea_informatiilor_in_organizatii",
        (251, 42, 1): "Automatizarea_si_optimizarea_proceselor",
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
    },
    
    "Baze_de_date_si_regasire_de_informatii/Modele_logice_de_date":{
        (255, 0, 170): "Modele_logice_de_date_magazine",
        (255, 247, 61): "Modele_logice_de_date_scoala",
        (255, 143, 25): "Modele_logice_de_date_biblioteca",
        (255, 57, 0): "Modele_logice_de_date_spital",
        (75, 75, 75): "Modele_logice_de_date_laborator",
        (61, 243, 62): "Modele_logice_de_date_parc",
        (141, 0, 255): "Modele_logice_de_date_monument"
    },
    
    "Baze_de_date_si_regasire_de_informatii/Mecanisme_de_stocare_si_indexare":{
        (61, 243, 62): "Mecanisme_de_stocare_si_indexare_parc",
        (75, 75, 75): "Mecanisme_de_stocare_si_indexare_fabrica",
        (255, 143, 25): "Mecanisme_de_stocare_si_indexare_biblioteca",
        (255, 0, 170): "Mecanisme_de_stocare_si_indexare_magazine",
        (255, 247, 61): "Mecanisme_de_stocare_si_indexare_scoala",
        (255, 57, 0): "Mecanisme_de_stocare_si_indexare_spital",
        (141, 0, 255): "Mecanisme_de_stocare_si_indexare_monument",
    },
    
    "Baze_de_date_si_regasire_de_informatii/Concurrency_control_and_transaction_management":{
        (255, 0, 170): "Concurrency_control_and_transaction_management_magazine",
        (75, 75, 75): "Concurrency_control_and_transaction_management_fabrica",
        (141, 0, 255): "Concurrency_control_and_transaction_management_monument",
        (255, 57, 0): "Concurrency_control_and_transaction_management_politie",
        (61, 243, 62): "Concurrency_control_and_transaction_management_parc",
        (255, 247, 61): "Concurrency_control_and_transaction_management_scoala",
        (255, 143, 25): "Concurrency_control_and_transaction_management_biblioteca",

    },
    "Baze_de_date_si_regasire_de_informatii/Acces_la_date_si_optimizarea_interogarilor":{
        (61, 243, 62): "Acces_la_date_si_optimizarea_interogarilor_parc",
        (141, 0, 255): "Acces_la_date_si_optimizarea_interogarilor_monument",
        (255, 247, 61): "Acces_la_date_si_optimizarea_interogarilor_scoala",
        (255, 143, 25): "Acces_la_date_si_optimizarea_interogarilor_biblioteca",
        (255, 0, 170): "Acces_la_date_si_optimizarea_interogarilor_magazine",
        (75, 75, 75): "Acces_la_date_si_optimizarea_interogarilor_laborator",
        (255, 57, 0): "Acces_la_date_si_optimizarea_interogarilor_spital",
    }
    
    
}

class MapExplorer:
    def __init__(self):
        # Istoricul: (folder, nume_imagine, nume_overlay, nivel, current_country, current_region, current_building)
        self.history = []  
        self.current_level = 0  # 0: harta mamă, 1: țară, 2: regiune/orăș, 3: clădire
        self.current_country = None
        self.current_region = None
        self.current_building = None

        self.root = ctk.CTk()
        self.root.title("Map Explorer")

        # Setare fullscreen fără state("zoomed")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        # Alternativ: self.root.attributes("-fullscreen", True)

        self.canvas = ctk.CTkCanvas(self.root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor="nw")
        self.canvas.image_tk = None

        # Butonul Back este mereu prezent
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

        # Butonul Exit (afișat doar în harta mamă)
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

        # Butonul Home (afișat pe toate nivelurile, cu excepția hărții mamă)
        self.home_button = ctk.CTkButton(
            self.root,
            text="Home",
            command=self.go_home,
            fg_color="light blue",
            hover_color="white",
            text_color="black",
            border_width=0,
            border_color="light blue",
            corner_radius=0
        )

        self.root.bind("<Escape>", lambda e: self.root.quit())
        self.canvas.bind("<Button-1>", self.on_click)

        # Debounce pentru redimensionare
        self.resize_id = None
        self.canvas.bind("<Configure>", self.debounced_update_image)

        # Încarcă harta de start (presupunem "map.jpg" cu overlay "map_cc.jpg")
        if not self.load_map(BASE_PATH, "map.jpg", "map_cc.jpg"):
            print("[EROARE] Harta de start nu a putut fi încărcată.")
        self.update_navigation_buttons()
        self.root.mainloop()

    def update_navigation_buttons(self):
        """Afișează butonul Exit doar pe harta mamă și, în caz contrar, afișează butonul Home."""
        if self.current_level == 0:
            self.exit_button.place(x=20, y=70)
            self.home_button.place_forget()
        else:
            self.exit_button.place_forget()
            self.home_button.place(x=20, y=70)

    def debounced_update_image(self, event):
        """Funcție de debounce pentru redimensionare."""
        if self.resize_id:
            self.root.after_cancel(self.resize_id)
        self.resize_id = self.root.after(150, self.update_image)

    def load_map(self, folder, image_file, overlay_file):
        # Verifică extensiile: dacă .jpg nu există, caută .jpeg
        jpg_path = os.path.join(folder, image_file)
        jpeg_path = jpg_path.replace(".jpg", ".jpeg")
        if not os.path.exists(jpg_path) and os.path.exists(jpeg_path):
            image_file = image_file.replace(".jpg", ".jpeg")
        image_path = os.path.join(folder, image_file)
        
        try:
            print(f"[INFO] Încărc hartă: {image_path}")
            temp_map = Image.open(image_path)

            if overlay_file:
                overlay_jpg_path = os.path.join(folder, overlay_file)
                overlay_jpeg_path = overlay_jpg_path.replace(".jpg", ".jpeg")
                if not os.path.exists(overlay_jpg_path) and os.path.exists(overlay_jpeg_path):
                    overlay_file = overlay_file.replace(".jpg", ".jpeg")
                overlay_path = os.path.join(folder, overlay_file)
                print(f"[INFO] Încărc overlay: {overlay_path}")
                temp_overlay = Image.open(overlay_path).convert("RGB")
            else:
                temp_overlay = None
                overlay_path = None

        except Exception as e:
            print(f"[EROARE] Nu se poate încărca harta sau overlay-ul: {e}")
            return False

        # Actualizează starea internă doar dacă încărcarea a decurs cu succes
        self.current_folder = folder
        self.image_path = image_path
        self.original_map = temp_map
        self.original_overlay = temp_overlay
        self.overlay_path = overlay_path  # Stocăm calea overlay-ului

        self.update_image()
        return True

    def update_image(self, event=None):
        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        if w < 2 or h < 2:
            return
        print(f"[DEBUG] Redimensionare la: {w}x{h}")
        self.resized_map = self.original_map.resize((w, h), Image.Resampling.LANCZOS)
        if self.original_overlay:
            self.resized_overlay = self.original_overlay.resize((w, h), Image.Resampling.NEAREST)
        else:
            self.resized_overlay = None
        self.canvas.image_tk = ImageTk.PhotoImage(self.resized_map)
        self.canvas.itemconfig(self.image_on_canvas, image=self.canvas.image_tk)

    def on_click(self, event):
        try:
            x, y = event.x, event.y
            print(f"[DEBUG] Click detectat la: ({x}, {y})")
            color = self.resized_overlay.getpixel((x, y))[:3] if self.resized_overlay else None
            print(f"[DEBUG] Culoare detectată: {color}")

            if self.current_level == 0:
                # Nivel 0: selectarea țării
                selected_country = country_map.get(color)
                if selected_country:
                    new_folder = LANDS_PATH
                    new_image = f"{selected_country}.jpg"
                    new_overlay = f"{selected_country}_cc.jpg"
                    backup_state = (
                        self.current_folder,
                        os.path.basename(self.image_path) if hasattr(self, "image_path") else None,
                        os.path.basename(self.overlay_path) if (hasattr(self, "overlay_path") and self.overlay_path) else None,
                        self.current_level,
                        self.current_country,
                        self.current_region,
                        self.current_building
                    )
                    if self.load_map(new_folder, new_image, new_overlay):
                        self.history.append(backup_state)
                        self.current_level = 1
                        self.current_country = selected_country
                        print(f"[INFO] Țara selectată: {selected_country}")
                        self.update_navigation_buttons()
                    else:
                        print("[EROARE] Nu se poate încărca harta pentru țara selectată. Nu se avansează nivelul.")
                else:
                    print("[WARN] Nicio țară identificată pentru această culoare.")

            elif self.current_level == 1:
                # Nivel 1: selectarea regiunii/orășului
                mapping = region_color_maps.get(self.current_country, {})
                selected_region = mapping.get(color)
                if selected_region:
                    new_folder = os.path.join(LANDS_PATH, self.current_country, selected_region)
                    new_image = f"{selected_region}.jpg"
                    new_overlay = f"{selected_region}_cc.jpg"
                    backup_state = (
                        self.current_folder,
                        os.path.basename(self.image_path),
                        os.path.basename(self.overlay_path) if self.overlay_path else None,
                        self.current_level,
                        self.current_country,
                        self.current_region,
                        self.current_building
                    )
                    if self.load_map(new_folder, new_image, new_overlay):
                        self.history.append(backup_state)
                        self.current_level = 2
                        self.current_region = selected_region
                        print(f"[INFO] Regiunea/Orășul selectat: {selected_region}")
                        self.update_navigation_buttons()
                    else:
                        print("[EROARE] Nu se poate încărca harta pentru regiunea/orășul selectat. Nu se avansează nivelul.")
                else:
                    print("[WARN] Nicio regiune identificată pentru această culoare.")
            
            elif self.current_level == 2:
                # Nivel 2: selectarea clădirii
                key = f"{self.current_country}/{self.current_region}"
                mapping = city_color_maps.get(key, {})
                selected_building = mapping.get(color)
                if selected_building:
                    new_folder = os.path.join(LANDS_PATH, self.current_country, self.current_region)
                    new_image = f"{selected_building}.jpg"
                    new_overlay = None  # La nivelul clădirii nu se folosește overlay
                    backup_state = (
                        self.current_folder,
                        os.path.basename(self.image_path),
                        os.path.basename(self.overlay_path) if self.overlay_path else None,
                        self.current_level,
                        self.current_country,
                        self.current_region,
                        self.current_building
                    )
                    if self.load_map(new_folder, new_image, new_overlay):
                        self.history.append(backup_state)
                        self.current_level = 3
                        self.current_building = selected_building
                        print(f"[INFO] Clădirea selectată: {selected_building}")
                        self.update_navigation_buttons()
                    else:
                        print("[EROARE] Nu se poate încărca harta pentru clădirea selectată. Nu se avansează nivelul.")
                else:
                    print("[WARN] Nicio clădire identificată pentru această culoare.")
            else:
                print("[INFO] La nivelul maxim — nu există alte hărți.")
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
            self.update_navigation_buttons()

    def go_home(self):
        """Resetează starea și reîncarcă harta mamă."""
        self.history.clear()
        self.current_level = 0
        self.current_country = None
        self.current_region = None
        self.current_building = None
        if not self.load_map(BASE_PATH, "map.jpg", "map_cc.jpg"):
            print("[EROARE] Nu se poate încărca harta mamă.")
        self.update_navigation_buttons()

if __name__ == "__main__":
    MapExplorer()
