============
django-erroneous
============

View all Django errors from right within the administration console.

Erroneous traps Django's in-built exception signal, captures the traceback . which would be the same beautiful exception page that Django displays when debugging is enabled . and saves it to the database so you can view it later.

It's quite similar to django-sentry from the folks at Disqus but a more lightweight, no-frills, error-logging system for Django. Credits to David Cramer over at Disqus for the initial django-db-log which is the work this is based upon.

If there's a feature that you're missing and you'd like added, please create an issue on the project page at Github or create the fix yourself and send me a pull request. Adding a few small features here and there are okay but this is in no way aimed to encompass all the functionality of a full-blown error-logging stack like Sentry.

See original repository for more documentation.

============
Version
============
This fork was updated to work with django as of version 3.2