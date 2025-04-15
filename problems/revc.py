def reverse_complement(dna_string):
    """
    https://rosalind.info/problems/revc/
    Rosalind problem 3: Given a DNA string consisting of characters
    A - adenine
    C - cytosine
    G - guanine
    T - thymine
    return a string in reverse order with
    A replaced by T
    C replaced by G
    G replaced by C
    T replaced by A
    
    Args:
        dna_string: string of characters A, C, G and T

    Raises:
        Exception: if the string contains an invalid character

    Returns:
        reverse complement of the input DNA string
    """
    rcomp = ""
    for char in reversed(dna_string):
        if char == 'A':
            rcomp += 'T'
        elif char == 'C':
            rcomp += 'G'
        elif char == 'G':
            rcomp += 'C'
        elif char == 'T':
            rcomp += 'A'
        else:
            raise Exception(char + " is not a nucleotide")
    return rcomp
