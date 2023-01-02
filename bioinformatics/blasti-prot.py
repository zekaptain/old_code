from Bio import SeqIO
from Bio.Blast import NCBIWWW

my_query = SeqIO.read("EF1a.fasta", format="fasta")
result_handle = NCBIWWW.qblast("blastp", "pdb", my_query.seq)
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
					print ("LENGTH:", hsp.align_length)
					print ("IDENTITIES:", hsp.identities)
					print ("SCORE:", hsp.score)
					print ("GAPS:", hsp.gaps)
					print (hsp.query[0:80])
					print (hsp.match[0:80])
					print (hsp.sbjct[0:80])
					
