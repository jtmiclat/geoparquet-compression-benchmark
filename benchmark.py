import geopandas as gpd
import time
import os
import json


files = [
    "data/polygons.gpkg",
]
compressions = {
    "none": None,
    "snappy": "snappy",
    "gzip": "gzip",
    "brotli": "brotli",
    "zstd": "zstd",
    "lz4": "lz4",
}
benchmarks = []
for file in files:
    for name, compression in compressions.items():
        gdf = gpd.read_file(file, engine="pyogrio")
        start = time.process_time()
        file_cleaned = file.replace(".", "_")
        filename = f"{file_cleaned}_{name}.parquet"
        gdf.to_parquet(filename, compression=compression)
        end = time.process_time()
        write_time = end - start
        start = time.process_time()
        gdf2 = gpd.read_parquet(filename)
        end = time.process_time()
        read_time = end - start
        benchmarks.append(
            {
                "file": file,
                "compression": name,
                "size": os.path.getsize(filename),
                "write_time": write_time,
                "read_time": read_time,
            }
        )
        print(benchmarks[-1])
with open("benchmark.json", "w") as f:
    json.dump(benchmarks, f)
