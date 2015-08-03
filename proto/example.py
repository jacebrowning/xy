#!/usr/bin/env python3

import uuid

import yorm


class Column:
    pass


class Row:

    def __init__(self):
        self.uuid = uuid.uuid4()

    def __str__(self):
        return str(self.uuid)


class UUID(yorm.Converter):

    def __call__(self, value=None):
        return uuid.uuid4(value)

    @classmethod
    def create_default(cls):
        return None

    @classmethod
    def to_data(cls, obj):
        return str(obj)

    @classmethod
    def to_value(cls, obj):
        return uuid.UUID(str(obj))


@yorm.attr(all=UUID)
class Rows(yorm.converters.List):
    pass


@yorm.attr(rows=Rows)
@yorm.sync("{self.name}/index.yml")
class Table:

    def __init__(self, name):
        self.name = name
        self.rows = []

    def add_row(self):
        row = Row()
        yorm.sync(row, "{}/{}.yml".format(self.name, row.uuid))
        self.rows.append(row)
        return row


def run():
    table = Table("foobar")
    row = table.add_row()
    row2 = table.add_row()
    row3 = table.add_row()



if __name__ == '__main__':
    run()
