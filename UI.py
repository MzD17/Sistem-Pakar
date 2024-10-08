class UI:
    def __init__(self):
        self.answers = [0] * 3  # Array dengan ukuran 4 untuk jawaban
        self.bulai = []  # Daftar untuk pertanyaan penyakit bulai
        self.blight = []  # Daftar untuk pertanyaan penyakit
        self.leafRust = []  # Daftar untuk pertanyaan penyakit
        self.burn = []  # Daftar untuk pertanyaan penyakit
        self.stemBorer = []  # Daftar untuk pertanyaan penyakit
        self.cobBorer = []  # Daftar untuk pertanyaan penyakit
        self.set_bulai()  # Inisialisasi pertanyaan
        self.set_blight()  # Inisialisasi pertanyaan
        self.set_leafRust()  # Inisialisasi pertanyaan
        self.set_burn()  # Inisialisasi pertanyaan
        self.set_stemBorer()  # Inisialisasi pertanyaan
        self.set_cobBorer()  # Inisialisasi pertanyaan

    def welcome(self):
        opsi=0
        print("=== Aplikasi Diagnosis Penyakit Tanaman Jagung ===")
        print("""Penyakit apa yang ingin anda prediksi:
              1.Bulai
              2.Hawar
              3.Karat Daun
              4.Burn
              5.Larva Pengerek Batang
              6.Larva Pengerek Bonggol""")
        print("Pilih opsi 1-6:")
        opsi=int(input())
        while opsi<0 and opsi>6:
            print("Masukan jawaban yang sesuai!")
            opsi=int(input())
        return opsi

    def show_question(self, questionList):
        # Menampilkan setiap pertanyaan dan menerima input dari pengguna
        i=0
        for q in questionList:
            print(q)
            print("0. Tidak    1. Ya")
            a = int(input())  # Menerima input sebagai integer
            while a != 0 and a != 1:
                print("Jawaban tidak sesuai!")
                a = int(input())
            self.answers[i] = a
            #print("number"+str(i))
            i += 1
                      
    def set_bulai(self):
        # Menambahkan pertanyaan ke dalam daftar pertanyaan bulai
        self.bulai.append("Apakah daun tanaman anda menguning?")
        self.bulai.append("Apakah daun tanaman melingkar?")
        self.bulai.append("Apakah pembentukan bonggol terganggu?")

    def get_bulai(self):
        facts=set()
        if self.answers[0] == 1:
            facts.add("1")
        if self.answers[1] == 1:
            facts.add("4")
        if self.answers[2] == 1:
            facts.add("5")
        return facts

    def set_blight(self):
        # Menambahkan pertanyaan ke dalam daftar pertanyaan penyakit blight
        self.blight.append("Apakah daun terlihat layu?")
        self.blight.append("Apakah tumbuhan memiliki bercak coklat elips?")
        self.blight.append("Apakah daun terlihat kering?")
    
    def get_blight(self):
        facts=set()
        if self.answers[0] == 1:
            facts.add("6")
        if self.answers[1] == 1:
            facts.add("9")
        if self.answers[2] == 1:
            facts.add("10")
        return facts


    def set_leafRust(self):
        # Menambahkan pertanyaan ke dalam daftar pertanyaan penyakit 2
        self.leafRust.append("Apakah ada bintik merah pada pelapah daun?")
        self.leafRust.append("Apakah ada bintik kuning pada daun?")
        self.leafRust.append("Apakah terlihat kering?")
     
    def get_leafRust(self):
        facts=set()
        if self.answers[0] == 1:
            facts.add("12")
        if self.answers[1] == 1:
            facts.add("11")
        if self.answers[2] == 1:
            facts.add("10")
        return facts
        
    def set_burn(self):
        # Menambahkan pertanyaan ke dalam daftar pertanyaan penyakit 3
        self.burn.append("Apakah terjadi pembengkakan pada bonggol?")
        self.burn.append("Apakah terdapat jamur berwarna putih sampai hitam pada biji")
        self.burn.append("Apakah biji membengkak")
     
    def get_burn(self):
        facts=set()
        if self.answers[0] == 1:
            facts.add("15")
        if self.answers[1] == 1:
            facts.add("16")
        if self.answers[2] == 1:
            facts.add("17")
        return facts 
        
    def set_stemBorer(self):
        # Menambahkan pertanyaan ke dalam daftar pertanyaan penyakit 4
        self.stemBorer.append("Apakah terdapat lubang kecil pada daun ?")
        self.stemBorer.append("Apakah terdapat celah pada batang?")
        self.stemBorer.append("Apakah terdapat tumpukan rumbai-rumbai yang patah?")
        #self.questions4.append("Apakah Anda mengalami 19?")
        #self.questions4.append("Apakah Anda mengalami 3?")
    
    def get_stemBorer(self):
        facts=set()
        if self.answers[0] == 1:
            facts.add("20")
        if self.answers[1] == 1:
            facts.add("21")
        if self.answers[2] == 1:
            facts.add("24")
        return facts
        
    def set_cobBorer(self):
        # Menambahkan pertanyaan ke dalam daftar pertanyaan penyakit 5
        self.cobBorer.append("Apakah rambbut jagung mengering?")
        self.cobBorer.append("Apakah sering terdapat larva?")
        #self.cobBorer.append("Apakah Anda mengalami 26?")
        
    def get_cobBorer(self):
        facts=set()
        if self.answers[0] == 1:
            facts.add("29")
        if self.answers[1] == 1:
            facts.add("31")
        return facts
        
    def show_conclusion(self, diagnosis, facts, inferred_facts):
        # Menampilkan semua fakta dan kesimpulan
        print("All facts:", facts)
        print("Inferred facts:", inferred_facts)
        if "a" in facts:
            print("Bulai terbukti benar")
        elif "b" in facts:
            print("Hawar terbukti benar")
        elif "c" in facts:
            print("Karat daun terbukti benar")
        elif "d" in facts:
            print("Burn terbukti benar")
        elif "e" in facts:
            print("Larva pengerek batang terbukti benar")
        elif "f" in facts:
            print("Larva pengerek bonggol terbukti benar")
        else:
            print("Penyakit pada tanaman tidak terbukti")