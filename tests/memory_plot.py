from draw import ploting

# define methods
methods = ['six.bubble', 'six.heap', 'six.insert', 'six.merge', 'six.quick', 'six.shell', 'list.sort()']
memories = []

con = {
    'xlabel': 'name',
    'ylabel': 'memory / KB',
    'title': 'Sort by Two Keywords within Data Scale at 1000 * 10000'
}

# ploting
ploting(methods, memories, con, (1, 7))