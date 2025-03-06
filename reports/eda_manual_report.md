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
- 'format': 57 unique values of format, including CD and Vinyl, can not be ordered.
- 'genre': hierarchy can not be set for a flat genre list. 
The task of ordering this data has taxonomy and classification level of complexity.

#### Columns with ordinal values:
- None

---

# Transforming data for consistency

## df_bandcamp_sales

### Interpreting columns 'item_type', 'slug_type': product type codes.

As we see from the auto-EDA output:

- Column "item_type" has 4 unique values.
  -- Unique values are:
 ['a' 'p' 't' 'b']

- Column "slug_type" has 3 unique values.
  -- Unique values are:
 ['a' 't' 'p' nan]

Both columns contain product type codes.
-- a: for albums; 
--- in 'item_type': a stands for all album types;
--- in 'slug_type': a stands only for digital albums;
-- t: for digital single tracks;
-- p: for physical items: merchendise or hard media (vynil/CD releases);
--- in 'item_type': p stands for all physical items;
--- in 'slug_type': p stands only for merch;
-- b: type-surprise, it was missing from the source description.

Comination | Product | Transformation notes
--- | --- | ---
Combination: ('a', 'a') | digital album only | Vynil is usually sold with digital included, should be summed up
Combination: ('t', 't') | digital single track | can be united with digital albums and saved as 'digital'
Combination: ('p', 'a') | CD or Vinyl | parse text from 'item_description' if not empty
Combination: ('p', 'p') | Merch or Bundle with CD / Vinyl | parse 'item_description', keep CD/Vinyl and drop all merch

### changes in data frame:
- new column: 'media_type' with values:
-- 'digital': for digital album and single track sales
-- 'CD': for hard media music sales, type CD
-- 'Vinyl': for hard media music sales, type CD
-- 'Cassette': surprise category, discovered accidentally in item descriptions
-- 'CD or Vinyl': for physical album sales (the ('p', 'a') case)

For finding Vinyl in item description the following cases are considered:
 - 'Vinyl'
 - 'LP', '2LP', etc
 - 'Double'
 - 'EP', 'EP2', 'EP3' etc.
 - '7' or '7"' (7-inch)
 - '12' or '12"' (12-inch)
 - '45RPM'
 - '33RPM'
 - 'Record'
 - 'Picture Disc' - Special edition vinyl releases

# Frequency table for df_bandcamp_sales ['media_type']

N | media_type | count
-- | --
0 | digital | 752599
1 | Vinyl | 107775
2 | CD | 39647
3 | CD or Vinyl | 23142
4 | Cassette | 22715

Donut chart has been created: see img/bandcamp_media_types.png

---

# Frequency table for df_discogs_artists["artist_data_quality"]

As we see from the auto-EDA output:
- Column "artist_data_quality" has 6 unique values.
   -- Unique values are:
 ['Needs Vote' 'Correct' 'Needs Major Changes' 'Complete and Correct'
 'Needs Minor Changes' 'Entirely Incorrect']

 They can be ordered by quality level, but this is not required in the context of the project.

N | artist_data_quality | count
0 | Needs Major Changes | 6014661
1 | Needs Vote | 2518536
2 | Correct | 657203
3 | Complete and Correct | 4211
4 | Needs Minor Changes | 260
5 | Entirely Incorrect | 36

Rows with with 'Entirely Incorrect' are removed from the dataframe.

---

# Frequency table for df_discogs_releases["genre"]

As we see from the auto-EDA output:

- Column "genre" has 15 unique values.
  -- Unique values are:
 ['Electronic' 'Hip Hop' 'Non-Music' 'Jazz' 'Rock' 'Latin' 'Funk / Soul'
 'Stage & Screen' 'Pop' 'Reggae' 'Folk, World, & Country' 'Classical'
 'Blues' 'Brass & Military' "Children's" nan]

Non-Music rows were dropped.

N | genre | count
0 | Rock | 4414291
1 | Electronic | 3491910
2 | Pop | 2546269
3 | Folk, World, & Country | 1507122
4 | Jazz | 1054791
5 | Funk / Soul | 922087
6 | Classical | 755037
7 | Hip Hop | 664307
8 | Latin | 504809
9 | Stage & Screen | 360972
10 | Reggae | 347399
11 | Blues | 284398
12 | Children's | 107230
13 | Brass & Military | 40996

Donut chart has been created: see img/

---

# Frequency table for df_discogs_releases["format"]

As we see from the auto-EDA output:
 - Column "format" has 57 unique values.

