
cdef extern from "../../headers/fpmain.h":
    void process_pdb(char *pdbname, s_fparams *params)

