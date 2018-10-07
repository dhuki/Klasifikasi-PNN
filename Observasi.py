#   NAMA    : DHUKI DWI RACHMAN
#   KELAS   : IF39-13
#   NIM     : 1301154265


import xlrd
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure().gca(projection = '3d')

#   class data testing
class hasill :

    def __init__(self, sum_0, sum_1 ,sum_2):
        self.sum_0 = sum_0
        self.sum_1 = sum_1
        self.sum_2 = sum_2

        if (self.sum_0 > self.sum_1):
            if (self.sum_0 > self.sum_2):
                self.label = 0
            else :
                self.label = 2
        else :
            if (self.sum_1 > self.sum_2):
                self.label = 1
            else :
                self.label = 2

#   class data train
class data :

    def __init__(self, x, y, z, label, g):
        self.x = x
        self.y = y
        self.z = z
        self.label = label
        self.g = g

#   class untuk meng-convert file .xlsx ke array
class databaseTrain :

    def getData(self):
        arraydata = list()
        book = xlrd.open_workbook("data_train_PNN.xlsx")
        sh = book.sheet_by_index(0)

        for i in range(sh.nrows):
            tempdata = data(sh.cell_value(i,0),sh.cell_value(i,1),sh.cell_value(i,2),sh.cell_value(i,3), 0)

            arraydata.append(tempdata)

        return arraydata

# fungsi untuk membuat grafik scatter plot
def grafik(data_grafik):
    temp = list()
    temp = data_grafik

    for i in range(140):
        fig.scatter(temp[i].x, temp[i].y, temp[i].z, c='r', marker='o')

    fig.set_xlabel('X Label')
    fig.set_ylabel('Y Label')
    fig.set_zlabel('Z Label')

#   mendeklarasikan array yang di assign oleh data pada excel
database = list()
datahasil = list()
databaseTrain = databaseTrain()

database = databaseTrain.getData()

#   memasukan data ke fungsi grafik
grafik(database)

plt.show()

#   perhitungan utama dalam proses klasifikasi PNN
#   melakukan observasi dari 10 data training terakhir yang dijadikan data testing untuk didapatkan hasil
#   klasifikasi yang optimal

for i in range(140,150): #  data training yang dijadikan data testing yaitu data ke - 140 sampai 150
    sum_0 = 0
    sum_1 = 0
    sum_2 = 0
    for j in range(140) : # melakukan modifikasi pada code dengan membatasi jumlah angka dibelakang koma, maksimal yaitu 10 angka
        # Rumus Gaussian =========================================================================
        database[j].g = float('{:.10f}'.format(math.exp(-((((database[i].x - database[j].x)**2)
                                    +((database[i].y - database[j].y)**2)
                                    +((database[i].z - database[j].z)**2))/(2*(0.1**2))))))
        #=========================================================================================

        # Perhitungan jumlah tiap label ==========================================================
        if (database[j].label == 0):
            sum_0 = sum_0 + database[j].g
        elif (database[j].label == 1):
            sum_1 += database[j].g
        elif (database[j].label == 2):
            sum_2 += database[j].g
        #=========================================================================================

    # Memasukan hasil penjumalahan tiap label ke class hasill
    hasil = hasill(sum_0,sum_1,sum_2)

    # Memasukannya ke array datahasil
    datahasil.append(hasil)

#   untuk menghitung persenan data yang benar terhadap data testing
total = 0.0
count = 140

for i in range(len(datahasil)):
    print datahasil[i].label
    if database[count].label == datahasil[i].label:
        total += 1
    count += 1

print "hasil: ",((total/10)*100)