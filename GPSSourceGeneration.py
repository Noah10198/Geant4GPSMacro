import sys

from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from ParticleGunUI import Ui_GPSSourceGenergation

outMacfile="GPS.mac"



class MyWindow(QMainWindow,Ui_GPSSourceGenergation):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.MacScriptList=''
        self.MacScriptdir=''
        self.MacScriptEnergy=''
        self.MacScriptPos=''
        self.MacScriptParticleName=''
        self.totalMac=''
        
        self.cancelPtn.clicked.connect(self.close)
        self.previewPtn.clicked.connect(self.preview)
        self.savePtn.clicked.connect(self.savefile)
        self.GPSListCheckBox.clicked.connect(self.list)
# total Mac 
    def totalMacFun(self):
        self.totalMac="# out source mac script\n"+self.MacScriptList+"\n"+self.MacScriptParticleName+"\n"+self.MacScriptPos+"\n"+self.MacScriptdir+"\n"+self.MacScriptEnergy+"\n"


# 定义preview function
    def preview(self):
        self.totalMacFun()
        print("preview")
        self.OutGPSMacBro.setText(self.totalMac)

# 定义save function
    def savefile(self):
        print("save file")
        self.totalMacFun()
        with open("gps.mac",'w') as file:
            file.write(self.totalMac)
        print("finished!")

# 定义list function
    def list(self):
        if self.GPSListCheckBox.isChecked():
            self.MacScriptList="/gps/List"
            print(self.MacScriptList)
        else:
            self.MacScriptList=""
            print("script canceled!")


# ParticleDirection function
    def ParticleDir(self):
         print("cost")
   
# ParticleEnergy function
    def ParticleEnergy(self):
        print("cost")


# ParticlePosition function
    def ParticlePos(self):
         print("cost")



if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    # 设置窗口标题
    w.setWindowTitle("GunSourceGeneration")
    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()

