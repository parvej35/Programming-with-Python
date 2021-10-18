dns_sequence = "GATGGAACTTGACTACGTAAATT "

"""
    DNA -> RNA Transcription. 
    Replacing Thymine (T) with Uracil (U) 
"""
rna_sequence = dns_sequence.replace("T", "U")

print("DNA Sequence: " + dns_sequence)
print("RNA Sequence: " + rna_sequence)
