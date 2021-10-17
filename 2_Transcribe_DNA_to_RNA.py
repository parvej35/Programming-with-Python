dns_sequence = "GATGGAACTTGACTACGTAAATT "
dns_sequence = dns_sequence.strip().upper()
rna_sequence = dns_sequence.replace("T", "U")

print("DNA Sequence: " + dns_sequence)
print("RNA Sequence: " + rna_sequence)
