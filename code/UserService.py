from Crud import Crud
from Types import User, UserRequest, DatabaseColumn, DatabaseTable, InsertRequest


hasLablesColumn, textIdenfifierColumn = DatabaseColumn(
    "has_lables", "boolean"), DatabaseColumn("text_identifier", "varchar(4)")


class UserService(Crud):

    def __init__(self, cursor: any, dbConnection, logger, activate):
        Crud.__init__(self, DatabaseTable(
            name="users", columns=[
                hasLablesColumn, textIdenfifierColumn
            ]),
            cursor=cursor, dbConnection=dbConnection, logger=logger, activate=activate)
        self.users = []
        self.logger = logger

    def init(self):
        self.users = self.fetchUsers()

    def fetchUsers(self):
        return self.serializeArray(self.getAll())

    def serialize(self, data):
        # column order defined in line 4
        return User(id=data[0], textIdentifier=data[2], hasLables=data[1])

    def serializeArray(self, data):
        return [self.serialize(user) for user in data]

    def getInMemory(self, user: UserRequest):
        for inMemUser in self.users:
            if (inMemUser.textIdentifier == user.textIdentifier):
                return inMemUser
        return None

    def create(self, user: UserRequest):
        user = self.insert([
            InsertRequest(column=textIdenfifierColumn, value=user.textIdentifier), InsertRequest(column=hasLablesColumn, value=user.hasLables)])
        self.users.append(user)
        return user

    def getOrCreate(self, user: UserRequest):
        inMemUser = self.getInMemory(user)
        if (inMemUser == None):
            self.logger.info("User does not exist, creating")
            return self.create(user)
        self.logger.info("User exists in cache")
        return inMemUser
