ROOT = ..
include ${ROOT}/defs.mk

ncbiGeneDb = output/ncbiGene.db

test: ncbiGeneDbTests

####
ncbiGeneDbTests: testNcbiGeneDbBuild testNcbiGeneTwoTables
	@echo "NOTE: use full-test to test build with the full gene database"

sqlite = sqlite3 -batch -separator $$'\t' -header

# call function 1 = test, 2 = table 3=order cols
sqliteDmp = ${sqlite} output/$(1).db  'SELECT * FROM $(2) ORDER BY $(3)' > output/$(1)/$(2).tsv
comma = ,
sqliteDmpDiff = diff -u expected/$(1)/$(2).tsv output/$(1)/$(2).tsv

testNcbiGeneDbBuild: mkdirs
	rm -f output/$@.db
	${ncbiGeneDbBuild} input/ncbiGene output/$@.db
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

testNcbiGeneTwoTables: mkdirs
	rm -f output/$@.db
	${ncbiGeneDbBuild} --table=gene_info --table=gene2refseq input/ncbiGene output/$@.db
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
full_ncbiGene_db = ${full_dir}/ncbiGene.db
full-test: ${full_download_dir}/done
	rm -f ${full_ncbiGene_db}
	time -p ${ncbiGeneDbBuild} --verbose ${full_download_dir} ${full_ncbiGene_db}

${full_download_dir}/done:
	@mkdir -p $(dir $@)
	cd ${full_download_dir} && wget -np -nv -nd -r -l 0 -A 'gene*.gz' --unlink -e robots=off https://ftp.ncbi.nih.gov/gene/DATA/
	touch $@


####
mkdirs:
	@mkdir -p output

clean:
	rm -rf output
