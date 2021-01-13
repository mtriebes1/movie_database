import mysql.connector
import config

# ------------------
# Main
# ------------------

def main():
    reset = 1
    # ---- Main Menu
    while reset != 0:
        start = main_menu()

        if (start == 1):
			print("\n<---SEARCH MOVIES--->\n")
			search_movies()
			reset = 0
			
        elif (start == 2):
			print("\n<---REVIEW MOVIES--->")
			review()
			reset = 0
			
        elif (start == 3):
			print("\n<---RECCOMENDED MOVIE--->")
			recc()
			reset = 0
			
        elif (start == 4):
			print("\n<---RANDOM MOVIE--->")
			random()
			reset = 0
        
        elif (start == 5):
			reset = 0
			exit(0)
			
        else:
			print("\nInvalid Input. Only (1-5) allowed\n")
			reset = 1

        
# ------------------
# Start Menu
# ------------------

def main_menu():
	print('<---MAIN MENU--->')
	print('1. Search Movies')
	print('2. Write Review')
	print('3. Recommendations')
	print('4. Random Movie')
	print('5. Exit')

	menu_input = input("Choose Option (1-5): ")

	return menu_input

# ------------------
# Basic Entry
# ------------------
def basic_entry(banner): 
    #print(banner)
    entry = raw_input(banner)
    return entry

# ------------------
# Rating Entry
# ------------------
def film_rating_entry():
    reset = 1
    while (reset == 1):
        rating = raw_input('Enter Rating (1-5)..............: ')  # Film Rating
        if rating != '1' and rating != '2' and rating != '3' and rating != '4' and rating != '5' and rating != '0':
			print("Invalid Rating, please enter a number between 1 - 5")
			reset
        else:
			reset = 0

    return rating

# ------------------
# UID Entry
# ------------------
def uid_entry():
	count = 0
	reset = 1
	
	while (reset == 1):
		uid = raw_input('Enter User ID (eg: 00010): ')
		count = len(uid)
		if (count != 5):
			print("Needs to be exactly 5 digits\n")
		elif (sum(num.isdigit() for num in uid) != 5):
			print("Integer Values Only (eg: 00010)\n")
		else:
			reset = 0

	return uid

# ------------------
# Search Movies
# ------------------
def search_movies():
	# ---- Connects To Database
	try: 
		# connection info
		usr = config.mysql['user']
		pwd = config.mysql['password']
		hst = config.mysql['host']
		dab = config.mysql['dab']
		# create a connection
		con = mysql.connector.connect(user=usr, password=pwd, host=hst, database=dab)

        # database cursor
		rs = con.cursor()
		queries = []
        
		# ---- Sets Up Menu
		print("--- IMPORTANT NOTE ---\n")
		print("Please only enter data into one field at a time\n")
		print('If you want to leave field blank, type: 0')
		print('EXAMPLE -- Enter Director Name: 0\n')
		print("--- IMPORTANT NOTE ---\n")

		# Film Title Entry
		reset = 1
		while (reset != 0):
			title = basic_entry('Enter Film Title................: ')
			if (title != '0'):
				query1 = 'SELECT * FROM movie WHERE title = %s'
				rs.execute(query1, (title,))
				row = rs.fetchone()
			else:
				reset = 0
				queries.append('0')
				break

			if row == None:
				print(title + ' is not in the Database\n')
				reset = 1
			else:
				reset = 0
				queries.append(title)
				
		# Year Entry
		reset = 1
		while (reset != 0):
			year = basic_entry('Enter Year Film the was Released: ')
			if (year != '0'):
				query1 = 'SELECT * FROM movie WHERE year_released = %s'
				rs.execute(query1, (year,))
				row = rs.fetchone()
			else:
				reset = 0
				queries.append('0')
				break

			if row == None:
				print("There are no movies from " + year)
				reset = 1
			else:
				reset = 0
				queries.append(year)
		
		# Genre Entry
		reset = 1
		while (reset != 0):
			genre = basic_entry('Enter Film Genre (e.g. Action)..: ')
			if (genre != '0'):
				query1 = 'SELECT * FROM movie WHERE genre = %s'
				rs.execute(query1, (genre,))
				row = rs.fetchone()
			else:
				reset = 0
				queries.append('0')
				break

			if row == None:
				print("There are no " + genre + " movies in the database")
				reset = 1
			else:
				reset = 0
				queries.append(genre)
				
		# Director Entry
		reset = 1
		while (reset != 0):
			director = basic_entry('Enter Director Name.............: ')
			if (director != '0'):
				query1 = 'SELECT * FROM director WHERE director_name = %s'
				rs.execute(query1, (director,))
				row = rs.fetchone()
			else:
				reset = 0
				queries.append('0')
				break

			if row == None:
				print(director + ' is not in the Database\n')
				reset = 1
			else:
				reset = 0
				queries.append(director)
		
        # Streaming Service Entry
		print('Streaming Service (1 = Netflix, 2 = Hulu, 3 = Prime)')
		streaming_service = raw_input('To search all, write as 123.....: ')
		if streaming_service == '0':
			queries.append('0')
		elif streaming_service == '1':
			queries.append('Netflix')
		elif streaming_service == '2':
			queries.append('Hulu')
		elif streaming_service == '3':
			queries.append('Prime')
		elif streaming_service == '123':
			queries.append('All')
        
        # Actor/Actress Entry
		reset = 1
		while (reset != 0):
			actor_actress = basic_entry('Enter Actor or Actress Name.....: ')
			if (actor_actress != '0'):
				query1 = 'SELECT * FROM actor_actress WHERE actor_name = %s'
				rs.execute(query1, (actor_actress,))
				row = rs.fetchone()
			else:
				reset = 0
				queries.append('0')
				break

			if row == None:
				print(actor_actress + ' is not in the Database\n')
				reset = 1
			else:
				reset = 0
				queries.append(actor_actress)
				

        # Rating Entry
		rating = film_rating_entry()
		queries.append(str(rating))
				
		exec_search(queries)
		print('\n')
		main()
    
    # ---- Triggered if unable to connect to database
	except mysql.connector.Error as err:
		print(err)


