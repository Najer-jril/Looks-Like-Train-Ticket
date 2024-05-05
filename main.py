import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from tubes import Ui_MainWindow 

class Locolink(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 450, 600)
        self.setFixedSize(400, 600)
        self.setWindowTitle("Locolink")
        self.setWindowIcon(QtGui.QIcon("logo.jpg"))
        self.stackedWidget.setCurrentIndex(0)
        self.btn_1.clicked.connect(self.pemesanan)
        self.btn_2.clicked.connect(self.konfirmasi)


        self.nama = ""
        self.jurusan = ""
        self.jenis_kelas = []

    def pemesanan(self):
        self.nama = self.lineEdit_Nama.text()

        self.jurusan = ""
        if self.checkBox_SRM.isChecked():
            self.jurusan += "Surabaya - Malang"
        if self.checkBox_SRJ.isChecked():
            self.jurusan += "Surabaya - Jogjakarta"

        self.jenis_kelas = []
        if self.checkBox_Ekonomi.isChecked():
            self.jenis_kelas.append("Ekonomi")
        if self.checkBox_Bisnis.isChecked():
            self.jenis_kelas.append("Bisnis")
        if self.checkBox_Premium.isChecked():
            self.jenis_kelas.append("Premium")

        jumlah_tiket = self.spinBox_JumlahTiket.value()
        harga_per_tiket = self.hitung_harga_per_tiket(self.jurusan, self.jenis_kelas)

        total_harga = jumlah_tiket * harga_per_tiket


        pesan = f"Lanjutkan Pembayaran?\n\nPembelian tiket untuk rute: {self.jurusan}\n"
        pesan += f"Kelas tiket: {', '.join(self.jenis_kelas)}\n\nTotal Harga: Rp. {total_harga}\n"

        msg = QMessageBox()
        msg.setText(pesan)
        msg.setWindowTitle("CONFIRMATION")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msg.exec()

        if returnValue == QMessageBox.Ok:
            self.pembayaran(self.nama, self.jurusan, self.jenis_kelas, jumlah_tiket, total_harga)
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.stackedWidget.setCurrentIndex(0)

    def hitung_harga_per_tiket(self, jurusan, jenis_kelas):
        if jurusan == "Surabaya - Malang":
            if "Ekonomi" in jenis_kelas:
                return 30000
            elif "Bisnis" in jenis_kelas:
                return 65000
            elif "Premium" in jenis_kelas:
                return 105000
        elif jurusan == "Surabaya - Jogjakarta":
            if "Ekonomi" in jenis_kelas:
                return 70000
            elif "Bisnis" in jenis_kelas:
                return 125000
            elif "Premium" in jenis_kelas:
                return 175000
        else:
            return 0

    def pembayaran(self, nama, jurusan, jenis_kelas, jumlah_tiket, total_harga):
        self.stackedWidget.setCurrentIndex(1)
        self.label_NamaPembeli.setText(nama)
        self.label_Jurusan.setText(jurusan)
        self.label_JenisKelas.setText(", ".join(jenis_kelas))
        self.label_HargaTiket.setText("Rp. {}".format(self.hitung_harga_per_tiket(jurusan, jenis_kelas[0])))
        self.label_JumlahTiket.setText(str(jumlah_tiket))
        self.label_JumlahTotalBayar.setText("Rp. {}".format(total_harga))

    def konfirmasi(self):
        jumlah_uang_pengguna = self.lineEdit_InputUang.text()
        print("jumlah uang pengguna", jumlah_uang_pengguna)

        if jumlah_uang_pengguna.isdigit():
            jumlah_uang_pengguna = int(jumlah_uang_pengguna)
            total_harga = int(self.label_JumlahTotalBayar.text().split(' ')[1])

            if jumlah_uang_pengguna < total_harga:
                msg = QMessageBox()
                msg.setText("Uang yang anda masukkan tidak mencukupi")
                msg.setWindowTitle("warning")
                msg.exec()
                return
            else:
                kembalian = jumlah_uang_pengguna - total_harga

            self.label_FinishPembeli.setText(self.nama)
            self.label_FinishRute.setText(self.jurusan)
            self.label_FinishKelas.setText(", ".join(self.jenis_kelas))
            self.label_JumlahUangPengguna.setText("Rp. {}".format(jumlah_uang_pengguna))
            self.label_kembalian.setText("Rp. {}".format(kembalian))

            self.stackedWidget.setCurrentIndex(2)
        else:
            QMessageBox.warning(self, "Error", "Masukkan jumlah uang yang valid!")

    def retranslateUi(self, MainWindow):
        return super().retranslateUi(MainWindow)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Locolink()
    main_window.show()
    sys.exit(app.exec_())
