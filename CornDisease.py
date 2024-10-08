import os
from UI import UI
from InferenceForwardChaining import InferenceForwardChaining
from Rule import Rule

def get_knowledge(file_path):
    rules = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()  # Menghapus karakter newline
                facts,conclusion = line.split('-')# Memisahkan fakta dan kesimpulan
                facts_list = facts.split(',')  # List fakta
                rules.append(Rule(facts_list, conclusion))
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except IOError:
        print("Terjadi kesalahan saat membaca file.")
    return rules

if __name__ == "__main__":
    ui = UI()
    facts = 0
    opsi=ui.welcome()
    #Jika terindikasi dalam penyakit 1    
    if opsi==1 :
        ui.show_question(ui.bulai)
        facts = ui.get_bulai()
    elif opsi==2:
        ui.show_question(ui.blight)
        facts = ui.get_blight()
    elif opsi==3:
        ui.show_question(ui.leafRust)
        facts = ui.get_leafRust()
    elif opsi==4:
        ui.show_question(ui.burn)
        facts = ui.get_burn()
    elif opsi==5:
        ui.show_question(ui.stemBorer)
        facts = ui.get_stemBorer()
    elif opsi==6:
        ui.show_question(ui.cobBorer)
        facts = ui.get_cobBorer()

    # Ambil knowledge base dari file
    file_path = "src/testData.txt"
    rules = get_knowledge(file_path)
    ##print(rules)
    # Terapkan forward chaining
    inferred_facts = InferenceForwardChaining.do_forward_chaining(rules, facts)

    # Tentukan apakah 'g' benar
    g_is_true = "g" in inferred_facts

    # Tampilkan kesimpulan
    ui.show_conclusion(g_is_true, facts, inferred_facts)