def exec_search(queries):
	# ---- Connects To Database
	try: 
		# connection info
		usr = config.mysql['user']
		pwd = config.mysql['password']
		hst = config.mysql['host']
		dab = config.mysql['dab']
		# create a connection
		con = mysql.connector.connect(user=usr, password=pwd, host=hst, database=dab)
		
		
		# All 
		query1 = 'SELECT * FROM movie WHERE '
		query2 = 'SELECT * FROM movie WHERE '
		query3 = '''SELECT DISTINCT h.movie_title, m.year_released, m.genre, m.director_name 
					FROM hosted_by h, movie m
					WHERE h.movie_title = m.title AND h.streaming_service_name=\''''
		query4 = '''SELECT m.title, m.year_released, m.genre, m.director_name
					FROM appears_in a, movie m
					WHERE a.movie_title = m.title AND a.actor_name = \''''
		query5 = '''SELECT m.title, m.year_released, m.genre, m.director_name, ROUND(AVG(ur.rating), 1)
					FROM movie_db_user_review ur, movie m
					WHERE ur.movie_title = m.title
					GROUP BY m.title
					HAVING AVG(ur.rating) > '''
					
		# Query Flags to determine if query is executed
		execQuery1 = False
		execQuery2 = False
		execQuery3 = False
		execQuery4 = False
		execQuery5 = False
		
		# Result set for each query
		rs1 = con.cursor()
		rs2 = con.cursor()
		rs3 = con.cursor()
		rs4 = con.cursor()
		rs5 = con.cursor()
		

		for i in range(7):
			if queries[i] != '0':
				if i == 0:
					query1 += 'title=' + '\'' + str(queries[i]) + '\''
					execQuery1 = True
				elif i == 1:
					query2 += 'year_released=' + '\'' + str(queries[i]) + '\''
					if queries[i+1] != '0':
						query2 += ' AND '
					execQuery2 = True
				elif i == 2:
					query2 += 'genre=' + '\'' + str(queries[i]) + '\''
					if queries[i+1] != '0':
						query2 += ' AND '
					execQuery2 = True
				elif i == 3:
					query2 += 'director_name=' + '\'' + str(queries[i]) + '\''
					execQuery2 = True
				elif i == 4:
					if queries[i] == 'All':
						query3 = 'SELECT * FROM movie'
					elif queries[i] != 'All':
						query3 += str(queries[i]) + '\''
					execQuery3 = True
				elif i == 5:
					query4 += str(queries[i]) + '\''
					execQuery4 = True
				elif i == 6:
					query5 += str(queries[i])
					execQuery5 = True
		
		if execQuery1 == True:
			rs1.execute(query1)
			for (title, year, genre, director) in rs1:
				print '{}, {}, {}, {}'.format(title, year, genre, director)
			print('\n')
		if execQuery2 == True:
			rs2.execute(query2)
			for (title, year, genre, director) in rs2:
				print '{}, {}, {}, {}'.format(title, year, genre, director)
			print('\n')
		if execQuery3 == True:
			rs3.execute(query3)
			for (title, year, genre, director) in rs3:
				print '{}, {}, {}, {}'.format(title, year, genre, director)
			print('\n')
		if execQuery4 == True:
			rs4.execute(query4)
			for (title, year, genre, director) in rs4:
				print '{}, {}, {}, {}'.format(title, year, genre, director)
			print('\n')
		if execQuery5 == True:
			rs5.execute(query5)
			for (title, year, genre, director, avg_rating) in rs5:
				print '{}, {}, {}, {}, {}'.format(title, year, genre, director, avg_rating)
			print('\n')
			
	# ---- Triggered if unable to connect to database
	except mysql.connector.Error as err:
		print(err)
		
