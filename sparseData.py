import numpy as np
from scipy.sparse import csr_matrix
sharad = np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(sharad))

sharad = np.array([[0,0,0,],[0,0,1],[1,0,2]])
print(csr_matrix(sharad).data)

# what if we want to count nonzeros, we can do this via count_nonzero() method.
import numpy as np
from scipy.sparse import csr_matrix
sharad = np.array([[0,0,0,],[0,0,1],[1,0,2]])
print(csr_matrix(sharad).count_nonzero())

# For removing the zero elemements from the matrix we will use eliminate_zeros().
import numpy as np
from scipy.sparse import csr_matrix
sharad = np.array([[0,0,0,],[0,0,1],[1,0,2]])
sharadnew = csr_matrix(sharad)
sharadnew.eliminate_zeros()
print(sharadnew)

# eliminating duplicate entries with the sum_duplicates() method:
import numpy as np
from scipy.sparse import csr_matrix
sharad = np.array([[0,0,0,],[0,0,1],[1,0,2]])
sharadnew = csr_matrix(sharad)
sharadnew.sum_duplicates()
print(sharadnew)

# here we will convert csr to csc with the tocsc():
import numpy as np
from scipy.sparse import csr_matrix
sharad = np.array([[0,0,0,],[0,0,1],[1,0,2]])
sharadnew = csr_matrix(sharad).tocsc()
print(sharadnew)