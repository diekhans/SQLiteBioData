ROOT = ..
include ${ROOT}/defs.mk

refseqGeneDb = output/refseqGene.db

test: refGeneDbTests

####
refGeneDbTests: testRefGeneDbBuild

testRefGeneDbBuild: mkdirs
	rm -f output/$@.db
	${refseqGeneDbBuild} input/refseqGene output/$@.db

####
mkdirs:
	@mkdir -p output

clean:
	rm -rf output