def review():
	# ---- Connects To Database
	try: 
		# connection info
		usr = config.mysql['user']
		pwd = config.mysql['password']
		hst = config.mysql['host']
		dab = config.mysql['dab']
		# create a connection
		con = mysql.connector.connect(user=usr, password=pwd, host=hst, database=dab)

		# ---- Sets Up DB cursor
		rs = con.cursor()
		# Main function loop
		restart = 1
		while (restart == 1):    
			# Film Title Entry
			reset = 1
			while (reset == 1):
				title = basic_entry('Enter Film Title.........: ')
				query1 = 'SELECT * FROM movie WHERE title = %s'
				rs.execute(query1, (title,))
				row = rs.fetchone()

				if row == None:
					print(title + ' is not in the Database\n')
					reset = 1
				else:
					reset = 0
			# Movie ID Entry
			uid = uid_entry()

			# User ID Check
			uid_check = 'SELECT * FROM db_user WHERE user_id = %s'
			rs.execute(uid_check, (uid,))
			row = rs.fetchone()

			if (row == None): # user ID is not in the table yet
				print("Would You like to Add New User (y/n):")
				choice = raw_input()
				if (choice == 'y'):
					insert_values = 'INSERT INTO db_user VALUES(%s)'
					rs.execute(insert_values, (uid,))
					con.commit()
				else:
					print("\nGoodbye\n")
					exit(0)
			# Check If user's already rated the same film
			input_check = 'SELECT * FROM movie_db_user_review WHERE movie_title = %s AND user_id = %s'
			rs.execute(input_check, (title, uid))
			row = rs.fetchone()

			if (row != None): # Movie Already reviewed by that user
				print(uid + " already reviewed " + title)
			else:
				restart = 0
				
		# Film Rating Entry
		rating = film_rating_entry()
		while (rating == '0'):
			print("Invalid Rating, please enter a number between 1 - 5")
			rating = film_rating_entry()

		# Adds The Rating to the Database
		insert_values = 'INSERT INTO movie_db_user_review VALUES(%s, %s, %s)'
		rs.execute(insert_values, (title, uid, rating))
		con.commit()

		rs.close()
		con.close()
		main()
	# ---- Triggered if unable to connect to database
	except mysql.connector.Error as err:
		print(err)

# ------------------
# Get Recommendations
# ------------------
def recc():
	# ---- Connects To Database
	try: 
		# connection info
		usr = config.mysql['user']
		pwd = config.mysql['password']
		hst = config.mysql['host']
		dab = config.mysql['dab']
		# create a connection
		con = mysql.connector.connect(user=usr, password=pwd, host=hst, database=dab)

		# ---- Sets Up DB cursor
		rs = con.cursor()
		title = ''

		# Film Title Entry
		reset = 1
		while (reset != 0):
			title = basic_entry('Enter Film Title: ')
			query1 = 'SELECT * FROM movie WHERE title = %s'
			rs.execute(query1, (title,))
			row = rs.fetchone()

			if row == None:
				print(title + ' is not in the Database\n')
				reset = 1
			else:
				reset = 0
		
		query = 'SELECT genre FROM movie WHERE title=%s'
		rs.execute(query, (title,))
		genre = rs.fetchone()[0]
				
		# Recommend Oscar Winning Movie
		print('Oscar Movie: ')
		award_query = '''SELECT m.title, m.year_released, m.genre, m.director_name
						 FROM movie m, movie_award ma
						 WHERE m.title = ma.movie_title AND ma.award_type=\'Oscar\' AND genre=%s
						 ORDER BY RAND()
						 LIMIT 1'''
		rs.execute(award_query, (genre,))
		
		for (title, year, genre, director) in rs:
			print '{}, {}, {}, {}'.format(title, year, genre, director)
		print('\n')
		
		# Recommend Highest Rated Movie of Specific Genre in DB
		print('Highest Rated Movie of the Same Genre: ')
		rating_query = '''SELECT m.title, m.year_released, m.genre, m.director_name
						  FROM movie m, movie_db_user_review mr
						  WHERE m.genre =%s AND m.title = mr.movie_title
						  GROUP BY m.title
						  HAVING AVG(mr.rating) >=  (SELECT AVG(mr2.rating)
													FROM movie m2, movie_db_user_review mr2
													WHERE m2.genre =%s AND m2.title = mr2.movie_title
													GROUP BY m2.title
													LIMIT 1)'''
		rs.execute(rating_query, (genre, genre))
		
		for (title, year, genre, director) in rs:
			print '{}, {}, {}, {}'.format(title, year, genre, director)
		print('\n')

		# Returns Reccomended Movie
		main()
    
	# ---- Triggered if unable to connect to database
	except mysql.connector.Error as err:
		print(err)
		
# ------------------
# Random Movie
# ------------------
def random():
	# ---- Connects To Database
	try: 
		# connection info
		usr = config.mysql['user']
		pwd = config.mysql['password']
		hst = config.mysql['host']
		dab = config.mysql['dab']
		# create a connection
		con = mysql.connector.connect(user=usr, password=pwd, host=hst, database=dab)

		# Sets Up DB cursor
		rs = con.cursor()
		
		query = 'SELECT * FROM movie ORDER BY RAND() LIMIT 1'
		rs.execute(query)
		
		for (title, year, genre, director) in rs:
			print '{}, {}, {}, {}'.format(title, year, genre, director)
		print('\n')
		
		main()

	except mysql.connector.Error as err:
		print(err)

if __name__ == '__main__':
	main()