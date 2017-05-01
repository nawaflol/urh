# -*- coding: utf-8 -*-

#
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SimulatorTab(object):
    def setupUi(self, SimulatorTab):
        SimulatorTab.setObjectName("SimulatorTab")
        SimulatorTab.resize(1009, 551)
        self.gridLayout_2 = QtWidgets.QGridLayout(SimulatorTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(SimulatorTab)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.frame_2 = QtWidgets.QFrame(self.splitter)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.frame_3 = QtWidgets.QFrame(self.splitter_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.toolButton = QtWidgets.QToolButton(self.frame_3)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.treeProtocols = GeneratorTreeView(self.frame_3)
        self.treeProtocols.setObjectName("treeProtocols")
        self.verticalLayout_3.addWidget(self.treeProtocols)
        self.btnStartSim = QtWidgets.QPushButton(self.frame_3)
        self.btnStartSim.setObjectName("btnStartSim")
        self.verticalLayout_3.addWidget(self.btnStartSim)
        self.frame_4 = QtWidgets.QFrame(self.splitter_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_4)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.btnPrevNav = QtWidgets.QToolButton(self.tab)
        self.btnPrevNav.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPrevNav.sizePolicy().hasHeightForWidth())
        self.btnPrevNav.setSizePolicy(sizePolicy)
        self.btnPrevNav.setMaximumSize(QtCore.QSize(20, 16777215))
        icon = QtGui.QIcon.fromTheme("go-previous")
        self.btnPrevNav.setIcon(icon)
        self.btnPrevNav.setObjectName("btnPrevNav")
        self.gridLayout_7.addWidget(self.btnPrevNav, 1, 1, 1, 1)
        self.btnNextNav = QtWidgets.QToolButton(self.tab)
        self.btnNextNav.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNextNav.sizePolicy().hasHeightForWidth())
        self.btnNextNav.setSizePolicy(sizePolicy)
        self.btnNextNav.setMaximumSize(QtCore.QSize(20, 16777215))
        icon = QtGui.QIcon.fromTheme("go-next")
        self.btnNextNav.setIcon(icon)
        self.btnNextNav.setObjectName("btnNextNav")
        self.gridLayout_7.addWidget(self.btnNextNav, 1, 3, 1, 1)
        self.navLineEdit = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navLineEdit.sizePolicy().hasHeightForWidth())
        self.navLineEdit.setSizePolicy(sizePolicy)
        self.navLineEdit.setObjectName("navLineEdit")
        self.gridLayout_7.addWidget(self.navLineEdit, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 1, 0, 1, 1)
        self.gvSimulator = SimulatorGraphicsView(self.tab)
        self.gvSimulator.setObjectName("gvSimulator")
        self.gridLayout_7.addWidget(self.gvSimulator, 0, 0, 1, 4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 1, 1, 1, 1)
        self.cbViewType = QtWidgets.QComboBox(self.tab_2)
        self.cbViewType.setObjectName("cbViewType")
        self.cbViewType.addItem("")
        self.cbViewType.addItem("")
        self.cbViewType.addItem("")
        self.gridLayout_8.addWidget(self.cbViewType, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem1, 1, 0, 1, 1)
        self.tblViewMessage = SimulatorMessageTableView(self.tab_2)
        self.tblViewMessage.setAlternatingRowColors(True)
        self.tblViewMessage.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tblViewMessage.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tblViewMessage.setShowGrid(False)
        self.tblViewMessage.setObjectName("tblViewMessage")
        self.tblViewMessage.horizontalHeader().setHighlightSections(False)
        self.tblViewMessage.verticalHeader().setHighlightSections(False)
        self.gridLayout_8.addWidget(self.tblViewMessage, 0, 0, 1, 3)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.splitter_2)
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.detail_view_widget = QtWidgets.QStackedWidget(self.frame)
        self.detail_view_widget.setObjectName("detail_view_widget")
        self.page_empty = QtWidgets.QWidget()
        self.page_empty.setObjectName("page_empty")
        self.detail_view_widget.addWidget(self.page_empty)
        self.page_goto_action = QtWidgets.QWidget()
        self.page_goto_action.setObjectName("page_goto_action")
        self.verticalLayout_6 = QtWidgets.QGridLayout(self.page_goto_action)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.page_goto_action)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2, 1, 0, 1, 1)
        self.goto_combobox = QtWidgets.QComboBox(self.page_goto_action)
        self.goto_combobox.setObjectName("goto_combobox")
        self.verticalLayout_6.addWidget(self.goto_combobox, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem3, 1, 2, 1, 1)
        self.detail_view_widget.addWidget(self.page_goto_action)
        self.page_message = QtWidgets.QWidget()
        self.page_message.setObjectName("page_message")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_message)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tblViewFieldValues = QtWidgets.QTableView(self.page_message)
        self.tblViewFieldValues.setAlternatingRowColors(True)
        self.tblViewFieldValues.setShowGrid(False)
        self.tblViewFieldValues.setObjectName("tblViewFieldValues")
        self.tblViewFieldValues.horizontalHeader().setDefaultSectionSize(150)
        self.tblViewFieldValues.horizontalHeader().setStretchLastSection(True)
        self.tblViewFieldValues.verticalHeader().setVisible(False)
        self.gridLayout_4.addWidget(self.tblViewFieldValues, 0, 0, 1, 1)
        self.detail_view_widget.addWidget(self.page_message)
        self.page_rule = QtWidgets.QWidget()
        self.page_rule.setObjectName("page_rule")
        self.verticalLayout_2 = QtWidgets.QGridLayout(self.page_rule)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rbAllApply = QtWidgets.QRadioButton(self.page_rule)
        self.rbAllApply.setChecked(True)
        self.rbAllApply.setObjectName("rbAllApply")
        self.verticalLayout_2.addWidget(self.rbAllApply, 0, 0, 1, 1)
        self.rbOneApply = QtWidgets.QRadioButton(self.page_rule)
        self.rbOneApply.setObjectName("rbOneApply")
        self.verticalLayout_2.addWidget(self.rbOneApply, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4, 0, 2, 1, 1)
        self.tblViewSimulatorRuleset = QtWidgets.QTableView(self.page_rule)
        self.tblViewSimulatorRuleset.setObjectName("tblViewSimulatorRuleset")
        self.tblViewSimulatorRuleset.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tblViewSimulatorRuleset, 5, 0, 4, 3)
        self.btnAddRule = QtWidgets.QToolButton(self.page_rule)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.btnAddRule.setIcon(icon)
        self.btnAddRule.setObjectName("btnAddRule")
        self.verticalLayout_2.addWidget(self.btnAddRule, 5, 3, 1, 1)
        self.btnRemoveRule = QtWidgets.QToolButton(self.page_rule)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.btnRemoveRule.setIcon(icon)
        self.btnRemoveRule.setObjectName("btnRemoveRule")
        self.verticalLayout_2.addWidget(self.btnRemoveRule, 6, 3, 1, 1)
        self.detail_view_widget.addWidget(self.page_rule)
        self.page_ext_prog_action = QtWidgets.QWidget()
        self.page_ext_prog_action.setObjectName("page_ext_prog_action")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_ext_prog_action)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_4 = QtWidgets.QLabel(self.page_ext_prog_action)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page_ext_prog_action)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem5, 4, 0, 1, 1)
        self.extProgramLineEdit = QtWidgets.QLineEdit(self.page_ext_prog_action)
        self.extProgramLineEdit.setReadOnly(True)
        self.extProgramLineEdit.setObjectName("extProgramLineEdit")
        self.gridLayout_5.addWidget(self.extProgramLineEdit, 1, 1, 1, 1)
        self.cmdLineArgsLineEdit = QtWidgets.QLineEdit(self.page_ext_prog_action)
        self.cmdLineArgsLineEdit.setObjectName("cmdLineArgsLineEdit")
        self.gridLayout_5.addWidget(self.cmdLineArgsLineEdit, 3, 1, 1, 4)
        self.btnChooseExtProg = QtWidgets.QToolButton(self.page_ext_prog_action)
        self.btnChooseExtProg.setObjectName("btnChooseExtProg")
        self.gridLayout_5.addWidget(self.btnChooseExtProg, 1, 3, 1, 2)
        self.detail_view_widget.addWidget(self.page_ext_prog_action)
        self.gridLayout.addWidget(self.detail_view_widget, 3, 0, 1, 7)
        self.lblMsgFieldsValues = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMsgFieldsValues.sizePolicy().hasHeightForWidth())
        self.lblMsgFieldsValues.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblMsgFieldsValues.setFont(font)
        self.lblMsgFieldsValues.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMsgFieldsValues.setObjectName("lblMsgFieldsValues")
        self.gridLayout.addWidget(self.lblMsgFieldsValues, 0, 0, 1, 7)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(SimulatorTab)
        self.tabWidget.setCurrentIndex(0)
        self.detail_view_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SimulatorTab)

    def retranslateUi(self, SimulatorTab):
        _translate = QtCore.QCoreApplication.translate
        SimulatorTab.setWindowTitle(_translate("SimulatorTab", "Form"))
        self.label.setText(_translate("SimulatorTab", "Protocols:"))
        self.toolButton.setText(_translate("SimulatorTab", "..."))
        self.btnStartSim.setText(_translate("SimulatorTab", "Start simulation ..."))
        self.btnPrevNav.setText(_translate("SimulatorTab", "<"))
        self.btnNextNav.setText(_translate("SimulatorTab", ">"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SimulatorTab", "Flow Graph"))
        self.label_5.setText(_translate("SimulatorTab", "Viewtype:"))
        self.cbViewType.setItemText(0, _translate("SimulatorTab", "Bit"))
        self.cbViewType.setItemText(1, _translate("SimulatorTab", "Hex"))
        self.cbViewType.setItemText(2, _translate("SimulatorTab", "ASCII"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SimulatorTab", "Messages"))
        self.label_2.setText(_translate("SimulatorTab", "Goto:"))
        self.rbAllApply.setText(_translate("SimulatorTab", "All rules must apply (AND)"))
        self.rbOneApply.setText(_translate("SimulatorTab", "At least one rule must apply (OR)"))
        self.btnAddRule.setToolTip(_translate("SimulatorTab", "Add ruleset"))
        self.btnAddRule.setText(_translate("SimulatorTab", "..."))
        self.btnRemoveRule.setToolTip(_translate("SimulatorTab", "Remove ruleset"))
        self.btnRemoveRule.setText(_translate("SimulatorTab", "..."))
        self.label_4.setText(_translate("SimulatorTab", "Command line arguments:"))
        self.label_3.setText(_translate("SimulatorTab", "External program:"))
        self.btnChooseExtProg.setText(_translate("SimulatorTab", "..."))
        self.lblMsgFieldsValues.setText(_translate("SimulatorTab", "Detail view for item"))

from urh.ui.views.GeneratorTreeView import GeneratorTreeView
from urh.ui.views.SimulatorGraphicsView import SimulatorGraphicsView
from urh.ui.views.SimulatorMessageTableView import SimulatorMessageTableView
from . import urh_rc