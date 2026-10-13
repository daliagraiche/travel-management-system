from model import VoyageModel
from view import VoyageView
from tkinter import messagebox

class VoyageController:
    def __init__(self):             #constructeur
        self.model = VoyageModel()
        self.view = VoyageView(self)
        self.model.creer_table_consultations()
        self.afficher_voyages()

    def ajouter_voyage(self, Destination, date_depart, date_retour, prix, places_disponibles, Descriptions):
        try:
            self.model.ajouter_voyage(Destination, date_depart, date_retour, prix, places_disponibles, Descriptions)
            self.view.Destination_var.set("")
            self.view.date_depart_var.set("")
            self.view.date_retour_var.set("")
            self.view.prix_var.set("")
            self.view.places_disponibles_var.set("")
            self.view.Descriptions_var.set("")
            messagebox.showinfo("Succès", "Voyage ajouté avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

    def afficher_voyages(self):
        return self.model.lire_voyages()
     
    def rechercher_voyage(self, Destination):
        try:
            voyages= self.model.rechercher_voyage(Destination)
            if not voyages:
                messagebox.showinfo("Information", "Aucun voyage trouvé pour cette destination.")
                self.view.rechercher_vss.destroy
            return voyages
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue lors de la recherche : {e}")
            return []
        

    def run(self):
        self.view.start()
