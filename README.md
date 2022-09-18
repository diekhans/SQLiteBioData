# SQLiteBioData

Tools to build SQLite3 database for various commonly used bioinformatics and
genomic databases. This project is focused on databases other than sequence
and sequence annotation datasets.

The goal is to convert the download files to SQLite3 tables with minimum data
transformations while creating useful SQLite3 databases. The data will remain
denormalized for the most part. The imported files are restructured only when
it is necessary to make SQL queries easier. For example, one-to-many and
many-to-many relationships. Additional derived fields for query purposes. For
example, adding columns with stable identifiers.

A separate database is produced for each supported resource, allowing one to
choose only the relevant datasets. The resulting SQLite3 database is designed
to be accessed read-only from any language with SQLite3 support. No additional
software is required.

The databases currently supported are

* NCBI Gene (partial)
