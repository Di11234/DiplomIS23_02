from PyQt6 import QtCore, QtGui, QtWidgets
import psycopg,sys
global currentMenu

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
            self.mainVertWidget = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
            self.mainVertWidget.setObjectName("mainVertWidget")
            self.mainVertLayout = QtWidgets.QVBoxLayout(self.mainVertWidget)
            self.mainVertLayout.setContentsMargins(11, 11, 11, 11)
            self.mainVertLayout.setObjectName("mainVertLayout")
            self.mainToday_L = QtWidgets.QLabel(parent=self.mainVertWidget)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(20)
            self.mainToday_L.setFont(font)
            self.mainToday_L.setStyleSheet("background-color:#64898F;padding: 5px; border-radius: 15px")
            self.mainToday_L.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.mainToday_L.setObjectName("mainToday_L")
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                               QtWidgets.QSizePolicy.Policy.MinimumExpanding)
            sizePolicy.setHorizontalStretch(50)
            sizePolicy.setVerticalStretch(50)
            sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
            self.mainToday_L.setSizePolicy(sizePolicy)
            self.mainVertLayout.addWidget(self.mainToday_L)
            self.todayContainer = QtWidgets.QHBoxLayout()
            self.todayContainer.setObjectName("todayContainer")
            self.eventTodayNumX = QtWidgets.QWidget(parent=self.mainVertWidget)
            # self.eventTodayNumX.setStyleSheet("border: 3px solid #64898F; border-radius: 15px")
            self.eventTodayNumX.setStyleSheet("""
                    QWidget#eventTodayNumX {
                   border: 3px solid #64898F; border-radius: 15px
                    }
                    """)
            self.eventTodayNumX.setObjectName("eventTodayNumX")
            self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.eventTodayNumX)
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.todayDateX = QtWidgets.QLabel(parent=self.eventTodayNumX)
            self.todayDateX.setAlignment(
                QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.todayDateX.setObjectName("todayDateX")
            self.verticalLayout_2.addWidget(self.todayDateX)
            self.todayNameX = QtWidgets.QLabel(parent=self.eventTodayNumX)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.todayNameX.setFont(font)
            self.todayNameX.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.todayNameX.setObjectName("todayNameX")
            self.verticalLayout_2.addWidget(self.todayNameX)
            self.todayDescX = QtWidgets.QLabel(parent=self.eventTodayNumX)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(18)
            self.todayDescX.setFont(font)
            self.todayDescX.setObjectName("todayDescX")
            self.verticalLayout_2.addWidget(self.todayDescX)
            spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                               QtWidgets.QSizePolicy.Policy.Minimum)
            self.verticalLayout_2.addItem(spacerItem)
            self.buttonsSchedMenuX = QtWidgets.QHBoxLayout()
            self.buttonsSchedMenuX.setContentsMargins(-1, 0, -1, -1)
            self.buttonsSchedMenuX.setObjectName("buttonsSchedMenuX")
            self.todayToDoX = QtWidgets.QPushButton(parent=self.eventTodayNumX)
            self.todayToDoX.setObjectName("todayToDoX")
            self.buttonsSchedMenuX.addWidget(self.todayToDoX)
            self.todayToCancelX = QtWidgets.QPushButton(parent=self.eventTodayNumX)
            self.todayToCancelX.setObjectName("todayToCancelX")
            self.buttonsSchedMenuX.addWidget(self.todayToCancelX)
            self.todayDoneX = QtWidgets.QLabel(parent=self.eventTodayNumX)
            self.todayDoneX.setAlignment(
                QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.todayDoneX.setObjectName("todayDoneX")
            self.buttonsSchedMenuX.addWidget(self.todayDoneX)
            self.verticalLayout_2.addLayout(self.buttonsSchedMenuX)
            self.todayContainer.addWidget(self.eventTodayNumX)
            self.mainVertLayout.addLayout(self.todayContainer)
            self.mainClosest = QtWidgets.QLabel(parent=self.mainVertWidget)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(20)
            self.mainClosest.setFont(font)
            self.mainClosest.setStyleSheet("background-color:#64898F;padding: 5px; border-radius: 15px")
            self.mainClosest.setObjectName("mainClosest")
            self.mainVertLayout.addWidget(self.mainClosest)
            self.closestContainer = QtWidgets.QHBoxLayout()
            self.closestContainer.setContentsMargins(0, 0, -1, -1)
            self.closestContainer.setObjectName("closestContainer")
            self.label_4 = QtWidgets.QLabel(parent=self.mainVertWidget)
            self.label_4.setObjectName("label_4")
            self.closestContainer.addWidget(self.label_4)
            self.label_4.setHidden(True)
            self.mainVertLayout.addLayout(self.closestContainer)
            self.mainVertLayout.setStretch(0, 3)
            self.mainVertLayout.setStretch(1, 7)
            self.horizontalLayout.addWidget(self.mainVertWidget)
            self.scrollAreaContainer.addWidget(self.scrollArea)
            self.horizontalLayout_2.addLayout(self.scrollAreaContainer)
            self.horizontalLayout_2.setStretch(0, 2)
            self.horizontalLayout_2.setStretch(1, 5)
            self.todayToDoX.setStyleSheet("background-color:#64898F")
            self.todayToCancelX.setStyleSheet("background-color:#64898F")
            self.todayNameX.setStyleSheet("background-color:#64898F;padding: 5px; border-radius: 15px")
            MainWindow.setCentralWidget(self.centralwidget)

            QtCore.QMetaObject.connectSlotsByName(MainWindow)

            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.mainPage.setText(_translate("MainWindow", "Главная"))
            self.petsPage.setText(_translate("MainWindow", "Питомцы"))
            self.schedPage.setText(_translate("MainWindow", "Расписание"))
            self.cagesPage.setText(_translate("MainWindow", "Клетки"))
            self.pushToCreateM.setText(_translate("MainWindow", "Добавить"))
            self.pushToRedactM.setText(_translate("MainWindow", "Редактировать"))
            self.pushToSearch.setText(_translate("MainWindow", "Найти"))
            self.mainToday_L.setText(_translate("MainWindow", "Сегодня"))
            self.todayDateX.setText(_translate("MainWindow", "Ежедневное/Дата"))
            self.todayNameX.setText(_translate("MainWindow", "Название"))
            self.todayDescX.setText(_translate("MainWindow", "Описание"))
            self.todayToDoX.setText(_translate("MainWindow", "Сделать"))
            self.todayToCancelX.setText(_translate("MainWindow", "Отменить"))
            self.todayDoneX.setText(_translate("MainWindow", "Сделано"))
            self.mainClosest.setText(_translate("MainWindow", "Ближайшие события"))
            self.label_4.setText(_translate("MainWindow", "TextLabel"))
        else:
            self.mainVertWidget.setParent(self.scrollAreaWidgetContents)
            self.mainVertWidget.show()

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
        if not hasattr(self,'containerPet'):
            self.containerPet = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
            self.containerPet.setStyleSheet("")
            self.containerPet.setObjectName("containerPet")
            self.formLayout = QtWidgets.QFormLayout(self.containerPet)
            self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.RowWrapPolicy.WrapLongRows)
            self.formLayout.setLabelAlignment(
                QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
            self.formLayout.setFormAlignment(
                QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
            self.formLayout.setContentsMargins(0, 5, 5, -1)
            self.formLayout.setSpacing(5)
            self.formLayout.setObjectName("formLayout")
            self.petNameLO = QtWidgets.QHBoxLayout()
            self.petNameLO.setContentsMargins(-1, 0, -1, -1)
            self.petNameLO.setObjectName("petNameLO")
            self.descName_L = QtWidgets.QLabel(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(20)
            self.descName_L.setFont(font)
            self.descName_L.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.descName_L.setObjectName("descName_L")
            self.petNameLO.addWidget(self.descName_L)
            self.petNameEdit = QtWidgets.QLineEdit(parent=self.containerPet)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.petNameEdit.sizePolicy().hasHeightForWidth())
            self.petNameEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light SemiCondensed")
            font.setPointSize(20)
            self.petNameEdit.setFont(font)
            self.petNameEdit.setObjectName("petNameEdit")
            self.petNameEdit.setHidden(True)
            self.petNameLO.addWidget(self.petNameEdit)
            self.formLayout.setLayout(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.petNameLO)
            self.petSpecLO = QtWidgets.QHBoxLayout()
            self.petSpecLO.setContentsMargins(-1, 0, -1, -1)
            self.petSpecLO.setObjectName("petSpecLO")
            self.petSpec = QtWidgets.QLabel(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petSpec.setFont(font)
            self.petSpec.setObjectName("petSpec")
            self.petSpecLO.addWidget(self.petSpec)
            self.petSpecEdit = QtWidgets.QComboBox(parent=self.containerPet)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.petSpecEdit.sizePolicy().hasHeightForWidth())
            self.petSpecEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petSpecEdit.setFont(font)
            self.petSpecEdit.setObjectName("petSpecEdit")
            self.petSpecEdit.setHidden(True)
            self.petSpecLO.addWidget(self.petSpecEdit)
            self.formLayout.setLayout(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.petSpecLO)
            self.petMorphLO = QtWidgets.QHBoxLayout()
            self.petMorphLO.setContentsMargins(-1, 0, -1, -1)
            self.petMorphLO.setObjectName("petMorphLO")
            self.petMorph = QtWidgets.QLabel(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petMorph.setFont(font)
            self.petMorph.setObjectName("petMorph")
            self.petMorphLO.addWidget(self.petMorph)
            self.petMorphEdit = QtWidgets.QComboBox(parent=self.containerPet)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.petMorphEdit.sizePolicy().hasHeightForWidth())
            self.petMorphEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petMorphEdit.setFont(font)
            self.petMorphEdit.setObjectName("petMorphEdit")
            self.petMorphLO.addWidget(self.petMorphEdit)
            self.petMorphEdit.setHidden(True)
            self.formLayout.setLayout(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.petMorphLO)
            self.petsAgeBirthdayLO = QtWidgets.QHBoxLayout()
            self.petsAgeBirthdayLO.setContentsMargins(-1, 0, -1, -1)
            self.petsAgeBirthdayLO.setObjectName("petsAgeBirthdayLO")
            self.petsAgeBirthday = QtWidgets.QLabel(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petsAgeBirthday.setFont(font)
            self.petsAgeBirthday.setObjectName("petsAgeBirthday")
            self.petsAgeBirthdayLO.addWidget(self.petsAgeBirthday)
            self.petsAgeEdit = QtWidgets.QSpinBox(parent=self.containerPet)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.petsAgeEdit.sizePolicy().hasHeightForWidth())
            self.petsAgeEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petsAgeEdit.setFont(font)
            self.petsAgeEdit.setObjectName("petsAgeEdit")
            self.petsAgeBirthdayLO.addWidget(self.petsAgeEdit)
            self.petsAgeEdit.setHidden(True)
            self.petsBirthdayEdit = QtWidgets.QDateEdit(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petsBirthdayEdit.setFont(font)
            self.petsBirthdayEdit.setObjectName("petsBirthdayEdit")
            self.petsAgeBirthdayLO.addWidget(self.petsBirthdayEdit)
            self.petsBirthdayEdit.setHidden(True)
            self.formLayout.setLayout(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.petsAgeBirthdayLO)
            self.petsGenLO = QtWidgets.QHBoxLayout()
            self.petsGenLO.setContentsMargins(-1, 0, -1, -1)
            self.petsGenLO.setObjectName("petsGenLO")
            self.petsGen = QtWidgets.QLabel(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petsGen.setFont(font)
            self.petsGen.setObjectName("petsGen")
            self.petsGenLO.addWidget(self.petsGen)
            self.petsGenEdit = QtWidgets.QComboBox(parent=self.containerPet)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.petsGenEdit.sizePolicy().hasHeightForWidth())
            self.petsGenEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petsGenEdit.setFont(font)
            self.petsGenEdit.setCurrentText("")
            self.petsGenEdit.setObjectName("petsGenEdit")
            self.petsGenLO.addWidget(self.petsGenEdit)
            self.petsGenEdit.setHidden(True)
            self.formLayout.setLayout(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.petsGenLO)
            self.petWeightLO = QtWidgets.QHBoxLayout()
            self.petWeightLO.setContentsMargins(-1, 0, -1, -1)
            self.petWeightLO.setObjectName("petWeightLO")
            self.petsWeight = QtWidgets.QLabel(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petsWeight.setFont(font)
            self.petsWeight.setObjectName("petsWeight")
            self.petWeightLO.addWidget(self.petsWeight)
            self.petWeightNumEdit = QtWidgets.QSpinBox(parent=self.containerPet)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.petWeightNumEdit.sizePolicy().hasHeightForWidth())
            self.petWeightNumEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petWeightNumEdit.setFont(font)
            self.petWeightNumEdit.setObjectName("petWeightNumEdit")
            self.petWeightNumEdit.setHidden(True)
            self.petWeightLO.addWidget(self.petWeightNumEdit)
            self.petWeightAsEdit = QtWidgets.QLineEdit(parent=self.containerPet)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.petWeightAsEdit.sizePolicy().hasHeightForWidth())
            self.petWeightAsEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petWeightAsEdit.setFont(font)
            self.petWeightAsEdit.setText("")
            self.petWeightAsEdit.setObjectName("petWeightAsEdit")
            self.petWeightLO.addWidget(self.petWeightAsEdit)
            self.petWeightAsEdit.setHidden(True)
            self.formLayout.setLayout(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.petWeightLO)
            self.petsSymptomsLO = QtWidgets.QHBoxLayout()
            self.petsSymptomsLO.setContentsMargins(-1, 0, -1, -1)
            self.petsSymptomsLO.setObjectName("petsSymptomsLO")
            self.petSympotms = QtWidgets.QLabel(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petSympotms.setFont(font)
            self.petSympotms.setObjectName("petSympotms")
            self.petsSymptomsLO.addWidget(self.petSympotms)
            self.petsSymptomsEdit = QtWidgets.QLineEdit(parent=self.containerPet)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.petsSymptomsEdit.sizePolicy().hasHeightForWidth())
            self.petsSymptomsEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petsSymptomsEdit.setFont(font)
            self.petsSymptomsEdit.setObjectName("petsSymptomsEdit")
            self.petsSymptomsLO.addWidget(self.petsSymptomsEdit)
            self.petsSymptomsEdit.setHidden(True)
            self.formLayout.setLayout(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.petsSymptomsLO)
            self.petDiagnosisLO = QtWidgets.QHBoxLayout()
            self.petDiagnosisLO.setContentsMargins(-1, 0, -1, -1)
            self.petDiagnosisLO.setObjectName("petDiagnosisLO")
            self.label = QtWidgets.QLabel(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.petDiagnosisLO.addWidget(self.label)
            self.petDiagnosisEdit = QtWidgets.QLineEdit(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petDiagnosisEdit.setFont(font)
            self.petDiagnosisEdit.setObjectName("petDiagnosisEdit")
            self.petDiagnosisLO.addWidget(self.petDiagnosisEdit)
            self.petDiagnosisEdit.setHidden(True)
            self.formLayout.setLayout(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.petDiagnosisLO)
            self.petNeuteredLO = QtWidgets.QHBoxLayout()
            self.petNeuteredLO.setContentsMargins(-1, 0, -1, -1)
            self.petNeuteredLO.setObjectName("petNeuteredLO")
            self.petNeutered = QtWidgets.QLabel(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petNeutered.setFont(font)
            self.petNeutered.setObjectName("petNeutered")
            self.petNeuteredLO.addWidget(self.petNeutered)
            self.petNeuteredEdit = QtWidgets.QCheckBox(parent=self.containerPet)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.petNeuteredEdit.sizePolicy().hasHeightForWidth())
            self.petNeuteredEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petNeuteredEdit.setFont(font)
            self.petNeuteredEdit.setObjectName("petNeuteredEdit")
            self.petNeuteredLO.addWidget(self.petNeuteredEdit)
            self.petNeuteredEdit.setHidden(True)
            self.formLayout.setLayout(10, QtWidgets.QFormLayout.ItemRole.FieldRole, self.petNeuteredLO)
            self.petsVacsLO = QtWidgets.QHBoxLayout()
            self.petsVacsLO.setContentsMargins(-1, 0, -1, -1)
            self.petsVacsLO.setObjectName("petsVacsLO")
            self.petsVacs = QtWidgets.QLabel(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petsVacs.setFont(font)
            self.petsVacs.setObjectName("petsVacs")
            self.petsVacsLO.addWidget(self.petsVacs)
            self.petsVacsEdit = QtWidgets.QLineEdit(parent=self.containerPet)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.petsVacsEdit.sizePolicy().hasHeightForWidth())
            self.petsVacsEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petsVacsEdit.setFont(font)
            self.petsVacsEdit.setObjectName("petsVacsEdit")
            self.petsVacsLO.addWidget(self.petsVacsEdit)
            self.petsVacsEdit.setHidden(True)
            self.formLayout.setLayout(11, QtWidgets.QFormLayout.ItemRole.FieldRole, self.petsVacsLO)
            self.petsMictochipLO = QtWidgets.QHBoxLayout()
            self.petsMictochipLO.setContentsMargins(-1, 0, -1, -1)
            self.petsMictochipLO.setObjectName("petsMictochipLO")
            self.petsMicrochip = QtWidgets.QLabel(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petsMicrochip.setFont(font)
            self.petsMicrochip.setObjectName("petsMicrochip")
            self.petsMictochipLO.addWidget(self.petsMicrochip)
            self.petMicrochipEdit = QtWidgets.QCheckBox(parent=self.containerPet)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.petMicrochipEdit.sizePolicy().hasHeightForWidth())
            self.petMicrochipEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petMicrochipEdit.setFont(font)
            self.petMicrochipEdit.setObjectName("petMicrochipEdit")
            self.petsMictochipLO.addWidget(self.petMicrochipEdit)
            self.petMicrochipEdit.setHidden(True)
            self.formLayout.setLayout(12, QtWidgets.QFormLayout.ItemRole.FieldRole, self.petsMictochipLO)
            self.petsOwnerLO = QtWidgets.QHBoxLayout()
            self.petsOwnerLO.setContentsMargins(-1, 0, -1, -1)
            self.petsOwnerLO.setObjectName("petsOwnerLO")
            self.petsOwner = QtWidgets.QLabel(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petsOwner.setFont(font)
            self.petsOwner.setObjectName("petsOwner")
            self.petsOwnerLO.addWidget(self.petsOwner)
            self.petsOwnerEdit = QtWidgets.QLineEdit(parent=self.containerPet)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.petsOwnerEdit.sizePolicy().hasHeightForWidth())
            self.petsOwnerEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petsOwnerEdit.setFont(font)
            self.petsOwnerEdit.setObjectName("petsOwnerEdit")
            self.petsOwnerLO.addWidget(self.petsOwnerEdit)
            self.petsOwnerEdit.setHidden(True)
            self.formLayout.setLayout(13, QtWidgets.QFormLayout.ItemRole.FieldRole, self.petsOwnerLO)
            self.petsLiveInLO = QtWidgets.QHBoxLayout()
            self.petsLiveInLO.setContentsMargins(-1, 0, -1, -1)
            self.petsLiveInLO.setObjectName("petsLiveInLO")
            self.petsLivein = QtWidgets.QLabel(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petsLivein.setFont(font)
            self.petsLivein.setObjectName("petsLivein")
            self.petsLiveInLO.addWidget(self.petsLivein)
            self.petsLiveinEdit = QtWidgets.QPushButton(parent=self.containerPet)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.petsLiveinEdit.sizePolicy().hasHeightForWidth())
            self.petsLiveinEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petsLiveinEdit.setFont(font)
            self.petsLiveinEdit.setObjectName("petsLiveinEdit")
            self.petsLiveInLO.addWidget(self.petsLiveinEdit)
            self.petsLiveinEdit.setHidden(True)
            self.formLayout.setLayout(14, QtWidgets.QFormLayout.ItemRole.FieldRole, self.petsLiveInLO)
            spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Policy.Minimum,
                                               QtWidgets.QSizePolicy.Policy.Expanding)
            self.formLayout.setItem(17, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem)
            self.eventActions = QtWidgets.QHBoxLayout()
            self.eventActions.setContentsMargins(-1, 0, -1, -1)
            self.eventActions.setObjectName("eventActions")
            spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                                QtWidgets.QSizePolicy.Policy.Minimum)
            self.eventActions.addItem(spacerItem1)
            self.pushToRedact = QtWidgets.QPushButton(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(12)
            self.pushToRedact.setFont(font)
            self.pushToRedact.setObjectName("pushToRedact")
            self.eventActions.addWidget(self.pushToRedact)
            self.pushButton = QtWidgets.QPushButton(parent=self.containerPet)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
            self.pushButton.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(12)
            self.pushButton.setFont(font)
            self.pushButton.setObjectName("pushButton")
            self.eventActions.addWidget(self.pushButton)
            self.eventActions.setStretch(0, 4)
            self.eventActions.setStretch(1, 3)
            self.formLayout.setLayout(20, QtWidgets.QFormLayout.ItemRole.FieldRole, self.eventActions)
            self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_7.setContentsMargins(-1, 50, -1, -1)
            self.horizontalLayout_7.setObjectName("horizontalLayout_7")
            self.petPhoto = QtWidgets.QLabel(parent=self.containerPet)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(15)
            self.petPhoto.setFont(font)
            self.petPhoto.setText("")
            self.petPhoto.setPixmap(QtGui.QPixmap("../maket/car.png"))
            self.petPhoto.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.petPhoto.setObjectName("petPhoto")
            self.horizontalLayout_7.addWidget(self.petPhoto)
            self.petPhotoWayToFile = QtWidgets.QLineEdit(parent=self.containerPet)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.petPhotoWayToFile.sizePolicy().hasHeightForWidth())
            self.petPhotoWayToFile.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light SemiCondensed")
            font.setPointSize(14)
            self.petPhotoWayToFile.setFont(font)
            self.petPhotoWayToFile.setText("")
            self.petPhotoWayToFile.setObjectName("petPhotoWayToFile")
            self.horizontalLayout_7.addWidget(self.petPhotoWayToFile)
            self.petPhotoWayToFile.setHidden(True)
            self.petPhotoChoose = QtWidgets.QPushButton(parent=self.containerPet)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                               QtWidgets.QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.petPhotoChoose.sizePolicy().hasHeightForWidth())
            self.petPhotoChoose.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Bahnschrift Light Condensed")
            font.setPointSize(14)
            self.petPhotoChoose.setFont(font)
            self.petPhotoChoose.setObjectName("petPhotoChoose")
            self.horizontalLayout_7.addWidget(self.petPhotoChoose)
            self.petPhotoChoose.setHidden(True)
            self.formLayout.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout_7)
            self.horizontalLayout.addWidget(self.containerPet)
            spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                                QtWidgets.QSizePolicy.Policy.Minimum)
            self.horizontalLayout.addItem(spacerItem2)
            self.scrollAreaContainer.addWidget(self.scrollArea)
            self.horizontalLayout_2.addLayout(self.scrollAreaContainer)
            self.horizontalLayout_2.setStretch(0, 2)
            self.horizontalLayout_2.setStretch(1, 5)
        self.containerPet.setStyleSheet("""
                QWidget#containerPet {
               border: 3px solid #CDA989; border-radius: 15px
                }
                """)
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

        self.pushToRedact.setStyleSheet("background-color: #CDA989")
        self.pushButton.setStyleSheet("background-color: #CDA989")
        self.containerPet.setParent(self.scrollAreaWidgetContents)
        self.containerPet.setHidden(False)

        # self.containerPet.setStyleSheet(""QWidget{:background-color:#CDA989;padding: 5px}"")
        # self.containerPet.setStyleSheet("""
        # QWidget {
        # background-color:#CDA989; padding: 5px;
        # }
        # """)
        self.descName_L.setStyleSheet("background-color:#CDA989;padding: 5px; border-radius: 15px")

        MainWindow.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainPage.setText(_translate("MainWindow", "Главная"))
        self.petsPage.setText(_translate("MainWindow", "Питомцы"))
        self.schedPage.setText(_translate("MainWindow", "Расписание"))
        self.cagesPage.setText(_translate("MainWindow", "Клетки"))
        self.pushToCreateM.setText(_translate("MainWindow", "Добавить"))
        self.pushToRedactM.setText(_translate("MainWindow", "Редактировать"))
        self.pushToSearch.setText(_translate("MainWindow", "Найти"))
        self.descName_L.setText(_translate("MainWindow", "Имя питомца"))
        self.petNameEdit.setPlaceholderText(_translate("MainWindow", "Имя"))
        self.petSpec.setText(_translate("MainWindow", "Вид"))
        self.petMorph.setText(_translate("MainWindow", "Порода"))
        self.petsAgeBirthday.setText(_translate("MainWindow", "Возраст и день рождения"))
        self.petsGen.setText(_translate("MainWindow", "Пол"))
        self.petsWeight.setText(_translate("MainWindow", "Вес"))
        self.petWeightAsEdit.setPlaceholderText(_translate("MainWindow", "Единица измерения (Килограмм, грамм, т.д.)"))
        self.petSympotms.setText(_translate("MainWindow", "Симптомы:"))
        self.petsSymptomsEdit.setPlaceholderText(_translate("MainWindow", "Симптомы"))
        self.label.setText(_translate("MainWindow", "Диагноз(ы):"))
        self.petDiagnosisEdit.setPlaceholderText(_translate("MainWindow", "Диагноз(ы)"))
        self.petNeutered.setText(_translate("MainWindow", "Кастрирован"))
        self.petNeuteredEdit.setText(_translate("MainWindow", "Кастрирован"))
        self.petsVacs.setText(_translate("MainWindow", "Прививки: (название прививки и дата прививки)"))
        self.petsVacsEdit.setPlaceholderText(_translate("MainWindow", "Прививки"))
        self.petsMicrochip.setText(_translate("MainWindow", "Микрочип:"))
        self.petMicrochipEdit.setText(_translate("MainWindow", "Микрочип"))
        self.petsOwner.setText(_translate("MainWindow", "Хозяин"))
        self.petsOwnerEdit.setPlaceholderText(_translate("MainWindow", "Хозяин"))
        self.petsLivein.setText(_translate("MainWindow", "Живёт в:"))
        self.petsLiveinEdit.setText(_translate("MainWindow", "Выбрать вольер/клетку"))
        self.pushToRedact.setText(_translate("MainWindow", "Редактировать"))
        self.pushButton.setText(_translate("MainWindow", "Удалить"))
        self.petPhotoWayToFile.setPlaceholderText(_translate("MainWindow", "Путь к изображению"))
        self.petPhotoChoose.setText(_translate("MainWindow", "Выбрать изображение"))


    def EventMenuGui(self):
        self.pushToSearch.setStyleSheet("background-color:#A59B77")
        self.pushToRedactM.setStyleSheet("background-color:#A59B77")
        self.pushToCreateM.setStyleSheet("background-color:#A59B77")
        self.allEventsLO = QtWidgets.QHBoxLayout()
        self.allEventsLO.setContentsMargins(11, 11, 11, 11)
        self.allEventsLO.setObjectName("allEventsLO")
        self.eventsForDayX = QtWidgets.QVBoxLayout()
        self.eventsForDayX.setContentsMargins(-1, 0, -1, -1)
        self.eventsForDayX.setObjectName("eventsForDayX")
        self.DayX_L = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(20)
        self.DayX_L.setFont(font)
        self.DayX_L.setStyleSheet("border: 2px solid black")
        self.DayX_L.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.DayX_L.setObjectName("DayX_L")
        self.eventsForDayX.addWidget(self.DayX_L)
        self.eventXdayX = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
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
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Name_eventXdayX.setFont(font)
        self.Name_eventXdayX.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Name_eventXdayX.setObjectName("Name_eventXdayX")
        self.verticalLayout_2.addWidget(self.Name_eventXdayX)
        self.Desc_eventXdayX = QtWidgets.QLabel(parent=self.eventXdayX)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
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
        self.horizontalLayout.addLayout(self.allEventsLO)
        self.scrollAreaContainer.addWidget(self.scrollArea)
        self.horizontalLayout_2.addLayout(self.scrollAreaContainer)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 5)
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
                    containerCage.setObjectName("containerCage")
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
                            if x != len(petsToCage) - 1: anims + ","
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
                    containerCage.setStyleSheet("""
                                                                        QWidget#containerCage {
                                                                       border: 3px solid #8DA578; border-radius: 15px
                                                                        }
                                                                        """)
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

    def doneChoosing(self):
        if self.dialog.ui.treeWidget.selectedItems()!=None:
            allItems=self.dialog.ui.treeWidget.selectedItems()
            self.ItemsPK=[]
            for i in range(len(allItems)):
                item=allItems[i].text(0)
                if item!=" ":
                    if self.currentList=="PetsToCages": collumnNum=3
                    for j in range(len(allItems)):
                        if (item[collumnNum+j]).isdigit and (item[collumnNum+j])!=" ":
                            self.ItemsPK.append(item[collumnNum+j])
                            print(self.ItemsPK)
                        else: break



    #Общие функции

    def redactInitiate(self,buttonName):
        self.containerNum=''
        preRevContainerNum=''
        for x in reversed(buttonName):
            if x.isdigit()==False:
                break
            else: preRevContainerNum=preRevContainerNum+x
        for x in reversed(preRevContainerNum):
            containerNum=self.containerNum+x
        if self.currentMenu==3:
            #Аминь
            for i in ["cagePhoto_","cageDescName_L_","cagePetsLabels_","cageLastClean_","cageQuar_","cageMoPart_",
                      "cageInfect_","cageSpecial_","cageNotes_"]:
                hideWidget=getattr(self,f'{i}{self.containerNum}')
                hideWidget.setHidden(True)
            getattr(self,f"cageType_{self.containerNum}").setText("Тип клетки")
            for i in ["cagePhotoWayToFile_","cagePhotoChoose_","cageNameEdit_","cageTypeEdit_","cagePetsEdit_","cageLastCleanEdit_",
                      "cageQuarEdit_","cageMoPartEdit_","cageInfectEdit_","cageSpecialAll_","cageSpecialEdit_","cagePetsChoosen_"]:
                showWidget=getattr(self,f'{i}{self.containerNum}')
                showWidget.setHidden(False)
        for i in self.currentRedactButtons:
            if i!=buttonName: getattr(self,i).setEnabled(False)
            else:
                getattr(self,buttonName).setText("Готово")
                getattr(self,f'cageActionsDelete_{self.containerNum}').setText("Отменить изменения")
                try:
                    getattr(self,buttonName).clicked.disconnect()
                    getattr(self, f'cageActionsDelete_{self.containerNum}').disconnect()
                    print("Кнопки отключены!")
                except Exception:
                    print("Кнопки не были отключены")
                    pass

    def specialEdit(self,buttonName):
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.pushButton_2.clicked.connect(self.doneChoosing)
        self.dialog.ui.pushButton_2.clicked.connect(self.saveChanges)
        if "cagePetsEdit" in buttonName:
            self.dialog.ui.fillInfo("Животные")
            self.currentList = "PetsToCages"
        else:
            print("aww")
        self.dialog.exec()

    def saveChanges(self):
        if self.currentList == "PetsToCages":
            for i in range(len(self.ItemsPK)):
                #Проверить существует ли запись
                cageName=getattr(self,"")
                cur.execute(f'''SELECT petid, имя FROM питомцы JOIN "животные к клеткам"
                                                               ON питомцы.petid="животные к клеткам"."id животного"
                                                               WHERE "животные к клеткам"."название прив клетки"={"'" + check[i][0] + "'"}''')
                petsToCage = cur.fetchall()
                cur.execute(f"SELECT petid FROM питомцы WHERE petid={self.ItemsPK[i]}")
                info=cur.fetchall()
                self.containerNum
                print(info)

    def updateMenu(self):
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
        if hasattr(self, 'containerPet'):
            self.containerPet.hide()
        if hasattr(self, 'mainVertLayout'):
            print(self.mainVertLayout.parent())
            self.mainVertWidget.setParent(None)
            self.mainVertWidget.hide()
            print(1)
        if hasattr(self, f"containerCage_{0}"):
            if hasattr(self, f"cagePhotoLO_{0}"):
                cur.execute('SELECT * FROM клетки')
                needToBeDeleted = len(cur.fetchall())
                for i in range(needToBeDeleted):
                    getattr(self, f"containerCage_{i}").setParent(None)
                    getattr(self, f"containerCage_{i}").setHidden(True)


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