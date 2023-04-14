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

|     | file               | compression |       size | write_time | read_time | compression_ratio | size_renamed |
| --: | :----------------- | :---------- | ---------: | ---------: | --------: | ----------------: | :----------- |
|   0 | data/polygons.gpkg | none        | 1315369042 |    15.7838 |   10.5932 |                 1 | 1.2 GB       |
|   1 | data/polygons.gpkg | snappy      |  780533978 |    21.0322 |   16.7709 |           1.68522 | 744.4 MB     |
|   2 | data/polygons.gpkg | gzip        |  599009828 |    58.3971 |    21.832 |           2.19591 | 571.3 MB     |
|   3 | data/polygons.gpkg | brotli      |  507856050 |    62.2907 |   21.2652 |           2.59004 | 484.3 MB     |
|   4 | data/polygons.gpkg | zstd        |  672104571 |    25.1084 |   19.6659 |           1.95709 | 641.0 MB     |
|   5 | data/polygons.gpkg | lz4         |  841515609 |    23.7573 |   18.9367 |            1.5631 | 802.5 MB     |
