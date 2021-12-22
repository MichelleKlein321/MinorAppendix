def performAnalysis(options):
    infile = open(options.inf, "r")
    compare = open(options.comp, "r")
    outfile = open(options.outf, "w")

    # This file extracts the data of the genes which are both in the input vcf file as in the burden output infile
    # To reduce the size of the file and filter only the mutations of interest

    # Extract the genes from the file generated in step 1
    Gene = []
    for line in compare:
        Gene.append(line)
    Gene = list(map(lambda s: s.strip(), Gene))

    # This step extracts the Gene names out of the input vcf file and
    # If the Gene names are equal to the Genes in the compare file, write the line of the input file to the outfile
    for lines in infile:
        if lines.startswith('#'):
            outfile.write(lines)
            continue
        line = lines.split("\t")

        # In some files, not the full line is available and therefore the gene name is in a different location
        if len(line) > 14:
            Genes = line[16]
            Genes = Genes.split(',')

            # Some files contain 1, 2 or more genes, besides the format differs
            # It can either be 'Gene', 'Gene;Gene' or 'Gene(ENSG*)'
            # from all possible formats an attempt has been made to filter the gene name

            # if len == 1
            if len(Genes) == 1:

                # If Gene name contains '('
                if '(' in Genes[0]:
                    # AND Gene name contains ';'
                    if ';' in Genes[0]:
                        Genes = Genes[0]
                        Genes = Genes.split(';')
                        Genes = Genes[0]
                        for j in Gene:
                            if Genes == j:
                                outfile.write(lines)
                    else:
                        Genes = Genes[0]
                        Genes = Genes.split('(')
                        Genes = Genes[0]
                        for j in Gene:
                            if Genes == j:
                                outfile.write(lines)

                # Gene name does not contain '(' and len == 1
                else:
                    for i in Genes:
                        i = i.replace('"', "")
                        for j in Gene:
                            if i == j:
                                outfile.write(lines)

            # if len > 1
            else:

                # If Gene name contains '('
                if '(' in Genes[0]:
                    # AND Gene name contains ';'
                    if ';' in Genes[0]:
                        Genes = Genes[0]
                        Genes = Genes.split(';')
                        Genes = Genes[0]
                        for j in Gene:
                            if Genes == j:
                                outfile.write(lines)
                    else:
                        Genes = Genes[0]
                        Genes = Genes.split('(')
                        Genes = Genes[0]
                        for j in Gene:
                            if Genes == j:
                                outfile.write(lines)

                # Gene name does not contain '(' and len > 1
                else:
                    for i in Genes:
                        i = i.replace('"', "")
                        for j in Gene:
                            if i == j:
                                outfile.write(lines)

        # When not the full line is available
        else:
            Genes = line[7]
            Genes = Genes.split('|')
            Genes = Genes[3]
            for j in Gene:
                if Genes == j:
                    outfile.write(lines)

    infile.close()
    compare.close()
    outfile.close()


if __name__ == '__main__':

    import optparse
    parser = optparse.OptionParser()
    parser.add_option('--inf', action='store', type='string', dest='inf', help='Spec..', default='')
    parser.add_option('--comp', action='store', type='string', dest='comp', help='Spec..', default='')
    parser.add_option('--outf', action='store', type='string', dest='outf', help='Spec..', default='')

    (options,args) = parser.parse_args()
    print("Starting analysis ....\n")

    performAnalysis(options)
    print("\nDone....")
