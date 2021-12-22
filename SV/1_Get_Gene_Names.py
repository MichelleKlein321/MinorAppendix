def striplist(l):
    return([x.strip() for x in l])
#
def listToTabSep(listItems, sep='\t'):
    return sep.join(listItems)

def performAnalysis(options):
    infile = open(options.inf, "r")
    compare = open(options.comp, "r")
    outfile = open(options.outf, "w")
    outfileBurden = open(options.outfB, "w")
    outfileSV = open(options.outfSV, "w")
    input = options.input

    final_list = []

    if input == 'Gene1_exon':

        for line in infile:
            Test = line.split(",")
            Test[19] = Test[19].strip('" "')

            Gene_list = []

            if 'intron' in Test[19] or Test[19].startswith('.')  :
               continue
            if Test[19] not in Gene_list:
                Gene_list.append(Test[19])
                print(line)
                outfileSV.write(line)

            SV1_Gene = []

            for i in Gene_list:
                SV1_Gene = i.split("_")

            List = Gene_list + SV1_Gene


            SV1_Gene_list = []

            if len(List) == 2 or len(List) == 3:
                SV1_Gene_list.append(List[0])
                SV1_Gene_list.append(List[1])
            elif len(List) == 4 or len(List) == 5:
                SV1_Gene_list.append(List[0])
                SV1_Gene_list.append(List[1])
                SV1_Gene_list.append(List[3])
            elif len(List) == 6 or len(List) == 7:
                SV1_Gene_list.append(List[0])
                SV1_Gene_list.append(List[1])
                SV1_Gene_list.append(List[3])
                SV1_Gene_list.append(List[5])

            if SV1_Gene_list not in final_list:
                final_list.append(SV1_Gene_list)

    if input == 'Gene1_intron':

        for line in infile:
            # print(line)
            Test = line.split(",")
            Test[19] = Test[19].strip('" "')
            Test[45] = Test[45].strip('" "')

            Gene_list = []

            if Test[19].startswith('.')  :
               continue
            if line.startswith('SampleID'):
                outfileSV.write(line)
            if 'intron' in Test[19]:
                if Test[45].startswith('.'):
                    continue
                Gene_list.append(Test[19])
                outfileSV.write(line)

            SV1_Gene = []

            for i in Gene_list:
                SV1_Gene = i.split("_")

            List = Gene_list + SV1_Gene


            SV1_Gene_list = []

            if len(List) == 2 or len(List) == 3:
                SV1_Gene_list.append(List[0])
                SV1_Gene_list.append(List[1])
            elif len(List) == 4 or len(List) == 5:
                SV1_Gene_list.append(List[0])
                SV1_Gene_list.append(List[1])
                SV1_Gene_list.append(List[3])
            elif len(List) == 6 or len(List) == 7:
                SV1_Gene_list.append(List[0])
                SV1_Gene_list.append(List[1])
                SV1_Gene_list.append(List[3])
                SV1_Gene_list.append(List[5])

            if SV1_Gene_list not in final_list:
                final_list.append(SV1_Gene_list)

    if input == 'Gene2_exon':

        for line in infile:
            Test = line.split(",")
            Test[29] = Test[29].strip('" "')

            Gene_list = []


            if 'intron' in Test[29] or Test[29].startswith('.')  :
               continue
            if Test[29] not in Gene_list:
                Gene_list.append(Test[29])
                outfileSV.write(line)

            SV1_Gene = []

            for i in Gene_list:
                SV1_Gene = i.split("_")

            List = Gene_list + SV1_Gene


            SV1_Gene_list = []

            if len(List) == 2 or len(List) == 3:
                SV1_Gene_list.append(List[0])
                SV1_Gene_list.append(List[1])
            elif len(List) == 4 or len(List) == 5:
                SV1_Gene_list.append(List[0])
                SV1_Gene_list.append(List[1])
                SV1_Gene_list.append(List[3])
            elif len(List) == 6 or len(List) == 7:
                SV1_Gene_list.append(List[0])
                SV1_Gene_list.append(List[1])
                SV1_Gene_list.append(List[3])
                SV1_Gene_list.append(List[5])

            if SV1_Gene_list not in final_list:
                final_list.append(SV1_Gene_list)

    if input == 'Gene2_intron':

        for line in infile:
            Test = line.split(",")
            Test[29] = Test[29].strip('" "')
            Test[45] = Test[45].strip('" "')
            # print(Test[45])

            Gene_list = []

            if Test[29].startswith('.')  :
               continue
            if line.startswith('SampleID'):
                outfileSV.write(line)
            if 'intron' in Test[29]:
                if Test[45].startswith('.'):
                    continue
                Gene_list.append(Test[29])
                outfileSV.write(line)

            SV1_Gene = []

            for i in Gene_list:
                SV1_Gene = i.split("_")

            List = Gene_list + SV1_Gene


            SV1_Gene_list = []

            if len(List) == 2 or len(List) == 3:
                SV1_Gene_list.append(List[0])
                SV1_Gene_list.append(List[1])
            elif len(List) == 4 or len(List) == 5:
                SV1_Gene_list.append(List[0])
                SV1_Gene_list.append(List[1])
                SV1_Gene_list.append(List[3])
            elif len(List) == 6 or len(List) == 7:
                SV1_Gene_list.append(List[0])
                SV1_Gene_list.append(List[1])
                SV1_Gene_list.append(List[3])
                SV1_Gene_list.append(List[5])

            if SV1_Gene_list not in final_list:
                final_list.append(SV1_Gene_list)

    Burden_Genes = []
    for i in compare:
        if i.startswith('GENE'):
            continue
        Burden_line = i.split("\t")
        Burden_Genes.append(Burden_line[0])

    Genes_result = []
    Burden_Genes_result = []

    for i in final_list:
        for j in Burden_Genes:
            if len(i) == 2:
                if i[1] == j:
                    if i[0] not in Genes_result:
                        Genes_result.append(i[0])
                    if i[1] not in Genes_result:
                        Burden_Genes_result.append(i[1])
            if len(i) == 3:
                if i[1] == j:
                    if i[0] not in Genes_result:
                        Genes_result.append(i[0])
                    if i[1] not in Genes_result:
                        Burden_Genes_result.append(i[1])
                if i[2] == j:
                    if i[0] not in Genes_result:
                        Genes_result.append(i[0])
                    if i[2] not in Genes_result:
                        Burden_Genes_result.append(i[2])
            if len(i) == 4:
                if i[1] == j:
                    if i[0] not in Genes_result:
                        Genes_result.append(i[0])
                    if i[1] not in Genes_result:
                        Burden_Genes_result.append(i[1])
                if i[2] == j:
                    if i[0] not in Genes_result:
                        Genes_result.append(i[0])
                    if i[2] not in Genes_result:
                        Burden_Genes_result.append(i[2])
                if i[3] == j:
                    if i[0] not in Genes_result:
                        Genes_result.append(i[0])
                    if i[3] not in Genes_result:
                        Burden_Genes_result.append(i[3])


    for i in Genes_result:
        outfile.write(i + '\n')
    for i in Burden_Genes_result:
        outfileBurden.write(i + '\n')



if __name__ == '__main__':

    import optparse
    parser = optparse.OptionParser()
    parser.add_option('--inf', action='store', type='string', dest='inf', help='Spec..', default='')
    parser.add_option('--comp', action='store', type='string', dest='comp', help='Spec..', default='')
    parser.add_option('--outf', action='store', type='string', dest='outf', help='Spec..', default='')
    parser.add_option('--outfB', action='store', type='string', dest='outfB', help='Spec..', default='')
    parser.add_option('--outfSV', action='store', type='string', dest='outfSV', help='Spec..', default='')
    parser.add_option('--input', action='store', type='string', dest='input', help='Gene1_exon, Gene1_intron, Gene2_exon, Gene2_intron', default='')

    (options,args) = parser.parse_args()
    print("Starting analysis ....\n")
    # if len(options.outf) <1 or len(options.inf) <1:
    #     print("Wrong")
    #     print("Parameter settings")
    #     print(options)
    performAnalysis(options)
    print("\nDone....")
