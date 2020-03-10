def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return dna1>dna2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    num_nucleotide=0

    for char in dna:
        if char==nucleotide:
            num_nucleotide+=1
    return num_nucleotide


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    for char in dna1:
        return dna2 in dna1


def is_valid_sequence(sequence):
    '''(str)->bool

    Return True if and only if the DNA sequence is valid (that is, it contains
    no characters other than 'A','T','C' and 'G')

    >>>is_valid_sequence('ATCGGC')
    True
    >>>is_valid_sequence('ATCFGC')
    False
    >>>is_valid_sequence('ATCATG')
    True
    >>>is_valid_sequence('NTCGGC')
    False
    '''

    num_not_nucleotides=0

    for char in sequence:
        if char not in 'ATCG':
            num_not_nucleotides+=1
    return num_not_nucleotides==0
            
      

def insert_sequence(seq1,seq2,index):

    '''(str,str,int)->str

    Return the DNA sequence obtained by inserting the second DNA sequence into
    the first DNA sequence at the given index.

    >>>insert_sequence('CCGG','AT',2)
    'CCATGG'
    >>>insert_sequence('TTCC','AA',0)
    'AATTCC'
    >>>insert_sequence('GCTA','TA',3)
    'GCTTAA'
    '''

    return seq1[:index]+seq2+seq1[index:]


def get_complement(nuc1):
    
    '''(str)->str

    Return the nucleotide's complement.

    >>>get_complement("A")
    'T'
    >>>get_complement("T")
    'A'
    >>>get_complement("C")
    'G'
    >>>get_complement("G")
    'C'
    '''

    if nuc1=="A":
        return "T"
    if nuc1=="T":
        return "A"
    if nuc1=="C":
        return "G"
    if nuc1=="G":
        return "C"


def get_complementary_sequence(seq):

    '''(str)->str

    Return the DNA sequence that is complementary to the given DNA sequence.

    >>>get_complementary_sequence("ATTA")
    'TAAT'
    >>>get_complementary_sequence("TATA")
    'ATAT'
    >>>get_complementary_sequence("CGGC")
    'GCCG'
    >>>get_complementary_sequence("GCAT")
    'CGTA'

    '''

    complementary_sequence=""

    for letter in seq:
        if letter=="A":
            complementary_sequence+="T"
        if letter=="T":
            complementary_sequence+="A"
        if letter=="C":
            complementary_sequence+="G"
        if letter=="G":
            complementary_sequence+="C"
    return(complementary_sequence)  

##    for letter in seq:
##        complementary_sequence+=get_complement(letter)
##    return complementary_sequence
