#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3.10

#Features:
#Dark and light themes
#To be continued

from PyQt5.QtWidgets import * 
from PyQt5.QtCore import QSize
import sys

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.lw = ListWidget()
		#self.addbtn = AddingTask()

		box = QHBoxLayout()
		box.addWidget(self.lw)
		#box.addWidget(self.addbtn)

		wdg = QWidget()
		wdg.setLayout(box)

		self.setCentralWidget(wdg)

		pass

		self.setWindowTitle("Pytask")
		self.setGeometry(0, 0, 1100, 700)

		#Set checking if window size less than *some_value* and if bigger *some_value* to display
		#Different interfaces

	
class AddingTask(QFrame):
	def __init_(self):
		super().__init__()
		self.initUI()	

	def button_addtask_clicked(self):
		TitleValue = self.task_title.text()
		DescriptionValue = self.task_description.text()

		with open("tasks.txt", "a") as file_with_tasks:
			#file_with_tasks.write(TitleValue + " " + DescriptionValue + "\n")
			file_with_tasks.write(TitleValue + "\n")
			file_with_tasks.write(DescriptionValue + "\n")
			file_with_tasks.close()

		QMessageBox.question(self, 'Message', "Task saved!", QMessageBox.Ok, QMessageBox.Ok)

		#Redesigned button
		#addtaskBtn = QMessageBox()
		#addtaskBtn.setIcon(QMessageBox.Information)
		#addtaskBtn.setText("Your task has been successfully added")
		#addtaskBtn.setWindowTitle("Success")
		#addtaskBtn.setStandardButtons(QMessageBox.Ok)

	def initUI(self):
		self.button1 = QPushButton(self)
		self.button1.setText("Add Task")
		self.button1.clicked.connect(self.button_addtask_clicked)
		self.button1.move(20, 140)

		self.task_title = QLineEdit(self)
		self.task_title.setPlaceholderText("Title")
		self.task_title.move(20, 20)
		self.task_title.resize(280, 40)

		self.task_description = QLineEdit(self)
		self.task_description.setPlaceholderText("Description")
		self.task_description.move(20, 80) 
		self.task_description.resize(280, 40) 

class ListWidget(QListWidget):
	LOCAL_STORAGE = {} #At first saving to local storage and than dispaly in widget

	def __init__(self):
		super().__init__()
		self.fillLocalStorage()
		#self.addItems(self.LOCAL_STORAGE)
		self.addItems([self.LOCAL_STORAGE[task] for task in self.LOCAL_STORAGE])
		self.initUI()

	def fillLocalStorage(self):
		with open("tasks.txt", "r") as file_with_tasks:
			counter = 0 
			title_save = ""
			try:
				for line in file_with_tasks:
					line = line[0:-1]
					if counter % 2 == 0:
						title_save = line
					else:
						self.LOCAL_STORAGE[title_save] = line
					counter += 1
			except:
				pass

	def initUI(self):
		self.resize(300, 300)

class WindowSplitter(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		pass

def main():
	app = QApplication([])
	main_window = MainWindow() 
	#main_window = ListWidget()
	main_window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
