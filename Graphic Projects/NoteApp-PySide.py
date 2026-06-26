from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QListWidget, QTextEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QMessageBox, QListWidgetItem 
)
import sys
import uuid


class NoteManager():
    def __init__(self):
        self.note_list = [{"id": "39268fff-8ef6-4521-a5c4-893bb24a8978", "title": "test 1", "description": "description testing 1"},
                          {"id": "6fb7165a-d7a0-49cc-893d-d997bd9d184b", "title": "test 2", "description": "description testing 2"}]


    def add_note(self, title, description):
        note_obj = {"id":str(uuid.uuid4()), "title": title, "description":description}
        self.note_list.append(note_obj)



    def delete_note(self,id):
        self.note_list = [
            note_item for note_item in self.note_list if note_item["id"] != id
        ]


    def update_note(self, id, title, description):
        for note_item in self.note_list:
            if note_item["id"] == id:
                note_item["title"] = title
                note_item["description"] = description
        

    
    def get_note_by_id(self, id):
         for note_item in self.note_list:
            if note_item["id"] == id:
                return note_item

    def get_note_list(self):
        return self.note_list

class NoteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Note App")
        self.note_manager = NoteManager()
        self.selected_item = None
        self.create_widgets()
        self.setup_layout()
        self.setup_connections()
        self.reload_note_list()

    def reload_note_list(self):
        self.note_list_widget.clear()
        for note_item in self.note_manager.get_note_list():
            list_item = QListWidgetItem()
            list_item.setText(note_item["title"]) #for selecting items
            list_item.setData(1, note_item["id"]) #id dor selecting item
            self.note_list_widget.addItem(list_item)





    def create_widgets(self):
        #Note List
        self.note_list_label = QLabel("Note List")
        self.note_list_widget = QListWidget()

        #Editor
        self.note_form_label = QLabel("Note Form:")
        self.note_form_title_entry = QLineEdit()
        self.note_form_title_entry.setPlaceholderText(
            "Enter your note title"
        )

        self.note_form_description_entry = QTextEdit()
        self.note_form_description_entry.setPlaceholderText(
            "Enter your note description"
        )


        self.note_form_add_btn = QPushButton(text = "Add Note")
        self.note_form_update_btn = QPushButton(text = "Update Note")
        self.note_form_update_btn.setEnabled(False) # in default they will be disable, when selecting an item they will be enable
        self.note_form_delete_btn = QPushButton(text = "Delete Note")
        self.note_form_delete_btn.setEnabled(False)
        self.note_form_clear_btn = QPushButton(text = "Clear Note")
        self.note_form_clear_btn.setEnabled(False)




    def setup_layout(self):
        #Left Layout : VBox Note List + Label
        left_layout = QVBoxLayout()

        left_layout.addWidget(self.note_list_label)
        left_layout.addWidget(self.note_list_widget)

        left_widget = QWidget()
        left_widget.setLayout(left_layout)


        #Right Layout : VBox Editor Label + Editor + Buttons
        right_layout = QVBoxLayout()

        right_layout.addWidget(self.note_form_label)
        right_layout.addWidget(self.note_form_title_entry)
        right_layout.addWidget(self.note_form_description_entry)
        right_layout.addWidget(self.note_form_add_btn)
        right_layout.addWidget(self.note_form_update_btn)
        right_layout.addWidget(self.note_form_delete_btn)
        right_layout.addWidget(self.note_form_clear_btn)



        right_widget = QWidget()
        right_widget.setLayout(right_layout)




        #Main Layout : HBox 
        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(right_widget)    


        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


    def setup_connections(self):
        self.note_form_add_btn.clicked.connect(self.add_note)
        self.note_form_update_btn.clicked.connect(self.update_note)
        self.note_form_delete_btn.clicked.connect(self.delete_note)
        self.note_form_clear_btn.clicked.connect(self.clear_selected_note)
        self.note_list_widget.itemClicked.connect(self.set_selected_note)


    def set_selected_note(self,item):
        id = item.data(1)
        self.selected_item = id
        note_item = self.note_manager.get_note_by_id(id)
        self.note_form_title_entry.setText(note_item["title"])
        self.note_form_description_entry.setText(note_item["description"])
        self.note_form_add_btn.setEnabled(False)  #add note btn will be disabled during selecting an item
        self.note_form_update_btn.setEnabled(True)
        self.note_form_delete_btn.setEnabled(True)
        self.note_form_clear_btn.setEnabled(True)



    def add_note(self):
        title = self.note_form_title_entry.text()
        description = self.note_form_description_entry.toPlainText()
        if not(len(title) > 0 and len(description) > 0):
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Entry Error")
            dlg.setText("Title or Description cannot be empty")
            dlg.exec()
            return
        self.note_manager.add_note(title, description)
        self.reload_note_list()

    def update_note(self):
        title = self.note_form_title_entry.text()
        description = self.note_form_description_entry.toPlainText()
        self.note_manager.update_note(self.selected_item,title,description)
        self.reload_note_list()

    def delete_note(self):
        self.note_manager.delete_note(self.selected_item)
        self.reload_note_list()

    def clear_selected_note(self):
        self.selected_item = None
        self.note_form_add_btn.setEnabled(True)   
        self.note_form_update_btn.setEnabled(False)
        self.note_form_delete_btn.setEnabled(False)
        self.note_form_clear_btn.setEnabled(False)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NoteApp()
    window.show()
    sys.exit(app.exec())