"""
SQL states to create NCBI gene tables
"""

# note: can't define GeneID as PRIMARY KEY or it becomes the rowid

################################################################
# gene_info
################################################################
geneInfoCreateSql = """
DROP TABLE IF EXISTS gene_info;
CREATE TABLE gene_info (
    tax_id INT NOT NULL,
    GeneID INT NOT NULL,
    Symbol TEXT,
    LocusTag TEXT,
    Synonyms TEXT,
    dbXrefs TEXT,
    chromosome TEXT,
    map_location TEXT,
    description TEXT,
    type_of_gene TEXT NOT NULL,
    Symbol_from_nomenclature_authority TEXT,
    Full_name_from_nomenclature_authority TEXT,
    Nomenclature_status TEXT,
    Other_designations TEXT,
    Modification_date TEXT NOT NULL,
    Feature_type TEXT
);
"""

geneInfoIndexSql = """
CREATE INDEX gene_info_tax_id ON gene_info (tax_id);
CREATE UNIQUE INDEX gene_info_GeneId ON gene_info (GeneId);
CREATE INDEX gene_info_Symbol ON gene_info (Symbol);
CREATE INDEX gene_info_type_of_gene ON gene_info (type_of_gene);
"""

################################################################
# gene2refseq
################################################################
gene2refseqCreateSql = """
DROP TABLE IF EXISTS gene2refseq;
CREATE TABLE gene2refseq (
    tax_id INT NOT NULL,
    GeneID INT NOT NULL,
    status TEXT,
    RNA_nucleotide_accession_version TEXT,
    RNA_nucleotide_gi TEXT,
    protein_accession_version TEXT,
    protein_gi TEXT,
    genomic_nucleotide_accession_version TEXT,
    genomic_nucleotide_gi TEXT,
    start_position_on_the_genomic_accession TEXT,
    end_position_on_the_genomic_accession TEXT,
    orientation TEXT,
    assembly TEXT,
    mature_peptide_accession_version TEXT,
    mature_peptide_gi TEXT,
    Symbol TEXT NOT NULL,
    RNA_nucleotide_accession TEXT,      -- RNA_nucleotide_accession_version without version
    protein_accession TEXT,             -- protein_accession_version without version
    genomic_nucleotide_accession TEXT,  -- genomic_nucleotide_accession_version without version
    mature_peptide_accession TEXT,      -- mature_peptide_accession_version without version
    FOREIGN KEY(GeneID) REFERENCES gene_info(GeneID)
);
"""

gene2refseqIndexSql = """
CREATE INDEX gene2refseq_tax_id ON gene2refseq (tax_id);
CREATE INDEX gene2refseq_GeneId ON gene2refseq (GeneId);
CREATE INDEX gene2refseq_RNA_nucleotide_accession_version ON gene2refseq (RNA_nucleotide_accession_version);
CREATE INDEX gene2refseq_protein_accession_version ON gene2refseq (protein_accession_version);
CREATE INDEX gene2refseq_genomic_nucleotide_accession_version ON gene2refseq (genomic_nucleotide_accession_version);
CREATE INDEX gene2refseq_mature_peptide_accession_version ON gene2refseq (mature_peptide_accession_version);
CREATE INDEX gene2refseq_assembly ON gene2refseq (assembly);
CREATE INDEX gene2refseq_Symbol ON gene2refseq (Symbol);
CREATE INDEX gene2refseq_RNA_nucleotide_accession ON gene2refseq (RNA_nucleotide_accession);
CREATE INDEX gene2refseq_protein_accession ON gene2refseq (protein_accession);
CREATE INDEX gene2refseq_genomic_nucleotide_accession ON gene2refseq (genomic_nucleotide_accession);
CREATE INDEX gene2refseq_mature_peptide_accession ON gene2refseq (mature_peptide_accession);
"""

################################################################
# gene_group and gene_orthologs
################################################################

geneAssocCreateSql = """
DROP TABLE IF EXISTS {table};
CREATE TABLE {table} (
    tax_id INT NOT NULL,
    GeneID INT NOT NULL,
    relationship TEXT NOT NULL,
    Other_tax_id INT NOT NULL,
    Other_GeneID INT NOT NULL,
    FOREIGN KEY(GeneID) REFERENCES gene_info(GeneID),
    FOREIGN KEY(Other_GeneID) REFERENCES gene_info(GeneID)
);
"""

geneAssocIndexSql = """
CREATE INDEX {table}_tax_id ON {table} (tax_id);
CREATE INDEX {table}_GeneId ON {table} (GeneId);
CREATE INDEX {table}_Other_tax_id ON {table} (Other_tax_id);
CREATE INDEX {table}_Other_GeneId ON {table} (Other_GeneId);
"""
