ROOT = ..
include ${ROOT}/defs.mk

refseqGeneDb = output/refseqGene.db

test: refGeneDbTests

####
refGeneDbTests: testRefGeneDbBuild

# call function 1 = test, 2 = table 3=order cols
sqliteDmp = sqlite3 -batch -separator $$'\t' -header output/$(1).db  'SELECT * FROM $(2) ORDER BY $(3)' > output/$(1)/$(2).tsv
comma = ,
sqliteDmpDiff = diff -u expected/$(1)/$(2).tsv output/$(1)/$(2).tsv

testRefGeneDbBuild: mkdirs
	rm -f output/$@.db
	${refseqGeneDbBuild} input/refseqGene output/$@.db
	mkdir -p output/$@
	$(call sqliteDmp,$@,gene2refseq,GeneID${comma}RNA_nucleotide_accession_version)
	$(call sqliteDmp,$@,gene_group,GeneID)
	$(call sqliteDmp,$@,gene_info,GeneID)
	$(call sqliteDmp,$@,gene_orthologs,GeneID)
	$(call sqliteDmpDiff,$@,gene2refseq)
	$(call sqliteDmpDiff,$@,gene_group)
	$(call sqliteDmpDiff,$@,gene_info)
	$(call sqliteDmpDiff,$@,gene_orthologs)

####
mkdirs:
	@mkdir -p output

clean:
	rm -rf output
