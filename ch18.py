import gzip

src_path = "deltas.gz"
src = gzip.open(src_path)

print src.read()
