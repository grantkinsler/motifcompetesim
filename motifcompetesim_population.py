from motifcompetesim_cell import Cell

class Population:

	def __init__(self,cells,motiflist,nr_motifs,nr_strands,nr_cells_with_motif):
		self.cells = cells
		self.motiflist = motiflist
		self.nr_motifs = self.count_motifs()
		self.nr_strands = self.count_strands()
		self.nr_cells_with_motif = self.count_cells_with_motif()

	def populate(self,numCells,motiflist,max_strand_nr):
		for cell_iterator in xrange(numCells):
			self.cells.append(Cell([],[],motiflist,max_strand_nr,'empty','empty','empty'))

	def update_counters(self):
		self.nr_motifs = self.count_motifs()
		self.nr_strands = self.count_strands()
		self.nr_cells_with_motif = self.count_cells_with_motif()

	def count_motifs(self):
		motif_count = [0] * len(self.motiflist)
		for cell in self.cells:
			for index in xrange(len(motif_count)):
				motif_count[index] = motif_count[index] + cell.motif_count()[index]
		return motif_count

	def count_strands(self):
		strand_count = 0
		for cell in self.cells:
			strand_count = strand_count + cell.nr_strands()
		return strand_count

	def count_cells_with_motif(self):
		cell_count = [0] * len(self.motiflist)
		for cell in self.cells:
			for index in xrange(len(cell_count)):
				if cell.has_motif[index] == True:
					cell_count[index] += 1
		return cell_count

	def returncontents(self):
		contents = []
		elong_contents = []
		for cell in self.cells:
			contents.append(cell.strands)
			elong_contents.append(cell.elongations)
		return contents, elong_contents


