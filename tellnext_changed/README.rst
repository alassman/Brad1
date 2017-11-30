tellnext
========

Next word prediction using a Markov chain and trigram model.

TellNext is a toy library and tool for predicting the next word in a sentence. It is a form of autocomplete, as seen in iOS and Android text input, where a list of candidate words is available for selection after entry of a word.

It currently only works with English words.


Quick Start
===========

Requires Python 3 (or PyPy 3 during training).

Dependencies::

    pip3 install -r requirements.txt

Train your language model::

    py -m tellnext_changed.tellnext --database MODEL.db train .\tellnext_changed\1.TXT .\tellnext_changed\2.TXT .\tellnext_changed\3.TXT .\tellnext_changed\4.TXT .\tellnext_changed\5.TXT .\tellnext_changed\6.TXT .\tellnext_changed\7.TXT .\tellnext_changed\8.TXT .\tellnext_changed\9.TXT .\tellnext_changed\Mockingbird.TXT

Train using Twitter Tweets::

   pypy3 -m tellnext --database MODEL.db train-twitter \
       archiveteam-twitter-spritzer-2012-03/
       archiveteam-twitter-spritzer-2013-08/

Get a list of predictions::

    python -m tellnext --database MODEL.db next i

Generate some sentences::

    python -m tellnext --database MODEL.db generate --lines 10


Credits
=======

Copyright 2014 Christopher Foo. License GPL 3.

