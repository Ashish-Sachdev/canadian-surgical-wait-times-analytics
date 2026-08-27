# Source loaders

Create one loader per source family, for example `cihi_priority.py`, `bc_open_data.py` and `ns_socrata.py`. A loader reads an immutable raw file and writes an interim table without silently changing suppression or definitions.
