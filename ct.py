# Created by: Satyadev Patel



from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(909, 692)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.input_bits = QtWidgets.QLabel(self.centralwidget)
        self.input_bits.setObjectName("input_bits")
        self.horizontalLayout.addWidget(self.input_bits)
        self.inputBits = QtWidgets.QLineEdit(self.centralwidget)
        self.inputBits.setObjectName("inputBits")
        self.horizontalLayout.addWidget(self.inputBits)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.encode = QtWidgets.QPushButton(self.centralwidget)
        self.encode.setObjectName("encode")
        self.horizontalLayout_7.addWidget(self.encode)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.encode_msg = QtWidgets.QLabel(self.centralwidget)
        self.encode_msg.setObjectName("encode_msg")
        self.horizontalLayout_2.addWidget(self.encode_msg)
        self.encoded = QtWidgets.QLabel(self.centralwidget)
        self.encoded.setObjectName("encoded")
        self.horizontalLayout_2.addWidget(self.encoded)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.bsc = QtWidgets.QRadioButton(self.centralwidget)
        self.bsc.setObjectName("bsc")
        self.horizontalLayout_3.addWidget(self.bsc)
        self.bec = QtWidgets.QRadioButton(self.centralwidget)
        self.bec.setObjectName("bec")
        self.horizontalLayout_3.addWidget(self.bec)
        self.gaussian = QtWidgets.QRadioButton(self.centralwidget)
        self.gaussian.setObjectName("gaussian")
        self.horizontalLayout_3.addWidget(self.gaussian)
        self.no_channel = QtWidgets.QRadioButton(self.centralwidget)
        self.no_channel.setChecked(True)
        self.no_channel.setObjectName("no_channel")
        self.horizontalLayout_3.addWidget(self.no_channel)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.proceed = QtWidgets.QPushButton(self.centralwidget)
        self.proceed.setObjectName("proceed")
        self.horizontalLayout_4.addWidget(self.proceed)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.channel_output = QtWidgets.QLabel(self.centralwidget)
        self.channel_output.setObjectName("channel_output")
        self.horizontalLayout_5.addWidget(self.channel_output)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.decode = QtWidgets.QPushButton(self.centralwidget)
        self.decode.setObjectName("decode")
        self.horizontalLayout_6.addWidget(self.decode)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setObjectName("output")
        self.horizontalLayout_8.addWidget(self.output)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem15)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 909, 31))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuOptions.addAction(self.actionNew)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.encode.clicked.connect(self.encoder)
        self.proceed.clicked.connect(self.channel)
        self.decode.clicked.connect(self.decoder)
        self.menubar.triggered[QtWidgets.QAction].connect(self.menu)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def menu(self,action):
        txt=action.text()
        if txt=='New':
            self.inputBits.clear()
            self.encoded.clear()
            self.channel_output.clear()
            self.output.clear()
    def channel(self):
        if self.bsc.isChecked()==True:
            random_nums=[i/1000 for i in range(1,1000,1)]
            prob,ok=QtWidgets.QInputDialog.getText(MainWindow, "BSC", "Enter Probability:")
            prob=float(prob)
            encoded_msg=self.encoded.text().split(" ")
            encoded_msg.pop(len(encoded_msg)-1)
            for i in range(0,len(encoded_msg)):
                encoded_msg[i]=int(encoded_msg[i])
            a=encoded_msg
            for i in range(0,len(a)):
                p=random.choice(random_nums)
                if a[i]==0:
                    if p<prob:
                        a[i]=1
                    else:
                        a[i]=0
                else:
                    if p<prob:
                        a[i]=0
                    else:
                        a[i]=1
            msg=""
            for i in range(0,len(a)):
                msg=msg+str(a[i])+" "
            self.channel_output.setText(msg)
        if self.bec.isChecked()==True:
            random_nums=[i/100 for i in range(1,100,1)]
            prob,ok=QtWidgets.QInputDialog.getText(MainWindow, "BEC", "Enter Probability:")
            prob=float(prob)
            encoded_msg=self.encoded.text().split(" ")
            encoded_msg.pop(len(encoded_msg)-1)
            for i in range(0,len(encoded_msg)):
                encoded_msg[i]=int(encoded_msg[i])
            a=encoded_msg
            for i in range(0,len(a)):
                p=random.choice(random_nums)
                if a[i]==0:
                    if p<prob:
                        a[i]=-1
                    else:
                        a[i]=0
                else:
                    if p<prob:
                        a[i]=-1
                    else:
                        a[i]=1
            msg=""
            for i in range(0,len(a)):
                msg=msg+str(a[i])+" "
            self.channel_output.setText(msg)
    def encoder(self):
        k=int(self.inputBits.text())
        x=[None]*k
        for i in range(0,k):
            x[i]=random.choice([0,1])
        m=[None]*(k+4)
        for i in range(0,k):
            x[i]=int(x[i])
        print(x)
        self.code=x
        for i in range(0,len(x)+4):
            if i<2 or i>=len(x)+2:
                m[i]=0
            else:
                m[i]=x[i-2]
        count=0
        self.e=[None]*(2*k+4)
        for i in range(2,len(m)):
            parity_1=(m[i]+m[i-2]+m[i-1])%2
            parity_2=(m[i]+m[i-2])%2
            self.e[count]=parity_1
            self.e[count+1]=parity_2
            count=count+2
        msg=""
        for i in range(0,len(self.e)):
            msg=msg+str(self.e[i])+" "
        self.encoded.setText(msg)
    def decoder(self):
        st=[0,0,1,1,1,0,0,1]
        st1=[1,1,0,0,0,1,1,0]
        c_msg=self.channel_output.text().split(" ")
        c_msg.pop(len(c_msg)-1)
        for i in range(0,len(c_msg)):
            c_msg[i]=int(c_msg[i])
        a=c_msg
        self.cc=a
        n=self.inputBits.text()
        n=int(n)+2
        b = [ [ None for i in range(4) ] for j in range(n) ]
        decoded=[None for i in range(n)]
        b[0][2]=1000
        b[0][3]=1000
        for j in range(0,2):
            b[0][j]=0;
            if st[j*2]!=a[0*2]:
                b[0][j]+=1
            if st[j*2+1]!=a[0*2+1]:
                b[0][j]+=1
        for i in range(1,n):
            for j in range(0,4):
                if j<2:
                    x=b[i-1][0];
                    if st[j*2]!=a[i*2]:
                        x+=1
                    if st[j*2+1]!=a[i*2+1]:
                        x+=1
                    y=b[i-1][2];
                    if st1[j*2]!=a[i*2]:
                        y+=1
                    if st1[j*2+1]!=a[i*2+1]:
                        y+=1

                    if x<y:
                        b[i][j]=x
                    if x>=y:
                        b[i][j]=y
                
                
                else:
                    x=b[i-1][1]
                    if st[j*2]!=a[i*2]:
                        x+=1
                    if st[j*2+1]!=a[i*2+1]:
                        x+=1


                    y=b[i-1][3] 
                    if st1[j*2]!=a[i*2]:
                        y+=1
                    if st1[j*2+1]!=a[i*2+1]:
                        y+=1
    
                    
                    if x<=y:
                        b[i][j]=x
                    if x>y:
                        b[i][j]=y
        x=0
        y=x
        for i in range(0,n):
            if x==0 or x==2:
                if b[i][0]>b[i][1]:
                    x=1
                if b[i][0]<b[i][1]:
                    x=0
                if b[i][0]==b[i][1]:
                    if i+1==n:
                        x=1
                    else:
                        if b[i+1][0]>b[i+1][1]:
                            a1=b[i+1][1]
                        else:
                            a1=b[i+1][0]
                        if b[i+1][2]>b[i+1][3]:
                            b1=b[i+1][3];
                        else:
                            b1=b[i+1][2];
                        if a1>b1:
                            x=1
                        elif b1>=a1:
                            x=0



            if x==1 or x==3:    
                if b[i][2]>b[i][3]:
                    x=3
                if b[i][2]<b[i][3]:
                    x=2
                if b[i][2]==b[i][3]:
                    if i+1==n:
                        x=2
                    else:
                        if b[i+1][0]>b[i+1][1]:
                            a1=b[i+1][1]
                        else:
                            a1=b[i+1][0]
    
                        if b[i+1][2]>b[i+1][3]:
                            b1=b[i+1][3]
                        else:
                            b1=b[i+1][2]
    
                        if a1>b1:
                            x=3
                        elif b1>=a1:
                            x=2



            decoded[i]=x%2
        msg=""
        count=0
        cnt=0
        for i in range(0,len(decoded)-2):
            msg=msg+str(decoded[i])+" "
        self.output.setText(msg)
        for i in range(0,len(decoded)-2):
            if decoded[i]!=self.code[i]:
                count=count+1
        for i in range(0,len(self.e)):
            if self.cc[i]!=self.e[i]:
                cnt=cnt+1

        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.input_bits.setText(_translate("MainWindow", "Your Message"))
        self.encode.setText(_translate("MainWindow", "Encode"))
        self.encode_msg.setText(_translate("MainWindow", "Encoded Message:"))
        self.encoded.setText(_translate("MainWindow", "None"))
        self.label_4.setText(_translate("MainWindow", "Select Channel:"))
        self.bsc.setText(_translate("MainWindow", "BSC"))
        self.bec.setText(_translate("MainWindow", "BEC"))
        self.gaussian.setText(_translate("MainWindow", "Gaussian"))
        self.no_channel.setText(_translate("MainWindow", "None"))
        self.proceed.setText(_translate("MainWindow", "Proceed"))
        self.label_5.setText(_translate("MainWindow", "Coded Message:"))
        self.channel_output.setText(_translate("MainWindow", "None"))
        self.decode.setText(_translate("MainWindow", "Decode"))
        self.label.setText(_translate("MainWindow", "Decoded message:"))
        self.output.setText(_translate("MainWindow", "None"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionNew.setText(_translate("MainWindow", "New"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
