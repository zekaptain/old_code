from Bio import SeqIO
from Bio.Blast import NCBIWWW

my_query = SeqIO.read("cftr1.txt", format="fasta")
result_handle = NCBIWWW.qblast("blastn", "nt", my_query.seq)
blast_result = open("my_blast.xml", "w")
blast_result.write(result_handle.read())
blast_result.close()
result_handle.close()

from Bio.Blast import NCBIXML

E_VALUE_THRESH = 1e-20

for record in NCBIXML.parse(open("my_blast.xml")):
	if record.alignments: #skip queries with no matches
		for align in record.alignments:
			for hsp in align.hsps:
				if hsp.expect < E_VALUE_THRESH:
					print ("MATCH: %s " % align.title[:60])
					print (hsp.expect)
					print (hsp.query[:60])
					print (hsp.match[:60])
					print (hsp.sbjct[:60])
