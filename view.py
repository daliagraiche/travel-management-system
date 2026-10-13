import tkinter as tk
from tkinter import messagebox, ttk  
from PIL import Image, ImageTk #pour faire defiler les image 

class VoyageView: 
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk() #fenetre principale
        self.root.title("Gestion des Voyages")

        # Variables pour les champs
        self.Destination_var = tk.StringVar()
        self.date_depart_var=tk.StringVar()
        self.date_retour_var=tk.StringVar()
        self.prix_var=tk.DoubleVar()
        self.places_disponibles_var=tk.IntVar()
        self.Descriptions_var = tk.StringVar()

        # UI: Interface Utilisateur
        self.setup_ui()

    def validate_numeric_input(self,input_text):
        """Valide que la saisie est un nombre (entier ou décimal)."""
        if input_text.replace(".", "", 1).isdigit() or input_text == "":  # Permet les nombres décimaux
            return True
        else:
            messagebox.showwarning("Erreur", "Veuillez saisir un nombre valide.")
            return False

    def setup_ui(self):

        #Menu
        menu=tk.Menu(self.root)
        self.root.config(menu=menu)

        #Menu cascade
        voyages_menu=tk.Menu(menu,tearoff=0)    #menu fixe 
        voyages_menu.add_command(label="Ajouter Voyage",accelerator="CTRL+A",font=("Arial",10),command=self.ajouter_voyage)
        voyages_menu.add_separator()
        voyages_menu.add_command(label="Rechercher Voyage 🔎",accelerator="CTRL+R",font=("Arial",10),command=self.rechercher_voyage)
        voyages_menu.add_separator()
        voyages_menu.add_command(label="Afficher Voyages",accelerator="CTRL+F",font=("Arial",10),command=self.afficher_voyages)
        voyages_menu.add_separator()
        voyages_menu.add_command(label="Quitter",font=("Arial",10),accelerator="CTRL+Q",background="red",command=self.quit)
        menu.add_cascade(label="         Menu     ",underline=0,accelerator="CTRL+M",menu=voyages_menu)

        vide_menu1=tk.Menu(menu,tearoff=0)
        menu.add_command(label="                                             ")

        ajouter_menu=tk.Menu(menu,tearoff=0)
        menu.add_command(label="     Ajouter Voyage     ",command=self.ajouter_voyage)

        vide_menu1=tk.Menu(menu,tearoff=0)
        menu.add_command(label="                                             ")

        afficher_menu=tk.Menu(menu,tearoff=0)
        menu.add_command(label="     Afficher Voyages     ",command=self.afficher_voyages,font=("Arial",14))

        vide_menu1=tk.Menu(menu,tearoff=0)
        menu.add_command(label="                                             ")

        rechercher_menu=tk.Menu(menu,tearoff=0)
        menu.add_command(label="     Rechercher Voyage 🔎     ",command=self.rechercher_voyage,font=("Arial",14))

        vide_menu1=tk.Menu(menu,tearoff=0)
        menu.add_command(label="                                             ")

        aide_menu=tk.Menu(menu,tearoff=0)
        menu.add_cascade(label="     Aide ?     ",menu=aide_menu)
        aide_menu.add_command(label="À propos", command=self.afficher_a_propos,font=("Arial",10),accelerator="CTRL+D")

        #Frame Principale
        self.main_frame=tk.Frame(self.root)   #conteneur pour les photos
        self.main_frame.pack(fill=tk.BOTH, expand=True)     #il va occuper tour l'espace disponible

        #zone pour les photos
        self.image_canvas=tk.Canvas(self.main_frame, width=1200, height=600)
        self.image_canvas.grid(row=0, column=0, padx=40, pady=10)

        self.images = []
        self.index_image_courrente =0 
        self.load_images()
        self.display_image()
        self.image_canvas.after(2000, self.next_image)

       # Ajout d'un conteneur transparent sur le Canvas
        frame = ttk.Frame(self.root, padding=20)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Titre
        title_label = ttk.Label(frame, text="Bienvenue dans le système de gestion de voyages", font=("Arial", 18))
        title_label.pack(pady=10)

        # Boutons principaux
        btn_ajout = ttk.Button(frame, text="Ajouter un Voyage", command=self.ajouter_voyage)
        btn_ajout.pack(pady=5)

        btn_affich = ttk.Button(frame, text="Afficher les Voyages", command=self.afficher_voyages)
        btn_affich.pack(pady=5)

        btn_rech = ttk.Button(frame, text="Rechercher un Voyage", command=self.rechercher_voyage)
        btn_rech.pack(pady=5)

        # Footer
        footer_label = ttk.Label(self.root, text="Agence de Voyage - Gestion v1.0", font=("Arial", 10))
        footer_label.place(relx=0.5, rely=0.95, anchor="center")

    def quit(self):
        confirm = messagebox.askokcancel("Confirmer", "Voulez-vous vraiment quitter l'application ?")
        if confirm:  # Si l'utilisateur confirme
            self.root.destroy()

    def load_images(self):
        try:
            image_paths=["./1.jpeg","./2.jpeg","./3.webp","./4.webp","./5.webp"]
            for path in image_paths:
                image = Image.open(path)
                image=image.resize((1200,600),Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                self.images.append(photo)
        except Exception as e:
            print(f"Erreur de chargement des images : {e}")

    def display_image(self):
        if self.images:
            self.image_canvas.create_image(0,0, anchor=tk.NW, image=self.images[self.index_image_courrente])

    def next_image(self):
        if not self.images: #verifie si la liste des images est vide
            print("Aucune image a afficher.")
            return 
        
        self.index_image_courrente = (self.index_image_courrente + 1) % len(self.images)
        self.display_image()
        self.image_canvas.after(2000, self.next_image)

        

    def afficher_a_propos(self):
        messagebox.showinfo("À propos", "Application de gestion des voyages \n Version 1.0")

   
    def ajouter_voyage(self):
        global date_e1
        global date_e2

        self.ajouter_v=tk.Toplevel(self.root)
        self.ajouter_v.title("Ajouter Voyage")
        self.ajouter_v.geometry("700x400")

        ttk.Label(self.ajouter_v, text="Ajouter un Nouveau Voyage", font=("Arial", 14)).pack(pady=10)

        ajouter_f1=tk.Frame(self.ajouter_v,height=200,width=400)
        ajouter_f1.pack(padx=10,pady=10)

        ajouter_f2=tk.Frame(self.ajouter_v,height=100,width=100)
        ajouter_f2.pack(padx=10,pady=10)

        # Fonction de validation
        vcmd = (self.root.register(self.validate_numeric_input), '%P')  # '%P' représente le texte après modification

        #formulaire d'ajout
        label1=tk.Label(ajouter_f1, text="Destination : ",font=("Arial",12),fg="black")
        label1.grid(row=0, column=0, padx=5, pady=5,sticky="w")
        label2=tk.Label(ajouter_f1, text="Champ Obligatoire* ",font=("Arial",8),fg="red")
        label2.grid(row=0, column=2, padx=5, pady=5)
        tk.Entry(ajouter_f1, textvariable=self.Destination_var).grid(row=0,column=1,padx=10,pady=5)
        
        label3=tk.Label(ajouter_f1, text="Date de depart :",font=("Arial",12),fg="black")
        label3.grid(row=1, column=0, padx=5, pady=5,sticky="w")
        date_e1=tk.Entry(ajouter_f1,width=20,textvariable=self.date_depart_var)
        date_e1.bind("<KeyRelease>", self.valider_saisie_date)    
        date_e1.grid(row=1,column=1,padx=5,pady=5)
        label4=tk.Label(ajouter_f1, text="Champ Obligatoire* ",font=("Arial",8),fg="red")
        label4.grid(row=1, column=2, padx=5, pady=5)
        labelf=tk.Label(ajouter_f1, text="format(aaaa-mm-jj) ",font=("Arial",8),fg="red")
        labelf.grid(row=1, column=3, padx=5, pady=5)
        
        label5=tk.Label(ajouter_f1, text="Date de retour :",font=("Arial",12),fg="black")
        label5.grid(row=2, column=0, padx=5, pady=5,sticky="w")
        date_e2=tk.Entry(ajouter_f1,width=20,textvariable=self.date_retour_var)
        date_e2.bind("<KeyRelease>", self.valider_saisie_dater)    
        date_e2.grid(row=2,column=1,padx=5,pady=5)
        label6=tk.Label(ajouter_f1, text="Champ Obligatoire* ",font=("Arial",8),fg="red")
        label6.grid(row=2, column=2, padx=5, pady=5)
        labelff=tk.Label(ajouter_f1,text="format(aaaa-mm-jj) ",font=("Arial",8),fg="red")
        labelff.grid(row=2, column=3, padx=5, pady=5)
        
        label7=tk.Label(ajouter_f1, text="Prix : ", font=("Arial",12),fg="black")
        label7.grid(row=3, column=0, padx=5, pady=5,sticky="w")
        label8=tk.Label(ajouter_f1, text="Champ Obligatoire* ", font=("Arial",8), fg="red")
        label8.grid(row=3, column=2, padx=5, pady=5)
        tk.Entry(ajouter_f1, textvariable=self.prix_var, validate="key",validatecommand=vcmd).grid(row=3, column=1, padx=10, pady=5)

        label9=tk.Label(ajouter_f1, text="Places Disponibles : ", font=("Arial",12),fg="black")
        label9.grid(row=4, column=0, padx=5, pady=5,sticky="w")
        label10=tk.Label(ajouter_f1, text="Champ Obligatoire * ", font=("Arial",8), fg="red")
        label10.grid(row=4, column=2, padx=5, pady=5)
        tk.Entry(ajouter_f1, textvariable=self.places_disponibles_var,validate="key",validatecommand=vcmd).grid(row=4, column=1, padx=10, pady=5)

        label11=tk.Label(ajouter_f1, text="Description : ", font=("Arial",12),fg="black")
        label11.grid(row=5, column=0, padx=5, pady=5,sticky="w")
        tk.Entry(ajouter_f1,textvariable=self.Descriptions_var).grid(row=5,column=1,padx=10,pady=5)

        ajouter_b1=tk.Button(ajouter_f2,text="Ajouter", bg="light green",command=self.confirmer)
        ajouter_b1.pack(side="left")
        ajouter_b2=tk.Button(ajouter_f2,text="Annuler",bg="light blue",command=self.quitter_v)
        ajouter_b2.pack(padx=20,side="left")

    def valider_saisie_date(self, event):
        """Valide la saisie de la date et la formate en 'aaaa-mm-jj' avec contrôle de validité des valeurs"""
        date_str = self.date_depart_var.get()

        if len(date_str) == 4 or len(date_str) == 7:
            if len(date_str) == 4:
                self.date_depart_var.set(date_str + '-')
            elif len(date_str) == 7:
                self.date_depart_var.set(date_str + '-')
            date_e1.icursor(len(date_str) + 1)  # Déplacer le curseur après "-"
        elif len(date_str) > 10:
            # Si l'utilisateur dépasse 10 caractères, supprimer la dernière saisie
            self.date_depart_var.set(date_str[:10])
        
        # Vérification de la validité de la date
        if len(date_str) == 10:  # Si la date a 10 caractères (format complet)
            try:
                aaaa,mm,jj = map(int, date_str.split('-'))
                # Vérification de l'année
                if aaaa < 2025:  # Année minimum 2025
                    self.date_depart_var.set(date_str[:0])
                    messagebox.showwarning("Erreur", "L'année doit être  Superieure ou egale à 2025.")
                    return
                if mm < 1 or mm > 12:  # Mois invalide
                    self.date_depart_var.set(date_str[:4]+'-')  # Revenir à un format valide partiellement
                    messagebox.showwarning("Erreur", "Le mois doit être compris entre 1 et 12.")
                    return
                if jj < 1 or jj > 31:  # Jour invalide
                    self.date_depart_var.set(date_str[:7] + '-')
                    messagebox.showwarning("Erreur", "Le jour doit être compris entre 1 et 31.")
                    return

                # Vérifier la validité des jours en fonction du mois
                if mm == 2:  # Mois de février
                    if not (1 <= jj <= 29):  # 29 jours maximum
                        self.date_depart_var.set(date_str[:7]+'-')
                        messagebox.showwarning("Erreur", "Le jour ne doit pas dépasser 29 pour février.")
                        return
                elif mm in [4, 6, 9, 11]:  # Mois avec 30 jours
                    if not (1 <= jj <= 30):  # 30 jours maximum
                        self.date_depart_var.set(date_str[:7]+'-')
                        messagebox.showwarning("Erreur", "Le jour ne doit pas dépasser 30 pour ce mois.")
                        return
                elif mm not in [2, 4, 6, 9, 11] and not (1 <= jj <= 31):  # Mois avec 31 jours
                    self.date_depart_var.set(date_str[:7]+'-')
                    messagebox.showwarning("Erreur", "Le jour ne doit pas dépasser 31 pour ce mois")
                    return

            except ValueError:
                messagebox.showwarning("Erreur", "La date n'est pas valide. Vérifiez le format.")
                self.date_depart_var.set(date_str[:5])  # Retour au format de base
                return
            
    def valider_saisie_dater(self, event):
        """Valide la saisie de la date et la formate en 'aaaa-mm-jj' avec contrôle de validité des valeurs"""
        date_str = self.date_retour_var.get()

        if len(date_str) == 4 or len(date_str) == 7:
            if len(date_str) == 4:
                self.date_retour_var.set(date_str + '-')
            elif len(date_str) == 7:
                self.date_retour_var.set(date_str + '-')
            date_e2.icursor(len(date_str) + 1) 
        elif len(date_str) > 10:
            # Si l'utilisateur dépasse 10 caractères, supprimer la dernière saisie
            self.date_retour_var.set(date_str[:10])
        
        # Vérification de la validité de la date
        if len(date_str) == 10:  # Si la date a 10 caractères (format complet)
            try:
                aaaa,mm,jj = map(int, date_str.split('-'))
                # Vérification de l'année
                if aaaa < 2025:  # Année minimum 2025
                    self.date_retour_var.set(date_str[:0])
                    messagebox.showwarning("Erreur", "L'année doit être  Superieure ou egale à 2025.")
                    return
                if mm < 1 or mm > 12:  # Mois invalide
                    self.date_retour_var.set(date_str[:4]+'-')  # Revenir à un format valide partiellement
                    messagebox.showwarning("Erreur", "Le mois doit être compris entre 1 et 12.")
                    return
                if jj < 1 or jj > 31:  # Jour invalide
                    self.date_retour_var.set(date_str[:7] + '-')
                    messagebox.showwarning("Erreur", "Le jour doit être compris entre 1 et 31.")
                    return

                # Vérifier la validité des jours en fonction du mois
                if mm == 2:  # Mois de février
                    if not (1 <= jj <= 29):  # 29 jours maximum
                        self.date_retour_var.set(date_str[:7]+'-')
                        messagebox.showwarning("Erreur", "Le jour ne doit pas dépasser 29 pour février.")
                        return
                elif mm in [4, 6, 9, 11]:  # Mois avec 30 jours
                    if not (1 <= jj <= 30):  # 30 jours maximum
                        self.date_retour_var.set(date_str[:7]+'-')
                        messagebox.showwarning("Erreur", "Le jour ne doit pas dépasser 30 pour ce mois.")
                        return
                elif mm not in [2, 4, 6, 9, 11] and not (1 <= jj <= 31):  # Mois avec 31 jours
                    self.date_retour_var.set(date_str[:7]+'-')
                    messagebox.showwarning("Erreur", "Le jour ne doit pas dépasser 31 pour ce mois")
                    return

            except ValueError:
                messagebox.showwarning("Erreur", "La date n'est pas valide. Vérifiez le format.")
                self.date_retour_var.set(date_str[:5])  # Retour au format de base
                return

    def confirmer(self):

        Destination = self.Destination_var.get()
        date_depart = self.date_depart_var.get()
        date_retour = self.date_retour_var.get()
        prix = self.prix_var.get()
        places_disponibles = self.places_disponibles_var.get()
        Descriptions = self.Descriptions_var.get()

        #verifier que les champs ne sont pas vide
        if not Destination or not date_depart or not date_retour or not prix or not places_disponibles:
            messagebox.showwarning("Erreur", "Tous les champs sauf la Description sont obligatoires.")
            return
 
        # Validation du prix
        try:
            prix = float(prix)  # Convertir en float
            if prix < 0:
                messagebox.showwarning("Erreur", "Le prix doit être un nombre positif.")
                return  # Arrêter l'exécution si le prix est invalide
        except ValueError:
            messagebox.showwarning("Erreur", "Le prix doit être un nombre.")
            return  # Arrêter l'exécution si le prix n'est pas valide

        # Validation des places disponibles
        try:
            places_disponibles = int(places_disponibles)  # Convertir en int
            if places_disponibles <= 0:
                messagebox.showwarning("Erreur", "Le nombre de places disponibles doit être un nombre positif.")
                return  # Arrêter l'exécution si le nombre de places est invalide
        except ValueError:
            messagebox.showwarning("Erreur", "Le nombre de places disponibles doit être un nombre.")
            return  # Arrêter l'exécution si le nombre de places n'est pas valide
            
        
        # Si tout est valide, demander une confirmation avant d'ajouter le voyage
        confirm = messagebox.askokcancel("Confirmer", "Voulez-vous ajouter ce voyage ?")
        if confirm:  # Si l'utilisateur confirme
            self.controller.ajouter_voyage(Destination, date_depart, date_retour, prix, places_disponibles, Descriptions)

    def quitter_v(self):
        self.ajouter_v.destroy()

    def rechercher_voyage(self):

        self.rechercher_v=tk.Toplevel(self.root)
        self.rechercher_v.title("Rechercher Voyage")
        self.rechercher_v.geometry("400x100")

        # Frame pour la barre de recherche
        search_frame = tk.Frame(self.rechercher_v)
        search_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Champ de texte pour la recherche
        self.search_var = tk.StringVar()

        search_entry = tk.Entry(search_frame, textvariable=self.search_var, font=("Arial", 10), width=30, bd=1, relief="solid")
        search_entry.grid(row=1, column=0, padx=10, pady=10)
        
        search_button = tk.Button(search_frame, text="Rechercher",bg="yellow", compound="left", command=self.rechercher_vs)
        search_button.grid(row=1, column=1, padx=10, pady=10)

    def rechercher_vs(self):
        self.rechercher_vss=tk.Toplevel(self.root)
        self.rechercher_vss.title("Resultats Recherche")
        self.rechercher_vss.geometry("460x500")

        # Création d'un Frame pour contenir le Canvas et les Scrollbars
        frame = tk.Frame(self.rechercher_vss)
        frame.pack(fill="both", expand=True)

        # Création du Canvas
        canvas = tk.Canvas(frame, bg="light gray")
        canvas.pack(side="left", fill="both", expand=True)

        # Création de la Scrollbar verticale
        vsb = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        vsb.pack(side="right", fill="y")

        # Connecter les Scrollbars au Canvas
        canvas.configure(yscrollcommand=vsb.set)

        # Créer un Frame à l'intérieur du Canvas (pour contenir le contenu scrollable)
        scrollable_frame = tk.Frame(canvas)

        # Ajouter le Frame à l'intérieur du Canvas avec create_window
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        voyages=self.controller.rechercher_voyage(self.search_var.get())
        for idx, voyage in enumerate(voyages):

            # Afficher la destination et le prix
            label = tk.Label(scrollable_frame, text=f"Destination: {voyage[1]}             -            Prix: {voyage[4]} DA \nDate depart: {voyage[2]}     -     Date retour: {voyage[3]}",font=("Arial",10),fg="black")
            label.grid(row=idx, column=0, sticky="w",padx=10,pady=10)

            # Bouton "Voir plus"
            voir_plus_button = tk.Button(scrollable_frame, text="Voir plus",bg="yellow", command=lambda v=voyage: self.afficher_details(v),fg="black")
            voir_plus_button.grid(row=idx, column=1,padx=10,pady=10)
        
       # Mettre à jour la zone de défilement lorsque le contenu change
        def update_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        # Lier l'événement de redimensionnement pour mettre à jour la zone de défilement
        canvas.bind("<Configure>", update_scroll_region)

    def afficher_details(self,voyage):

        self.afficher_v=tk.Toplevel(self.root)
        self.afficher_v.title("Afficher Voyage")
        self.afficher_v.geometry("300x400")

        # Frame pour les détails
        details_frame = tk.Frame(self.afficher_v, padx=20, pady=20)
        details_frame.pack(fill=tk.BOTH, expand=True)

        # Labels et champs pour afficher les détails
        labels = ["ID", "Destination", "Date de départ", "Date de retour", "Prix", "Places Disponibles", "Description"]
        for i, label in enumerate(labels):
            tk.Label(details_frame, text=f"{label}:", font=("Arial", 12, "bold")).grid(row=i, column=0, sticky="w", pady=5)
            tk.Label(details_frame, text=voyage[i], font=("Arial", 12)).grid(row=i, column=1, sticky="w", pady=5)

        # Bouton pour fermer la fenêtre
        tk.Button(details_frame, text="Fermer", bg="light blue", command=self.afficher_v.destroy).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def afficher_voyages(self):

        voyages = self.controller.afficher_voyages()

        afficher_vs=tk.Toplevel(self.root)
        afficher_vs.title("Afficher Voyages")
        afficher_vs.geometry("1400x500")

        ttk.Label(afficher_vs, text="Liste Des Voyages", font=("Arial", 14)).pack(pady=10)

        afficher_vs_f1=tk.Frame(afficher_vs,height=400,width=1000)
        afficher_vs_f1.pack(fill="both", expand=True, padx=10, pady=10)

        # Création d'une Scrollbar verticale
        scrollbar = tk.Scrollbar(afficher_vs_f1, orient="vertical")

        afficher_vs_f2=tk.Frame(afficher_vs,height=100,width=100)
        afficher_vs_f2.pack(padx=10,pady=10)

        # Table pour afficher les destinations
        columns = ("ID", "Destination","Date de depart","Date de retour", "Prix", "Places Disponibles","Description")
        tree = ttk.Treeview(afficher_vs_f1, columns=columns, show="headings", yscrollcommand=scrollbar.set)

        # Entêtes des colonnes
        tree.heading("ID", text="ID")
        tree.column("ID",width=60)
        tree.heading("Destination", text="Destination")
        tree.column("Destination",width=200)
        tree.heading("Date de depart", text="Date de depart")
        tree.column("Date de depart",width=200)
        tree.heading("Date de retour",text="Date de retour")
        tree.column("Date de retour",width=200)
        tree.heading("Prix", text="Prix (DA)")
        tree.column("Prix",width=100)
        tree.heading("Places Disponibles",text="Places Disponibles")
        tree.column("Places Disponibles",width=150)
        tree.heading("Description",text="Description")
        tree.column("Description",width=300)

        voyages = self.controller.afficher_voyages()
        
        for voy in voyages:
            tree.insert("", tk.END, values=voy)

        tree.pack(side="left",fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Connecter la scrollbar au Treeview
        scrollbar.config(command=tree.yview)

        btn_annul = tk.Button(afficher_vs, text="Annuler",bg="light blue", command=afficher_vs.destroy)
        btn_annul.pack(pady=5)


    def start(self):
        """try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1) 
        except (ImportError, AttributeError):  # Ajout de AttributeError pour gérer les cas où SetProcessDpiAwareness n'existe pas
            pass"""

        self.root.mainloop()

