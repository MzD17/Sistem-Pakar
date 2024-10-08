class Rule:
    def __init__(self, antecedent, consequent):
        # Menginisialisasi variabel antecedent dan consequent
        self.antecedent = antecedent  # antecedent adalah list of string
        self.consequent = consequent  # consequent adalah string

    def get_antecedent(self):
        return self.antecedent

    def get_consequent(self):
        return self.consequent

    def __repr__(self):
        # Representasi string untuk objek Rule
        return f"Rule(antecedent={self.antecedent}, consequent={self.consequent})"
