import customtkinter as ctk
from PIL import Image, ImageTk
import os
import webbrowser

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
    (255, 136, 20): "Informatica_organizatoriala",
    (4, 0, 177): "https://www.uvt.ro/"
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
        (235, 131, 6): "Teoria_algoritmilor",
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
         (0, 255, 207): "Recuperarea_si_integritatea_bazelor_de_date",
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
        (152, 255, 13): "UI_UX_design",
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
        (252, 231, 0): "Arhitectura_sistemelor_informatice_pt_organizatii",
        (251, 133, 1): "Retele_si_securitatea_informatiilor_in_organizatii",
        (251, 42, 1): "Automatizarea_si_optimizarea_proceselor",
    }
     
}

# Mapare culori pentru clădiri (nivel 2)
city_color_maps = {
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
    },
    
    "Baze_de_date_si_regasire_de_informatii/Big_data_si_bd_distribuite":{
        (255, 247, 61) : "Big_data_si_bd_distribuite_scoala",
        (255, 143, 25) : "Big_data_si_bd_distribuite_biblioteca",
        (141, 0, 255) : "Big_data_si_bd_distribuite_monument",
        (61, 243, 62) : "Big_data_si_bd_distribuite_parc",
        (75, 75, 75) : "Big_data_si_bd_distribuite_laborator",
        (255, 57, 0) : "Big_data_si_bd_distribuite_spital",
        (255, 0, 170) : "Big_data_si_bd_distribuite_magazine",
    },
    
    "Baze_de_date_si_regasire_de_informatii/Recuperarea_si_integritatea_bazelor_de_date":{
        (255, 247, 61) : "Recuperarea_si_integritatea_bazelor_de_date_scoala",
        (255, 143, 25) : "Recuperarea_si_integritatea_bazelor_de_date_biblioteca",
        (141, 0, 255) : "Recuperarea_si_integritatea_bazelor_de_date_monument",
        (61, 243, 62) : "Recuperarea_si_integritatea_bazelor_de_date_parc",
        (255, 57, 0) : "Recuperarea_si_integritatea_bazelor_de_date_spital",
        (75, 75, 75) : "Recuperarea_si_integritatea_bazelor_de_date_fabrica",
        (255, 0, 170):"Recuperarea_si_integritatea_bazelor_de_date_magazine",
    },
    
    "Baze_de_date_si_regasire_de_informatii/Securitate_si_confidentialitate":{
        (255, 247, 61) : "Securitate_si_confidentialitate_scoala",
        (255, 143, 25) : "Securitate_si_confidentialitate_biblioteca",
        (141, 0, 255) : "Securitate_si_confidentialitate_monument",
        (61, 243, 62) : "Securitate_si_confidentialitate_parc",
        (255, 57, 0) : "Securitate_si_confidentialitate_politie",
        (75, 75, 75) : "Securitate_si_confidentialitate_fabrica",
        (255, 0, 170):"Securitate_si_confidentialitate_magazine",
    },
    
    "Baze_de_date_si_regasire_de_informatii/Depozitarea_datelor_si_analiza":{
       (255, 247, 61) : "Depozitarea_datelor_si_analiza_scoala",
        (255, 143, 25) : "Depozitarea_datelor_si_analiza_biblioteca",
        (141, 0, 255) : "Depozitarea_datelor_si_analiza_monument",
        (61, 243, 62) : "Depozitarea_datelor_si_analiza_parc",
        (255, 57, 0) : "Depozitarea_datelor_si_analiza_spital",
        (75, 75, 75) : "Depozitarea_datelor_si_analiza_fabrica",
        (255, 0, 170):"Depozitarea_datelor_si_analiza_magazine",
     
    },
    
    "Baze_de_date_si_regasire_de_informatii/Heterogenous_data_si_multimedia_interogation":{
       (255, 247, 61) : "Heterogenous_data_si_multimedia_interogation_scoala",
        (255, 143, 25) : "Heterogenous_data_si_multimedia_interogation_biblioteca",
        (141, 0, 255) : "Heterogenous_data_si_multimedia_interogation_monument",
        (61, 243, 62) : "Heterogenous_data_si_multimedia_interogation_parc",
        (255, 57, 0) : "Heterogenous_data_si_multimedia_interogation_politie",
        (75, 75, 75) : "Heterogenous_data_si_multimedia_interogation_fabrica",
        (255, 0, 170):"Heterogenous_data_si_multimedia_interogation_magazine",
     
    },
    
    "Baze_de_date_si_regasire_de_informatii/Reprezentari_avansate_ale_datelor_si_vm":{
       (255, 247, 61) : "Reprezentari_avansate_ale_datelor_si_vm_scoala",
        (255, 143, 25) : "Reprezentari_avansate_ale_datelor_si_vm_biblioteca",
        (141, 0, 255) : "Reprezentari_avansate_ale_datelor_si_vm_monument",
        (61, 243, 62) : "Reprezentari_avansate_ale_datelor_si_vm_parc",
        (255, 57, 0) : "Reprezentari_avansate_ale_datelor_si_vm_politie",
        (75, 75, 75) : "Reprezentari_avansate_ale_datelor_si_vm_laborator",
        (255, 0, 170):"Reprezentari_avansate_ale_datelor_si_vm_magazine",
     
    },
    
    "Limbaje_de_programare/Programare_imperativa":{
        (255, 247, 61) : "Programare_imperativa_scoala",
        (255, 143, 25) : "Programare_imperativa_biblioteca",
        (141, 0, 255) : "Programare_imperativa_monument",
        (61, 243, 62) : "Programare_imperativa_parc",
        (255, 57, 0) : "Programare_imperativa_spital",
        (75, 75, 75) : "Programare_imperativa_atelier",
        (255, 0, 170):"Programare_imperativa_magazine",
    },
    
    "Limbaje_de_programare/Programare_orientata_pe_obiect":{
        (255, 247, 61) : "Programare_orientata_pe_obiect_scoala",
        (255, 143, 25) : "Programare_orientata_pe_obiect_biblioteca",
        (141, 0, 255) : "Programare_orientata_pe_obiect_monument",
        (61, 243, 62) : "Programare_orientata_pe_obiect_parc",
        (255, 57, 0) : "Programare_orientata_pe_obiect_spital",
        (75, 75, 75) : "Programare_orientata_pe_obiect_ferma",
        (255, 0, 170):"Programare_orientata_pe_obiect_magazine",
    },
    
    "Limbaje_de_programare/Programare_functionala":{
        (255, 247, 61) : "Programare_functionala_scoala",
        (255, 143, 25) : "Programare_functionala_biblioteca",
        (141, 0, 255) : "Programare_functionala_monument",
        (61, 243, 62) : "Programare_functionala_parc",
        (255, 57, 0) : "Programare_functionala_politie",
        (75, 75, 75) : "Programare_functionala_ferma",
        (255, 0, 170):"Programare_functionala_magazine",
    },
    
    "Arhitectura_calculatoarelor/Arhitectura_securitatii_informatice":{
        (188, 26, 247): "Arhitectura_securitatii_mov",
        (247, 27, 177): "Arhitectura_securitatii_roz",
        (213, 28, 26): "Arhitectura_securitatii_rosu",
        (248, 129, 27): "Arhitectura_securitatii_portocaliu",
        (248, 238, 27): "Arhitectura_securitatii_galben",
        (27, 178, 247): "Arhitectura_securitatii_albastru", 
        (130, 207, 227): "Arhitectura_securitatii_mare", 
    },
    
    "Limbaje_de_programare/Programare_logica":{
        (255, 247, 61) : "Programare_logica_scoala",
        (255, 143, 25) : "Programare_logica_biblioteca",
        (141, 0, 255) : "Programare_logica_monument",
        (61, 243, 62) : "Programare_logica_parc",
        (255, 57, 0) : "Programare_logica_politie",
        (75, 75, 75) : "Programare_logica_ferma",
        (255, 0, 170):"Programare_logica_magazine",
    },
    
    "Limbaje_de_programare/Programare_declarativa":{
        (255, 247, 61) : "Programare_declarativa_scoala",
        (255, 143, 25) : "Programare_declarativa_biblioteca",
        (141, 0, 255) : "Programare_declarativa_monument",
        (75, 75, 75) : "Programare_declarativa_atelier",
        (255, 0, 170):"Programare_declarativa_magazine",
    },
    
    "Limbaje_de_programare/Programare_reactiva_si_event_based":{
        (255, 247, 61) : "Programare_reactiva_si_event_based_scoala",
        (255, 143, 25) : "Programare_reactiva_si_event_based_biblioteca",
        (141,0,255) : "Programare_reactiva_si_event_based_monument",
        (255, 57, 0) : "Programare_reactiva_si_event_based_politie",
        (75, 75, 75) : "Programare_reactiva_si_event_based_ferma",
        (255, 0, 170):"Programare_reactiva_si_event_based_magazine",
    },
    
    
    "Limbaje_de_programare/Metaprogramming":{
        (255, 247, 61) : "Metaprogramming_scoala",
        (255, 143, 25) : "Metaprogramming_biblioteca",
        (141,0,255) : "Metaprogramming_monument",
        (255, 57, 0) : "Metaprogramming_politie",
        (75, 75, 75) : "Metaprogramming_atelier",
        (255, 0, 170):"Metaprogramming_magazine",
        (61, 243, 62) : "Metaprogramming_parc",
    },
    
    "Limbaje_de_programare/Programare_concurenta_si_paralela":{
        (255, 247, 61) : "Programare_concurenta_si_paralela_scoala",
        (255, 143, 25) : "Programare_concurenta_si_paralela_biblioteca",
        (141,0,255) : "Programare_concurenta_si_paralela_monument",
        (255, 57, 0) : "Programare_concurenta_si_paralela_politie",
        (75, 75, 75) : "Programare_concurenta_si_paralela_atelier",
        (255, 0, 170):"Programare_concurenta_si_paralela_magazine",
        (61, 243, 62) : "Programare_concurenta_si_paralela_parc",
    },
    
    "ASD/Teoria_algoritmilor":{
        (255, 197, 19) : "Teoria_algoritmilor_turn",
        (148, 18, 254) : "Teoria_algoritmilor_biblioteca",
        (18, 137, 255) : "Teoria_algoritmilor_teatru",
        (18, 255, 207) : "Teoria_algoritmilor_spital",
        (151, 255, 18) : "Teoria_algoritmilor_verde",
        (255, 18, 184):"Teoria_algoritmilor_roz",
        (255, 76, 18) : "Teoria_algoritmilor_parc",
    },
    
    "ASD/Algoritmi_fundamentali":{
        (38, 243, 0) : "Algoritmi_fundamentali_turn",
        (0, 243, 241) : "Algoritmi_fundamentali_biblioteca",
        (241, 0, 255) : "Algoritmi_fundamentali_teatru",
        (0, 87, 255) : "Algoritmi_fundamentali_spital",
        (243, 140, 1) : "Algoritmi_fundamentali_portocaliu",
        #(255, 18, 184):"Algoritmi_fundamentali_roz",
    },
    
    "ASD/Structuri_de_date_clasice":{
        (21, 1, 248) : "Structuri_de_date_clasice_turn",
        (0, 236, 247) : "Structuri_de_date_clasice_biblioteca",
        (248, 215, 0) : "Structuri_de_date_clasice_teatru",
        (149, 71, 131) : "Structuri_de_date_clasice_spital",
        #(151, 255, 18) : "Teoria_algoritmilor_verde",
        (248, 64, 0):"Structuri_de_date_clasice_rosu",
        (248, 150, 0) : "Structuri_de_date_clasice_parc",
    },
    
    "ASD/Structuri_de_date_avansate":{
        (0, 236, 247) : "Structuri_de_date_avansate_turn",
        (248, 46, 0) : "Structuri_de_date_avansate_biblioteca",
        (69, 248, 0) : "Structuri_de_date_avansate_teatru",
        (248, 0, 234) : "Structuri_de_date_avansate_spital",
        (248, 150, 0) : "Structuri_de_date_avansate_castel",
        (246, 248, 0):"Structuri_de_date_avansate_galben",
        (149, 71, 131) : "Structuri_de_date_avansate_parc",
    },
    
    "ASD/Algoritmi_pe_grafuri":{
        (234, 3, 255) : "Algoritmi_pe_grafuri_turn",
        (0, 252, 43) : "Algoritmi_pe_grafuri_biblioteca",
        (255, 230, 3) : "Algoritmi_pe_grafuri_teatru",
        (254, 76, 2) : "Algoritmi_pe_grafuri_spital",
        (2, 11, 254) : "Algoritmi_pe_grafuri_castel",
        (108, 72, 134) : "Algoritmi_pe_grafuri_parc",
    },
    
    "ASD/Algoritmi_geometrici":{
        (0, 213, 255) : "Algoritmi_geometrici_turn",
        (255, 243, 0) : "Algoritmi_geometrici_biblioteca",
        (240, 0, 255) : "Algoritmi_geometrici_teatru",
        (255, 50, 0) : "Algoritmi_geometrici_spital",
        (1, 255, 0) : "Algoritmi_geometrici_castel",
        (0, 87, 255) : "Algoritmi_geometrici_albastru",
    },
    
    "ASD/Algoritmi_paraleli_si_distribuiti":{
        (242, 0, 0) : "Algoritmi_paraleli_si_distribuiti_turn",
        (241, 228, 0) : "Algoritmi_paraleli_si_distribuiti_biblioteca",
        (0, 218, 240) : "Algoritmi_paraleli_si_distribuiti_teatru",
        (46, 241, 1) : "Algoritmi_paraleli_si_distribuiti_spital",
        (233, 0, 241) : "Algoritmi_paraleli_si_distribuiti_castel",
        (241, 140, 0) : "Algoritmi_paraleli_si_distribuiti_portocaliu",
    },
    
    "ASD/Algoritmi_probabilistici_si_randomizati":{
        (0, 236, 247) : "Algoritmi_probabilistici_si_randomizati_turn",
        (69, 248, 0) : "Algoritmi_probabilistici_si_randomizati_biblioteca",
        (248, 150, 0) : "Algoritmi_probabilistici_si_randomizati_teatru",
        (246, 248, 0) : "Algoritmi_probabilistici_si_randomizati_spital",
        (248, 46, 0) : "Algoritmi_probabilistici_si_randomizati_castel",
        (149, 71, 131) : "Algoritmi_probabilistici_si_randomizati_albastru",
    },
    
    "Arhitectura_calculatoarelor/Arhitectura_hardware":{
        (69, 248, 0) : "Arhitectura_hardware_sfinx",
         (248, 0, 202) : "Arhitectura_hardware_roz",
        (248, 86, 1) : "Arhitectura_hardware_piramida",
        (134, 0, 247) : "Arhitectura_hardware_mov",
        (248, 220, 0) : "Arhitectura_hardware_galben",
        (0, 241, 248) : "Arhitectura_hardware_albastru",
    },
    
    "Arhitectura_calculatoarelor/Arhitectura_software":{
        (249, 0, 226) : "Arhitectura_software_roz",
         (248, 19, 0) : "Arhitectura_software_rosu",
        (248, 86, 1) : "Arhitectura_software_portocaliu",
        (248, 220, 0) : "Arhitectura_software_galben",
        (55, 0, 249) : "Arhitectura_software_albastru_inchis",
        (0, 241, 248) : "Arhitectura_software_albastru",
        (69, 248, 0) : "Arhitectura_software_verde",
    },
    
    "Arhitectura_calculatoarelor/Arhitectura_sistemelor_distribuite":{
       (228, 0, 248) : "Arhitectura_sistemelor_distribuite_mov",
        (248, 19, 0) : "Arhitectura_sistemelor_distribuite_rosu",
        (248, 86, 1) : "Arhitectura_sistemelor_distribuite_portocaliu",
        (248, 231, 1) : "Arhitectura_sistemelor_distribuite_sfinx",
        (55, 0, 249) : "Arhitectura_sistemelor_distribuite_albastru",
        (0, 245, 248) : "Arhitectura_sistemelor_distribuite_piramide",
        (23, 247, 0) : "Arhitectura_sistemelor_distribuite_verde",
    },
    
    "Arhitectura_calculatoarelor/Arhitectura_retelelor_si_comunicatiilo":{
       (179, 0, 249) : "Arhitectura_retelelor_si_comunicatiilor_mov",
        (248, 19, 0) : "Arhitectura_retelelor_si_comunicatiilor_rosu",
        (249, 0, 226) : "Arhitectura_retelelor_si_comunicatiilor_roz",
        (248, 231, 1) : "Arhitectura_retelelor_si_comunicatiilor_sfinx",
        (55, 0, 249) : "Arhitectura_retelelor_si_comunicatiilor_albastru",
        (23, 247, 0) : "Arhitectura_retelelor_si_comunicatiilor_piramida",
    },
    
    "Arhitectura_calculatoarelor/Arhitectura_bazei_de_date":{
       (247, 221, 0) : "Arhitectura_bazei_de_date_galben",
        (40, 249, 0) : "Arhitectura_bazei_de_date_verde",
        (225, 1, 248) : "Arhitectura_bazei_de_date_roz",
        (248, 29, 1) : "Arhitectura_bazei_de_date_sfinx",
        (0, 248, 247) : "Arhitectura_bazei_de_date_albastru",
        (248, 143, 0) : "Arhitectura_bazei_de_date_piramide",
        (0, 107, 249) : "Arhitectura_bazei_de_date_mare",
    }, 
    
    "Arhitectura_calculatoarelor/Arhitectura_cloud_si_devops":{
       (248, 220, 0) : "Arhitectura_cloud_si_devops_galben",
        (69, 248, 0) : "Arhitectura_cloud_si_devops_verde",
        (248, 0, 202) : "Arhitectura_cloud_si_devops_roz",
        (0, 241, 248) : "Arhitectura_cloud_si_devops_sfinx",
        (0, 107, 249) : "Arhitectura_cloud_si_devops_albastru",
        (248, 86, 1) : "Arhitectura_cloud_si_devops_piramide",
        (134, 0, 247) : "Arhitectura_cloud_si_devops_mov",
    }, 
    
    
    
    
    
    "AI_si_robotica/Invatare_automata_si_deeplearning":{
       (249, 25, 0) : "Invatare_automata_si_deeplearning_biblioteca",
        (0, 248, 248) : "Invatare_automata_si_deeplearning_scoala",
        (246, 0, 249) : "Invatare_automata_si_deeplearning_biserica",
        (249, 154, 0) : "Invatare_automata_si_deeplearning_spital",
        (108, 72, 134) : "Invatare_automata_si_deeplearning_parc",
        (204, 249, 0) : "Invatare_automata_si_deeplearning_galben",
    }, 
    
    "AI_si_robotica/Procesarea_limbajului_natural_si_viziune_computerizata":{
       (1, 249, 49) : "Procesarea_limbajului_natural_si_viziune_computerizata_biblioteca",
        (249, 28, 1) : "Procesarea_limbajului_natural_si_viziune_computerizata_scoala",
        (0, 16, 249) : "Procesarea_limbajului_natural_si_viziune_computerizata_biserica",
        (215, 1, 249) : "Procesarea_limbajului_natural_si_viziune_computerizata_spital",
        (204, 249, 0) : "Procesarea_limbajului_natural_si_viziune_computerizata_casa",
        (0, 207, 249) : "Procesarea_limbajului_natural_si_viziune_computerizata_public",
    }, 
    
    "AI_si_robotica/AI_explicabil_si_sisteme_multiagent":{
       (133, 249, 0) : "AI_explicabil_si_sisteme_multiagent_biblioteca",
        (246, 0, 249) : "AI_explicabil_si_sisteme_multiagent_scoala",
        (1, 53, 250) : "AI_explicabil_si_sisteme_multiagent_biserica",
        (249, 0, 0) : "AI_explicabil_si_sisteme_multiagent_spital",
        (248, 194, 0) : "AI_explicabil_si_sisteme_multiagent_casa",
        (0, 249, 245) : "AI_explicabil_si_sisteme_multiagent_public",
    },
    
    "AI_si_robotica/Roboti_autonomi_si_industriali":{
        (249, 28, 1) : "Roboti_autonomi_si_industriali_biblioteca",
        (0, 240, 249) : "Roboti_autonomi_si_industriali_scoala",
        (144, 249, 0) : "Roboti_autonomi_si_industriali_biserica",
        (255, 0, 228) : "Roboti_autonomi_si_industriali_spital",
        (250, 181, 0) : "Roboti_autonomi_si_industriali_social",
        (108, 72, 134) : "Roboti_autonomi_si_industriali_parc",
    },
    
    "AI_si_robotica/Roboti_umanoizi_si_colaborativi":{
        (255, 0, 228) : "Roboti_umanoizi_si_colaborativi_biblioteca",
        (0, 255, 39) : "Roboti_umanoizi_si_colaborativi_scoala",
        (255, 231, 0) : "Roboti_umanoizi_si_colaborativi_biserica",
        (0, 213, 255) : "Roboti_umanoizi_si_colaborativi_spital",
        (255, 76, 1) : "Roboti_umanoizi_si_colaborativi_social",
        (108, 72, 134) : "Roboti_umanoizi_si_colaborativi_parc",
    },
    
    "AI_si_robotica/Robotica_medicala_si_soft_robotics":{
       (247, 0, 255) : "Robotica_medicala_si_soft_robotics_biblioteca",
        (255, 75, 0) : "Robotica_medicala_si_soft_robotics_scoala",
        (0, 255, 39) : "Robotica_medicala_si_soft_robotics_biserica",
        (255, 233, 0) : "Robotica_medicala_si_soft_robotics_spital",
        (0, 230, 240) : "Robotica_medicala_si_soft_robotics_social",
        (108, 72, 134) : "Robotica_medicala_si_soft_robotics_parc",
    },
    
    "AI_si_robotica/Robotica_de_tip_roi":{
       (240, 0, 97) : "Robotica_de_tip_roi_biblioteca",
       (240, 93, 0) : "Robotica_de_tip_roi_social",
        (240, 208, 1) : "Robotica_de_tip_roi_biserica",
        (0, 240, 13) : "Robotica_de_tip_roi_spital",
        (0, 230, 240) : "Robotica_de_tip_roi_scoala",
        (108, 72, 134) : "Robotica_de_tip_roi_parc",
    },
     
    "AI_si_robotica/Robotica_cognitiva_si_sisteme_de_control_inteligente":{
       (0, 213, 255) : "Robotica_cognitiva_si_sisteme_de_control_inteligente_biblioteca",
       (240, 0, 1) : "Robotica_cognitiva_si_sisteme_de_control_inteligente_cladire",
        (255, 231, 0) : "Robotica_cognitiva_si_sisteme_de_control_inteligente_biserica",
        (0, 255, 39) : "Robotica_cognitiva_si_sisteme_de_control_inteligente_spital",
        (134, 72, 121) : "Robotica_cognitiva_si_sisteme_de_control_inteligente_scoala",
        (108, 72, 134) : "Robotica_cognitiva_si_sisteme_de_control_inteligente_parc",
    },
    
    "AI_si_robotica/Simulare_si_realitate_virtuala":{
       (255, 223, 0) : "Simulare_si_realitate_virtuala_biblioteca",
       (255, 75, 0) : "Simulare_si_realitate_virtuala_social",
       (244, 0, 254) : "Simulare_si_realitate_virtuala_biserica",
        (44, 255, 0) : "Simulare_si_realitate_virtuala_spital",
        (255, 154, 0) : "Simulare_si_realitate_virtuala_scoala",
        (108, 72, 134) : "Simulare_si_realitate_virtuala_parc",
    },
    
    "Grafica/2d":{
       (150, 167, 183) : "2d_biblioteca",
       (53, 109, 100) : "2d_magazin",
       (210, 186, 162) : "2d_catedrala",
        (175, 0, 5) : "2d_spital",
        (86, 90, 101) : "2d_scoala",
        (55, 255, 0) : "2d_parc",
    },
    
    "Grafica/3d":{
       (255, 233, 0) : "3d_biblioteca",
       (12, 1, 255) : "3d_magazin",
       (4, 255, 0) : "3d_catedrala",
        (0, 255, 239) : "3d_spital",
        (255, 0, 16) : "3d_scoala",
        (254, 0, 212) : "3d_alimentara",
    },
    
    "Grafica/AR":{
       (58, 133, 165) : "AR_biblioteca",
       (255, 0, 200) : "AR_magazin",
       (149, 71, 131) : "AR_catedrala",
        (255, 241, 48) : "AR_spital",
        (255, 71, 47) : "AR_scoala",
        (59, 0, 248) : "AR_muzeu",
    },
    
    "Grafica/VR":{
       (0, 236, 247) : "VR_teatru",
       (0, 248, 29) : "VR_magazine",
       (149, 71, 131) : "VR_catedrala",
        (249, 139, 0) : "VR_spital",
        (248, 46, 0) : "VR_scoala",
        (59, 0, 248) : "VR_muzeu",
    },
    
    "Grafica/Grafica_pentru_jocuri_video":{
       (58, 133, 165) : "Grafica_pentru_jocuri_video_biblioteca",
       (255, 0, 200) : "Grafica_pentru_jocuri_video_magazine",
       (149, 71, 131) : "Grafica_pentru_jocuri_video_catedrala",
        (255, 241, 48) : "Grafica_pentru_jocuri_video_spital",
        (255, 71, 47) : "Grafica_pentru_jocuri_video_scoala",
        (59, 0, 248) : "Grafica_pentru_jocuri_video_muzeu",
    },
    
    "Grafica/CGI":{
       (0, 236, 247) : "CGI_teatru",
       (0, 248, 29) : "CGI_catedrala",
       (149, 71, 131) : "CGI_magazine",
        (249, 139, 0) : "CGI_spital",
        (248, 46, 0) : "CGI_scoala",
        (59, 0, 248) : "CGI_muzeu",
    },
    
     "Grafica/Vizualizarea_datelor":{
       (0, 236, 247) : "Vizualizarea_datelor_parc",
       (0, 248, 29) : "Vizualizarea_datelor_biblioteca",
       (149, 71, 131) : "Vizualizarea_datelor_magazine",
        (249, 139, 0) : "Vizualizarea_datelor_muzeu",
        (248, 46, 0) : "Vizualizarea_datelor_scoala",
        (59, 0, 248) : "Vizualizarea_datelor_catedrala",
    },
    
    "Grafica/GUI":{
       (0, 236, 247) : "GUI_muzeu",
       (0, 248, 29) : "GUI_biblioteca",
       (149, 71, 131) : "GUI_magazine",
        (249, 139, 0) : "GUI_spital",
        (248, 46, 0) : "GUI_scoala",
        (59, 0, 248) : "GUI_catedrala",
    },
    
    "Interactiune_om_computer/UI_UX_design":{
       (255, 0, 198) : "UI_UX_design_muzeu",
       (255, 117, 0) : "UI_UX_design_biblioteca",
       (254, 5, 0) : "UI_UX_design_monument",
        (255, 229, 0) : "UI_UX_design_admin",
        (117, 0, 255) : "UI_UX_design_scoala",
        (0, 255, 1) : "UI_UX_design_parc",
    },
    
    "Interactiune_om_computer/Interactiunea_bazata_pe_ai":{
       (8, 178, 255) : "Interactiunea_bazata_pe_ai_muzeu",
       (255, 0, 198) : "Interactiunea_bazata_pe_ai_biblioteca",
       (117, 0, 255) : "Interactiunea_bazata_pe_ai_monument",
       (255, 117, 0) : "Interactiunea_bazata_pe_ai_admin",
        (0, 255, 1) : "Interactiunea_bazata_pe_ai_scoala",
        (108, 72, 134) : "Interactiunea_bazata_pe_ai_parc",
    },
    
    "Interactiune_om_computer/Interactiunea_in_medii_colaborative":{
       (1, 210, 251) : "Interactiunea_in_medii_colaborative_muzeu",
       (255, 0, 198): "Interactiunea_in_medii_colaborative_biblioteca",
       (253, 217, 0) : "Interactiunea_in_medii_colaborative_monument",
       (255, 30, 0) : "Interactiunea_in_medii_colaborative_admin",
         (97, 254, 0) : "Interactiunea_in_medii_colaborative_scoala",
        (108, 72, 134) : "Interactiunea_in_medii_colaborative_parc",
    },
    
    "Interactiune_om_computer/Factori_umani_si_psihologia_interactiunii":{
       (255, 0, 198) : "Factori_umani_si_psihologia_interactiunii_muzeu",
       (255, 117, 0) : "Factori_umani_si_psihologia_interactiunii_admin",
       (254, 5, 0) : "Factori_umani_si_psihologia_interactiunii_biblioteca",
        (255, 229, 0) : "Factori_umani_si_psihologia_interactiunii_scoala",
        (117, 0, 255) : "Factori_umani_si_psihologia_interactiunii_parc",
        (0, 255, 1) : "Factori_umani_si_psihologia_interactiunii_monument",
    },
    
    "Interactiune_om_computer/Interactiunea_in_contexte_specifice":{
       (8, 178, 255) : "Interactiunea_in_contexte_specifice_muzeu",
       (253, 217, 0) : "Interactiunea_in_contexte_specifice_biblioteca",
       (0, 255, 1) : "Interactiunea_in_contexte_specifice_monument",
        (255, 0, 198) : "Interactiunea_in_contexte_specifice_admin",
       (255, 117, 0) : "Interactiunea_in_contexte_specifice_scoala",
        (108, 72, 134) : "Interactiunea_in_contexte_specifice_parc",
    },
    
    "Interactiune_om_computer/Securitate_si_etica_in_HCI":{
       (252, 246, 0) : "Securitate_si_etica_in_HCI_muzeu",
       (245, 0, 241) : "Securitate_si_etica_in_HCI_biblioteca",
      (252, 148, 0) : "Securitate_si_etica_in_HCI_monument",
        (1, 210, 251) : "Securitate_si_etica_in_HCI_admin",
       (0, 251, 47) : "Securitate_si_etica_in_HCI_scoala",
        (81, 72, 135) : "Securitate_si_etica_in_HCI_parc",
    },
    
    
    "Bioinformatica/Analiza_secventelor_biologice":{
       (245, 0, 241) : "Analiza_secventelor_biologice_monument",
       (1, 210, 251) : "Analiza_secventelor_biologice_magazin",
        (0, 251, 47) : "Analiza_secventelor_biologice_spital",
        (252, 32, 0) : "Analiza_secventelor_biologice_admin",
        (252, 148, 0) : "Analiza_secventelor_biologice_fabrica",
        (149, 71, 131) : "Analiza_secventelor_biologice_parc",
    },
    
    "Bioinformatica/Genomica":{
       (0, 236, 247) : "Genomica_monument",
       (0, 248, 29) : "Genomica_magazin",
        (149, 71, 131) : "Genomica_teatru",
        (248, 64, 0) : "Genomica_admin",
        (21, 1, 248) : "Genomica_fabrica",
        (248, 150, 0) : "Genomica_parc",
    },
    
    "Bioinformatica/Proteomica":{
       (240, 0, 249) : "Proteomica_scoala",
       (75, 248, 0) : "Proteomica_magazin",
        (21, 1, 248) : "Proteomica_spital",
        (0, 245, 248) : "Proteomica_admin",
        (248, 167, 0) : "Proteomica_fabrica",
        (249, 20, 1) : "Proteomica_parc",
    },
    
    "Bioinformatica/Bioinformatica_structurala":{
       (246, 248, 0) : "Bioinformatica_structurala_teatru",
       (248, 150, 0) : "Bioinformatica_structurala_magazin",
        (248, 46, 0) : "Bioinformatica_structurala_scoala",
        (0, 236, 247) : "Bioinformatica_structurala_admin",
        (69, 248, 0) : "Bioinformatica_structurala_fabrica",
        (149, 71, 131) : "Bioinformatica_structurala_parc",
    },
    
    "Bioinformatica/Bioinformatica_evolutionista":{
       (252, 148, 0) : "Bioinformatica_evolutionista_scoala",
       (245, 0, 241) : "Bioinformatica_evolutionista_magazin",
        (252, 32, 0) : "Bioinformatica_evolutionista_spital",
        (0, 251, 47) : "Bioinformatica_evolutionista_admin",
        (252, 222, 0) : "Bioinformatica_evolutionista_fabrica",
        (0, 236, 247) : "Bioinformatica_evolutionista_parc",
    },
    
    "Bioinformatica/Bioinformatica_medicala":{
       (95, 0, 252) : "Bioinformatica_medicala_scoala",
       (252, 148, 0) : "Bioinformatica_medicala_magazin",
        (0, 236, 247) : "Bioinformatica_medicala_teatru",
        (248, 239, 0) : "Bioinformatica_medicala_admin",
        (0, 248, 29) : "Bioinformatica_medicala_fabrica",
        (149, 71, 131) : "Bioinformatica_medicala_parc",
    },
    
    
    "Bioinformatica/Bioinformatica_aplicata_in_farmacologie":{
       (252, 32, 0) : "Bioinformatica_aplicata_in_farmacologie_scoala",
       (245, 0, 241) : "Bioinformatica_aplicata_in_farmacologie_magazin",
        (1, 210, 251) : "Bioinformatica_aplicata_in_farmacologie_teatru",
        (0, 251, 47) : "Bioinformatica_aplicata_in_farmacologie_admin",
        (252, 148, 0) : "Bioinformatica_aplicata_in_farmacologie_fabrica",
        (149, 71, 131) : "Bioinformatica_aplicata_in_farmacologie_parc",
    },
    
    "Bioinformatica/Biotehnologie":{
       (248, 150, 0) : "Biotehnologie_scoala",
       (0, 5, 247) : "Biotehnologie_magazin",
        (0, 236, 247) : "Biotehnologie_teatru",
        (248, 46, 0) : "Biotehnologie_admin",
        (0, 248, 29) : "Biotehnologie_fabrica",
        (149, 71, 131) : "Biotehnologie_parc",
    },
    
    "Bioinformatica/Bioinformatica_sistemelor":{
       (248, 46, 0) : "Bioinformatica_sistemelor_teatru",
       (69, 248, 0) : "Bioinformatica_sistemelor_magazin",
        (0, 236, 247) : "Bioinformatica_sistemelor_scoala",
        (248, 150, 0) : "Bioinformatica_sistemelor_admin",
        (246, 248, 0) : "Bioinformatica_sistemelor_fabrica",
        (149, 71, 131) : "Bioinformatica_sistemelor_parc",
    },
    
    "Sisteme_de_operare_si_retele/Teoria_planificarii_proceselor":{
       (0, 252, 255) : "Teoria_planificarii_proceselor_biblioteca",
       (151, 0, 253) : "Teoria_planificarii_proceselor_magazin",
        (45, 255, 0) : "Teoria_planificarii_proceselor_scoala",
        (253, 11, 0) : "Teoria_planificarii_proceselor_catedrala",
        (254, 177, 1) : "Teoria_planificarii_proceselor_spital",
    },
    
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
        
        # Butonul de ajutor (Help), mereu vizibil
        self.help_button = ctk.CTkButton(
            self.root,
            text="Help",
            command=self.show_help_popup,
            fg_color="light blue",
            hover_color="white",
            text_color="black",
            border_width=0,
            corner_radius=0
        )
        self.help_button.place(x=20, y=120)

        self.root.bind("<Escape>", lambda e: self.root.quit())
        self.canvas.bind("<Button-1>", self.on_click)

        # Debounce pentru redimensionare
        self.resize_id = None
        self.canvas.bind("<Configure>", self.debounced_update_image)

        # Încarcă harta de start (presupunem "map.jpg" cu overlay "map_cc.jpg")
        if not self.load_map(BASE_PATH, "map.jpg", "map_cc.jpg"):
            print("[EROARE] Harta de start nu a putut fi încărcată.")
        self.update_navigation_buttons()
        
        # Afișează tutorialul la pornire
        self.root.after(500, self.show_help_popup)  # 500ms întârziere pentru a evita probleme la inițializare
        
        self.root.mainloop()

    def show_help_popup(self):
        """Afișează un popup cu tutorialul de utilizare."""
        help_window = ctk.CTkToplevel(self.root, fg_color="white")
        help_window.title("Tutorial de utilizare")
        # Setează dimensiunea popup‑ului
        popup_width = 600
        popup_height = 500
        # Calculează poziția în funcție de dimensiunea ecranului
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - popup_width) // 2
        y = (screen_height - popup_height) // 2

        help_window.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
        help_window.attributes("-topmost", True)  # Fereastra apare în față

        # Textul tutorialului
        tutorial_text = (
            "\t \t MAP EXPLORER\n\n"
            "Bun venit la MAP EXPLORER! Aceasta aplictaie este o reprezentare vizuala a informaticii, asa cum au vazut-o membrii echipei de dezvoltare a acestei aplicatii.\n"
            "\nAveti in vedere faptul ca scopul acestei aplicatii este unl strict educativ.\n\n"
            " Cum să folosești aplicația Map Explorer\n\n"
            "1️ Navigare pe hartă:\n   - Click pe o țară pentru a intra.\n   - Click pe o regiune pentru detalii.\n   - Click pe o clădire pentru zoom.\n\n"
            "2️ Butoane disponibile:\n   - `Back` → Revine la nivelul anterior.\n   - `Home` → Te întoarce la harta principală.\n   - `Exit` → Închide aplicația.\n   - `Help` → Afișează acest tutorial.\n\n"
            "3️ Detecția culorilor:\n   - Apasă pe hartă pentru a explora locațiile disponibile.\n   - Harta folosește culori pentru identificarea zonelor.\n\n"
            "✨ Distracție plăcută!"
        )

        # Etichetă pentru tutorial
        tutorial_label = ctk.CTkLabel(
            help_window, text=tutorial_text, text_color="black", justify="left", wraplength=500
        )
        tutorial_label.pack(pady=20, padx=20)

        # Buton pentru închiderea tutorialului
        close_button = ctk.CTkButton(
            help_window,
            text="Close",
            command=help_window.destroy,
            fg_color="red",
            hover_color="pink",
            text_color="black",
            corner_radius=0
        )
        close_button.pack(pady=10)
        
        
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
                    if selected_country.startswith("http"):
                        print(f"[INFO] Deschidere link: {selected_country}")
                        webbrowser.open(selected_country)
                    else:
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
