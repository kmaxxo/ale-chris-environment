import sqlite3


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_to_do_table()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
          id INTEGER PRIMARY KEY,
          Title TEXT,
          _is_done boolean DEFAULT 0,
          _is_deleted boolean DEFAULT 0,
          CreatedOn Date DEFAULT CURRENT_DATE
        );
        """

        self.conn.execute(query)


class ToDoModel:
    TABLENAME = "Todo"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def get_by_id(self, _id):
        where_clause = f"AND id={_id}"
        return self.list_items(where_clause)

    def create(self, params):
        print (params)
        query = f'insert into {self.TABLENAME} ' \
                f'(Title) ' \
                f'values ("{params.get("title")}")'
        result = self.conn.execute(query)
        return self.get_by_id(result.lastrowid)

    def delete(self, item_id):
        query = f"UPDATE {self.TABLENAME} " \
                f"SET _is_deleted =  {1} " \
                f"WHERE id = {item_id}"
        print (query)
        self.conn.execute(query)
        return self.list_items()

#     def update(self, item_id, update_dict):
#         """
#         column: value
#         Title: new title
#         """
#         set_query = " ".join([f'{column} = {value}'
#                      for column, value in update_dict.items()])
#
#         query = f"UPDATE {self.TABLENAME} " \
#                 f"SET {set_query} " \
#                 f"WHERE id = {item_id}"
#         self.conn.execute(query)
#         return self.get_by_id(item_id)

    def list_items(self, where_clause=""):
        query = f"SELECT id, Title, _is_done " \
                f"from {self.TABLENAME} WHERE _is_deleted != {1} " + where_clause
        print (query)
        result_set = self.conn.execute(query).fetchall()
        result = [{column: row[i]
                  for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result
