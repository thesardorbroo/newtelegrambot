from mysql import connector
# from psycopg2 import connect
from random import randint
from user_ import User

class AnonDB:
    def __init__(self) -> None:
        self.connnection = connector.connect(
            host="localhost",
            database="projects",
            username="root",
            password="root",
        )

    async def is_user_exist(self,user_id: int):
        query = f"""SELECT * FROM anonbot WHERE user_id = {user_id}"""
        if await self.read_from_db(query):
            print("User is exist!")
            return True

        else: return False

    async def update_user(self,user_id):
        query = f"""UPDATE anonbot SET couple_id = 0, status = False WHERE user_id = {user_id}"""
        await self.write_to_db(query)
        print("User is seccessfuly updated!")

    async def make_object(self,user_id: int):
        query = f"""SELECT * FROM anonbot WHERE user_id = {user_id}"""
        data = await self.read_from_db(query)
        data = data[0]
        return User(data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8])

    async def adding_into(self,name: str, user_id: int):
        query = f"""INSERT INTO anonbot (user_id,name,step) VALUES ({user_id},"{name}",1)"""
        await self.write_to_db(query)
        print("User is seccessfuly added!")

    async def update_col_val(self,user_id: int, col: str, val: any):
        if type(val) == int:
            query = f"""
            UPDATE anonbot SET {col} = {val} WHERE user_id = {user_id}
            """
        else:
            query = f"""
            UPDATE anonbot SET {col} = "{val}" WHERE user_id = {user_id}
            """
        
        await self.write_to_db(query)

    async def write_to_db(self, query):
        c = self.connnection.cursor()
        c.execute(query)
        self.connnection.commit()

    async def read_from_db(self,query):
        c = self.connnection.cursor()
        c.execute(query)
        return c.fetchall()

    async def find_couple(self, user_id: int):
        query = f"""SELECT user_id FROM anonbot WHERE status = 0"""
        data = await self.read_from_db(query)
        
        try:
            print(data)
            while True:
                data = list(data[randint(0,len(data))])
                if data[0] != user_id: 
                    break

            query1 = f"""UPDATE anonbot SET couple_id = {data[0]},status = 1 WHERE user_id = {user_id}"""
            await self.write_to_db(query1)
            # query = f"""UPDATE anonbot SET couple_id = {user_id},status = 1 WHERE user_id = {data[0]}"""
            # await self.write_to_db(query)
            return True
        except IndexError:
            print("Error expected!")
            return False

    async def is_user_selected(self,user_id):
        query = f"""SELECT couple_id FROM anonbot WHERE couple_id = {user_id}"""
        data = await self.read_from_db(query)
        if len(data) != 0: return True
        else: return False