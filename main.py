import glob

from DataManager import DataManager
from PlotGenerator import PlotGenerator
from ImageGenerator import ImageGenerator

path = 'D:/spotify-unwrapped-plots'

# Configure matplotlib
pg = PlotGenerator(path=path, style='./spotify.mplstyle')
dm = DataManager(glob.glob('D:/Documents/user-data/spotify/StreamingHistory[0-9].json'))

# Top artists by hours_played
top = dm.get_top_n_artists(20)
pg.top_artists_by_hours_streamed(top)


# Filter by hours
hour = dm.get_streamed_hours_by_time_of_day()
pg.streamed_hours_by_time_of_the_day(hour)

# Filter by day of week
day_of_the_week = dm.get_streamed_hours_by_day_of_week()
pg.streamed_hours_by_day_of_the_week(day_of_the_week)

# Cumsum by week (now it has a more decent implementation)
cumsum = dm.get_cumsum_by_week(10)
top_artists = list(dm.get_top_n_artists(10).index)
top_artists.reverse()

pg.cumsum_by_week(cumsum, top_artists)


# Get percent of hours played in top artists
hours = dm.get_percent_hours_played_in_top_artists(20)
pg.pie_top_streamed_artists(hours)

# Achievements
# Hours streaming all i want for christmas is you
# all_i_want_for_christmas_is_you = df[df.trackName == 'All I Want for Christmas Is You'].groupby('trackName')\
#                                                                 .agg({'hours_played': np.sum})\
#                                                                 .hours_played[0] # > 1

# # The definitive halloween experience
# streamed_thriller = df[(df.trackName == 'Thriller') & (df.artistName == 'Michael Jackson')]

# # Days that used
# streamed_every_day = df.groupby('date').size().size # == 365

# # Songs in top 100 spotify 2021

# # Streamed enemy from arcane
# # :(

# # Variety is the Spice of Life
# variety_is_the_spice_of_life = top_hours / total_hours # < 0.25

## GENERATE IMAGE
ig = ImageGenerator(size = (1500, 2000))
ig.add_font('title', 'gotham-medium.otf', 60)
ig.add_font('achievement-title', 'gotham-medium.otf', 24)
ig.add_font('achievement-body', 'gotham-medium.otf', 18)
ig.add_font('icons', 'font-awesome-5-free-solid-900.otf', 58)


# Draw title
ig.write_text('Spotify rewrapped', 'title', (0, 50), horizontal_center=True)

# Draw top played artists plot
ig.paste_image(f'{path}/top-artists.png', (25, 175))

# Draw top played artists plot
ig.paste_image(f'{path}/top-20-pie.png', (750, 175))

# Draw hourly plot
ig.paste_image(f'{path}/hourly-plot.png', (25, 550))

# Draw day of the week plot
ig.paste_image(f'{path}/day-of-the-week-plot.png', (750, 550))

# Draw artists through the year
ig.paste_image(f'{path}/artists-through-the-year.png', (25, 925))

#Achievements
ig.show_achievement(u'\uf7aa', (25, 1700), (100, 100), 'Christmas spirit', 'I streamed at least 1 hour of\nAll I Want for Christmas Is You by Mariah Carey\n({:.2f}/{:.1f})'.format(0.42360786, 1.0), False)
ig.show_achievement(u'\uf717', ((ig.W/2) + 25, 1700), (100, 100), 'The deffinitive Halloween experience', 'I streamed Thriller by Michael Jackson in 2021', True)
ig.show_achievement(u'\uf6d7', (25, 1850), (100, 100), 'Variety is the Spice of Life', 'Less than 30% of my total streams are from my\ntop 20 streamed artists', True)
ig.show_achievement(u'\uf274', ((ig.W/2) + 25, 1850), (100, 100), 'Everyday routine', 'I streamed at least one track every day of 2021', False)

# Save image
ig.save(f'{path}/spotify-rewrapped.png')
