import sys

from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from ParticleGunUI import Ui_GPSSourceGenergation
from PyQt5.QtGui import QIcon
outMacfile="GPS.mac"



class MyWindow(QMainWindow,Ui_GPSSourceGenergation):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowIcon(QIcon("particleGunIcon.png"))
        
        self.setupUi(self)
        self.MacScriptList=''


        self.MacScriptPos=''
        self.MacScriptParticleName=''
        
        self.ParticleEnergyValue=''
        self.ParticleEnergyUnitsValue=''
        
        self.ParticleDirTotalValue=''
        self.ParticleDirXValue=''
        self.ParticleDirYValue=''
        self.ParticleDirZValue=''

        self.ParticlePosTotalValue=''
        self.ParticlePosXValue=''
        self.ParticlePosYValue=''
        self.ParticlePosZValue=''
        
        self.ParticleNameValue=''
        self.ParticleIonAtomicZ=''
        self.ParticleIonMassA=''        
        self.ParticleIonicChargeQ=''    
        self.ParticleExcitationE=''
        
        
        self.totalMac='' 

        self.cancelPtn.clicked.connect(self.close)
        self.previewPtn.clicked.connect(self.preview)
        self.savePtn.clicked.connect(self.savefile)
        
        self.GPSListCheckBox.clicked.connect(self.list)
        
        self.ParticleDirX.valueChanged.connect(self.ParticleDirXFun)
        self.ParticleDirY.valueChanged.connect(self.ParticleDirYFun)
        self.ParticleDirZ.valueChanged.connect(self.ParticleDirZFun)
        
        self.ParticlePosX.valueChanged.connect(self.ParticlePosXFun)
        self.ParticlePosY.valueChanged.connect(self.ParticlePosYFun)
        self.ParticlePosZ.valueChanged.connect(self.ParticlePosZFun)
        
        self.ParticleEnergy.valueChanged.connect(self.ParticleEnergyFun)

        self.ParticleNameNormal.toggled.connect(self.ParticleNameFun)
        self.ParticleNameIon.toggled.connect(self.ParticleNameFun)
        # self.source_arouseExcitation.valueChanged.connect(self.ParticleNameFun)
        # self.source_atomChargeQ.valueChanged.connect(self.ParticleNameFun)
        # self.source_atomMass.valueChanged.connect(self.ParticleNameFun)
        # self.source_atomNumZ.valueChanged.connect(self.ParticleNameFun)
        
        

    def totalMacFun(self):
        self.ParticlePosTotalFun()
        self.ParticleDirTotalFun()
        self.ParticleEnergyFun()
        self.ParticleNameFun()
        self.totalMac = "# out source mac script\n"
        self.totalMac = self.totalMac+"# List block\n"+self.MacScriptList+"\n"+"\n\n"         
        self.totalMac = self.totalMac+"# Paticle Name block\n"+ "/gps/particle"+" "+self.ParticleNameValue+"\n"+"\n\n"       
        self.totalMac = self.totalMac+"# Paticle Position block\n"+"/gps/position"+" "+self.ParticlePosTotalValue+"\n"+"\n\n"          
        self.totalMac = self.totalMac+"# Paticle Direction block\n"+"/gps/direction"+" "+self.ParticleDirTotalValue+"\n"+"\n\n"         
        self.totalMac = self.totalMac+"# Paticle Energy block\n"+"/gps/energy"+" "+self.ParticleEnergyValue+"\n"+"\n\n"  

# 定义preview function
    def preview(self):
        self.totalMacFun()
        print("preview")
        self.OutGPSMacBro.setText(self.totalMac)

# save function
    def savefile(self):
        print("save file")
        self.totalMacFun()
        with open("gps.mac",'w') as file:
            file.write(self.totalMac)
        print("finished!")

# list function
    def list(self):
        if self.GPSListCheckBox.isChecked():
            self.MacScriptList="/gps/List"
            print(self.MacScriptList)
        else:
            self.MacScriptList=""
            print("script canceled!")


# ParticleDirection function
# ParticleDirection function
# ParticleDirection function
    def ParticleDirXFun(self):
         self.ParticleDirXValue=self.ParticleDirX.value()
         print(self.ParticleDirXValue)

    def ParticleDirYFun(self):
         self.ParticleDirYValue=self.ParticleDirY.value()
         print(self.ParticleDirYValue)

    def ParticleDirZFun(self):
         self.ParticleDirZValue=self.ParticleDirZ.value()
         print(self.ParticleDirZValue)
    
    def ParticleDirTotalFun(self):
        self.ParticleDirXFun()
        self.ParticleDirYFun()
        self.ParticleDirZFun()
        self.ParticleDirTotalValue=str(self.ParticleDirXValue)+" "+str(self.ParticleDirYValue)+" "+str(self.ParticleDirZValue)+" "
        
# ParticleEnergy function
    def ParticleEnergyUnitFun(self):
        self.ParticleEnergyUnitsValue=self.ParticleEnergyUnit.currentText()
        #print(self.ParticleEnergyUnitsValue)

    def ParticleEnergyFun(self):
        self.ParticleEnergyUnitFun()
        self.ParticleEnergyValue=str(self.ParticleEnergy.value())+" "+self.ParticleEnergyUnitsValue

# ParticlePosition function
# ParticlePosition function
    def ParticlePosXFun(self):
         self.ParticlePosXValue=self.ParticlePosX.value()
         print(self.ParticlePosXValue)

    def ParticlePosYFun(self):
         self.ParticlePosYValue=self.ParticlePosY.value()
         print(self.ParticlePosYValue)

    def ParticlePosZFun(self):
         self.ParticlePosZValue=self.ParticlePosZ.value()
         print(self.ParticlePosZValue)

    def ParticlePosTotalFun(self):
        self.ParticlePosXFun()
        self.ParticlePosYFun()
        self.ParticlePosZFun()
        self.ParticlePosTotalValue=str(self.ParticlePosXValue)+" "+str(self.ParticlePosYValue)+" "+str(self.ParticlePosZValue)+" "
    
    def ParticleNameFun(self):
        print("testfffff")
        if self.ParticleNameNormal.isChecked():
            self.ParticleNameValue=self.ParticleName_2.currentText()
            print(self.ParticleName_2.currentText())
        elif self.ParticleNameIon.isChecked():
            self.ParticleNameValue=str(self.source_atomNumZ.value())+" "+str(self.source_atomMass.value())+" "+str(self.source_atomChargeQ.value())+" "+str(self.source_arouseExcitation.value())
        
            
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    # 设置窗口标题
    w.setWindowTitle("GunSourceGeneration")
    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()

