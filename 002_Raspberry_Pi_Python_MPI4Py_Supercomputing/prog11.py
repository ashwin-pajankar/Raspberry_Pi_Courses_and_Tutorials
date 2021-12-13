from mpi4py import MPI
import numpy as np
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = np.arange(100, dtype=np.float64)
    comm.Send(data, dest = 1, tag = 13)
    sys.stdout.write("Sent NumPy data from rank 0.\n")

elif rank == 1:
    data = np.empty(100, dtype=np.float64)
    comm.Recv(data, source = 0, tag = 13)
    sys.stdout.write("Received NumPy data at rank 1.\n")
