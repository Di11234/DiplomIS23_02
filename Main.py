from PyQt6 import QtCore, QtGui, QtWidgets
import psycopg,sys
import random
global currentMenu
from datetime import datetime

conn = psycopg.connect(dbname="postgres", user="postgres", password="55665", host="localhost", port="2024")
cur = conn.cursor()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(454, 480)
        Dialog.setStyleSheet("background-color:#FFF5F2")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(parent=Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 430, 368))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(parent=self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(15)
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.setStyleSheet("border: 3px solid #64898F")
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)

        self.pushButton.setStyleSheet("background-color:#64898F")
        self.pushButton_2.setStyleSheet("background-color:#64898F")

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Найти"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", ""))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        #self.treeWidget.topLevelItem(0).setText(0, _translate("Dialog", "Предмет"))
        #self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Dialog", "Название предмета"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("Dialog", "Готово"))
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def fillInfo(self,tableName):
        if tableName=="Животные":
            self.treeWidget.headerItem().setText(0,"Животные")
            cur.execute("SELECT DISTINCT вид,группа FROM питомцы "
                        "JOIN виды ON питомцы.вид=виды.название")
            mainGroup=cur.fetchall()
            for i in range(len(mainGroup)):
                item = QtWidgets.QTreeWidgetItem()
                self.treeWidget.insertTopLevelItem(i, item)
                item.setText(0, mainGroup[i][1])
                item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsSelectable)
                print(mainGroup[i][1])
                cur.execute("SELECT DISTINCT имя,petid,вид FROM питомцы "
                                f"WHERE вид = {"'"+mainGroup[i][0]+"'"}")
                insideItems = cur.fetchall()
                for j in range(len(insideItems)):
                    insideItem=QtWidgets.QTreeWidgetItem()
                    insideItem.setText(0,f"ID {insideItems[j][1]} {insideItems[j][0]} {insideItems[j][2]}")
                    item.addChild(insideItem)
                    insideItem.setDisabled(False)
            cur.execute("SELECT имя,вид,группа FROM питомцы "
                        "JOIN виды ON питомцы.вид=виды.название")
            info = cur.fetchall()
            print(info)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.currentRedactButtons = []
        self.currentDeleteButtons =[]
        self.currentMenu=0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1003, 620)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color:#FFF5F2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menuPages = QtWidgets.QVBoxLayout()
        self.menuPages.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.menuPages.setObjectName("menuPages")
        self.mainPage = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPage.sizePolicy().hasHeightForWidth())
        self.mainPage.setSizePolicy(sizePolicy)
        self.mainPage.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.mainPage.setFont(font)
        self.mainPage.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.mainPage.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.mainPage.setStyleSheet("pushButton.setStyleSheet(\"text-align:left;\")")
        self.mainPage.setObjectName("mainPage")
        self.mainPage.setStyleSheet("""
        QPushButton {
        background-color:#64898F;
    }
            QPushButton:disabled {
                background-color: #4B6773;
                color: black;
            }
        """)
        self.menuPages.addWidget(self.mainPage)
        self.petsPage = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.petsPage.sizePolicy().hasHeightForWidth())
        self.petsPage.setSizePolicy(sizePolicy)
        self.petsPage.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.petsPage.setFont(font)
        self.petsPage.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.petsPage.setObjectName("petsPage")
        self.petsPage.setStyleSheet("""
        QPushButton {
        background-color:#64898F;
    }
            QPushButton:disabled {
                background-color: #4B6773;
                color: black;
            }
        """)
        self.menuPages.addWidget(self.petsPage)
        self.schedPage = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.schedPage.sizePolicy().hasHeightForWidth())
        self.schedPage.setSizePolicy(sizePolicy)
        self.schedPage.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.schedPage.setFont(font)
        self.schedPage.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.schedPage.setObjectName("schedPage")
        self.schedPage.setStyleSheet("""
        QPushButton {
        background-color:#64898F;
    }
            QPushButton:disabled {
                background-color: #4B6773;
                color: black;
            }
        """)
        self.menuPages.addWidget(self.schedPage)
        self.cagesPage = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cagesPage.sizePolicy().hasHeightForWidth())
        self.cagesPage.setSizePolicy(sizePolicy)
        self.cagesPage.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(16)
        self.cagesPage.setFont(font)
        self.cagesPage.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.cagesPage.setObjectName("cagesPage")
        self.cagesPage.setStyleSheet("""
        QPushButton {
        background-color:#64898F;
    }
            QPushButton:disabled {
                background-color: #4B6773;
                color: black;
            }
        """)
        self.menuPages.addWidget(self.cagesPage)
        self.horizontalLayout_2.addLayout(self.menuPages)
        self.scrollAreaContainer = QtWidgets.QVBoxLayout()
        self.scrollAreaContainer.setContentsMargins(-1, 0, 0, -1)
        self.scrollAreaContainer.setObjectName("scrollAreaContainer")
        self.scrollAreaMenu = QtWidgets.QHBoxLayout()
        self.scrollAreaMenu.setContentsMargins(-1, 0, -1, -1)
        self.scrollAreaMenu.setObjectName("scrollAreaMenu")
        self.pushToCreateM = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(12)
        self.pushToCreateM.setFont(font)
        self.pushToCreateM.setObjectName("pushToCreateM")
        self.pushToCreateM.setStyleSheet("background-color:#64898F")
        self.scrollAreaMenu.addWidget(self.pushToCreateM)
        self.pushToRedactM = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushToRedactM.setStyleSheet("background-color:#64898F")
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(12)
        self.pushToRedactM.setFont(font)
        self.pushToRedactM.setObjectName("pushToRedactM")
        self.scrollAreaMenu.addWidget(self.pushToRedactM)
        self.pushToSearch = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushToSearch.setStyleSheet("background-color:#64898F")
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(12)
        self.pushToSearch.setFont(font)
        self.pushToSearch.setObjectName("pushToSearch")
        self.scrollAreaMenu.addWidget(self.pushToSearch)
        self.searchWhat = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.searchWhat.setObjectName("searchWhat")
        self.scrollAreaMenu.addWidget(self.searchWhat)
        self.scrollAreaMenu.setStretch(0, 2)
        self.scrollAreaMenu.setStretch(1, 2)
        self.scrollAreaMenu.setStretch(2, 2)
        self.scrollAreaMenu.setStretch(3, 5)
        self.scrollAreaContainer.addLayout(self.scrollAreaMenu)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 671, 570))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollAreaContainer.addWidget(self.scrollArea)
        self.horizontalLayout_2.addLayout(self.scrollAreaContainer)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)

        self.mainMenuGui()

        self.mainPage.setDisabled(True)

        self.mainPage.clicked.connect(self.setMenu0)

        self.petsPage.clicked.connect(self.setMenu1)

        self.schedPage.clicked.connect(self.setMenu2)

        self.cagesPage.clicked.connect(self.setMenu3)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#Менюшки
    def mainMenuGui(self):

        self.pushToSearch.setStyleSheet("background-color:#64898F")
        self.pushToRedactM.setStyleSheet("background-color:#64898F")
        self.pushToCreateM.setStyleSheet("background-color:#64898F")

        if not hasattr(self,'mainVertLayout'):
            setattr(self, "mainVertWidget", QtWidgets.QWidget(parent=self.scrollAreaWidgetContents))
            mainVertWidget = getattr(self, "mainVertWidget")
            mainVertWidget.setObjectName("mainVertWidget")
            mainVertLayout = QtWidgets.QVBoxLayout(mainVertWidget)
            mainVertLayout.setContentsMargins(11, 11, 11, 11)
            mainVertLayout.setObjectName("mainVertLayout")
            mainToday_L = QtWidgets.QLabel(parent=mainVertWidget)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(20)
            mainToday_L.setFont(font)
            mainToday_L.setStyleSheet("background-color:#64898F;padding: 5px; border-radius: 15px")
            mainToday_L.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            mainToday_L.setObjectName("mainToday_L")
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                               QtWidgets.QSizePolicy.Policy.MinimumExpanding)
            sizePolicy.setHorizontalStretch(50)
            sizePolicy.setVerticalStretch(50)
            sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
            mainToday_L.setSizePolicy(sizePolicy)
            mainVertLayout.addWidget(mainToday_L)
            todayContainer = QtWidgets.QHBoxLayout()
            todayContainer.setObjectName("todayContainer")

            cur.execute("SELECT * FROM события")
            check=cur.fetchall()
            todaysdate=str(datetime.today().strftime('%Y-%m-%d'))
            print(todaysdate)

            for i in range(len(check)):
                if check[i][3]==True or str(check[i][2])==str(todaysdate):
                    eventTodayNumX = QtWidgets.QWidget(parent=mainVertWidget)
                    # eventTodayNumX.setStyleSheet("border: 3px solid #64898F; border-radius: 15px")
                    eventTodayNumX.setStyleSheet("""
                                                        QWidget#eventTodayNumX {
                                                       border: 3px solid #64898F; border-radius: 15px
                                                        }
                                                        """)
                    eventTodayNumX.setObjectName("eventTodayNumX")
                    verticalLayout_2 = QtWidgets.QVBoxLayout(eventTodayNumX)
                    verticalLayout_2.setObjectName("verticalLayout_2")
                    todayDateX = QtWidgets.QLabel(parent=eventTodayNumX)
                    if check[i][3]==True:
                        todayDateX.setText("Ежедневное")
                    else:
                        todayDateX.setText(str(check[i][2]))
                    todayDateX.setAlignment(
                        QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
                    todayDateX.setObjectName("todayDateX")
                    verticalLayout_2.addWidget(todayDateX)
                    todayNameX = QtWidgets.QLabel(parent=eventTodayNumX)
                    todayNameX.setText(check[i][1])
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(20)
                    font.setBold(True)
                    font.setWeight(75)
                    todayNameX.setFont(font)
                    todayNameX.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    todayNameX.setObjectName("todayNameX")
                    verticalLayout_2.addWidget(todayNameX)
                    todayDescX = QtWidgets.QLabel(parent=eventTodayNumX)
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(18)
                    todayDescX.setFont(font)
                    todayDescX.setObjectName("todayDescX")
                    verticalLayout_2.addWidget(todayDescX)
                    setattr(self, "spacerItem", QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                                                      QtWidgets.QSizePolicy.Policy.Minimum))
                    spacerItem = getattr(self, "spacerItem")
                    verticalLayout_2.addItem(spacerItem)
                    buttonsSchedMenuX = QtWidgets.QHBoxLayout()
                    buttonsSchedMenuX.setContentsMargins(-1, 0, -1, -1)
                    buttonsSchedMenuX.setObjectName("buttonsSchedMenuX")
                    todayToDoX = QtWidgets.QPushButton(parent=eventTodayNumX)
                    todayToDoX.setObjectName("todayToDoX")
                    buttonsSchedMenuX.addWidget(todayToDoX)
                    todayToCancelX = QtWidgets.QPushButton(parent=eventTodayNumX)
                    todayToCancelX.setObjectName("todayToCancelX")
                    buttonsSchedMenuX.addWidget(todayToCancelX)
                    todayDoneX = QtWidgets.QLabel(parent=eventTodayNumX)
                    todayDoneX.setAlignment(
                        QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
                    todayDoneX.setObjectName("todayDoneX")
                    buttonsSchedMenuX.addWidget(todayDoneX)
                    verticalLayout_2.addLayout(buttonsSchedMenuX)
                    todayContainer.addWidget(eventTodayNumX)
                    mainVertLayout.addLayout(todayContainer)
                    closestContainer = QtWidgets.QHBoxLayout()
                    closestContainer.setContentsMargins(0, 0, -1, -1)
                    closestContainer.setObjectName("closestContainer")
                    label_4 = QtWidgets.QLabel(parent=mainVertWidget)
                    label_4.setObjectName("label_4")
                    closestContainer.addWidget(label_4)
                    label_4.setHidden(True)
                    mainVertLayout.addLayout(closestContainer)
                    mainVertLayout.setStretch(0, 3)
                    mainVertLayout.setStretch(1, 7)
                    self.horizontalLayout.addWidget(mainVertWidget)
                    self.scrollAreaContainer.addWidget(self.scrollArea)
                    self.horizontalLayout_2.addLayout(self.scrollAreaContainer)
                    self.horizontalLayout_2.setStretch(0, 2)
                    self.horizontalLayout_2.setStretch(1, 5)
                    todayToDoX.setStyleSheet("background-color:#64898F")
                    todayToCancelX.setStyleSheet("background-color:#64898F")
                    todayNameX.setStyleSheet("background-color:#64898F;padding: 5px; border-radius: 15px")

                    _translate = QtCore.QCoreApplication.translate
                    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                    mainToday_L.setText(_translate("MainWindow", "Сегодня"))
                    todayDescX.setText(_translate("MainWindow", "Описание"))
                    todayToDoX.setText(_translate("MainWindow", "Сделать"))
                    todayToCancelX.setText(_translate("MainWindow", "Отменить"))
                    todayDoneX.setText(_translate("MainWindow", "Сделано"))
                    #mainClosest.setText(_translate("MainWindow", "Ближайшие события"))
                    label_4.setText(_translate("MainWindow", "TextLabel"))



            MainWindow.setCentralWidget(self.centralwidget)

            QtCore.QMetaObject.connectSlotsByName(MainWindow)


        else:
            getattr(self, "mainVertWidget").setParent(self.scrollAreaWidgetContents)
            getattr(self, "mainVertWidget").show()

        self.petsPage.setStyleSheet("""
                                    QPushButton {
                                    background-color:#64898F;
                                }
                                        QPushButton:disabled {
                                            background-color: #4B6773;
                                            color: black;
                                        }
                                    """)
        self.mainPage.setStyleSheet("""
                                    QPushButton {
                                    background-color:#64898F;
                                }
                                        QPushButton:disabled {
                                            background-color: #4B6773;
                                            color: black;
                                        }
                                    """)
        self.schedPage.setStyleSheet("""
                                    QPushButton {
                                    background-color:#64898F;
                                }
                                        QPushButton:disabled {
                                            background-color: #4B6773;
                                            color: black;
                                        }
                                    """)
        self.cagesPage.setStyleSheet("""
                                    QPushButton {
                                    background-color:#64898F;
                                }
                                        QPushButton:disabled {
                                            background-color: #4B6773;
                                            color: black;
                                        }
                                    """)

        #self.containerEvent.setStyleSheet("background-color: #64898F")
        #self.pushToDo.setStyleSheet("background-color: #FFF5F2")
        #self.eventActions.addWidget(self.pushToDo)
        #self.pushToRedact.setStyleSheet("background-color: #FFF5F2")
        #self.pushToCancel.setStyleSheet("background-color: #FFF5F2")


    def petsMenuGui(self):
        self.pushToSearch.setStyleSheet("background-color:#CDA989")
        self.pushToRedactM.setStyleSheet("background-color:#CDA989")
        self.pushToCreateM.setStyleSheet("background-color:#CDA989")

        cur.execute("SELECT * FROM питомцы")
        check = cur.fetchall()

        for i in range(len(check)):
            if not hasattr(self,f'containerPet_{i}'):
                setattr(self, f"containerPet_{i}", QtWidgets.QWidget(parent=self.scrollAreaWidgetContents))
                containerPet = getattr(self, f"containerPet_{i}")
                containerPet.setObjectName("containerPet")
                self.formLayout = QtWidgets.QFormLayout(containerPet)
                self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.RowWrapPolicy.WrapLongRows)
                self.formLayout.setLabelAlignment(
                    QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
                self.formLayout.setFormAlignment(
                    QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
                self.formLayout.setContentsMargins(0, 5, 5, -1)
                self.formLayout.setSpacing(5)
                self.formLayout.setObjectName("formLayout")

                setattr(self, f"petNameLO_{i}", QtWidgets.QHBoxLayout())
                petNameLO = getattr(self, f"petNameLO_{i}")

                petNameLO = QtWidgets.QHBoxLayout()
                petNameLO.setContentsMargins(-1, 0, -1, -1)
                petNameLO.setObjectName("petNameLO")

                setattr(self, f"descName_L_{i}", QtWidgets.QLabel(parent=containerPet))
                descName_L = getattr(self, f"descName_L_{i}")
                print(check[i][1])

                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(20)
                descName_L.setFont(font)
                descName_L.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                descName_L.setObjectName("descName_L")
                petNameLO.addWidget(descName_L)

                setattr(self, f"petNameEdit_{i}", QtWidgets.QLineEdit(parent=containerPet))
                petNameEdit = getattr(self, f"petNameEdit_{i}")

                descName_L.setText(check[i][1])
                petNameEdit.setPlaceholderText("Имя питомца")
                petNameEdit.setText(check[i][1])

                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(petNameEdit.sizePolicy().hasHeightForWidth())
                petNameEdit.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light SemiCondensed")
                font.setPointSize(20)
                petNameEdit.setFont(font)
                petNameEdit.setObjectName("petNameEdit")
                petNameEdit.setHidden(True)
                petNameLO.addWidget(petNameEdit)
                self.formLayout.setLayout(2, QtWidgets.QFormLayout.ItemRole.FieldRole, petNameLO)

                setattr(self, f"petSpecLO_{i}", QtWidgets.QHBoxLayout())
                petSpecLO = getattr(self, f"petSpecLO_{i}")

                petSpecLO.setContentsMargins(-1, 0, -1, -1)
                petSpecLO.setObjectName("petSpecLO")

                setattr(self, f"petSpec_{i}", QtWidgets.QLabel(parent=containerPet))
                petSpec = getattr(self, f"petSpec_{i}")
                petSpec.setText(("Вид: "+check[i][2]))

                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petSpec.setFont(font)
                petSpec.setObjectName("petSpec")
                petSpecLO.addWidget(petSpec)

                setattr(self, f"petSpecEdit_{i}", QtWidgets.QComboBox(parent=containerPet))
                petSpecEdit = getattr(self, f"petSpecEdit_{i}")

                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(petSpecEdit.sizePolicy().hasHeightForWidth())
                petSpecEdit.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petSpecEdit.setFont(font)
                petSpecEdit.setObjectName("petSpecEdit")
                petSpecEdit.setHidden(True)
                petSpecLO.addWidget(petSpecEdit)
                self.formLayout.setLayout(3, QtWidgets.QFormLayout.ItemRole.FieldRole, petSpecLO)

                setattr(self, f"petMorphLO_{i}", QtWidgets.QHBoxLayout())
                petMorphLO = getattr(self, f"petMorphLO_{i}")

                petMorphLO.setContentsMargins(-1, 0, -1, -1)
                petMorphLO.setObjectName("petMorphLO")

                setattr(self, f"petMorph_{i}", QtWidgets.QLabel(parent=containerPet))
                petMorph = getattr(self, f"petMorph_{i}")

                if check[i][5]!=None: petMorph.setText(check[i][5])
                else: petMorph.hide()

                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petMorph.setFont(font)
                petMorph.setObjectName("petMorph")
                petMorphLO.addWidget(petMorph)

                setattr(self, f"petMorphEdit_{i}", QtWidgets.QComboBox(parent=containerPet))
                petMorphEdit = getattr(self, f"petMorphEdit_{i}")

                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(petMorphEdit.sizePolicy().hasHeightForWidth())
                petMorphEdit.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petMorphEdit.setFont(font)
                petMorphEdit.setObjectName("petMorphEdit")
                petMorphLO.addWidget(petMorphEdit)
                petMorphEdit.setHidden(True)
                self.formLayout.setLayout(4, QtWidgets.QFormLayout.ItemRole.FieldRole, petMorphLO)

                setattr(self, f"petsAgeBirthdayLO_{i}", QtWidgets.QHBoxLayout())
                petsAgeBirthdayLO = getattr(self, f"petsAgeBirthdayLO_{i}")

                petsAgeBirthdayLO.setContentsMargins(-1, 0, -1, -1)
                petsAgeBirthdayLO.setObjectName("petsAgeBirthdayLO")

                setattr(self, f"petsAgeBirthday_{i}", QtWidgets.QLabel(parent=containerPet))
                petsAgeBirthday = getattr(self, f"petsAgeBirthday_{i}")

                texttoadd="Возраст и день рождения:"
                if check[i][3]==None and check[i][4]==None: petsAgeBirthday.hide()
                else:
                    if check[i][3]!=None:texttoadd=texttoadd+" "+str(check[i][3])+" г."
                    if check[i][4]!=None: texttoadd=texttoadd+" "+str(check[i][4])
                    petsAgeBirthday.setText(texttoadd)

                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petsAgeBirthday.setFont(font)
                petsAgeBirthday.setObjectName("petsAgeBirthday")
                petsAgeBirthdayLO.addWidget( petsAgeBirthday)

                setattr(self, f"petsAgeEdit_{i}", QtWidgets.QSpinBox(parent=containerPet))
                petsAgeEdit = getattr(self, f"petsAgeEdit_{i}")

                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(petsAgeEdit.sizePolicy().hasHeightForWidth())
                petsAgeEdit.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petsAgeEdit.setFont(font)
                petsAgeEdit.setObjectName("petsAgeEdit")
                petsAgeBirthdayLO.addWidget(petsAgeEdit)
                petsAgeEdit.setHidden(True)

                setattr(self, f"petsBirthdayEdit_{i}", QtWidgets.QDateEdit(parent=containerPet))
                petsBirthdayEdit = getattr(self, f"petsBirthdayEdit_{i}")

                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petsBirthdayEdit.setFont(font)
                petsBirthdayEdit.setObjectName("petsBirthdayEdit")
                petsAgeBirthdayLO.addWidget(petsBirthdayEdit)
                petsBirthdayEdit.setHidden(True)
                self.formLayout.setLayout(5, QtWidgets.QFormLayout.ItemRole.FieldRole, petsAgeBirthdayLO)

                setattr(self, f"petsGenLO_{i}", QtWidgets.QHBoxLayout())
                petsGenLO = getattr(self, f"petsGenLO_{i}")

                petsGenLO.setContentsMargins(-1, 0, -1, -1)
                petsGenLO.setObjectName("petsGenLO")

                setattr(self, f"petsGen_{i}", QtWidgets.QLabel(parent=containerPet))
                petsGen = getattr(self, f"petsGen_{i}")

                if check[i][11]!=None: petsGen.setText(("Пол: "+check[i][11]))
                else: petsGen.hide()

                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petsGen.setFont(font)
                petsGen.setObjectName("petsGen")
                petsGenLO.addWidget(petsGen)

                setattr(self, f"petsGenEdit_{i}", QtWidgets.QComboBox(parent=containerPet))
                petsGenEdit = getattr(self, f"petsGenEdit_{i}")

                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(petsGenEdit.sizePolicy().hasHeightForWidth())
                petsGenEdit.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petsGenEdit.setFont(font)
                petsGenEdit.setCurrentText("")
                petsGenEdit.setObjectName("petsGenEdit")
                petsGenLO.addWidget(petsGenEdit)
                petsGenEdit.setHidden(True)
                self.formLayout.setLayout(6, QtWidgets.QFormLayout.ItemRole.FieldRole, petsGenLO)

                setattr(self, f"petWeightLO_{i}", QtWidgets.QHBoxLayout())
                petWeightLO = getattr(self, f"petWeightLO_{i}")

                petWeightLO.setContentsMargins(-1, 0, -1, -1)
                petWeightLO.setObjectName("petWeightLO")

                setattr(self, f"petsWeight_{i}", QtWidgets.QLabel(parent=containerPet))
                petsWeight = getattr(self, f"petsWeight_{i}")
                texttoadd=""

                if check[i][12]!=None and check[i][9]!=None:
                    texttoadd="Вес: "+str(check[i][9])+" "+check[i][12]
                    petsWeight.setText(texttoadd)
                else: petsWeight.hide()

                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petsWeight.setFont(font)
                petsWeight.setObjectName("petsWeight")
                petWeightLO.addWidget(petsWeight)

                setattr(self, f"petWeightNumEdit_{i}", QtWidgets.QSpinBox(parent=containerPet))
                petWeightNumEdit = getattr(self, f"petWeightNumEdit_{i}")

                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(petWeightNumEdit.sizePolicy().hasHeightForWidth())
                petWeightNumEdit.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petWeightNumEdit.setFont(font)
                petWeightNumEdit.setObjectName("petWeightNumEdit")
                petWeightNumEdit.setHidden(True)
                petWeightLO.addWidget(petWeightNumEdit)

                setattr(self, f"petWeightAsEdit_{i}", QtWidgets.QLineEdit(parent=containerPet))
                petWeightAsEdit = getattr(self, f"petWeightAsEdit_{i}")

                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth( petWeightAsEdit.sizePolicy().hasHeightForWidth())
                petWeightAsEdit.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petWeightAsEdit.setFont(font)
                petWeightAsEdit.setText("")
                petWeightAsEdit.setObjectName("petWeightAsEdit")
                petWeightLO.addWidget( petWeightAsEdit)
                petWeightAsEdit.setHidden(True)
                self.formLayout.setLayout(7, QtWidgets.QFormLayout.ItemRole.FieldRole, petWeightLO)

                setattr(self, f"petsSymptomsLO_{i}", QtWidgets.QHBoxLayout())
                petsSymptomsLO = getattr(self, f"petsSymptomsLO_{i}")

                petsSymptomsLO.setContentsMargins(-1, 0, -1, -1)
                petsSymptomsLO.setObjectName("petsSymptomsLO")

                setattr(self, f"petSympotms_{i}", QtWidgets.QLabel(parent=containerPet))
                petSympotms = getattr(self, f"petSympotms_{i}")

                if check[i][13]!=None:
                    petSympotms.setText(("Симптомы: "+check[i][13]))
                else:
                    petSympotms.hide()

                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petSympotms.setFont(font)
                petSympotms.setObjectName("petSympotms")
                petsSymptomsLO.addWidget(petSympotms)

                setattr(self, f"petsSymptomsEdit_{i}", QtWidgets.QLineEdit(parent=containerPet))
                petsSymptomsEdit = getattr(self, f"petsSymptomsEdit_{i}")

                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(petsSymptomsEdit.sizePolicy().hasHeightForWidth())
                petsSymptomsEdit.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petsSymptomsEdit.setFont(font)
                petsSymptomsEdit.setObjectName("petsSymptomsEdit")
                petsSymptomsLO.addWidget(petsSymptomsEdit)
                petsSymptomsEdit.setHidden(True)
                self.formLayout.setLayout(8, QtWidgets.QFormLayout.ItemRole.FieldRole, petsSymptomsLO)

                setattr(self, f"petDiagnosisLO_{i}", QtWidgets.QHBoxLayout())
                petDiagnosisLO = getattr(self, f"petDiagnosisLO_{i}")

                petDiagnosisLO.setContentsMargins(-1, 0, -1, -1)
                petDiagnosisLO.setObjectName("petDiagnosisLO")

                setattr(self, f"label_{i}", QtWidgets.QLabel(parent=containerPet))
                label = getattr(self, f"label_{i}")

                if check[i][14]!=None and check[i][14]!="":
                    label.setText(("Диагнозы: "+check[i][14]))
                else: label.hide()

                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                label.setFont(font)
                label.setObjectName("label")
                petDiagnosisLO.addWidget(label)

                setattr(self, f"petDiagnosisEdit_{i}", QtWidgets.QLineEdit(parent=containerPet))
                petDiagnosisEdit= getattr(self, f"petDiagnosisEdit_{i}")

                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petDiagnosisEdit.setFont(font)
                petDiagnosisEdit.setObjectName("petDiagnosisEdit")
                petDiagnosisLO.addWidget(petDiagnosisEdit)
                petDiagnosisEdit.setHidden(True)
                self.formLayout.setLayout(9, QtWidgets.QFormLayout.ItemRole.FieldRole, petDiagnosisLO)

                setattr(self, f"petNeuteredLO_{i}", QtWidgets.QHBoxLayout())
                petNeuteredLO = getattr(self, f"petNeuteredLO_{i}")

                petNeuteredLO.setContentsMargins(-1, 0, -1, -1)
                petNeuteredLO.setObjectName("petNeuteredLO")

                setattr(self, f"petNeutered_{i}", QtWidgets.QLabel(parent=containerPet))
                petNeutered = getattr(self, f"petNeutered_{i}")

                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petNeutered.setFont(font)
                petNeutered.setObjectName("petNeutered")
                petNeuteredLO.addWidget(petNeutered)

                setattr(self, f"petNeuteredEdit_{i}", QtWidgets.QCheckBox(parent=containerPet))
                petNeuteredEdit = getattr(self, f"petNeuteredEdit_{i}")

                if check[i][8]!=None and check[i][8]!=False:
                    petNeutered.show()
                else: petNeutered.hide()

                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(petNeuteredEdit.sizePolicy().hasHeightForWidth())
                petNeuteredEdit.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petNeuteredEdit.setFont(font)
                petNeuteredEdit.setObjectName("petNeuteredEdit")
                petNeuteredLO.addWidget(petNeuteredEdit)
                petNeuteredEdit.setHidden(True)
                self.formLayout.setLayout(10, QtWidgets.QFormLayout.ItemRole.FieldRole, petNeuteredLO)

                setattr(self, f"petsVacsLO_{i}", QtWidgets.QHBoxLayout())
                petsVacsLO = getattr(self, f"petsVacsLO_{i}")

                petsVacsLO.setContentsMargins(-1, 0, -1, -1)
                petsVacsLO.setObjectName("petsVacsLO")

                setattr(self, f"petsVacs_{i}", QtWidgets.QLabel(parent=containerPet))
                petsVacs = getattr(self, f"petsVacs_{i}")

                if check[i][7]!=None and check[i][7]!="":
                    petsVacs.setText(("Прививки: "+check[i][7]))
                else: petsVacs.hide()

                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petsVacs.setFont(font)
                petsVacs.setObjectName("petsVacs")
                petsVacsLO.addWidget(petsVacs)
                petsVacsEdit = QtWidgets.QLineEdit(parent=containerPet)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(petsVacsEdit.sizePolicy().hasHeightForWidth())
                petsVacsEdit.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petsVacsEdit.setFont(font)
                petsVacsEdit.setObjectName("petsVacsEdit")
                petsVacsLO.addWidget(petsVacsEdit)
                petsVacsEdit.setHidden(True)
                self.formLayout.setLayout(11, QtWidgets.QFormLayout.ItemRole.FieldRole, petsVacsLO)

                setattr(self, f"petsMictochipLO_{i}", QtWidgets.QHBoxLayout())
                petsMictochipLO = getattr(self, f"petsMictochipLO_{i}")

                setattr(self, f"petMicrochipEdit_{i}", QtWidgets.QCheckBox(parent=containerPet))
                petMicrochipEdit = getattr(self, f"petMicrochipEdit_{i}")

                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(petMicrochipEdit.sizePolicy().hasHeightForWidth())

                setattr(self, f"petsMicrochip_{i}", QtWidgets.QLabel(parent=containerPet))
                petsMicrochip = getattr(self, f"petsMicrochip_{i}")

                if check[i][6]!=None and check[i][6]!=False:
                    petsMicrochip.setText("Микрочип")
                else: petsMicrochip.hide()

                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petsMicrochip.setFont(font)
                petsMicrochip.setObjectName("petsMicrochip")
                petsMictochipLO.addWidget(petsMicrochip)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(petMicrochipEdit.sizePolicy().hasHeightForWidth())
                petMicrochipEdit.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petMicrochipEdit.setFont(font)
                petMicrochipEdit.setObjectName("petMicrochipEdit")
                petsMictochipLO.addWidget(petMicrochipEdit)
                petMicrochipEdit.setHidden(True)
                self.formLayout.setLayout(12, QtWidgets.QFormLayout.ItemRole.FieldRole, petsMictochipLO)

                setattr(self, f"petsOwnerLO_{i}", QtWidgets.QHBoxLayout())
                petsOwnerLO = getattr(self, f"petsOwnerLO_{i}")

                petsOwnerLO.setContentsMargins(-1, 0, -1, -1)
                petsOwnerLO.setObjectName("petsOwnerLO")

                setattr(self, f"petsOwner_{i}", QtWidgets.QLabel(parent=containerPet))
                petsOwner = getattr(self, f"petsOwner_{i}")

                if check[i][15]!=None and check[i][15]!="":
                    petsOwner.setText(("Хозяин: "+check[i][15]))

                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petsOwner.setFont(font)
                petsOwner.setObjectName("petsOwner")
                petsOwnerLO.addWidget(petsOwner)
                petsOwnerEdit = QtWidgets.QLineEdit(parent=containerPet)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(petsOwnerEdit.sizePolicy().hasHeightForWidth())
                petsOwnerEdit.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petsOwnerEdit.setFont(font)
                petsOwnerEdit.setObjectName("petsOwnerEdit")
                petsOwnerLO.addWidget(petsOwnerEdit)
                petsOwnerEdit.setHidden(True)
                self.formLayout.setLayout(13, QtWidgets.QFormLayout.ItemRole.FieldRole, petsOwnerLO)
                petsLiveInLO = QtWidgets.QHBoxLayout()
                petsLiveInLO.setContentsMargins(-1, 0, -1, -1)
                petsLiveInLO.setObjectName("petsLiveInLO")

                setattr(self, f"petsLivein_{i}", QtWidgets.QLabel(parent=containerPet))
                petsLivein = getattr(self, f"petsLivein_{i}")

                cur.execute(f'SELECT "название прив клетки" FROM "животные к клеткам" WHERE "id животного"={check[i][0]}')
                animsCages=cur.fetchall()
                if animsCages!=[]:
                    petsLivein.setText(("Живёт в: " + animsCages[0][0]))
                else: petsLivein.setText("Живёт в: ")



                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petsLivein.setFont(font)
                petsLivein.setObjectName("petsLivein")
                petsLiveInLO.addWidget(petsLivein)
                petsLiveinEdit = QtWidgets.QPushButton(parent=containerPet)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(petsLiveinEdit.sizePolicy().hasHeightForWidth())
                petsLiveinEdit.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petsLiveinEdit.setFont(font)
                petsLiveinEdit.setObjectName("petsLiveinEdit")
                petsLiveInLO.addWidget(petsLiveinEdit)
                petsLiveinEdit.setHidden(True)
                self.formLayout.setLayout(14, QtWidgets.QFormLayout.ItemRole.FieldRole, petsLiveInLO)

                setattr(self,"spacerItem",QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Policy.Minimum,
                                                   QtWidgets.QSizePolicy.Policy.Expanding))

                spacerItem = getattr(self,"spacerItem")
                self.formLayout.setItem(17, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem)
                eventActions = QtWidgets.QHBoxLayout()
                eventActions.setContentsMargins(-1, 0, -1, -1)
                eventActions.setObjectName("eventActions")
                spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                                    QtWidgets.QSizePolicy.Policy.Minimum)
                eventActions.addItem(spacerItem1)
                pushToRedact = QtWidgets.QPushButton(parent=containerPet)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(12)
                pushToRedact.setFont(font)
                pushToRedact.setObjectName("pushToRedact")
                eventActions.addWidget(pushToRedact)
                pushButton = QtWidgets.QPushButton(parent=containerPet)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(pushButton.sizePolicy().hasHeightForWidth())
                pushButton.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(12)
                pushButton.setFont(font)
                pushButton.setObjectName("pushButton")
                eventActions.addWidget(pushButton)
                eventActions.setStretch(0, 4)
                eventActions.setStretch(1, 3)
                self.formLayout.setLayout(20, QtWidgets.QFormLayout.ItemRole.FieldRole, eventActions)
                horizontalLayout_7 = QtWidgets.QHBoxLayout()
                horizontalLayout_7.setContentsMargins(-1, 50, -1, -1)
                horizontalLayout_7.setObjectName("horizontalLayout_7")

                setattr(self, f"petPhoto_{i}",QtWidgets.QLabel(parent=containerPet))
                petPhoto = getattr(self, f"petPhoto_{i}")

                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(15)
                petPhoto.setFont(font)
                petPhoto.setText("")
                petPhoto.setPixmap(QtGui.QPixmap("../maket/car.png"))
                petPhoto.setMaximumSize(250,250)

                if check[i][10]!=None and check[i][10]!="":
                    petPhoto.setPixmap(QtGui.QPixmap(check[i][10]))

                petPhoto.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                petPhoto.setObjectName("petPhoto")
                horizontalLayout_7.addWidget(petPhoto)
                petPhotoWayToFile = QtWidgets.QLineEdit(parent=containerPet)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(petPhotoWayToFile.sizePolicy().hasHeightForWidth())
                petPhotoWayToFile.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light SemiCondensed")
                font.setPointSize(14)
                petPhotoWayToFile.setFont(font)
                petPhotoWayToFile.setText("")
                petPhotoWayToFile.setObjectName("petPhotoWayToFile")
                horizontalLayout_7.addWidget(petPhotoWayToFile)
                petPhotoWayToFile.setHidden(True)
                petPhotoChoose = QtWidgets.QPushButton(parent=containerPet)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                   QtWidgets.QSizePolicy.Policy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(petPhotoChoose.sizePolicy().hasHeightForWidth())
                petPhotoChoose.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setFamily("Bahnschrift Light Condensed")
                font.setPointSize(14)
                petPhotoChoose.setFont(font)
                petPhotoChoose.setObjectName("petPhotoChoose")
                horizontalLayout_7.addWidget(petPhotoChoose)
                petPhotoChoose.setHidden(True)
                self.formLayout.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, horizontalLayout_7)
                self.horizontalLayout.addWidget(containerPet)
                spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                                    QtWidgets.QSizePolicy.Policy.Minimum)
                self.horizontalLayout.addItem(spacerItem2)
                self.scrollAreaContainer.addWidget(self.scrollArea)
                self.horizontalLayout_2.addLayout(self.scrollAreaContainer)
                self.horizontalLayout_2.setStretch(0, 2)
                self.horizontalLayout_2.setStretch(1, 5)

                pushButton.setStyleSheet("background-color: #CDA989")
                pushToRedact.setStyleSheet("background-color: #CDA989")

                containerPet.setStyleSheet("""
                                                QWidget#containerPet {
                                               border: 3px solid #CDA989; border-radius: 15px
                                                }
                                                """)
                containerPet.setParent(self.scrollAreaWidgetContents)
                containerPet.setHidden(False)

                descName_L.setStyleSheet("background-color:#CDA989;padding: 5px; border-radius: 15px")
                self.petsPage.setStyleSheet("""
                                                        QPushButton {
                                                        background-color:#CDA989;
                                                    }
                                                            QPushButton:disabled {
                                                                background-color: #B28B77;
                                                                color: black;
                                                            }
                                                        """)
                self.schedPage.setStyleSheet("""
                                                                QPushButton {
                                                                background-color:#CDA989;
                                                            }
                                                                    QPushButton:disabled {
                                                                        background-color: #B28B77;
                                                                        color: black;
                                                                    }
                                                                """)
                self.mainPage.setStyleSheet("""
                                                                QPushButton {
                                                                background-color:#CDA989;
                                                            }
                                                                    QPushButton:disabled {
                                                                        background-color: #B28B77;
                                                                        color: black;
                                                                    }
                                                                """)
                self.cagesPage.setStyleSheet("""
                                                                QPushButton {
                                                                background-color:#CDA989;
                                                            }
                                                                    QPushButton:disabled {
                                                                        background-color: #B28B77;
                                                                        color: black;
                                                                    }
                                                                """)



                _translate = QtCore.QCoreApplication.translate
                petWeightAsEdit.setPlaceholderText(
                    _translate("MainWindow", "Единица измерения (Килограмм, грамм, т.д.)"))
                petsSymptomsEdit.setPlaceholderText(_translate("MainWindow", "Симптомы"))
                petDiagnosisEdit.setPlaceholderText(_translate("MainWindow", "Диагноз(ы)"))
                petNeutered.setText(_translate("MainWindow", "Кастрирован"))
                petNeuteredEdit.setText(_translate("MainWindow", "Кастрирован"))
                petsVacsEdit.setPlaceholderText(_translate("MainWindow", "Прививки"))
                petsMicrochip.setText(_translate("MainWindow", "Микрочип:"))
                petMicrochipEdit.setText(_translate("MainWindow", "Микрочип"))
                petsOwnerEdit.setPlaceholderText(_translate("MainWindow", "Хозяин"))
                petsLiveinEdit.setText(_translate("MainWindow", "Выбрать вольер/клетку"))
                pushToRedact.setText(_translate("MainWindow", "Редактировать"))
                pushButton.setText(_translate("MainWindow", "Удалить"))
                petPhotoWayToFile.setPlaceholderText(_translate("MainWindow", "Путь к изображению"))
                petPhotoChoose.setText(_translate("MainWindow", "Выбрать изображение"))
            else:
                getattr(self,f"containerPet_{i}").setParent(self.scrollAreaWidgetContents)
                getattr(self,f"containerPet_{i}").setHidden(False)

            MainWindow.setCentralWidget(self.centralwidget)




    def EventMenuGui(self):
        self.pushToSearch.setStyleSheet("background-color:#A59B77")
        self.pushToRedactM.setStyleSheet("background-color:#A59B77")
        self.pushToCreateM.setStyleSheet("background-color:#A59B77")
        self.allEventsWidget = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.allEventsWidget.setObjectName("allEventsWidget")
        self.allEventsLO = QtWidgets.QHBoxLayout(self.allEventsWidget)
        self.allEventsLO.setContentsMargins(11, 11, 11, 11)
        self.allEventsLO.setObjectName("allEventsLO")
        self.eventsForDayX = QtWidgets.QVBoxLayout()
        self.eventsForDayX.setContentsMargins(-1, 0, -1, -1)
        self.eventsForDayX.setObjectName("eventsForDayX")
        self.DayX_L = QtWidgets.QLabel(parent=self.allEventsWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(20)
        self.DayX_L.setFont(font)
        self.DayX_L.setStyleSheet("border: 2px solid black")
        self.DayX_L.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.DayX_L.setObjectName("DayX_L")
        self.eventsForDayX.addWidget(self.DayX_L)
        self.eventXdayX = QtWidgets.QWidget(parent=self.allEventsWidget)
        self.eventXdayX.setObjectName("eventXdayX")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.eventXdayX)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Date_eventXdayX = QtWidgets.QLabel(parent=self.eventXdayX)
        self.Date_eventXdayX.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Date_eventXdayX.setObjectName("Date_eventXdayX")
        self.verticalLayout_2.addWidget(self.Date_eventXdayX)
        self.Name_eventXdayX = QtWidgets.QLabel(parent=self.eventXdayX)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Name_eventXdayX.setFont(font)
        self.Name_eventXdayX.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Name_eventXdayX.setObjectName("Name_eventXdayX")
        self.verticalLayout_2.addWidget(self.Name_eventXdayX)
        self.Desc_eventXdayX = QtWidgets.QLabel(parent=self.eventXdayX)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Desc_eventXdayX.setFont(font)
        self.Desc_eventXdayX.setObjectName("Desc_eventXdayX")
        self.verticalLayout_2.addWidget(self.Desc_eventXdayX)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.eventXdayX_buttonrs = QtWidgets.QHBoxLayout()
        self.eventXdayX_buttonrs.setContentsMargins(-1, 0, -1, -1)
        self.eventXdayX_buttonrs.setObjectName("eventXdayX_buttonrs")
        self.todayToDo_eventXdayX = QtWidgets.QPushButton(parent=self.eventXdayX)
        self.todayToDo_eventXdayX.setObjectName("todayToDo_eventXdayX")
        self.eventXdayX_buttonrs.addWidget(self.todayToDo_eventXdayX)
        self.pushToRedact_eventXdayX = QtWidgets.QPushButton(parent=self.eventXdayX)
        self.pushToRedact_eventXdayX.setObjectName("pushToRedact_eventXdayX")
        self.eventXdayX_buttonrs.addWidget(self.pushToRedact_eventXdayX)
        self.todayToCancel_eventXdayX = QtWidgets.QPushButton(parent=self.eventXdayX)
        self.todayToCancel_eventXdayX.setObjectName("todayToCancel_eventXdayX")
        self.eventXdayX_buttonrs.addWidget(self.todayToCancel_eventXdayX)
        self.todayDone_eventXdayX = QtWidgets.QLabel(parent=self.eventXdayX)
        self.todayDone_eventXdayX.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.todayDone_eventXdayX.setObjectName("todayDone_eventXdayX")
        self.eventXdayX_buttonrs.addWidget(self.todayDone_eventXdayX)
        self.verticalLayout_2.addLayout(self.eventXdayX_buttonrs)
        self.eventsForDayX.addWidget(self.eventXdayX)
        self.eventsForDayX.setStretch(0, 1)
        self.eventsForDayX.setStretch(1, 5)
        self.allEventsLO.addLayout(self.eventsForDayX)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.allEventsLO.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.allEventsWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollAreaContainer.addWidget(self.scrollArea)
        self.horizontalLayout_2.addLayout(self.scrollAreaContainer)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)


        MainWindow.setCentralWidget(self.centralwidget)

        self.pushToRedact_eventXdayX.setStyleSheet("background-color:#A59B77")
        self.todayToDo_eventXdayX.setStyleSheet("background-color:#A59B77")
        self.todayToCancel_eventXdayX.setStyleSheet("background-color:#A59B77")
        self.Name_eventXdayX.setStyleSheet("background-color:#A59B77;padding: 5px; border-radius: 15px")
        self.DayX_L.setStyleSheet("background-color:#A59B77;padding: 5px; border-radius: 15px")
        self.petsPage.setStyleSheet("""
                                QPushButton {
                                background-color:#A59B77;
                            }
                                    QPushButton:disabled {
                                        background-color: #958C61;
                                        color: black;
                                    }
                                """)
        self.mainPage.setStyleSheet("""
                                QPushButton {
                                background-color:#A59B77;
                            }
                                    QPushButton:disabled {
                                        background-color: #958C61;
                                        color: black;
                                    }
                                """)
        self.schedPage.setStyleSheet("""
                                QPushButton {
                                background-color:#A59B77;
                            }
                                    QPushButton:disabled {
                                        background-color: #958C61;
                                        color: black;
                                    }
                                """)
        self.cagesPage.setStyleSheet("""
                                QPushButton {
                                background-color:#A59B77;
                            }
                                    QPushButton:disabled {
                                        background-color: #958C61;
                                        color: black;
                                    }
                                """)
        self.eventXdayX.setStyleSheet("""
                        QWidget#eventXdayX {
                       border: 3px solid #A59B77; border-radius: 15px
                        }
                        """)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainPage.setText(_translate("MainWindow", "Главная"))
        self.petsPage.setText(_translate("MainWindow", "Питомцы"))
        self.schedPage.setText(_translate("MainWindow", "Расписание"))
        self.cagesPage.setText(_translate("MainWindow", "Клетки"))
        self.pushToCreateM.setText(_translate("MainWindow", "Добавить"))
        self.pushToRedactM.setText(_translate("MainWindow", "Редактировать"))
        self.pushToSearch.setText(_translate("MainWindow", "Найти"))
        self.DayX_L.setText(_translate("MainWindow", "Сегодня"))
        self.Date_eventXdayX.setText(_translate("MainWindow", "Ежедневное/Дата"))
        self.Name_eventXdayX.setText(_translate("MainWindow", "Название"))
        self.Desc_eventXdayX.setText(_translate("MainWindow", "Описание"))
        self.todayToDo_eventXdayX.setText(_translate("MainWindow", "Сделать"))
        self.pushToRedact_eventXdayX.setText(_translate("MainWindow", "Редактировать"))
        self.todayToCancel_eventXdayX.setText(_translate("MainWindow", "Отменить"))
        self.todayDone_eventXdayX.setText(_translate("MainWindow", "Сделано"))


    def CagesMenuGui(self):
        self.petsPage.setStyleSheet("""
                                                                            QPushButton {
                                                                            background-color:#8DA578;
                                                                        }
                                                                                QPushButton:disabled {
                                                                                    background-color: #64825C;
                                                                                    color: black;
                                                                                }
                                                                            """)
        self.mainPage.setStyleSheet("""
                                                                            QPushButton {
                                                                            background-color:#8DA578;
                                                                        }
                                                                                QPushButton:disabled {
                                                                                    background-color: #64825C;
                                                                                    color: black;
                                                                                }
                                                                            """)
        self.schedPage.setStyleSheet("""
                                                                            QPushButton {
                                                                            background-color:#8DA578;
                                                                        }
                                                                                QPushButton:disabled {
                                                                                    background-color: #64825C;
                                                                                    color: black;
                                                                                }
                                                                            """)
        self.cagesPage.setStyleSheet("""
                                                                            QPushButton {
                                                                            background-color:#8DA578;
                                                                        }
                                                                                QPushButton:disabled {
                                                                                    background-color: #64825C;
                                                                                    color: black;
                                                                                }
                                                                            """)
        self.pushToCreateM.setStyleSheet("background-color:#8DA578")
        self.pushToRedactM.setStyleSheet("background-color:#8DA578")
        self.pushToSearch.setStyleSheet("background-color:#8DA578")

        self.info_order = []

        cur.execute('SELECT * FROM клетки')
        check = cur.fetchall()
        if check==[]: print("Ничего нет")
        else:
            for i in range(len(check)):
                if not hasattr(self,f'containerCage_{i}'):
                    self.info_order.append(check[i][0])
                    setattr(self, f"containerCage_{i}", QtWidgets.QWidget(parent=self.scrollAreaWidgetContents))
                    containerCage = getattr(self, f"containerCage_{i}")
                    containerCage.setObjectName(f"containerCage_{i}")
                    self.formLayout = QtWidgets.QFormLayout(containerCage)
                    self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.RowWrapPolicy.WrapLongRows)
                    self.formLayout.setLabelAlignment(
                        QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
                    self.formLayout.setFormAlignment(
                        QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
                    self.formLayout.setContentsMargins(0, 5, 5, -1)
                    self.formLayout.setSpacing(5)
                    self.formLayout.setObjectName("formLayout")

                    setattr(self, f"cagePhotoLO_{i}", QtWidgets.QHBoxLayout())
                    cagePhotoLO = getattr(self, f"cagePhotoLO_{i}")
                    cagePhotoLO.setContentsMargins(-1, 50, -1, -1)
                    cagePhotoLO.setObjectName(f"cagePhotoLO_{i}")

                    setattr(self, f"spacerphotoL_{i}",
                            QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Expanding,
                                                  QtWidgets.QSizePolicy.Policy.Minimum))
                    spacerphotoL = getattr(self, f"spacerphotoL_{i}")
                    cagePhotoLO.addSpacerItem(spacerphotoL)

                    setattr(self, f"cagePhoto_{i}", QtWidgets.QLabel(parent=containerCage))
                    cagePhoto = getattr(self, f"cagePhoto_{i}")
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(15)
                    cagePhoto.setFont(font)
                    cagePhoto.setText("")
                    cagePhoto.setObjectName(f"cagePhoto_{i}")
                    cagePhotoLO.addWidget(cagePhoto)
                    setattr(self, f"cagePhotoWayToFile_{i}", QtWidgets.QLineEdit(parent=containerCage))
                    cagePhotoWayToFile = getattr(self, f"cagePhotoWayToFile_{i}")
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                       QtWidgets.QSizePolicy.Policy.Preferred)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(cagePhotoWayToFile.sizePolicy().hasHeightForWidth())
                    cagePhotoWayToFile.setSizePolicy(sizePolicy)
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light SemiCondensed")
                    font.setPointSize(14)
                    cagePhotoWayToFile.setFont(font)
                    cagePhotoWayToFile.setText("")
                    cagePhotoWayToFile.setObjectName(f"cagePhotoWayToFile_{i}")
                    cagePhotoWayToFile.setPlaceholderText("Путь к изображению")
                    cagePhotoLO.addWidget(cagePhotoWayToFile)
                    setattr(self, f"cagePhotoChoose_{i}", QtWidgets.QPushButton(parent=containerCage))
                    cagePhotoChoose = getattr(self, f"cagePhotoChoose_{i}")
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                       QtWidgets.QSizePolicy.Policy.Preferred)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(cagePhotoChoose.sizePolicy().hasHeightForWidth())
                    cagePhotoChoose.setSizePolicy(sizePolicy)
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cagePhotoChoose.setFont(font)
                    cagePhotoChoose.setObjectName(f"cagePhotoChoose_{i}")
                    cagePhotoLO.addWidget(cagePhotoChoose)
                    cagePhotoChoose.setText("Выбрать изображение")
                    self.formLayout.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, cagePhotoLO)

                    if check[i][7] != None:
                        cagePhotoWayToFile.setText(check[i][7])
                        cagePhoto.setPixmap(QtGui.QPixmap(check[i][7]))
                        cagePhoto.setMaximumSize(200, 200)
                        cagePhoto.setScaledContents(True)
                    else:
                        cagePhoto.hide()
                        cagePhotoWayToFile.setHidden(True)

                    setattr(self, f"cageNameLO_{i}", QtWidgets.QHBoxLayout())
                    cagePhotoChoose.setHidden(True)
                    cagePhotoWayToFile.hide()
                    cagePhoto.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                    setattr(self, f"spacerphotoR_{i}",
                            QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Expanding,
                                                  QtWidgets.QSizePolicy.Policy.Minimum))
                    spacerphotoR = getattr(self, f"spacerphotoR_{i}")
                    cagePhotoLO.addSpacerItem(spacerphotoL)

                    cageNameLO = getattr(self, f"cageNameLO_{i}")
                    cageNameLO.setContentsMargins(-1, 0, -1, -1)
                    cageNameLO.setObjectName(f"cageNameLO_{i}")
                    setattr(self, f"cageDescName_L_{i}", QtWidgets.QLabel(parent=containerCage))
                    cageDescName_L = getattr(self, f"cageDescName_L_{i}")
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(20)
                    cageDescName_L.setFont(font)
                    cageDescName_L.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    cageDescName_L.setObjectName(f"cageDescName_L_{i}")
                    cageNameLO.addWidget(cageDescName_L)
                    cageDescName_L.setText(check[i][0])
                    setattr(self, f"cageNameEdit_{i}", QtWidgets.QLineEdit(parent=containerCage))
                    cageNameEdit = getattr(self, f"cageNameEdit_{i}")
                    cageNameEdit.setPlaceholderText("Название вольера")
                    cageNameEdit.setText(check[i][0])
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                                       QtWidgets.QSizePolicy.Policy.Preferred)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(cageNameEdit.sizePolicy().hasHeightForWidth())
                    cageNameEdit.setSizePolicy(sizePolicy)
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light SemiCondensed")
                    font.setPointSize(20)
                    cageNameEdit.setFont(font)
                    cageNameEdit.setObjectName(f"cageNameEdit_{i}")
                    cageNameLO.addWidget(cageNameEdit)
                    self.formLayout.setLayout(2, QtWidgets.QFormLayout.ItemRole.FieldRole, cageNameLO)
                    setattr(self, f"cageTypeLO_{i}", QtWidgets.QHBoxLayout())
                    cageTypeLO = getattr(self, f"cageTypeLO_{i}")
                    cageTypeLO.setContentsMargins(-1, 0, -1, -1)
                    cageTypeLO.setObjectName(f"cageTypeLO_{i}")
                    setattr(self, f"cageType_{i}", QtWidgets.QLabel(parent=containerCage))
                    cageType = getattr(self, f"cageType_{i}")
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cageType.setFont(font)
                    cageType.setObjectName(f"cageType_{i}")
                    cageType.setText(("Тип клетки: " + check[i][6]))
                    cageTypeLO.addWidget(cageType)
                    setattr(self, f"cageTypeEdit_{i}", QtWidgets.QComboBox(parent=containerCage))
                    cageTypeEdit = getattr(self, f"cageTypeEdit_{i}")
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                       QtWidgets.QSizePolicy.Policy.Preferred)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(cageTypeEdit.sizePolicy().hasHeightForWidth())
                    cageTypeEdit.setSizePolicy(sizePolicy)
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cageTypeEdit.setFont(font)
                    cageTypeEdit.setObjectName(f"cageTypeEdit_{i}")
                    cageTypeEdit.addItem(check[i][6])
                    cageTypeEdit.setStyleSheet("background-color:#8DA578")

                    cur.execute(f'''SELECT "наименование клетки" FROM "тип клеток"
                                                WHERE "наименование клетки"!={"'" + check[i][6] + "'"} AND "наименование клетки"!={"'" + "Общее" + "'"}''')
                    cagesTypes = cur.fetchall()
                    for x in range(len(cagesTypes)):
                        cageTypeEdit.addItem(cagesTypes[x][0])

                    cageTypeLO.addWidget(cageTypeEdit)
                    self.formLayout.setLayout(3, QtWidgets.QFormLayout.ItemRole.FieldRole, cageTypeLO)
                    setattr(self, f"cagePetsLO_{i}", QtWidgets.QHBoxLayout())
                    cagePetsLO = getattr(self, f"cagePetsLO_{i}")
                    cagePetsLO.setContentsMargins(-1, 0, -1, -1)
                    cagePetsLO.setObjectName(f"cagePetsLO_{i}")

                    setattr(self, f"cagePetsLabels_{i}", QtWidgets.QLabel(parent=containerCage))
                    cagePetsLabels = getattr(self, f"cagePetsLabels_{i}")
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cagePetsLabels.setFont(font)
                    cagePetsLabels.setObjectName(f"cagePetsLabels_{i}")
                    cagePetsLO.addWidget(cagePetsLabels)
                    setattr(self, f"cagePetsChoosen_{i}", QtWidgets.QLabel(parent=containerCage))
                    cagePetsChoosen = getattr(self, f"cagePetsChoosen_{i}")
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cagePetsChoosen.setFont(font)
                    cagePetsChoosen.setObjectName(f"cagePetsChoosen_{i}")
                    cagePetsLO.addWidget(cagePetsChoosen)
                    setattr(self, f"cagePetsEdit_{i}", QtWidgets.QPushButton(parent=containerCage))
                    cagePetsEdit = getattr(self, f"cagePetsEdit_{i}")
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                       QtWidgets.QSizePolicy.Policy.Preferred)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(cagePetsEdit.sizePolicy().hasHeightForWidth())
                    cagePetsEdit.setSizePolicy(sizePolicy)
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cagePetsEdit.setFont(font)
                    cagePetsEdit.setObjectName(f"cagePetsEdit_{i}")
                    cagePetsLO.addWidget(cagePetsEdit)
                    self.formLayout.setLayout(4, QtWidgets.QFormLayout.ItemRole.FieldRole, cagePetsLO)

                    cur.execute(f'''SELECT petid, имя FROM питомцы JOIN "животные к клеткам"
                                                ON питомцы.petid="животные к клеткам"."id животного"
                                                WHERE "животные к клеткам"."название прив клетки"={"'" + check[i][0] + "'"}''')
                    petsToCage = cur.fetchall()
                    if petsToCage != []:
                        anims = ""
                        for x in range(len(petsToCage)):
                            anims = anims + str(petsToCage[x][0]) + " ID " + str(petsToCage[x][1])
                            if x != (len(petsToCage)-1): anims= anims + ","
                        cagePetsLabels.setText("Животные: " + anims)
                        cagePetsChoosen.setText(anims)
                    else:
                        cagePetsLabels.setText("Животные: Нет")
                        cagePetsChoosen.setText("Нет")

                    setattr(self, f"cageLastCleanLO_{i}", QtWidgets.QHBoxLayout())
                    cageLastCleanLO = getattr(self, f"cageLastCleanLO_{i}")
                    cageLastCleanLO.setContentsMargins(-1, 0, -1, -1)
                    cageLastCleanLO.setObjectName(f"cageLastCleanLO_{i}")
                    setattr(self, f"cageLastClean_{i}", QtWidgets.QLabel(parent=containerCage))
                    cageLastClean = getattr(self, f"cageLastClean_{i}")
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cageLastClean.setFont(font)
                    cageLastClean.setObjectName(f"cageLastClean_{i}")
                    cageLastCleanLO.addWidget(cageLastClean)

                    setattr(self, f"cageLastCleanEdit_{i}", QtWidgets.QDateEdit(parent=containerCage))
                    cageLastCleanEdit = getattr(self, f"cageLastCleanEdit_{i}")
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cageLastCleanEdit.setFont(font)
                    cageLastCleanEdit.setObjectName("cageLastCleanEdit")
                    cageLastCleanLO.addWidget(cageLastCleanEdit)

                    if check[i][1] != None:
                        cageLastClean.setText("Дата последней уборки: " + str(check[i][1]))
                        cageLastCleanEdit.setDate(check[i][1])
                    else:
                        cageLastClean.hide()

                    setattr(self, f"cageQuarLO_{i}", QtWidgets.QHBoxLayout())
                    self.formLayout.setLayout((5), QtWidgets.QFormLayout.ItemRole.FieldRole,
                                              cageLastCleanLO)
                    cageQuarLO = getattr(self, f"cageQuarLO_{i}")
                    cageQuarLO.setContentsMargins(-1, 0, -1, -1)
                    cageQuarLO.setObjectName(f"cageQuarLO_{i}")

                    setattr(self, f"cageQuar_{i}", QtWidgets.QLabel(parent=containerCage))
                    cageQuar = getattr(self, f"cageQuar_{i}")
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cageQuar.setFont(font)
                    cageQuar.setObjectName(f"cageQuar_{i}")
                    cageQuarLO.addWidget(cageQuar)

                    setattr(self, f"cageQuarEdit_{i}", QtWidgets.QCheckBox(parent=containerCage))
                    cageQuarEdit = getattr(self, f"cageQuarEdit_{i}")
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                       QtWidgets.QSizePolicy.Policy.Preferred)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(cageQuarEdit.sizePolicy().hasHeightForWidth())
                    cageQuarEdit.setSizePolicy(sizePolicy)
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cageQuarEdit.setFont(font)
                    cageQuarEdit.setObjectName(f"cageQuarEdit_{i}")
                    cageQuarLO.addWidget(cageQuarEdit)

                    if (check[i][2] != None and check[i][2] != False) or check[i][2] == True:
                        cageQuarEdit.setChecked(True)
                    else:
                        cageQuarEdit.setChecked(False)
                        cageQuar.hide()

                    self.formLayout.setLayout(6, QtWidgets.QFormLayout.ItemRole.FieldRole, cageQuarLO)

                    setattr(self, f"cageMoPartLO_{i}", QtWidgets.QHBoxLayout())
                    cageMoPartLO = getattr(self, f"cageMoPartLO_{i}")
                    cageMoPartLO.setContentsMargins(-1, 0, -1, -1)
                    cageMoPartLO.setObjectName(f"cageMoPartLO_{i}")

                    setattr(self, f"cageMoPart_{i}", QtWidgets.QLabel(parent=containerCage))
                    cageMoPart = getattr(self, f"cageMoPart_{i}")
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cageMoPart.setFont(font)
                    cageMoPart.setObjectName(f"cageMoPart_{i}")
                    cageMoPartLO.addWidget(cageMoPart)

                    setattr(self, f"cageMoPartEdit_{i}", QtWidgets.QCheckBox(parent=containerCage))
                    cageMoPartEdit = getattr(self, f"cageMoPartEdit_{i}")
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cageMoPartEdit.setFont(font)
                    cageMoPartEdit.setObjectName(f"cageMoPartEdit_{i}")
                    cageMoPartLO.addWidget(cageMoPartEdit)

                    if check[i][3] == True:
                        cageMoPartEdit.setChecked(True)
                    else:
                        cageMoPartEdit.setChecked(False)
                        cageMoPart.hide()

                    self.formLayout.setLayout((7), QtWidgets.QFormLayout.ItemRole.FieldRole, cageMoPartLO)
                    setattr(self, f"cageInfectLO_{i}", QtWidgets.QHBoxLayout())
                    cageInfectLO = getattr(self, f"cageInfectLO_{i}")
                    cageInfectLO.setContentsMargins(-1, 0, -1, -1)
                    cageInfectLO.setObjectName(f"cageInfectLO_{i}")

                    setattr(self, f"cageInfect_{i}", QtWidgets.QLabel(parent=containerCage))
                    cageInfect = getattr(self, f"cageInfect_{i}")
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cageInfect.setFont(font)
                    cageInfect.setObjectName(f"cageInfect_{i}")
                    cageInfectLO.addWidget(cageInfect)

                    setattr(self, f"cageInfectEdit_{i}", QtWidgets.QCheckBox(parent=containerCage))
                    cageInfectEdit = getattr(self, f"cageInfectEdit_{i}")
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                       QtWidgets.QSizePolicy.Policy.Preferred)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(cageInfectEdit.sizePolicy().hasHeightForWidth())
                    cageInfectEdit.setSizePolicy(sizePolicy)
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cageInfectEdit.setFont(font)
                    cageInfectEdit.setObjectName("cageInfectEdit")
                    cageInfectLO.addWidget(cageInfectEdit)

                    if (check[i][4] != None and check[i][4] != False) or check[i][4] == True:
                        cageInfectEdit.setChecked(True)
                    else:
                        cageInfectEdit.setChecked(False)
                        cageInfect.hide()

                    self.formLayout.setLayout((8), QtWidgets.QFormLayout.ItemRole.FieldRole, cageInfectLO)
                    setattr(self, f"cageSpecialLO_{i}", QtWidgets.QHBoxLayout())
                    cageSpecialLO = getattr(self, f"cageSpecialLO_{i}")
                    cageSpecialLO.setContentsMargins(-1, 0, -1, -1)
                    cageSpecialLO.setObjectName(f"cageSpecialLO_{i}")
                    setattr(self, f"cageSpecial_{i}", QtWidgets.QLabel(parent=containerCage))
                    cageSpecial = getattr(self, f"cageSpecial_{i}")
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cageSpecial.setFont(font)
                    cageSpecial.setObjectName(f"cageSpecial_{i}")
                    cageSpecialLO.addWidget(cageSpecial)

                    setattr(self, f"cageSpecialAll_{i}", QtWidgets.QLabel(parent=containerCage))
                    cageSpecialAll = getattr(self, f"cageSpecialAll_{i}")
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cageSpecialAll.setFont(font)
                    cageSpecialAll.setObjectName(f"cageSpecialAll_{i}")
                    cageSpecialLO.addWidget(cageSpecialAll)

                    setattr(self, f"cageSpecialEdit_{i}", QtWidgets.QPushButton(parent=containerCage))
                    cageSpecialEdit = getattr(self, f"cageSpecialEdit_{i}")
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cageSpecialEdit.setFont(font)
                    cageSpecialEdit.setObjectName(f"cageSpecialEdit_{i}")
                    cageSpecialLO.addWidget(cageSpecialEdit)

                    cur.execute(f'''SELECT "спец тег" FROM "спец теги к клеткам" JOIN клетки
                                                                ON "спец теги к клеткам"."название клетки"=клетки."название клетки"
                                                                WHERE "спец теги к клеткам"."название клетки"={"'" + check[i][0] + "'"}''')
                    specialToCage = cur.fetchall()
                    print(specialToCage)
                    if specialToCage != []:
                        specCage = ""
                        for x in range(len(specialToCage)):
                            specCage = specCage + specialToCage[x][0]
                            if x != len(specialToCage) - 1: specCage = specCage + ","
                        cageSpecial.setText("Особенности: " + specCage)
                        cageSpecialAll.setText(specCage)
                    else:
                        cageSpecial.setText("Особенности: Нет")
                        cageSpecialAll.setText("Особенностей нет")

                    self.formLayout.setLayout((9), QtWidgets.QFormLayout.ItemRole.FieldRole, cageSpecialLO)

                    setattr(self, f"cageNotesLO_{i}", QtWidgets.QHBoxLayout())
                    cageNotesLO = getattr(self, f"cageNotesLO_{i}")
                    cageNotesLO.setContentsMargins(-1, 0, -1, -1)
                    cageNotesLO.setObjectName(f"cageNotesLO_{i}")

                    setattr(self, f"cageNotes_{i}", QtWidgets.QLabel(parent=containerCage))
                    cageNotes = getattr(self, f"cageNotes_{i}")
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(14)
                    cageNotes.setFont(font)
                    cageNotes.setObjectName(f"cageNotes_{i}")
                    cageNotesLO.addWidget(cageNotes)

                    setattr(self, f"cageNotesEdit_{i}", QtWidgets.QLineEdit(parent=containerCage))
                    cageNotesEdit = getattr(self, f"cageNotesEdit_{i}")
                    cageNotesEdit.setFont(font)
                    cageNotesEdit.setObjectName(f"cageNotesEdit_{i}")
                    cageNotesLO.addWidget(cageNotesEdit)

                    if check[i][5] != None or check[i][5] != "":
                        cageNotesEdit.setText(check[i][5])
                        cageNotes.setText("Заметки: " + check[i][5])
                    else:
                        cageNotes.hide()

                    self.formLayout.setLayout((10), QtWidgets.QFormLayout.ItemRole.FieldRole, cageNotesLO)
                    spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Policy.Minimum,
                                                       QtWidgets.QSizePolicy.Policy.Expanding)
                    self.formLayout.setItem((13), QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem)

                    setattr(self, f"cageActionsLO_{i}", QtWidgets.QHBoxLayout())
                    cageActionsLO = getattr(self, f"cageActionsLO_{i}")
                    cageActionsLO.setContentsMargins(-1, 0, -1, -1)
                    cageActionsLO.setObjectName(f"cageActionsLO_{i}")

                    setattr(self, f" spacerItem1_{i}",
                            QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                                  QtWidgets.QSizePolicy.Policy.Minimum))
                    spacerItem1 = getattr(self, f" spacerItem1_{i}")

                    cageActionsLO.addItem(spacerItem1)

                    setattr(self, f"cageActionsRedact_{i}", QtWidgets.QPushButton(parent=containerCage))
                    cageActionsRedact = getattr(self, f"cageActionsRedact_{i}")

                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(12)

                    cageActionsRedact.setFont(font)
                    cageActionsRedact.setObjectName(f"cageActionsRedact_{i}")
                    cageActionsLO.addWidget(cageActionsRedact)

                    setattr(self, f"cageActionsDelete_{i}", QtWidgets.QPushButton(parent=containerCage))
                    cageActionsDelete = getattr(self, f"cageActionsDelete_{i}")

                    self.currentDeleteButtons.append(f"cageActionsDelete_{i}")

                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                                       QtWidgets.QSizePolicy.Policy.Preferred)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(cageActionsDelete.sizePolicy().hasHeightForWidth())
                    cageActionsDelete.setSizePolicy(sizePolicy)
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift Light Condensed")
                    font.setPointSize(12)

                    cageActionsDelete.setFont(font)
                    cageActionsDelete.setObjectName(f"cageActionsDelete_{i}")
                    cageActionsLO.addWidget(cageActionsDelete)
                    cageActionsLO.setStretch(0, 4)
                    cageActionsLO.setStretch(1, 3)
                    self.formLayout.setLayout(16, QtWidgets.QFormLayout.ItemRole.FieldRole, cageActionsLO)
                    self.horizontalLayout.addWidget(containerCage)
                    if len(check) < 3 and i == (len(check) - 1):
                        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                                            QtWidgets.QSizePolicy.Policy.Minimum)
                        self.horizontalLayout.addItem(spacerItem2)

                    self.scrollAreaContainer.addWidget(self.scrollArea)
                    self.horizontalLayout_2.addLayout(self.scrollAreaContainer)
                    self.horizontalLayout_2.setStretch(0, 2)
                    self.horizontalLayout_2.setStretch(1, 5)
                    MainWindow.setCentralWidget(self.centralwidget)

                    cageDescName_L.setStyleSheet("background-color:#8DA578;padding: 5px; border-radius: 15px")
                    cageActionsDelete.setStyleSheet("background-color:#8DA578")
                    cageActionsRedact.setStyleSheet("background-color:#8DA578")
                    containerStyle=f"QWidget#containerCage_{i}"+"{border: 3px solid #8DA578; border-radius: 15px}"
                    containerCage.setStyleSheet(containerStyle)
                    cageNameEdit.setHidden(True)
                    cageNotesEdit.setHidden(True)
                    cageQuarEdit.setHidden(True)
                    cageInfectEdit.setHidden(True)
                    cageLastCleanEdit.setHidden(True)
                    cagePetsEdit.setHidden(True)
                    cageTypeEdit.setHidden(True)
                    cageMoPartEdit.setHidden(True)
                    cageSpecialEdit.setHidden(True)
                    cageSpecialAll.setHidden(True)
                    cagePetsChoosen.hide()

                    cagePhotoChoose.setHidden(True)
                    cagePhotoWayToFile.setHidden(True)
                    cageNameEdit.setHidden(True)

                    cageActionsRedact.clicked.connect(
                        lambda: self.redactInitiate((cageActionsRedact.sender()).objectName()))
                    cagePetsEdit.clicked.connect(
                        lambda: self.specialEdit((cagePetsEdit.sender()).objectName()))
                    cagePhotoChoose.clicked.connect(self.open_file_dialog)

                    self.currentRedactButtons.append(f"cageActionsRedact_{i}")

                    cageNotesEdit.setPlaceholderText("Заметки")
                    cagePetsEdit.setText("Выбрать животных")
                    cageQuar.setText("Карантинный")
                    cageQuarEdit.setText("Карантинный")
                    cageMoPart.setText("Часть модуля")
                    cageMoPartEdit.setText("Часть модуля")
                    cageInfect.setText("Инфекционный")
                    cageInfectEdit.setText("Инфекционный")
                    # cageSpecial.setText("Особенности:")
                    # cageSpecialAll.setText("Список особенностей")
                    cageSpecialEdit.setText("Выбрать особенности")
                    cageActionsRedact.setText("Редактировать")
                    cageActionsDelete.setText("Удалить")

                (getattr(self,f'containerCage_{i}')).setParent(self.scrollAreaWidgetContents)
                getattr(self, f'containerCage_{i}').setHidden(False)

    #Функции окна списка

    def doneChoosing(self,button):
        cageName = getattr(self, f"cageDescName_L_{self.containerNum}").text()
        if self.dialog.ui.treeWidget.selectedItems()!=[]:
            allItems=self.dialog.ui.treeWidget.selectedItems()
            self.ItemsPK=[]
            for i in range(len(allItems)):
                item=allItems[i].text(0)
                if item!=" ":
                    if self.currentList=="PetsToCages": collumnNum=3
                    for j in range(len(allItems)):
                        if (item[collumnNum+j]).isdigit and (item[collumnNum+j])!=" ":
                            self.ItemsPK.append(item[collumnNum+j])
                            print("ItemsPK")
                            print(self.ItemsPK)
                        else: break
            for i in range(len(self.ItemsPK)):  # Проверка, есть ли у животных привязка к другой клетке
                cur.execute(
                    'SELECT "название прив клетки", "id животного" '
                    'FROM "животные к клеткам" '
                    'WHERE "id животного" = %s AND "название прив клетки" != %s',
                    (self.ItemsPK[i], cageName)
                )
                if cur.fetchall() != []:
                    self.show_error("К этому животному уже прикреплена другая клетка!")
                    return
        self.saveListChangesToEdit(button)

    def saveListChangesToEdit(self,button_name):
        if self.currentList == "PetsToCages":
            textChange = getattr(self, f"cagePetsChoosen_{self.containerNum}").setText("Нет")
            textChange = getattr(self, f"cagePetsLabels_{self.containerNum}").setText("Животные: Нет")
            cageName = getattr(self, f"cageDescName_L_{self.containerNum}").text()
            print(self.dialog.ui.treeWidget.selectedItems())
            if self.dialog.ui.treeWidget.selectedItems()==[]:
                print(1)
                #petsToCage = cur.fetchall()
            else:
                anims = ""
                for i in range(len(self.ItemsPK)):
                    # Проверить существует ли запись
                    #cur.execute(
                    #    'SELECT "название прив клетки", "id животного" '
                    #    'FROM "животные к клеткам" '
                    #    'WHERE "название прив клетки" = %s AND "id животного" = %s',
                    #    (cageName, self.ItemsPK[i])
                    #)
                    #petsToCage = cur.fetchall()
                    cur.execute(f'''SELECT petid, имя FROM питомцы WHERE petid={"'" + self.ItemsPK[i] + "'"}''')
                    pets = cur.fetchall()
                    for x in range(len(pets)):
                        anims = anims + str(pets[x][0]) + " ID " + str(pets[x][1])
                        if i == (len(self.ItemsPK[i]) - 1) and len(self.ItemsPK)>1:
                            anims=anims + ","
                    #if petsToCage == []:
                    #    cur.execute(
                    #    'SELECT "название прив клетки", "id животного" '
                    #    'FROM "животные к клеткам" '
                    #    'WHERE "название прив клетки" = %s AND "id животного" = %s',
                    #    (cageName, self.ItemsPK[i])
                    #)

                    textChange = getattr(self, f"cagePetsChoosen_{self.containerNum}").setText(anims)
                    textChange = getattr(self, f"cagePetsLabels_{self.containerNum}").setText("Животные: " + anims)
                    self.dialog.done(0)

    #Общие функции

    def open_file_dialog(self):
        #options = QtWidgets.QFileDialog.Options
        file_path= QtWidgets.QFileDialog
        choosenpath= file_path.getOpenFileName(
            self.scrollAreaWidgetContents,
            "Выберите файл",
            "",
            "Изображения (*.png *.jpg *.jpeg *.bmp *.gif);;Все файлы (*)"
            #options=options,
        )
        if file_path: choosenpath=choosenpath[0]
        else: choosenpath=""

        if self.currentMenu==3:
            getattr(self,f"cagePhotoWayToFile_{self.containerNum}").setText(str(choosenpath))
            getattr(self, f"cagePhoto_{self.containerNum}").setPixmap(QtGui.QPixmap(str(choosenpath)))


    def show_error(self,error_message):
        # Создаем и показываем модальное сообщение об ошибке
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg.setWindowTitle("Ошибка")
        msg.setText("Ошибка выполнения операции")
        msg.setInformativeText(error_message)
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

    def request_permission(self,message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg.setWindowTitle("")
        msg.setText("Подтвердить операцию")
        msg.setInformativeText(message)
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
        result=msg.exec()
        return result == QtWidgets.QMessageBox.StandardButton.Yes

    def redactInitiate(self,buttonName):
        self.containerNum=''
        preRevContainerNum=''
        for x in reversed(buttonName):
            if x.isdigit()==False:
                break
            else: preRevContainerNum=preRevContainerNum+x
        for x in reversed(preRevContainerNum):
            self.containerNum=self.containerNum+x
        if self.currentMenu==3:
            #Аминь
            print(self.containerNum)
            for i in ["cagePhoto_","cageDescName_L_","cagePetsLabels_","cageLastClean_","cageQuar_","cageMoPart_",
                      "cageInfect_","cageSpecial_"]:
                widgetName=i+self.containerNum
                hideWidget=getattr(self,f'{widgetName}')
                hideWidget.setHidden(True)
            getattr(self,f"cageType_{self.containerNum}").setText("Тип клетки")
            getattr(self, f"cageNotes_{self.containerNum}").setText("Заметки")
            for i in ["cagePhotoWayToFile_","cagePhotoChoose_","cageNameEdit_","cageTypeEdit_","cagePetsEdit_","cageLastCleanEdit_",
                      "cageQuarEdit_","cageMoPartEdit_","cageInfectEdit_","cageSpecialAll_","cageSpecialEdit_","cagePetsChoosen_","cageNotesEdit_"]:
                showWidget=getattr(self,f'{i}{self.containerNum}')
                showWidget.setHidden(False)
        for i in self.currentRedactButtons:
            if i!=buttonName: getattr(self,i).setEnabled(False)
            else:
                getattr(self,buttonName).setText("Готово")
                getattr(self,f'cageActionsDelete_{self.containerNum}').setText("Отменить изменения")
                try:
                    getattr(self,buttonName).clicked.disconnect()
                    getattr(self, buttonName).clicked.connect(
                        lambda: self.saveChangesToDB(self.containerNum))
                    getattr(self, f'cageActionsDelete_{self.containerNum}').disconnect()
                    print("Кнопки отключены!")
                except Exception:
                    print("Кнопки не были отключены")
                    pass

    def specialEdit(self,buttonName):
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose, True)

        if "cagePetsEdit" in buttonName:
            self.dialog.ui.fillInfo("Животные")
            self.currentList = "PetsToCages"
        else:
            print("aww")
        print(buttonName)
        self.dialog.ui.pushButton_2.clicked.connect(
            lambda: self.doneChoosing(buttonName))
        self.dialog.exec()
    def saveChangesToDB(self, num):
        if self.currentMenu==3:

            #Проверить остались ли привязанные записи при переименовании
            prevName=getattr(self,f'cageDescName_L_{num}').text()
            cur.execute(f'SELECT * FROM "животные к клеткам" WHERE "название прив клетки"={"'"+prevName+"'"}')
            check1=cur.fetchall()
            cur.execute(f'SELECT * FROM "спец теги к клеткам" WHERE "название клетки"={"'" + prevName + "'"}')
            check2=cur.fetchall()
            if (check1!=[] or check2!=[]) and prevName!=getattr(self,f'cageNameEdit_{num}').text():
                self.show_error("К данной клетке ещё привязаны теги или животные, отсоедените все связанные данные перед перименованием!")
                return

            # Подготовка к сохранению данных

            cur.execute(f'SELECT "тип клетки" FROM "спец теги к клеткам" JOIN "спец теги" ON "спец теги к клеткам"."спец тег"="спец теги"."спец тег" WHERE "спец теги к клеткам"."название клетки"={"'" + prevName + "'"}')
            info=cur.fetchall()
            if info!=[]:
                for i in range(len(info)):
                    if info[i][0]!=getattr(self,f"cageTypeEdit_{num}").currentText() and info[i][0]!="Общее":
                        self.show_error("Выбраныне спец теги не подходят этому типу клеток")
                        return

            allchecks = []
            for x in [f"cageQuarEdit_{num}", f"cageMoPartEdit_{num}", f"cageInfectEdit_{num}"]:
                allchecks.append(getattr(self, x).isChecked())

            linked_anims=(getattr(self, f"cagePetsChoosen_{self.containerNum}").text()).split(',')
            print(linked_anims, "nen")
            cur.execute(f'SELECT * FROM "животные к клеткам" WHERE "название прив клетки"={"'" + getattr(self,f'cageNameEdit_{num}').text() + "'"}')
            check_anim=cur.fetchall()
            animIds=[]
            if (check_anim!=[] or linked_anims!=[]) and linked_anims[0]!="Нет":
                for x in range(len(linked_anims)):
                    add_an = ""
                    for y in linked_anims[x]:
                        if y.isdigit() != False: add_an = add_an + y
                    animIds.append(int(add_an))


            #Сохранение данных

            try:
                cur.execute(
                    f'UPDATE клетки SET "путь к фото"={"'" + getattr(self, f"cagePhotoWayToFile_{num}").text() + "'"} WHERE "название клетки"={"'" + getattr(self, f'cageNameEdit_{num}').text() + "'"}')
                conn.commit()
            except Exception:
                self.show_error("Что-то пошло не так при изменении типа клеток, проверьте верность данных")
                return

            if prevName != getattr(self, f'cageNameEdit_{num}').text():
                try:
                    cur.execute(
                        f'UPDATE "клетки" SET "название клетки" = {"'" + getattr(self, f'cageNameEdit_{num}').text() + "'"} WHERE "название клетки"={"'" + prevName + "'"}')
                    conn.commit()
                except Exception:
                    self.show_error("Что-то пошло не так при переименовании клетки. Проверьте верность данных")
                    return

            try:
                cur.execute(
                    f'UPDATE клетки SET "тип клетки"={"'" + getattr(self, f"cageTypeEdit_{num}").currentText() + "'"} WHERE "название клетки"={"'" + getattr(self, f'cageNameEdit_{num}').text() + "'"}')
                conn.commit()
            except Exception:
                self.show_error("Что-то пошло не так при изменении типа клеток, проверьте верность данных")
                return


            if linked_anims[0]=="Нет" and check_anim!=[]:
                if not self.request_permission("Вы уверены, что хотите удалить все связи?"):
                    pass
                else:
                    try:
                        cur.execute(f'DELETE FROM "животные к клеткам" WHERE "название прив клетки"={"'" + getattr(self, f'cageNameEdit_{num}').text() + "'"}')
                        conn.commit()
                        textChange = getattr(self, f"cagePetsChoosen_{self.containerNum}").setText("Нет")
                        textChange = getattr(self, f"cagePetsLabels_{self.containerNum}").setText("Животные: Нет")
                    except Exception:
                        self.show_error("Что-то пошло не так при удалении связей, проверьте верность данных")
                        return
            elif linked_anims!="Нет":
                print("ровалились")
                print(animIds)
                for i in range(len(animIds)):
                    newPK = random.randint(0, 999999)
                    cur.execute(
                        f'INSERT INTO "животные к клеткам"("id привязка животные к клеткам", "id животного", "название прив клетки") VALUES({newPK}, {animIds[i]}, {"'" + getattr(self, f'cageNameEdit_{num}').text() + "'"});')
                    conn.commit()
            elif check_anim!=[]:
                check_anim_ids=[]
                for i in range(len(check_anim)):
                    check_anim_ids.append(check_anim[i][1])
                toAdd=list(set(animIds)-set(check_anim_ids))
                if toAdd!=[]:
                    for i in range(len(toAdd)):
                        newPK=random.randint(0,999999)
                        cur.execute(
                            f'INSERT INTO "животные к клеткам"("id привязка животные к клеткам", "id животного", "название прив клетки") VALUES({newPK}, {toAdd[i]}, {"'" + getattr(self, f'cageNameEdit_{num}').text() + "'"});')
                        conn.commit()
                toDelete=list(set(check_anim_ids)-set(animIds))
                if toDelete!=[]:
                    for i in range(len(toDelete)):
                        cur.execute(f'DELETE FROM "животные к клеткам" WHERE "id животного"={toDelete[i]};')
                        conn.commit()
            else: print("черти")


            try:
                cur.execute(
                    f'UPDATE клетки SET "дата последней уборки"={"'" + str(getattr(self, f'cageLastCleanEdit_{num}').date().toPyDate()) + "'"} WHERE "название клетки"={"'" + getattr(self, f'cageNameEdit_{num}').text() + "'"}')
                conn.commit()
            except Exception:
                self.show_error("Что-то пошло не так при изменении даты, проверьте верность данных")
                return

            try:
                cur.execute(
                    f'UPDATE public.клетки SET карантийный={allchecks[0]}, "часть модуля"={allchecks[1]}, инфекционный={allchecks[2]} WHERE "название клетки"={"'" + getattr(self, f'cageNameEdit_{num}').text() + "'"}')
                conn.commit()
            except Exception:
                self.show_error("Что-то пошло не так при установке параметров, попробуйте ещё раз")
                return

            try:
                cur.execute(
                    f'UPDATE public.клетки SET заметки={"'" + getattr(self, f'cageNotesEdit_{num}').text() + "'"} WHERE "название клетки"={"'" + getattr(self, f'cageNameEdit_{num}').text() + "'"}')
                conn.commit()
            except Exception:
                self.show_error("Что-то пошло не так при установке параметров, попробуйте ещё раз")
                return

            self.updateMenu("клетки",num)

    def updateMenu(self, currentList, button_name):
        cur.execute(f'SELECT * FROM "{currentList}"')
        check = cur.fetchall()
        if self.currentMenu == 3:
            self.currentDeleteButtons = []
            numofContainers = 0
            immediate_children = self.scrollAreaWidgetContents.findChildren(QtCore.QObject,
                                                                            options=QtCore.Qt.FindChildOption.FindDirectChildrenOnly)
            for j in immediate_children:
                if j.objectName() != "horizontalLayout" and j.objectName() != "horizontalSpacer_2": numofContainers += 1
            if len(check) > numofContainers:
                print("more needed")
            elif len(check) < numofContainers:
                print("need to hide")
            else:
                for i in range(len(check)):
                    if check == []:
                        print("Ничего нет")
                    else:
                        for i in range(len(check)):
                            if hasattr(self, f'containerCage_{i}'):
                                containerCage = getattr(self, f"containerCage_{i}")
                                cagePhotoLO = getattr(self, f"cagePhotoLO_{i}")
                                spacerphotoL = getattr(self, f"spacerphotoL_{i}")
                                cagePhoto = getattr(self, f"cagePhoto_{i}")
                                cagePhotoWayToFile = getattr(self, f"cagePhotoWayToFile_{i}")
                                cagePhotoChoose = getattr(self, f"cagePhotoChoose_{i}")

                                if check[i][7] != None:
                                    cagePhotoWayToFile.setText(check[i][7])
                                    cagePhoto.setPixmap(QtGui.QPixmap(check[i][7]))
                                    cagePhoto.setMaximumSize(200, 200)
                                    cagePhoto.setScaledContents(True)
                                else:
                                    cagePhoto.hide()
                                    cagePhotoWayToFile.setHidden(True)

                                cagePhotoChoose.setHidden(True)
                                cagePhotoWayToFile.hide()

                                spacerphotoR = getattr(self, f"spacerphotoR_{i}")
                                cageNameLO = getattr(self, f"cageNameLO_{i}")

                                cageDescName_L = getattr(self, f"cageDescName_L_{i}")
                                cageDescName_L.setText(check[i][0])

                                cageNameEdit = getattr(self, f"cageNameEdit_{i}")
                                cageNameEdit.setPlaceholderText("Название вольера")
                                cageNameEdit.setText(check[i][0])
                                cageTypeLO = getattr(self, f"cageTypeLO_{i}")

                                cageType = getattr(self, f"cageType_{i}")

                                cageType.setText(("Тип клетки: " + check[i][6]))

                                cageTypeEdit = getattr(self, f"cageTypeEdit_{i}")
                                cageTypeEdit.addItem(check[i][6])

                                cur.execute(f'''SELECT "наименование клетки" FROM "тип клеток"
                                                               WHERE "наименование клетки"!={"'" + check[i][6] + "'"} AND "наименование клетки"!={"'" + "Общее" + "'"}''')
                                cagesTypes = cur.fetchall()
                                for x in range(len(cagesTypes)):
                                    cageTypeEdit.addItem(cagesTypes[x][0])

                                cagePetsLO = getattr(self, f"cagePetsLO_{i}")

                                cagePetsLabels = getattr(self, f"cagePetsLabels_{i}")

                                cagePetsChoosen = getattr(self, f"cagePetsChoosen_{i}")

                                cagePetsEdit = getattr(self, f"cagePetsEdit_{i}")

                                cur.execute(f'''SELECT petid, имя FROM питомцы JOIN "животные к клеткам"
                                                               ON питомцы.petid="животные к клеткам"."id животного"
                                                               WHERE "животные к клеткам"."название прив клетки"={"'" + check[i][0] + "'"}''')
                                petsToCage = cur.fetchall()
                                if petsToCage != []:
                                    anims = ""
                                    for x in range(len(petsToCage)):
                                        anims = anims + str(petsToCage[x][0]) + " ID " + str(petsToCage[x][1])
                                        if x != (len(petsToCage) - 1): anims = anims + ","
                                    cagePetsLabels.setText("Животные: " + anims)
                                    cagePetsChoosen.setText(anims)
                                else:
                                    cagePetsLabels.setText("Животные: Нет")
                                    cagePetsChoosen.setText("Нет")

                                cageLastCleanLO = getattr(self, f"cageLastCleanLO_{i}")

                                cageLastClean = getattr(self, f"cageLastClean_{i}")

                                cageLastCleanEdit = getattr(self, f"cageLastCleanEdit_{i}")

                                if check[i][1] != None:
                                    cageLastClean.setText("Дата последней уборки: " + str(check[i][1]))
                                    cageLastCleanEdit.setDate(check[i][1])
                                else:
                                    cageLastClean.hide()

                                cageQuarLO = getattr(self, f"cageQuarLO_{i}")

                                cageQuar = getattr(self, f"cageQuar_{i}")

                                cageQuarEdit = getattr(self, f"cageQuarEdit_{i}")

                                if (check[i][2] != None and check[i][2] != False) or check[i][2] == True:
                                    cageQuarEdit.setChecked(True)
                                    cageQuar.show()
                                else:
                                    cageQuarEdit.setChecked(False)
                                    cageQuar.hide()

                                cageMoPartLO = getattr(self, f"cageMoPartLO_{i}")

                                cageMoPart = getattr(self, f"cageMoPart_{i}")

                                cageMoPartEdit = getattr(self, f"cageMoPartEdit_{i}")

                                if check[i][3] == True:
                                    cageMoPartEdit.setChecked(True)
                                    cageMoPart.show()
                                else:
                                    cageMoPartEdit.setChecked(False)
                                    cageMoPart.hide()

                                cageInfectLO = getattr(self, f"cageInfectLO_{i}")

                                cageInfect = getattr(self, f"cageInfect_{i}")

                                cageInfectEdit = getattr(self, f"cageInfectEdit_{i}")

                                if (check[i][4] != None and check[i][4] != False) or check[i][4] == True:
                                    cageInfectEdit.setChecked(True)
                                    cageInfect.show()
                                else:
                                    cageInfectEdit.setChecked(False)
                                    cageInfect.hide()

                                cageSpecialLO = getattr(self, f"cageSpecialLO_{i}")

                                cageSpecial = getattr(self, f"cageSpecial_{i}")

                                cageSpecialAll = getattr(self, f"cageSpecialAll_{i}")

                                cageSpecialEdit = getattr(self, f"cageSpecialEdit_{i}")

                                cur.execute(f'''SELECT "спец тег" FROM "спец теги к клеткам" JOIN клетки
                                                                               ON "спец теги к клеткам"."название клетки"=клетки."название клетки"
                                                                               WHERE "спец теги к клеткам"."название клетки"={"'" + check[i][0] + "'"}''')
                                specialToCage = cur.fetchall()
                                if specialToCage != []:
                                    specCage = ""
                                    for x in range(len(specialToCage)):
                                        specCage = specCage + specialToCage[x][0]
                                        if x != len(specialToCage) - 1: specCage = specCage + ","
                                    cageSpecial.setText("Особенности: " + specCage)
                                    cageSpecialAll.setText(specCage)
                                else:
                                    cageSpecial.setText("Особенности: Нет")
                                    cageSpecialAll.setText("Особенностей нет")

                                cageNotesLO = getattr(self, f"cageNotesLO_{i}")

                                cageNotes = getattr(self, f"cageNotes_{i}")

                                cageNotesEdit = getattr(self, f"cageNotesEdit_{i}")

                                if check[i][5] != None or check[i][5] != "":
                                    cageNotesEdit.setText(check[i][5])
                                    cageNotes.setText("Заметки: " + check[i][5])
                                    cageNotes.show()
                                else:
                                    cageNotes.hide()

                                cageActionsLO = getattr(self, f"cageActionsLO_{i}")

                                spacerItem1 = getattr(self, f" spacerItem1_{i}")

                                cageActionsRedact = getattr(self, f"cageActionsRedact_{i}")

                                cageActionsDelete = getattr(self, f"cageActionsDelete_{i}")

                                self.currentDeleteButtons.append(f"cageActionsDelete_{i}")
                                if len(check) < 3 and i == (len(check) - 1):
                                    spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                                                        QtWidgets.QSizePolicy.Policy.Minimum)
                                    self.horizontalLayout.addItem(spacerItem2)

                                cageDescName_L.setStyleSheet(
                                    "background-color:#8DA578;padding: 5px; border-radius: 15px")
                                cageActionsDelete.setStyleSheet("background-color:#8DA578")
                                cageActionsRedact.setStyleSheet("background-color:#8DA578")
                                containerStyle = f"QWidget#containerCage_{i}" + "{border: 3px solid #8DA578; border-radius: 15px}"
                                containerCage.setStyleSheet(containerStyle)
                                cageNameEdit.setHidden(True)
                                cageNotesEdit.setHidden(True)
                                cageQuarEdit.setHidden(True)
                                cageInfectEdit.setHidden(True)
                                cageLastCleanEdit.setHidden(True)
                                cagePetsEdit.setHidden(True)
                                cageTypeEdit.setHidden(True)
                                cageMoPartEdit.setHidden(True)
                                cageSpecialEdit.setHidden(True)
                                cageSpecialAll.setHidden(True)
                                cagePetsChoosen.hide()

                                cagePhotoChoose.setHidden(True)
                                cagePhotoWayToFile.setHidden(True)
                                cageNameEdit.setHidden(True)

                                cageActionsRedact.clicked.disconnect()
                                cagePetsEdit.clicked.disconnect()
                                cagePhotoChoose.clicked.disconnect()

                                cageActionsRedact.clicked.connect(
                                    lambda: self.redactInitiate((cageActionsRedact.sender()).objectName()))
                                cagePetsEdit.clicked.connect(
                                    lambda: self.specialEdit((cagePetsEdit.sender()).objectName()))
                                cagePhotoChoose.clicked.connect(self.open_file_dialog)

                                self.currentRedactButtons.append(f"cageActionsRedact_{i}")

                                cageNotesEdit.setPlaceholderText("Заметки")
                                cagePetsEdit.setText("Выбрать животных")
                                cageQuar.setText("Карантинный")
                                cageQuarEdit.setText("Карантинный")
                                cageMoPart.setText("Часть модуля")
                                cageMoPartEdit.setText("Часть модуля")
                                cageInfect.setText("Инфекционный")
                                cageInfectEdit.setText("Инфекционный")
                                # cageSpecial.setText("Особенности:")
                                # cageSpecialAll.setText("Список особенностей")
                                cageSpecialEdit.setText("Выбрать особенности")
                                cageActionsRedact.setText("Редактировать")
                                cageActionsDelete.setText("Удалить")

                                for j in ["cagePhoto_", "cageDescName_L_", "cagePetsLabels_", "cageLastClean_",
                                          "cageQuar_", "cageMoPart_",
                                          "cageInfect_", "cageSpecial_"]:
                                    widgetName = j + str(i)
                                    showWidget = getattr(self, f'{widgetName}')
                                    showWidget.setHidden(False)
                                getattr(self, f"cageType_{i}").setText("Тип клетки")
                                getattr(self, f"cageNotes_{i}").setText("Заметки")
                                for j in ["cagePhotoWayToFile_", "cagePhotoChoose_", "cageNameEdit_", "cageTypeEdit_",
                                          "cagePetsEdit_", "cageLastCleanEdit_",
                                          "cageQuarEdit_", "cageMoPartEdit_", "cageInfectEdit_", "cageSpecialAll_",
                                          "cageSpecialEdit_", "cagePetsChoosen_", "cageNotesEdit_"]:
                                    widgetName = j + str(i)
                                    hideWidget = getattr(self, f'{widgetName}')
                                    hideWidget.setHidden(True)

                            (getattr(self, f'containerCage_{i}')).setParent(self.scrollAreaWidgetContents)
                            getattr(self, f'containerCage_{i}').setHidden(False)


    def hideOldWidgets(self):
        print(1)

    def cancelChanges(self):
        print(1)

    def setMenu0(self):
        self.currentMenu=0
        self.enablingButtons()
        self.mainPage.setDisabled(True)
        self.switchMenu()
        self.mainMenuGui()

    def setMenu1(self):
        self.currentMenu = 1
        self.enablingButtons()
        self.petsPage.setDisabled(True)
        self.switchMenu()
        self.petsMenuGui()

    def setMenu2(self):
        self.currentMenu = 2 #Event
        self.enablingButtons()
        self.schedPage.setDisabled(True)
        self.switchMenu()
        self.EventMenuGui()

    def setMenu3(self):
        self.currentMenu = 3  # Клетки
        self.enablingButtons()
        self.cagesPage.setDisabled(True)
        self.switchMenu()
        self.CagesMenuGui()

    def hideEverything(self):
        if hasattr(self, f'containerPet_{0}'):
            cur.execute('SELECT * FROM питомцы')
            needToBeDeleted = len(cur.fetchall())
            for i in range(needToBeDeleted):
                getattr(self, f"containerPet_{i}").setParent(None)
                getattr(self, f"containerPet_{i}").setHidden(True)
        if hasattr(self, 'mainVertWidget'):
            for i in reversed(range(self.horizontalLayout.count())):
                item = self.horizontalLayout.itemAt(i)
                if isinstance(item, QtWidgets.QSpacerItem):
                    self.horizontalLayout.takeAt(i)
            getattr(self, "mainVertWidget").setParent(None)
            getattr(self, "mainVertWidget").hide()
            getattr(self, "spacerItem")
            print(2)
        if hasattr(self, f"containerCage_{0}"):
            print(3)
            cur.execute('SELECT * FROM клетки')
            needToBeDeleted = len(cur.fetchall())
            for i in range(needToBeDeleted):
                getattr(self, f"containerCage_{i}").setParent(None)
                getattr(self, f"containerCage_{i}").setHidden(True)
        if hasattr(self,"allEventsWidget"):
            print("GAAAH")
            for i in reversed(range(self.allEventsLO.count())):
                item = self.allEventsLO.itemAt(i)
                if isinstance(item, QtWidgets.QSpacerItem):
                    self.allEventsLO.takeAt(i)
                    print(i)
            self.allEventsWidget.setParent(None)
            self.allEventsWidget.hide()




    def switchMenu(self):
        self.currentDeleteButtons=[]
        self.currentRedactButtons=[]
        self.hideEverything()

        #Создание scrollArea заново

    def enablingButtons(self):
        if self.currentMenu==0:
            self.petsPage.setEnabled(True)
            self.cagesPage.setEnabled(True)
            self.schedPage.setEnabled(True)
        elif self.currentMenu==1:
            self.mainPage.setEnabled(True)
            self.cagesPage.setEnabled(True)
            self.schedPage.setEnabled(True)
        elif self.currentMenu==2:
            self.petsPage.setEnabled(True)
            self.mainPage.setEnabled(True)
            self.cagesPage.setEnabled(True)
        else:
            self.mainPage.setEnabled(True)
            self.petsPage.setEnabled(True)
            self.schedPage.setEnabled(True)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainPage.setText(_translate("MainWindow", "Главная"))
        self.petsPage.setText(_translate("MainWindow", "Питомцы"))
        self.schedPage.setText(_translate("MainWindow", "Расписание"))
        self.cagesPage.setText(_translate("MainWindow", "Клетки"))
        self.pushToCreateM.setText(_translate("MainWindow", "Добавить"))
        self.pushToRedactM.setText(_translate("MainWindow", "Редактировать"))
        self.pushToSearch.setText(_translate("MainWindow", "Найти"))


if __name__ == "__main__":
    import sys
    import faulthandler
    faulthandler.enable()
    faulthandler.dump_traceback()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()
    sys.exit()