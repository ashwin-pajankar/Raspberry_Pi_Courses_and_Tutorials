from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

sys.stdout.write("Rank: %d," % rank)
sys.stdout.write(" Process Count: %d\n" % size)

