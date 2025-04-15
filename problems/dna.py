def count_nucleotides(dna_string):
    """
    https://rosalind.info/problems/dna/
    Rosalind.info problem 1: Given a DNA string consisting of characters 
    'A' - adenine
    'C' - cytosine
    'G' - guanine
    'T' - thymine
    
    Count the number of each character and return a tuple of the results
    Args:
        dna_string: string consisting of letters A, C, G and T

    Raises:
        Exception: if one of the input characters is not one of A, C, G or T

    Returns:
        tuple (#A, #C, #G, #T) consisting of the number of each of the four characters in the string
    """
    Acount =  0
    Tcount = 0
    Ccount = 0
    Gcount = 0
    for char in dna_string:
        if char == 'A':
            Acount += 1
        elif char == 'T':
            Tcount += 1
        elif char == 'C':
            Ccount += 1
        elif char == 'G':
            Gcount += 1
        else:
            raise Exception(f"{char} is not a nucleotide")
    return Acount, Ccount, Gcount, Tcount
