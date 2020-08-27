
import sys
from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import QMainWindow, QAction, QHBoxLayout, QVBoxLayout,QLineEdit,QTextEdit , QApplication,QWidget, QLabel
from PySide2.QtCore import QDateTime, QTimeZone

class WordHelper(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Zh's WordHelper")
        self.menu = self.menuBar()

        self.InitFileMenu();
        self.InitParagraphMenu();
        self.InitWordMenu();
        self.InitTagMenu();

        self.InitContainer();
        self.status = self.statusBar()


    def InitFileMenu(self):
        self.file_menu = self.menu.addMenu("File")

        save_action = QAction("Save",self)
        save_action.setShortcut(QKeySequence.Save)
        save_action.triggered.connect(self.SaveFile)
        self.file_menu.addAction(save_action)

        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)

        self.file_menu.addAction(exit_action)


    def SaveFile(self):
        pass


    def InitParagraphMenu(self):
        self.para_menu = self.menu.addMenu("Paragraph")

        new_para_action = QAction("NewParagraph (NP)",self)
        new_para_action.triggered.connect(self.NewParagraph)

        search_para_action = QAction("SearchParagraph (SP)",self)
        search_para_action.triggered.connect(self.SearchParagraph)

        manage_para_action = QAction("ManageParagraph (MP)",self)
        manage_para_action.triggered.connect(self.ManageParagraph)

        for i in [new_para_action,search_para_action,manage_para_action]:
            self.para_menu.addAction(i)

    def InitWordMenu(self):
        self.word_menu = self.menu.addMenu("Word");

        manage,search = (QAction("ManageWord (MW)",self),QAction("SearchWord (SW)",self))
        manage.triggered.connect(self.ManageWord);
        search.triggered.connect(self.SearchWord);

        for i in [manage,search]:
            self.word_menu.addAction(i)

    def InitTagMenu(self):
        self.tag_menu = self.menu.addMenu("Tag");
        new,manage,search = (QAction("NewTag (NT)",self),QAction("ManageTag (MT)",self),QAction("SearchTag (ST)",self))
        new.triggered.connect(self.NewTag)
        manage.triggered.connect(self.ManageTag);
        search.triggered.connect(self.SearchTag);

        for i in [new,manage,search]:
            self.tag_menu.addAction(i)


    def InitContainer(self):

        main_widget = QWidget()

        main_table = QHBoxLayout()

        left = QVBoxLayout()
        self.right_info = QVBoxLayout();

        self.para_info = QLabel()
        self.para_graph = QTextEdit()
        self.word_info = QTextEdit(readOnly=True)

        left.addWidget(self.para_info,2)
        left.addWidget(self.para_graph,20)
        left.addWidget(self.word_info,20)

        main_table.addLayout(left)
        main_table.addLayout(self.right_info)
        main_widget.setLayout(main_table)

        self.setCentralWidget(main_widget)



    def ManageWord(self):
        pass

    def SearchWord(self):
        pass

    def NewParagraph(self):
        pass

    def ManageParagraph(self):
        pass

    def SearchParagraph(self):
        pass

    def NewTag(self):
        pass

    def ManageTag(self):
        pass

    def SearchTag(self):
        pass



def main():
    app = QApplication(sys.argv)
    word_helper = WordHelper()
    word_helper.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()
