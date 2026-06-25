#imports and global  variables
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import QSize, Qt

import sys



app = QApplication(sys.argv)


#logics
def calculate_bmi_and_result():
    result = None

    weight = float(weight_entry.text())

    height = float(height_entry.text())

    bmi = weight // (height**2)

    if bmi < 18.5:

        result = "Under Weight"

    elif 18.5 <= bmi < 25:

        result = "Normal"

    elif 25 <= bmi < 30:

        result = "Over Weight"

    elif 30 <= bmi < 35:

        result = "Obese"

    else:

        result = "Extremely Obese"

    result_Label.setText(f"Result : {result}")




#UI Design

#Create a Qt widget, which will be oujr window
window = QMainWindow()
window.setWindowTitle("GUI BMI Calculator")
window.setFixedSize(QSize(400, 300))
widget = QWidget()
layout = QVBoxLayout()



height_label = QLabel("Height (m):")
height_entry = QLineEdit()

weight_label = QLabel("W(eight (kg)")
weight_entry = QLineEdit()


calculate_button = QPushButton(text="Calculate BMI")
calculate_button.clicked.connect(calculate_bmi_and_result)
result_Label = QLabel("Result:")





layout.addWidget(height_label)
layout.addWidget(height_entry)
layout.addWidget(weight_label)
layout.addWidget(weight_entry)
layout.addWidget(calculate_button)
layout.addWidget(result_Label)



widget.setLayout(layout)
window.setCentralWidget(widget)


window.show()


#Start the Event Loop



#Runnig the Application
app.exec()