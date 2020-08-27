
from PySide2.QtWidgets import QWidget,QHBoxLayout


# word widget 最好有一种在左侧滚动栏显示和新建时的。


def WordWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.ID = ""
        self.word = ""
        self.phonetic = ""
        self.memo = ""
        self.sentenses = [""]

    def Save(self):
        pass


def ShowWordWidget(WordWidget):

    def __init__(self):
        WordWidget.__init__(self)

        self.L = QHBoxLayout()

    def Init(self,ID,word,phonetic,memos,sentenses):
        self.ID = ID
        self.word = word
        self.phonetic = phonetic
        self.memos = memos
        self.sentenses = sentenses

        self.word_text = QLabel(self.word)
        self.phontic = QLabel(phonetic)
        self.self_created_sentense = []
        self.memo = QTextEdit(self.memo)

        for i in [self.word_text,self.phontic,self.memo] + self.self_created_sentense:
            self.L.addWidget(i)

        self.setLayout(self.L)


def EditWordWidget(WordWidget):

    def __init__(self):
        WordWidget.__init__(self)


    def Init(self):
        self.id_label = QLineEdit("word")
        self.phontic = QLineEidt("-")
        self.memos = []
        self.self_created_sentense = []

    def AddSentense(self):
        pass

    def ModifiedSentense(self,ID,sentense):
        pass

    def DeleteSentense(self):
        pass

    def AddMemo(self):
        pass

    def ModifiedMemo(self,ID,sentense):
        pass

    def DeleteMemo(self):
        pass
