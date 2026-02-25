import os

region_color_maps = {
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
    
    "Stiinta_computationala":{
        (254, 41, 1): "Analiza_numerica",
        (254, 155, 0): "Calcul_de_inalta_performanta",
        (253, 236, 0): "Aplicatii_fizica_computationala",
        (83, 254, 0): "Aplicatii_biologia_computationala",
        (0, 254, 254): "Aplicatii_chimia_computationala",
        (0, 69, 253): "Aplicatii_economia_computationala",
        (201, 0, 254): "Aplicatii_ingineria_computationala"
    }
     
}

def create_folder_structure(base_path, structure):
    for domain, topics in structure.items():
        domain_path = os.path.join(base_path, domain)
        os.makedirs(domain_path, exist_ok=True)
        for _, folder_name in topics.items():
            subfolder_path = os.path.join(domain_path, folder_name)
            os.makedirs(subfolder_path, exist_ok=True)
            print(f"Creat: {subfolder_path}")

# Exemplu de rulare
if __name__ == "__main__":
    base_folder = r"C:\\Users\\Alexandra C\\OneDrive\\Desktop\\F. SEM II\\MPI\\MAP EXPLORER\\assets\\lands"  # <-- schimbă aici!
    create_folder_structure(base_folder, region_color_maps)