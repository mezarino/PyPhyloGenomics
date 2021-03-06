import unittest
import os
from pyphylogenomics import BLAST
from pyphylogenomics import OrthoDB


class BLASTTest(unittest.TestCase):

    def setUp(self):
        self.genes = OrthoDB.single_copy_genes(
                "OrthoDB/OrthoDB6_Arthropoda_tabtext.csv", "Bombyx mori")
        self.genome = "BLAST/silkcds.fa"

    def test_get_cds(self):
        BLAST.get_cds(self.genes, "BLAST/silkcds.fa")
        f = open("pulled_seqs.fasta", "r")
        result = len(f.read())
        f.close()
        """Extracting genes and saving them as fasta file"""
        self.assertEqual(result, 63178)
        os.remove("pulled_seqs.fasta")

    def test_makeblastdb_true(self):
        mask = True
        BLAST.makeblastdb(self.genome, mask)
        for name in os.listdir("BLAST/"):
            if name[:10] == "silkcds.fa" and len(name) > 10:
                os.remove("BLAST/" + name)
                result = "true"
        self.assertEqual(result, "true")

    def test_makeblastdb_false(self):
        mask = False
        BLAST.makeblastdb(self.genome, mask)
        for name in os.listdir("BLAST/"):
            if name[:10] == "silkcds.fa" and len(name) > 10:
                os.remove("BLAST/" + name)
                result = "true"
        self.assertEqual(result, "true")

    def test_blastn(self):
        BLAST.blastn("BLAST/query.fas", "BLAST/silkcds.fa")
        file = open("BLAST/query_blastn_out.csv", "r").readlines()
        result = file[0].split(",")[1]
        for name in os.listdir("BLAST/"):
            if name[:10] == "silkcds.fa" and len(name) > 10:
                os.remove("BLAST/" + name)
        self.assertEqual(result, "BGIBMGA000001-TA")

    def test_getLargestExon(self):
        exons = BLAST.getLargestExon("BLAST/query_blastn_out.csv", 
                E_value=0.001, ident=98, exon_len=300)
        result = len(exons)
        self.assertEqual(result, 38)

    def test_eraseFalsePosi(self):
        exons = BLAST.getLargestExon("BLAST/query_blastn_out.csv", 
                E_value=0.001, ident=98, exon_len=300)
        exons = BLAST.eraseFalsePosi(exons)
        result = len(exons)
        self.assertEqual(result, 3)

    def test_wellSeparatedExons(self):
        exons = BLAST.getLargestExon("BLAST/query_blastn_out.csv", 
                E_value=0.001, ident=98, exon_len=300)
        exons = BLAST.eraseFalsePosi(exons)
        exons = BLAST.wellSeparatedExons(exons)
        result = len(exons)
        self.assertEqual(result, 3)
        os.remove("BLAST/query_blastn_out.csv")

    # todo BLAST.storeExonsInFrame

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity = 2)
    unittest.main(testRunner=runner)

