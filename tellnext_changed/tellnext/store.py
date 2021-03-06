import abc
import collections
import sqlite3
import random


class BaseStore(object, metaclass=abc.ABCMeta):
    def add_one(self, trigram):
        self.add_many((trigram,))

    @abc.abstractmethod
    def add_many(self, trigrams):
        pass

    @abc.abstractmethod
    def get_trigram_values(self, word_1, word_2):
        pass

    @abc.abstractmethod
    def count(self):
        pass

    @abc.abstractmethod
    def trim(self, target_count, min_probability_count=2):
        pass


class SQLiteStore(BaseStore):
    def __init__(self, path=':memory:', wal=False):
        self.connection = sqlite3.connect(path)
        if wal:
            self.connection.execute('PRAGMA journal_mode=WAL')
        self.connection.execute('PRAGMA synchronous=NORMAL')
        self.connection.execute(
            '''CREATE TABLE IF NOT EXISTS
            markov_model
            (
            word_1 TEXT NOT NULL,
            word_2 TEXT NOT NULL,
            word_3 TEXT NOT NULL,
            count INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY (word_1, word_2, word_3)
            )
            ''')

    def add_many(self, trigrams):
        trigrams = [( (trigram[0] if trigram[0].isalpha() else '') if trigram[0] else '', 
            (trigram[1] if trigram[1].isalpha() else '') if trigram[1] else '', 
            (trigram[2] if trigram[2].isalpha() else '') if trigram[2] else '')
                    for trigram in trigrams]
        with self.connection:
            self.connection.executemany(
                '''INSERT OR IGNORE INTO markov_model
                (word_1, word_2, word_3) VALUES (?, ?, ?)
                ''',
                trigrams
            )
            self.connection.executemany(
                '''UPDATE markov_model
                SET count = count + 1
                WHERE word_1 = ? AND word_2 = ? AND word_3 = ?
                ''',
                trigrams
            )

    def get_trigram_values(self, word_1, word_2):
        query = self.connection.execute(
            '''SELECT word_3, count FROM markov_model
            WHERE word_1 = ? AND word_2 = ? AND word_3 <> ""
            ORDER BY count DESC LIMIT 100
            ''',
            (word_1 or '', word_2 or '')
        )

        value_dict = collections.OrderedDict()

        for row in query:
            value_dict[row[0] or None] = row[1]

        if not value_dict:
            #raise KeyError()
            return {}

        return value_dict

    def count(self):
        query = self.connection.execute(
            '''SELECT COUNT(1) FROM markov_model LIMIT 1'''
        )

        for row in query:
            return row[0]

    def trim(self, target_count, min_probability_count=2):
        num_rows = self.count()
        limit = max(0, num_rows - target_count)
        delete_list = []
        with self.connection:
            sql_cmd = 'SELECT word_1, word_2, word_3 FROM markov_model WHERE count < %d LIMIT %d' % (min_probability_count, limit)
            query = self.connection.execute( sql_cmd )
            for row in query:
                delete_list.append(row)
            for i in delete_list:
                sql_cmd_tmp = '''DELETE FROM markov_model WHERE word_1 = \"%s\" AND word_2 = \"%s\" AND word_3 = \"%s\"'''%(i[0] or '', i[1] or '', i[2] or '')
                print(sql_cmd_tmp)
                self.connection.execute( sql_cmd_tmp )

    def get_rand_word(self):
        numrow = self.count()
        query = self.connection.execute(
            '''SELECT word_1 FROM markov_model LIMIT 1 OFFSET %d''' % int(numrow * random.random())
        )

        for row in query:
            return row[0]

    def __del__(self):
        self.connection.close()
            


