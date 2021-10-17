START_CODON = "AUG"

DNA_MOLECULES = ["A", "T", "C", "G"]

MOLECULES_REPLACING_DICT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

CODON_TABLE = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


def get_encoded_protein_string(rna_sequence):
    encoded_protein = ""

    position = rna_sequence.find(START_CODON)
    # print("Position: " + str(position))

    if position < 0:
        return encoded_protein
    else:
        for i in range(position + 3, len(rna_sequence), 3):

            codon = rna_sequence[i:i + 3]
            # print(codon)

            if CODON_TABLE[codon] == "Stop":
                break
            else:
                encoded_protein += CODON_TABLE[codon]

    return encoded_protein


def replace_dna_molecules(dna_sequence):
    dna_seq_list = []
    for i in dna_sequence:
        dna_seq_list.append(MOLECULES_REPLACING_DICT[i])

    return ''.join(dna_seq_list)


def is_valid_dna_sequence(dna_sequence):
    for molecule in dna_sequence:
        if molecule not in DNA_MOLECULES:
            return False

    return True


def convert_to_rna_sequence(sequence):
    return sequence.replace("T", "U")


if __name__ == "__main__":

    # Valid Sequence
    given_sequence = "CGTTATACAAGTATCTGCTCAATTAGTCGACT"

    # Invalid Sequence
    # given_sequence = "TTTATGTAGGTAATGAATGAGG"

    print("Given DNA Sequence: " + given_sequence)

    if is_valid_dna_sequence(given_sequence):

        # First: Replace A -> T & C -> G. And Vice Versa
        replaced_dna_molecules = replace_dna_molecules(given_sequence)
        print("Replaced DNA Sequence: " + replaced_dna_molecules)

        # Second: Replace T -> U
        converted_rna_seq = convert_to_rna_sequence(replaced_dna_molecules)
        print("Converted RNA Sequence: " + converted_rna_seq)

        # Third: Get code from CODON table
        encoded_protein = get_encoded_protein_string(converted_rna_seq)
        if encoded_protein == "":
            print("\nInvalid DNA sequence")
        else:
            print("\nThe Encoded Protein String: " + encoded_protein)

    else:
        print("Given DNA sequence is not valid")
