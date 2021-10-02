import uuid
# for abstract classes in python
from abc import ABC, abstractclassmethod
from Types import InsertRequest


class Crud(ABC):
    def __init__(self, table, cursor, dbConnection, logger, cls=None):
        self.tableName = table.name
        self.table = table
        self.cursor = cursor
        self.columns = ','.join(
            ['id'] + [column.name for column in self.table.columns])
        self.dbConnection = dbConnection
        self.logger = logger
        self.cls = cls

    @abstractclassmethod
    def serialize(cls, data):
        yield "Not implemened"

    def get(self, id):
        self.logger.debug("Getting object with id", id)
        self.cursor.execute("SELECT %s FROM %s WHERE id='%s'" %
                            (self.columns, self.tableName, id))
        return self.serialize(self.cursor.fetchall()[0])

    def getAll(self):
        self.cursor.execute("SELECT %s FROM %s" %
                            (self.columns, self.tableName))
        return self.cursor.fetchall()

    def prepearValue(self, inputRequest):
        if("varchar" in inputRequest.column.type.lower() or "text" in inputRequest.column.type.lower() or "timestamp" in inputRequest.column.type.lower()):
            return "\'%s\'" % inputRequest.value
        else:
            return str(inputRequest.value)

    """
        Using pythons uuid4 as mysql uuid sucks and does not use uuid 4....
    """

    def insert(self, data, returnData=True):
        id = str(uuid.uuid4())
        columns = ','.join(['id'] + [ir.column.name for ir in data])
        values = ','.join(["\'%s\'" % id] + [self.prepearValue(ir)
                          for ir in data])

        self.logger.debug("Inserting: insert into %s (%s) values (%s)" % (
            self.tableName, columns,  values))

        result = self.cursor.execute(
            "insert into %s(%s) values (%s)" % (self.tableName, columns, values))
        cr = self.dbConnection.commit()
        if(returnData):
            return self.get(id)
