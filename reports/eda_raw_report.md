================= df_bandcamp_sales =================
df_bandcamp_sales has shape (1000000, 15)

df_bandcamp_sales has numerical data in columns: ['utc_date', 'art_id', 'releases', 'amount_paid_usd']
- Column "utc_date" has 999990 unique values.
- Column "art_id" has 271430 unique values.
- Column "amount_paid_usd" has 5866 unique values.
- Column "releases" has 220 unique values.

df_bandcamp_sales has categorical data in columns: ['_id', 'item_type', 'country_code', 'country', 'slug_type', 'item_description', 'url', 'artist_name', 'album_title', 'amount_over_fmt', 'item_slug']
- Column "_id" has 1000000 unique values.
- Column "item_type" has 4 unique values.
  -- Unique values are:
 ['a' 'p' 't' 'b']
- Column "country_code" has 186 unique values.
- Column "country" has 186 unique values.
- Column "slug_type" has 3 unique values.
  -- Unique values are:
 ['a' 't' 'p' nan]
- Column "item_description" has 336985 unique values.
- Column "url" has 374473 unique values.
- Column "artist_name" has 159746 unique values.
- Column "album_title" has 103697 unique values.
- Column "amount_over_fmt" has 3084 unique values.
- Column "item_slug" has 156 unique values.

================= df_discogs_artists =================
df_discogs_artists has shape (9194907, 12)

df_discogs_artists has numerical data in columns: ['Unnamed: 0', 'aliases_name_id', 'artist_id', 'groups_name_id', 'members_name_id']
- Column "Unnamed: 0" has 9194907 unique values.
- Column "artist_id" has 9194907 unique values.
- Column "aliases_name_id" has 479617 unique values.
- Column "members_name_id" has 450795 unique values.
- Column "groups_name_id" has 449588 unique values.

df_discogs_artists has categorical data in columns: ['aliases_name', 'artist_data_quality', 'artist_name', 'artist_realname', 'groups_name', 'members_name', 'namevariations_name']
- Column "aliases_name" has 479615 unique values.
- Column "artist_data_quality" has 6 unique values.
  -- Unique values are:
 ['Needs Vote' 'Correct' 'Needs Major Changes' 'Complete and Correct'
 'Needs Minor Changes' 'Entirely Incorrect']
- Column "artist_name" has 9194896 unique values.
- Column "artist_realname" has 541891 unique values.
- Column "groups_name" has 449587 unique values.
- Column "members_name" has 450795 unique values.
- Column "namevariations_name" has 1582994 unique values.

================= df_discogs_releases =================
df_discogs_releases has shape (17246710, 5)

df_discogs_releases has numerical data in columns: ['release_id', 'year']
- Column "release_id" has 12867979 unique values.
- Column "year" has 132 unique values.

df_discogs_releases has categorical data in columns: ['country', 'genre', 'format']
- Column "country" has 281 unique values.
- Column "genre" has 15 unique values.
  -- Unique values are:
 ['Electronic' 'Hip Hop' 'Non-Music' 'Jazz' 'Rock' 'Latin' 'Funk / Soul'
 'Stage & Screen' 'Pop' 'Reggae' 'Folk, World, & Country' 'Classical'
 'Blues' 'Brass & Military' "Children's" nan]
- Column "format" has 57 unique values.

