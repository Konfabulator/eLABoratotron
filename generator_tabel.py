#LaTex table generator (for the results of the experiments)
from math import log10, floor
from tabulate import tabulate

column_names = [
    'Nr',
    '$f_{in}[Hz]$',
    '$U_{in}$[V]',
    '$\mathcal{U}_{U_{in}}$[V]',
    '$U_{out}$[V]',
    '$\mathcal{U}_{U_{out}}$[V]',
]

column_values = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],
    [ 1.5400, 1.4200, 1.2800, 1.1200, 1.0000, 0.9200, 0.8000, 0.7200, 0.6400, 0.5200, 0.4000, 0.3200, 0.2000, 0.1020, 0.0780, 0.0520, 0.0272, 0.0122,],
    [0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.010000000000000002, 0.0025000000000000005, 0.0025000000000000005, 0.001, 0.001, 0.00025],  
    [-13.4,-13.4,-12.5,-11.4,-10.2,-9.2,-8.4,-7.4,-6.2,-5.2,-4.4,-3.4,-1.96,-0.98,-0.76,-0.504,-0.256,-0.092],  
    [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.05, 0.025, 0.025, 0.010000000000000002, 0.010000000000000002, 0.0025000000000000005],    
]
cyfry_znaczace = 2
separator = ","                 #separator of decimal part

def round_to_n(x,n):
    try:
        return str(floor(x)) + separator + str('%s' % float(f'%.{n}g' % (x-floor(x))))[2:]
    except:
        return x
        
print("\\begin{center}")
print("\t\\textit{Tabela (x)} : Title\\\\")
print("\t\\begin{tabular}{||"+"l"*len(column_names)+"||}")
print("\t\\hline")
print("\t"+" & ".join(column_names)+"\\\\")
# print("\t\\hline")
rows = []
for i in range(len(column_values[0])):
    # row = ""
    row = []
    for j in range(len(column_values)):
        # if j == 0:
        #     row.append('\t\t'+round_to_n(column_values[j][i],cyfry_znaczace))
        # else:
        # row += round_to_n(column_values[j][i],cyfry_znaczace)+" & "	#add column value
        row.append(round_to_n(column_values[j][i],cyfry_znaczace))
    # print("\t\t"+row[:-2]+"\\\\")
    # rows.append("\t\t"+row[:-2]+"\\\\")
    rows.append(row)
# print rows list so that columns are aligned by & using tabulate
aligned_table = tabulate(rows, tablefmt='latex_raw').replace('\n','\n\t')
aligned_table = aligned_table[aligned_table.find('\n')+1:]


print(aligned_table)


# print("\t\\hline")
# print("\t\\end{tabular}")
print("\\end{center}")
