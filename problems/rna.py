def dna_to_rna(dna_string):
    """
    https://rosalind.info/problems/rna/
    Rosalind problem 2: Given a DNA string consisting of characters
    A - adenine
    C- cytosine
    G - guanine
    T - thymine
    Replace the character T with U, which corresponds to replacing the nucleotide thymine in DNA
    with the nucleotide uracil.
    
    Args:
        dna_string: string of characters A, C, G and T

    Returns:
        string with all occurrences of T replaced by U
    """
    rna_string = ""
    for char in dna_string:
        if char == 'T':
            rna_string += 'U'
        else:
            rna_string += char
    return rna_string
