# Geoparquet Compression Comparision

Some benchmarks for geoparquet compressions

## Setup

```bash
wget -o http://download.geofabrik.de/asia/philippines-latest-free.shp.zip data/philippines.shp.zip
```

```bash
pip install poetry
poetry install
```

### Experiment

## Data

Shapes of buildings OSM Data for the Philippines

```python
>>> gdf.geom_type.value_counts()
Polygon         10587798
MultiPolygon         101
Name: count, dtype: int64
```

## Compression Algorithms

1. Uncrompressed
2. Snappy
3. GZIP
4. BROTLI
5. ZSTD
6. LZ4

## Experiemtn setup

Running on a M2 mac book air 521gb

## Results

### Summary

| compression | write_time | read_time | size_renamed | compression_ratio |
| :---------- | ---------: | --------: | :----------- | ----------------: |
| none        |    15.7838 |   10.5932 | 1.2 GB       |                 1 |
| snappy      |    21.0322 |   16.7709 | 744.4 MB     |           1.68522 |
| gzip        |    58.3971 |    21.832 | 571.3 MB     |           2.19591 |
| brotli      |    62.2907 |   21.2652 | 484.3 MB     |           2.59004 |
| zstd        |    25.1084 |   19.6659 | 641.0 MB     |           1.95709 |
| lz4         |    23.7573 |   18.9367 | 802.5 MB     |            1.5631 |
