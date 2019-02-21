class circ_rloop_exon():

    def __init__(self,circ_id):

        self.circ_iso = circ_id
        self.chr = [x[2] for x in ownlist if x[1] == circ_id][0]
        self.circ_start = [int(x[3]) for x in ownlist if x[1] == circ_id][0]
        self.circ_end = [int(x[4]) for x in ownlist if x[1] == circ_id][0]
        self.circ_ori = [x[5] for x in ownlist if x[1] == circ_id][0]
        self.circ_exon = [x[6] for x in ownlist if x[1] == circ_id][0]
        self.circ_ss = [x[7] for x in ownlist if x[1] == circ_id][0]

        self.categ = "exon"
        self.r_loops()

        self.printing()
        #self.saving()


    def r_loops(self):

        self.rloop_ins_num = 0
        self.rloop_start_num = 0
        self.rloop_end_num = 0
        self.rloop_neigh_num = 0


        for j in xrange(0, len(nplist)):
            if np_chr[j] == self.chr and np_start[j] > self.circ_start and np_end[j] < self.circ_end:
                self.rloop_ins_num = self.rloop_ins_num +1

        for k in xrange(0, len(nplist)):
            if np_chr[k] == self.chr and np_start[k] == self.circ_start:
                self.rloop_start_num = self.rloop_start_num +1

        for l in xrange(0, len(nplist)):
            if np_chr[l] == self.chr and np_end[l] == self.circ_end:
                self.rloop_end_num = self.rloop_end_num +1

        for m in xrange(0, len(nplist)):
            if np_chr[m] == self.chr and (np_end[m] == self.circ_start or np_start[m] == self.circ_end):
                self.rloop_neigh_num = self.rloop_neigh_num +1



        return self.rloop_ins_num

    def printing(self):

        print self.chr, self.circ_iso, self.circ_start, self.circ_end, self.circ_ori, self.circ_exon, self.circ_ss, "R-loop", self.rloop_list

