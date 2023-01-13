# replacer for string
def DNA_strand(dna):
    new_str= []
    for i in dna:
        if(i == 'A'):
            str1 = i.replace('A','T')
            new_str.append(str1)
        if (i == 'T'):
            str1 = i.replace('T', 'A')
            new_str.append(str1)
        if (i == 'G'):
            str1 = i.replace('G', 'C')
            new_str.append(str1)
        if (i == 'C'):
            str1 = i.replace('C', 'G')
            new_str.append(str1)

    return ''.join(new_str)
print(DNA_strand('ATTGC'))
pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])