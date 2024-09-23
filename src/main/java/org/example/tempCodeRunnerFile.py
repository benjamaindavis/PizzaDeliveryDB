def insertUsers (full_name:String, username:String, password:String, birthday:String, postal_code:String):
#     #add pass_hash later

#     #birthday_date = DateTime.strptime(birthday, '%Y-%m-%d').date()


#     with engine.connect() as conn:
#         conn.execute(insert(Users).values(full_name = full_name, username = username, password = password, birthday = birthday, pizza_count = 0, postal_code = postal_code))
        
#         conn.commit()

# insertUsers('Vernon Jones', 'vernonjones1988', 'moneybag123', '2005-12-14','123A')