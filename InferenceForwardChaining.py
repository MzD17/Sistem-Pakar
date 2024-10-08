class InferenceForwardChaining:
    
    @staticmethod
    def do_forward_chaining(rules, facts):
        # Menerapkan forward chaining dengan deteksi loop
        inferred_facts = set()
        while True:
            #print("TESSSSSS")
            inferred = False
            for rule in rules:
                # Jika semua antecedent ada di dalam fakta dan consequent belum disimpulkan
                if set(rule.get_antecedent()).issubset(facts) and rule.get_consequent() not in inferred_facts:
                    facts.add(rule.get_consequent())
                    inferred_facts.add(rule.get_consequent())
                    inferred = True
                    break
            if not inferred:
                break
        return inferred_facts
