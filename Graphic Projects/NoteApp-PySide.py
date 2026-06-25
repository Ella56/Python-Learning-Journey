from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QListWidget, QTextEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QMessageBox, QListWidgetItem 
)
import sys
import uuid


class NoteManager():
    def __init__(self):
        self.note_list = []


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
        

    
    def get_note_by_id(self):
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
            list_item.setText(note_item["title"])
            list_item.setText(note_item["id"])
            list_item.setData(1, note_item["id"])
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
        self.note_form_delete_btn = QPushButton(text = "Delete Note")
        self.note_form_clear_btn = QPushButton(text = "Clear Note")




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
        pass

    def delete_note(self):
        pass

    def clear_selected_note(self):
        pass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NoteApp()
    window.show()
    sys.exit(app.exec())