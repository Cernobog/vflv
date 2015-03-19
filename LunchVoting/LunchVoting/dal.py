
import database as d
import helpers as h

def get_user_by_username(username):
    db = d.get_db()
    cur = db.execute('select pass from users where name=?', [username])
    entries = cur.fetchall()
    return entries
   
def get_pubs():
    db = d.get_db()
    cur = db.execute('select * from pubs')
    entries = cur.fetchall()
    return entries
    
def get_actual_voting_for_all_user():
    db = d.get_db()
    cur = db.execute('select * from votings where date=?', 
        [h.get_current_time_in_s()])
    entries = cur.fetchall()
    return entries