# db.py

import sqlite3

conn = sqlite3.connect("legos.db")



def connect_cursor():
    c = conn.cursor()
    return c

def insert_new_piece(
        studded=None, 
        units=None, 
        name=None,
        description=None, 
        price=None, 
        color=None):

    vars = [studded, units, name, description, price, color]
    for i in vars: 
        c.execute(f"""INSERT INTO piece VALUES('{studded}','{units}','{name}','{description}', '{price}', '{color}')""")

def create_tables():
    c.execute("""CREATE TABLE beams (
            studded     binary,
            units_len   integer,
            units_height integer,
            units_width real,
            name        text,
            angle       integer,
            description text,
            price       real,
            color       char
    )""")

    c.execute("""CREATE TABLE bricks (
            technic    binary,
            units_len   integer,
            units_height integer,
            units_width real,
            name        text,
            description text,
            price       real,
            color       char
    )""")

    c.execute("""CREATE TABLE pins_conns_axle (
            type     char,
            units_len   integer,
            friction    binary,
            connection  char,
            adapter     binary,
            description char,
            price       real,
            color       char
    )""")

   c.execute("""CREATE TABLE gears (
            style     char,
            units_diam  real,
            num_teeth   integer,
            shaft_type  char,
            description char,
            price       real,
            color       char
    )""")


def create_custom_table():
    table_name = input("Name the table: ")
    use_for_fields = []
    temp_for_input = (" ", " ")
    while temp_for_input != ("",""):
        try:

            data_name, data_type = input("Enter name of field and the data type")
        except ValueError:
            data_name, data_type = " "," "
        finally:
            temp_for_input = (data_name, data_type)
            use_for_fields.append(temp_for_input)

    c.execute("""CREATE TABLE pieces (
            studded binary,
            units   integer,
            name    text,
            description text,
            price   real,
            color   text
    )""")




def commit_and_close():
    # Commit canges to db
    conn.commit()
    # Close db connection
    conn.close()


if __name__=='__main__':
    c = connect_cursor()
    g = c.fetchall()
    print(g)