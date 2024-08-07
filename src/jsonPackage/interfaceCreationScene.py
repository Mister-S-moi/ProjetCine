import tkinter as tk
from tkinter import ttk
import json
import os

class SceneFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulaire de Scène")

        self.scenes = []
        self.file_name = ""
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.show_start_options()

    def show_start_options(self):
        self.clear_frame(self.main_frame)
        tk.Label(self.main_frame, text="Nom du film:").grid(row=0, column=0, sticky=tk.W)
        self.movie_name_entry = tk.Entry(self.main_frame)
        self.movie_name_entry.grid(row=0, column=1, sticky=tk.W)

        new_button = tk.Button(self.main_frame, text="Nouveau Film", command=self.new_movie)
        new_button.grid(row=1, column=0, sticky=tk.W)

        load_button = tk.Button(self.main_frame, text="Reprendre Film", command=self.load_movie)
        load_button.grid(row=1, column=1, sticky=tk.W)

    def new_movie(self):
        self.file_name = self.movie_name_entry.get() + ".json"
        self.show_scene_form()

    def load_movie(self):
        self.file_name = self.movie_name_entry.get() + ".json"
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                self.scenes = data.get("scenes", [])
            self.show_scene_form()
        else:
            tk.messagebox.showerror("Erreur", "Fichier non trouvé!")

    def show_scene_form(self):
        self.clear_frame(self.main_frame)

        self.canvas = tk.Canvas(self.main_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))

        self.content_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.content_frame, anchor='nw')

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.content_frame, text="ID Scene").grid(row=0, column=0, sticky=tk.W)
        self.id_scene_entry = tk.Entry(self.content_frame)
        self.id_scene_entry.grid(row=0, column=1, sticky=tk.W)

        tk.Label(self.content_frame, text="Lieu").grid(row=1, column=0, sticky=tk.W)
        self.lieu_entry = tk.Entry(self.content_frame)
        self.lieu_entry.grid(row=1, column=1, sticky=tk.W)

        tk.Label(self.content_frame, text="Intérieur/Extérieur").grid(row=2, column=0, sticky=tk.W)
        self.int_ext_entry = tk.Entry(self.content_frame)
        self.int_ext_entry.grid(row=2, column=1, sticky=tk.W)

        tk.Label(self.content_frame, text="URL Texte").grid(row=3, column=0, sticky=tk.W)
        self.url_texte_entry = tk.Entry(self.content_frame)
        self.url_texte_entry.grid(row=3, column=1, sticky=tk.W)

        # Section pour les personnages
        tk.Label(self.content_frame, text="Personnages").grid(row=4, column=0, sticky=tk.W)
        self.personnages_frame = tk.Frame(self.content_frame)
        self.personnages_frame.grid(row=4, column=1, sticky=tk.W)
        self.add_personnage_button = tk.Button(self.personnages_frame, text="Ajouter Personnage", command=self.add_personnage)
        self.add_personnage_button.grid(row=0, column=0, sticky=tk.W)
        self.personnage_entries = []

        # Section pour les voies
        tk.Label(self.content_frame, text="Voies").grid(row=5, column=0, sticky=tk.W)
        self.voies_frame = tk.Frame(self.content_frame)
        self.voies_frame.grid(row=5, column=1, sticky=tk.W)
        self.add_voie_button = tk.Button(self.voies_frame, text="Ajouter Voie", command=self.add_voie)
        self.add_voie_button.grid(row=0, column=0, sticky=tk.W)
        self.voie_entries = []

        # Section pour les actes
        tk.Label(self.content_frame, text="Actes").grid(row=6, column=0, sticky=tk.W)
        self.actes_frame = tk.Frame(self.content_frame)
        self.actes_frame.grid(row=6, column=1, sticky=tk.W)
        self.add_acte_button = tk.Button(self.actes_frame, text="Ajouter Acte", command=self.add_acte)
        self.add_acte_button.grid(row=0, column=0, sticky=tk.W)
        self.acte_entries = []

        # Section pour les conditions
        tk.Label(self.content_frame, text="Conditions").grid(row=7, column=0, sticky=tk.W)
        self.conditions_frame = tk.Frame(self.content_frame)
        self.conditions_frame.grid(row=7, column=1, sticky=tk.W)
        self.add_condition_button = tk.Button(self.conditions_frame, text="Ajouter condition", command=self.add_condition)
        self.add_condition_button.grid(row=0, column=0, sticky=tk.W)
        self.condition_entries = []

        # Bouton de soumission
        self.submit_button = tk.Button(self.content_frame, text="Soumettre", command=self.submit)
        self.submit_button.grid(row=8, column=1, sticky=tk.W)

    def add_personnage(self):
        frame = tk.Frame(self.personnages_frame)
        frame.grid(row=len(self.personnage_entries) + 1, column=0, sticky=tk.W)
        entry = tk.Entry(frame)
        entry.grid(row=0, column=0, sticky=tk.W)
        delete_button = tk.Button(frame, text="Supprimer", command=lambda: self.remove_entry(frame, self.personnage_entries))
        delete_button.grid(row=0, column=1, sticky=tk.W)
        self.personnage_entries.append(frame)

    def add_voie(self):
        frame = tk.Frame(self.voies_frame)
        frame.grid(row=len(self.voie_entries) + 1, column=0, sticky=tk.W)
        entry = tk.Entry(frame)
        entry.grid(row=0, column=0, sticky=tk.W)
        delete_button = tk.Button(frame, text="Supprimer", command=lambda: self.remove_entry(frame, self.voie_entries))
        delete_button.grid(row=0, column=1, sticky=tk.W)
        self.voie_entries.append(frame)

    def add_acte(self):
        frame = tk.Frame(self.actes_frame)
        frame.grid(row=len(self.acte_entries) + 1, column=0, sticky=tk.W)
        entry = tk.Entry(frame)
        entry.grid(row=0, column=0, sticky=tk.W)
        delete_button = tk.Button(frame, text="Supprimer", command=lambda: self.remove_entry(frame, self.acte_entries))
        delete_button.grid(row=0, column=1, sticky=tk.W)
        self.acte_entries.append(frame)

    def add_condition(self):
        condition_frame = tk.Frame(self.conditions_frame)
        condition_frame.grid(row=len(self.condition_entries) + 1, column=0, sticky=tk.W)
        
        condition_var = tk.StringVar()
        condition_menu = ttk.Combobox(condition_frame, textvariable=condition_var)
        condition_menu['values'] = ('conditionSceneSuivante', 'conditionAutre')
        condition_menu.grid(row=0, column=0, sticky=tk.W)
        condition_menu.bind('<<ComboboxSelected>>', lambda event, frame=condition_frame, var=condition_var: self.add_condition_fields(frame, var))
        
        delete_button = tk.Button(condition_frame, text="Supprimer", command=lambda: self.remove_entry(condition_frame, self.condition_entries))
        delete_button.grid(row=0, column=1, sticky=tk.W)
        
        self.condition_entries.append(condition_frame)

    def add_condition_fields(self, frame, var):
        if var.get() == 'conditionSceneSuivante':
            add_id_scene_button = tk.Button(frame, text="Ajouter idScene", command=lambda: self.add_id_scene(frame))
            add_id_scene_button.grid(row=1, column=0, sticky=tk.W)
        elif var.get() == 'conditionAutre':
            other_entry = tk.Entry(frame)
            other_entry.grid(row=1, column=0, sticky=tk.W)

    def add_id_scene(self, frame):
        id_scene_frame = tk.Frame(frame)
        id_scene_frame.grid(row=len(frame.winfo_children()), column=0, sticky=tk.W)
        id_scene_entry = tk.Entry(id_scene_frame)
        id_scene_entry.grid(row=0, column=0, sticky=tk.W)
        delete_button = tk.Button(id_scene_frame, text="Supprimer", command=lambda: self.remove_entry(id_scene_frame, frame.winfo_children()))
        delete_button.grid(row=0, column=1, sticky=tk.W)

    def remove_entry(self, frame, entries_list):
        frame.destroy()
        entries_list.remove(frame)

    def submit(self):
        form_data = {
            "idScene": self.id_scene_entry.get(),
            "lieu": self.lieu_entry.get(),
            "interieurExterieur": self.int_ext_entry.get(),
            "urlTexte": self.url_texte_entry.get(),
            "personnages": [entry.winfo_children()[0].get() for entry in self.personnage_entries],
            "voies": [entry.winfo_children()[0].get() for entry in self.voie_entries],
            "actes": [entry.winfo_children()[0].get() for entry in self.acte_entries],
        }
        
        conditions_data = self.get_conditions()

        scene = {
            "info": form_data,
            "conditions": conditions_data
        }
        
        self.scenes.append(scene)
        self.show_submit_options()

    def show_submit_options(self):
        options_window = tk.Toplevel(self.root)
        options_window.title("Options de soumission")

        tk.Label(options_window, text="Souhaitez-vous ajouter une autre scène ou enregistrer le film?").grid(row=0, column=0, columnspan=2, sticky=tk.W)

        new_scene_button = tk.Button(options_window, text="Ajouter une autre scène", command=lambda: [options_window.destroy(), self.clear_frame(self.main_frame), self.show_scene_form()])
        new_scene_button.grid(row=1, column=0, sticky=tk.W)

        save_button = tk.Button(options_window, text="Enregistrer le film", command=lambda: [self.save_movie(), options_window.destroy()])
        save_button.grid(row=1, column=1, sticky=tk.W)

    def save_movie(self):
        data = {
            "scenes": self.scenes
        }
        with open(self.file_name, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {self.file_name}")

    def get_conditions(self):
        conditions = []
        for frame in self.condition_entries:
            widgets = frame.winfo_children()
            condition_type = widgets[0].get()
            if condition_type == 'conditionSceneSuivante':
                ids = [widget.winfo_children()[0].get() for widget in widgets[1:] if isinstance(widget, tk.Frame)]
                conditions.append({"type": condition_type, "idScenesSuivantesPossibles": ids})
            elif condition_type == 'conditionAutre':
                other_text = next(widget.get() for widget in widgets if isinstance(widget, tk.Entry))
                conditions.append({"type": condition_type, "other": other_text})
        return conditions

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

def lancerInterfaceGraphique():
    root = tk.Tk()
    app = SceneFormApp(root)
    root.mainloop()

if __name__ == "__main__":
    lancerInterfaceGraphique()
