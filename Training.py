#   NAMA    : DHUKI DWI RACHMAN
#   KELAS   : IF39-13
#   NIM     : 1301154265


import xlrd
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure().gca(projection = '3d')

#   class data testing
class data :

    def __init__(self, x, y, z, label, g):
        self.x = x
        self.y = y
        self.z = z
        self.label = label
        self.g = g

#   class untuk meng-convert file .xlsx ke array (data training)
class databaseTrain :

    def getData(self):
        arraydata = list()
        book = xlrd.open_workbook("data_train_PNN.xlsx")
        sh = book.sheet_by_index(0)

        for i in range(sh.nrows):
            tempdata = data(sh.cell_value(i,0),sh.cell_value(i,1),sh.cell_value(i,2),sh.cell_value(i,3), 0)

            arraydata.append(tempdata)

        return arraydata

#   class untuk meng-convert file .xlsx ke array (data test)
class databaseTes :

    def getData(self):
        arraydata = list()
        book = xlrd.open_workbook("data_test_PNN.xlsx")
        sh = book.sheet_by_index(0)

        for i in range(sh.nrows):
            tempdata = data(sh.cell_value(i,0),sh.cell_value(i,1),sh.cell_value(i,2), 0, 0)

            arraydata.append(tempdata)

        return arraydata

# fungsi untuk membuat grafik scatter plot
def grafik(data_grafik):
    temp = list()
    temp = data_grafik

    for i in range(len(temp)):
        fig.scatter(temp[i].x, temp[i].y, temp[i].z, c='c', marker='o')

    fig.set_xlabel('X Label')
    fig.set_ylabel('Y Label')
    fig.set_zlabel('Z Label')

#   mendeklarasikan array yang di assign oleh data pada excel
databaseLatihan = list()
databaseUji = list()
databaseTrain = databaseTrain()
databaseTes = databaseTes()

databaseLatihan = databaseTrain.getData()
databaseUji = databaseTes.getData()

#   memasukan data ke fungsi grafik
grafik(databaseUji)

plt.show()

#   perhitungan utama dalam proses klasifikasi PNN
#   melakukan pengujian oleh data testing

for i in range(len(databaseUji)): #  data testing
    sum_0 = 0
    sum_1 = 0
    sum_2 = 0
    for j in range(len(databaseLatihan)) :  # melakukan modifikasi pada code dengan membatasi jumlah angka dibelakang koma, maksimal yaitu 10 angka

        # Rumus Gaussian =========================================================================
        databaseLatihan[j].g = float('{:.10f}'.format(math.exp(-((((databaseUji[i].x - databaseLatihan[j].x)**2)
                                                            +((databaseUji[i].y - databaseLatihan[j].y)**2)
                                                            +((databaseUji[i].z - databaseLatihan[j].z)**2))/(2*(0.1**2))))))
        # =========================================================================================

        # Perhitungan jumlah tiap label ==========================================================
        if (databaseLatihan[j].label == 0):
            sum_0 += databaseLatihan[j].g
        elif (databaseLatihan[j].label == 1):
            sum_1 += databaseLatihan[j].g
        elif (databaseLatihan[j].label == 2):
            sum_2 += databaseLatihan[j].g
        # =========================================================================================

    # Proses perbandingan nilai dari jumlah tiap label
    if (sum_0 > sum_1):
        if (sum_0 > sum_2):
            databaseUji[i].label = 0
        else:
            databaseUji[i].label = 2
    else :
        if (sum_1 > sum_2):
            databaseUji[i].label = 1
        else :
            databaseUji[i].label = 2
    #=================================================

#   Memasukannya ke file .txt
handle = open('Hasil_data_test_PNN.txt','w')

for i in range(len(databaseUji)):
    handle.write(str(databaseUji[i].x)+" "+str(databaseUji[i].y)
                 +" "+str(databaseUji[i].z)+" "+str(databaseUji[i].label)+"\n")

handle.close()