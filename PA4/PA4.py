# Deric Shaffer
# CS471 - PA4
# Due Date: March 22nd, 2023
# Purpose: Remove corrupted data from a file and return a cleaned/updated new file in Python

def main():
    # CONTROL-B and CONTROL-C ASCII values
    control_b = chr(2)
    control_c = chr(3)

    # indicator variable starter CONTROL-C
    flag = False
    
    # variables
    original = open("control-char.txt", 'r') # read example file
    updated = open("python-out.txt", 'w') # write to new output file

    for line in original:
        for i in range(len(line)):
            # when the first/starting CONTROL-C is found, update flag
            if line[i] == control_c and flag == False:
                flag = True

            # when the ending CONTROL-B is found, update flag and skip/continue to not write it to new file
            if line[i] == control_b and flag == True:
                flag = False
                continue
            
            # character in line is not part of the corrupted data, write to new/updated file
            if flag == False:
                updated.write(line[i])

    # close both open calls
    original.close()
    updated.close()

    # Confirmation Print Statement
    print("Data Removal is Done")

# function call
main()