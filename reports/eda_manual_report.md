## EDA for numerical data

### df_bandcamp_sales
#### Columns with continuous data
- 'utc_date': timestamps are in exponential format initially. 
- 'amount_paid_usd': users of Bandcamp can pay extra from the initial minimal price voluntarily to support the artists
#### Columns with descrete data
- 'art_id': IDs are always discrete

### df_discogs_artists
#### Columns with continuous data
- None
#### Columns with descrete data
- 'Unnamed: 0': IDs are always discrete
- 'artist_id': IDs are always discrete

### df_discogs_releases
#### Columns with continuous data
- None
#### Columns with descrete data
- 'release_id': IDs are always discrete
- 'year': If timestamp only contains year, then it is descrete

---

## EDA for categorical data

### df_bandcamp_sales
#### Columns with nominal values:
- '_id': unique identifier combining the sale's URL and UTC timestamp.
- 'url': web link.
- 'artist_name': name of the artist(s).
- 'album_title': name of the album if it is an album.
- 'country_code', 'country': geographic data.
- 'item_description': unique text for each item, can not be compared for ranking.
- 'item_type', 'slug_type': product type codes.
#### Columns with ordinal values:
- None.
- 'country_code', 'country' can be considered ordinal if aggregated by regions of the world. But this is not required in the business context for this project.

### df_discogs_artists
#### Columns with nominal values:
- 'artist_name': name of the artist(s).
#### Columns with ordinal values:
- 'artist_data_quality': values can be ordered from low quality to best quality. Not required in the context of this project.

### df_discogs_releases
#### Columns with nominal values:
- 'country': geographic data.
- 'format': 
- 'genre': hierarchy can not be set for a flat genre list. 
The task of ordering this data has taxonomy and classification level of complexity.

#### Columns with ordinal values:
- None

