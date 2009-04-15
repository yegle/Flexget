import logging
from filter_seen import FilterSeen

log = logging.getLogger('seenmovies')

class FilterSeenMovies(FilterSeen):

    """
        Prevents movies being downloaded twice.
        Works only on entries which have imdb url available.

        How duplicate movie detection works:
        1) Remember all imdb urls from downloaded entries.
        2) If stored imdb url appears again, entry is rejected.
    """

    def register(self, manager, parser):
        manager.register('seen_movies')

        # remember and filter by these fields
        self.fields = ['imdb_url']
        self.keyword = 'seen_movies'
        
    def feed_filter(self, feed):
        # strict method
        if feed.config['seen_movies']=='strict':
            for entry in feed.entries:
                if not 'imdb_url' in entry:
                    log.info('Rejecting %s because of missing imdb url' % entry['title'])
                    feed.reject(entry)
        # call super
        super(FilterSeenMovies, self).feed_filter(feed)