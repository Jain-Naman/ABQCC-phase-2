import numpy as np
import sys

def read_pdos_file(filename):
    """
    Reads a PDOS file and returns the energy and PDOS values as numpy arrays.
    Assumes the format is:
    energy   ldos pdos_value_1   pdos_value_2 ... pdos_value_n
    """
    data = np.loadtxt(filename)
    energy = data[:, 0]
    ldos = data[:, 1]
    return energy, ldos

def sum_pdos(filenames):
    """
    Sums the PDOS data from multiple files.
    
    Parameters:
    filenames (list): List of filenames containing PDOS data.
    
    Returns:
    energy (numpy array): The energy values (assumed to be the same in all files).
    pdos_sum (numpy array): The summed PDOS values.
    """
    energy, pdos_sum = read_pdos_file(filenames[0])  # Read the first file
    # pdos_sum = np.pad(pdos_sum, ((0, 0), (0, 4 - pdos_sum.shape[1])), 'constant')
    # Loop through the remaining files and sum the PDOS values
    for filename in filenames[1:]:
        print(filename)
        _, pdos = read_pdos_file(filename)
        # pdos = np.pad(pdos, ((0, 0), (0, 4 - pdos.shape[1])), 'constant')
        pdos_sum += pdos  # Sum the PDOS values

    return energy, pdos_sum

def write_summed_pdos(output_file, energy, pdos_sum):
    """
    Writes the summed PDOS data to a file.
    
    Parameters:
    output_file (str): The name of the output file.
    energy (numpy array): Array of energy values.
    pdos_sum (numpy array): Array of summed PDOS values.
    """
    data = np.column_stack((energy, pdos_sum))
    np.savetxt(output_file, data, header="Energy    Summed_PDOS", fmt="%12.6f")

if __name__ == "__main__":
    # List of PDOS files to sum (these would be your input files)
    m = '''MgAl2Cu_pdos.dat.pdos_atm#1(H)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#2(H)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#3(C)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#3(C)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#4(C)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#4(C)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#5(H)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#6(C)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#6(C)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#7(C)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#7(C)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#8(H)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#9(C)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#9(C)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#10(C)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#10(C)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#11(N)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#11(N)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#12(N)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#12(N)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#13(H)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#14(N)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#14(N)_wfc#2(p)'''

    n = '''MgAl2Cu_pdos.dat.pdos_atm#14(N)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#14(N)_wfc#2(p)'''

    al = '''MgAl2Cu_pdos.dat.pdos_atm#15(Al)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#15(Al)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#16(Al)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#16(Al)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#17(Al)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#17(Al)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#18(Al)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#18(Al)_wfc#2(p)'''

    mg_cu = '''MgAl2Cu_pdos.dat.pdos_atm#19(Mg)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#19(Mg)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#20(Mg)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#20(Mg)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#21(Mg)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#21(Mg)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#22(Mg)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#22(Mg)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#23(Cu)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#23(Cu)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#23(Cu)_wfc#3(d)
    MgAl2Cu_pdos.dat.pdos_atm#24(Cu)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#24(Cu)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#24(Cu)_wfc#3(d)
    MgAl2Cu_pdos.dat.pdos_atm#25(Cu)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#25(Cu)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#25(Cu)_wfc#3(d)
    MgAl2Cu_pdos.dat.pdos_atm#26(Cu)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#26(Cu)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#26(Cu)_wfc#3(d)'''

    cu = '''MgAl2Cu_pdos.dat.pdos_atm#23(Cu)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#23(Cu)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#23(Cu)_wfc#3(d)
    MgAl2Cu_pdos.dat.pdos_atm#24(Cu)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#24(Cu)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#24(Cu)_wfc#3(d)
    MgAl2Cu_pdos.dat.pdos_atm#25(Cu)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#25(Cu)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#25(Cu)_wfc#3(d)
    MgAl2Cu_pdos.dat.pdos_atm#26(Cu)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#26(Cu)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#26(Cu)_wfc#3(d)'''

    al_only_n = '''MgAl2Cu_pdos.dat.pdos_atm#18(Al)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#18(Al)_wfc#2(p)'''

    mg = '''MgAl2Cu_pdos.dat.pdos_atm#19(Mg)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#19(Mg)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#20(Mg)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#20(Mg)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#21(Mg)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#21(Mg)_wfc#2(p)
    MgAl2Cu_pdos.dat.pdos_atm#22(Mg)_wfc#1(s)
    MgAl2Cu_pdos.dat.pdos_atm#22(Mg)_wfc#2(p)'''

    total = 'MgAl2Cu_pdos.dat.pdos_tot'

    # pdos_filenames = m.split("\n")
    # pdos_filenames = n.split("\n")
    # pdos_filenames = al.split("\n")
    # pdos_filenames = mg_cu.split("\n")
    # pdos_filenames = cu.split("\n")
    # pdos_filenames = al_only_n.split("\n")
    # pdos_filenames = mg.split("\n")
    pdos_filenames = total.split("\n")

    pdos_files = ["./data_original/"+s.strip() for s in pdos_filenames]
    # Output file to store the summed PDOS

    # output_file = "molecule_summed_pdos.dat"
    # output_file = "molecule_summed_ldos.dat"
    # output_file = "nitrogen_summed_ldos.dat"
    # output_file = "Al_summed_ldos.dat"
    # output_file = "MgCu_summed_ldos.dat"
    # output_file = "Cu_summed_ldos.dat"
    output_file = "Total_summed_ldos.dat"

    # Sum the PDOS data
    energy, pdos_sum = sum_pdos(pdos_files)

    # Write the summed PDOS data to the output file
    write_summed_pdos(output_file, energy, pdos_sum)

    print(f"Summed PDOS written to {output_file}")
