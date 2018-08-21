import datetime as dt

from marshmallow import Schema, fields


class Transaction(object):
    # I am Guessing this is a constructor?
    def __init__(self, description, amount, type):
        self.description = description
        self.amount = amount
        self.created_at = dt.datetime.now()
        self.type = type

    ## I am guessing this is similar to tostring???
    def __repr__(self):
        return '<Transaction(name={self.description!r})>'.format(self=self)


class TransactionSchema(Schema):
    description = fields.Str()
    amount = fields.Number()
    created_at = fields.Date()
    type = fields.Str()