This is above treshold 20, so the list of values is not auto-generated.
Here it is:

['Vinyl', 'CD', 'Cassette', 'Box Set', 'All Media', 'File', 'Floppy Disk', 'Flexi-disc', 'DAT', 'Minidisc', 'DVD', 'Lathe Cut', 'CDV', 'Hybrid', 'VHS', 'Acetate', 'SACD', 'DVDr', 'Shellac', '8-Track Cartridge', 'MVD', 'Laserdisc', 'Reel-To-Reel', 'Memory Stick', 'Betamax', 'DCC', 'UMD', 'Microcassette', 'HD DVD', 'Blu-ray', 'Pathé Disc', 'Cylinder', 'DualDisc', 'Edison Disc', '4-Track Cartridge', 'VHD', 'Blu-ray-R', 'SelectaVision', 'U-matic', 'Film Reel', 'MiniDV', 'Video8', 'Betacam SP', 'PlayTape', 'Video 2000', 'Elcaset', 'Wire Recording', 'NT Cassette', 'Betacam', 'Tefifon', 'RCA Tape Cartridge', 'Pocket Rocker', 'DC-International', 'Sabamobil', 'Revere Magnetic Stereo Tape Ca', 'Cartrivision', 'HD DVD-R']


For the purpose of the project this needs to be reduced and simplified to match with 'media_type' from Bandcamp dataframe.

Chat_GPT has defined these categories and provided explanations:

🎵 1. Vinyl & Shellac Formats

Formats commonly used for analog records:
	•	Vinyl → Standard format for LPs, EPs, and singles.
	•	Shellac → Older format used for 78 RPM records.
	•	Lathe Cut → Custom-cut vinyl-like records, usually low-volume pressings.
	•	Acetate → Dubplates used for test pressings.
	•	Pathé Disc → Early shellac format.
	•	Edison Disc → Early disc records.

💿 2. Optical Discs (CD/DVD/Blu-ray)

Digital formats using laser-read technology:
	•	CD → Standard compact disc.
	•	CDV (CD Video) → Hybrid format with video and audio.
	•	SACD (Super Audio CD) → High-fidelity format for audiophiles.
	•	DVD / DVDr → Used for music videos, concerts.
	•	Blu-ray / Blu-ray-R → High-definition audio and video.
	•	HD DVD / HD DVD-R → Competing format with Blu-ray (now obsolete).
	•	DualDisc → CD on one side, DVD on the other.
	•	Laserdisc → Large disc format for music videos.

📼 3. Magnetic Tape (Cassettes, Reel, and Cartridges)

Analog and digital magnetic tape storage:
	•	Cassette → Standard analog compact cassette.
	•	Microcassette → Smaller version, sometimes used for music.
	•	Elcaset → Larger high-quality cassette format.
	•	NT Cassette → Digital cassette format.
	•	DCC (Digital Compact Cassette) → Digital cassette by Philips.
	•	8-Track Cartridge → Popular format in the 70s.
	•	4-Track Cartridge → Predecessor to 8-Track.
	•	Reel-To-Reel → Professional high-quality analog tape.
	•	Wire Recording → Early magnetic wire format.

🎥 4. Video-Based Formats (VHS, Betamax, etc.)

Formats primarily used for music videos:
	•	VHS / Video 2000 → Analog videotape for music concerts.
	•	Betamax / Betacam / Betacam SP → Sony’s tape format.
	•	U-matic → Professional videotape format.
	•	MiniDV / Video8 → Digital video cassette.
	•	VHD / SelectaVision → Video disc formats.

📀 5. Digital File-Based Media

Solid-state storage & non-physical formats:
	•	File → Digital-only music.
	•	Memory Stick → Sony’s flash storage.
	•	Pocket Rocker → Mini digital player format.
	•	UMD (Universal Media Disc) → Sony’s disc format for PSP.

📼 6. Experimental & Rare Formats

Lesser-known or short-lived formats:
	•	Floppy Disk → Used for some music distribution.
	•	Flexi-disc → Thin vinyl-like format in magazines.
	•	DAT (Digital Audio Tape) → Digital tape for professional use.
	•	MVD (Music Video Disc) → Experimental format.
	•	Tefifon → Tape-based record format.
	•	RCA Tape Cartridge → Proprietary RCA format.
	•	Sabamobil / Cartrivision → Rare cartridge-based formats.
	•	Revere Magnetic Stereo Tape Cartridge → Obscure tape format.





