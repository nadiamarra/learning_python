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
