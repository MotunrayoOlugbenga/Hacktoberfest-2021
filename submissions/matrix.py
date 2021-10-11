def calc_matrix_product(A,B):
  

    if len(A) !=len(B):
        print ('invalid matrix multiplication')
        return


    output=[[0 for y in range(len(B[0])) ]for x in range (len(A))]    
 
    # iterating by row of A
    for a in range(len(A)):

        # iterating by column by B
        for b in range(len(B[0])):

            # iterating by rows of B
            for c in range(len(B)):
                output[a][b] += A[a][c] * B[c][b]

    for r in output:
        print(r)