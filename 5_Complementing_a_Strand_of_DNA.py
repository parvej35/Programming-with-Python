# http://rosalind.info/problems/revc/

DNA_MOLECULES = ["A", "T", "C", "G"]
MOLECULES_REPLACING_DICT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


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


if __name__ == "__main__":

    # Valid Sequence
    given_sequence = "AAAACCCGGT"
    print("Given DNA Sequence: " + given_sequence)

    if is_valid_dna_sequence(given_sequence):

        reverse_sequence = given_sequence[::-1]

        # Replace A -> T & C -> G. And Vice Versa
        replaced_dna_molecules = replace_dna_molecules(reverse_sequence)
        print("Complement of the given DNA Sequence: " + replaced_dna_molecules)

    else:
        print("Given DNA sequence is not valid")
