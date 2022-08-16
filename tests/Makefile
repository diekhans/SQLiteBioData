ROOT = ..
include ${ROOT}/defs.mk

refseqGeneDb = output/refseqGene.db

test: refGeneDbTests

####
refGeneDbTests: testRefGeneDbBuild testRefGeneTwoTables
	@echo "NOTE: use full-test to test build with the full gene database"

sqlite = sqlite3 -batch -separator $$'\t' -header

# call function 1 = test, 2 = table 3=order cols
sqliteDmp = ${sqlite} output/$(1).db  'SELECT * FROM $(2) ORDER BY $(3)' > output/$(1)/$(2).tsv
comma = ,
sqliteDmpDiff = diff -u expected/$(1)/$(2).tsv output/$(1)/$(2).tsv

testRefGeneDbBuild: mkdirs
	rm -f output/$@.db
	${refseqGeneDbBuild} input/refseqGene output/$@.db
	mkdir -p output/$@
	$(call sqliteDmp,$@,gene_info,GeneID)
	$(call sqliteDmp,$@,gene2refseq,GeneID${comma}RNA_nucleotide_accession_version)
	$(call sqliteDmp,$@,gene_group,GeneID)
	$(call sqliteDmp,$@,gene_orthologs,GeneID)
	$(call sqliteDmp,$@,gene2go,GeneID)
	$(call sqliteDmp,$@,pubmed_ref,id)
	$(call sqliteDmp,$@,gene2ensembl,GeneID)
	$(call sqliteDmpDiff,$@,gene_info)
	$(call sqliteDmpDiff,$@,gene2refseq)
	$(call sqliteDmpDiff,$@,gene_group)
	$(call sqliteDmpDiff,$@,gene_orthologs)
	$(call sqliteDmpDiff,$@,gene2go)
	$(call sqliteDmpDiff,$@,pubmed_ref)
	$(call sqliteDmpDiff,$@,gene2ensembl)

testRefGeneTwoTables: mkdirs
	rm -f output/$@.db
	${refseqGeneDbBuild} --table=gene_info --table=gene2refseq input/refseqGene output/$@.db
	mkdir -p output/$@
	${sqlite} output/$@.db 'SELECT name FROM sqlite_master where type="table" ORDER BY name' > output/$@.tables
	diff expected/$@.tables output/$@.tables
	$(call sqliteDmp,$@,gene_info,GeneID)
	$(call sqliteDmp,$@,gene2refseq,GeneID${comma}RNA_nucleotide_accession_version)
	$(call sqliteDmpDiff,$@,gene_info)
	$(call sqliteDmpDiff,$@,gene2refseq)

# need a FS with a lot of space
full_dir = /hive/users/markd/NCBI-SqlLite/full
full_download_dir = ${full_dir}/download
full_refseqGene_db = ${full_dir}/refseqGene.db
full-test: ${full_download_dir}/done
	rm -f ${full_refseqGene_db}
	time -p ${refseqGeneDbBuild} --verbose ${full_download_dir} ${full_refseqGene_db}

${full_download_dir}/done:
	@mkdir -p $(dir $@)
	cd ${full_download_dir} && wget -np -nv -nd -r -l 0 -A 'gene*.gz' --unlink -e robots=off https://ftp.ncbi.nih.gov/gene/DATA/
	touch $@


####
mkdirs:
	@mkdir -p output

clean:
	rm -rf output
