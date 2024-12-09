import random
import mysql.connector
from collections import defaultdict

# #hard_constraint1 = students timetabled first
# #hard_constraint2 = students must not have the same lesson more than once a day
# #soft_constraint1 = teachers should preferably stay the same for a subject for a specific class
# #soft_constraint2 = rooms should prefereably be allocated according to the subject department they belong to
# #non_constraint1 = lessons can go anywhere as long as they adhere to the first hard constraint
    


# #creating the actual timetable for students

# week_timetable = ["Free"] * 25

# def timetable_subjects(week_timetable):
#     imp_subj_arr = ["Maths", "English", "Chemistry", "Biology", "Physics"]
#     oth_subj_arr = ["Geography", "History", "Art", "Music", "PE"]
#     i = 0  #index for week_timetable
#     j = 0  #imp_subj_arr
#     k = 0  #oth_subj_arr
#     counter = 0  #count how many times each subject has been placed
    
#     while i < 15:  #only assign the first 15 slots
#         if counter < 3:  #place 3 of the same subject in a row
#             week_timetable[i] = imp_subj_arr[j]
#             counter += 1
#             i += 1
#         else:
#             j += 1  #move to the next subject
#             counter = 0  #reset the counter for the new subject
#     counter = 0

#     while i < 25:     # assigns the rest of the slots
#         if counter < 2:  #place 2 of the same subject in a row
#             week_timetable[i] = oth_subj_arr[k]
#             counter += 1
#             i += 1
#         else:
#             k += 1  #move to the next subject
#             counter = 0  #reset the counter for the new subject

#     return week_timetable

# print(timetable_subjects(week_timetable))

# #keeping an original copy of the array to oompare later
# original_timetable = timetable_subjects(week_timetable)

# #fill the timetable
# filled_timetable = timetable_subjects(week_timetable)

# #shuffle the timetable
# random.shuffle(filled_timetable)


# print("Original timetable:", filled_timetable)



# def check_blocks_of_five(filled_timetable):
#     #iterate over list in steps of 5
#     for i in range(0, len(filled_timetable), 5):
#         block = filled_timetable[i:i+5]  #get block of five subjects
#         if len(block) != len(set(block)):
#             return False  #return False if theres duplicates in the block
#     return True  #return True if no duplicates found in any block


# #shuffle until no duplicates are found in any block of five
# while not check_blocks_of_five(filled_timetable):
#     random.shuffle(filled_timetable)

# print("Shuffled timetable with no duplicates in blocks of five:", filled_timetable)

# def generate_unique_timetables(original_timetable, num_timetables):
#     """
#     Generates a specified number of unique timetables by shuffling the original timetable.
#     """
#     unique_timetables = []
    
#     while len(unique_timetables) < num_timetables:
#         #shuffle timetable until it meets condition
#         shuffled_timetable = original_timetable[:]  #copy original timetable
#         while not check_blocks_of_five(shuffled_timetable):
#             random.shuffle(shuffled_timetable)
        
#         #check if shuffled timetable is unique
#         if shuffled_timetable not in unique_timetables:
#             unique_timetables.append(shuffled_timetable[:])  #add copy of shuffled timetable

#     return unique_timetables

# #original timetable list
# filled_timetable = ['History', 'PE', 'Maths', 'Maths', 'English', 'Maths', 'English', 'English', 'Physics', 'Chemistry',
#                     'Biology', 'Physics', 'Art', 'Music', 'Geography', 'Biology', 'Music', 'Physics', 'History', 
#                     'Chemistry', 'Chemistry', 'Biology', 'Geography', 'Art', 'PE']

# #generate 5 unique shuffled timetables
# unique_timetables = generate_unique_timetables(filled_timetable, 5)

# #print unique timetables
# for index, timetable in enumerate(unique_timetables):
#     print(f"9z{index + 1}: {timetable}")



# #inserting the data into the table in mysql

# # Example data structure similar to what you showed
# class_timetables = {
#     "9z1": ['Physics', 'English', 'History', 'Music', 'Art', 'English', 'Maths', 'Geography', 'Chemistry', 'PE', 'Chemistry',
#              'Physics', 'Maths', 'Music', 'Biology', 'Geography', 'Physics', 'Chemistry', 'Biology', 'Art', 'History', 'PE', 
#              'Maths', 'Biology', 'English'],

#     "9z2": ['Physics', 'History', 'Chemistry', 'English', 'Maths', 'Physics', 'Biology', 'Maths', 'Geography', 'English',
#              'Biology', 'History', 'Maths', 'Music', 'English', 'Music', 'Art', 'Chemistry', 'Geography', 'PE', 'Biology',
#                'PE', 'Physics', 'Art', 'Chemistry'],

#     "9z3": ['Biology', 'Art', 'English', 'Maths', 'History', 'Maths', 'Music', 'English', 'Physics', 'Chemistry', 'Geography',
#              'PE', 'Chemistry', 'History', 'Physics', 'Chemistry', 'Biology', 'Geography', 'Physics', 'Music', 'Maths', 'PE',
#                'Biology', 'English', 'Art'],

#     "9z4": ['Chemistry', 'Art', 'PE', 'Music', 'English', 'Music', 'Physics', 'Maths', 'History', 'Biology', 'Maths', 'Geography',
#              'English', 'Physics', 'Art', 'PE', 'Biology', 'Maths', 'Geography', 'Chemistry', 'History', 'Chemistry', 'Biology',
#                'Physics', 'English'],

#     "9z5": ['Art', 'Physics', 'Music', 'English', 'Biology', 'Geography', 'Chemistry', 'Physics', 'History', 'PE', 'English', 'Maths',
#              'Art', 'Geography', 'Chemistry', 'Biology', 'History', 'Maths', 'Music', 'PE', 'Maths', 'Biology', 'Physics', 'English',
#                'Chemistry']
# }
# days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# #connect to MySQL
# connection = mysql.connector.connect(
#     host="localhost",       
#     user="root",     
#     password="Libraries4Life!", 
#     database="test"    
#     )

# cursor = connection.cursor()

# #loop through each class timetable
# for student_class, timetable in class_timetables.items():
#     #split timetable into chunks of 5 (one for each day)
#     for i in range(0, len(timetable), 5):
#         day_index = i // 5  #get index for day
#         day = days_of_week[day_index]  #map index to actual day

#         #extract subjects for current day (periods 1-5)
#         period1, period2, period3, period4, period5 = timetable[i:i + 5]

#         #SQL insert query to insert a new row for each class and day
#         insert_query = """
#         INSERT INTO student_timetables (day, student_class, period1, period2, period3, period4, period5) 
#         VALUES (%s, %s, %s, %s, %s, %s, %s);
#         """

#         #execute query with subjects and parameters
#         cursor.execute(insert_query, (day, student_class, period1, period2, period3, period4, period5))
#         connection.commit()  #commit after each insert to save changes

# #close connection
# cursor.close()
# connection.close()

# print("All records inserted successfully!")


# #adding teachers into the student timetable, firstly taking them out of the database and adding them into a list in python

# #SQL query to fetch the required columns
# select_query = "SELECT teach_username, teach_subj FROM teachers"

# #execute query
# cursor.execute(select_query)

# #fetch all rows from query
# rows = cursor.fetchall()

# #create empty dict to add subjects and corresponding teacehrs
# teacher_subjects = {}

# #process results and add to dictionary
# for row in rows:
#     teach_username, teach_subj = row
#     if teach_subj in teacher_subjects:
#         teacher_subjects[teach_subj].append(teach_username)
#     else:
#         teacher_subjects[teach_subj] = [teach_username]

# #finish connectoin
# cursor.close()
# connection.close()

# # print final dictionary
# print(teacher_subjects)












# Provided data structures
teacher_subjects = {
    'Chemistry': ['ajackson', 'athompson', 'ebrooks'], 
    'history': ['anelson', 'jreed'], 
    'Art': ['cwhite', 'edavis'], 
    'Music': ['cyoung', 'zedwards'], 
    'Biology': ['dhill', 'gtaylor', 'sbennett'], 
    'PE': ['iking', 'tlewis'], 
    'English': ['janderson', 'jscott', 'sharris'], 
    'Maths': ['lroberts', 'madams', 'rgreen'], 
    'Physics': ['mcarter', 'nwalker', 'wjohnson'], 
    'geography': ['ofoster', 'vsanders']
}

class_timetables = {

       "9z1": ['Physics', 'English', 'History', 'Music', 'Art', 'English', 'Maths', 'Geography', 'Chemistry', 'PE', 'Chemistry',
             'Physics', 'Maths', 'Music', 'Biology', 'Geography', 'Physics', 'Chemistry', 'Biology', 'Art', 'History', 'PE', 
             'Maths', 'Biology', 'English'],

    "9z2": ['Physics', 'History', 'Chemistry', 'English', 'Maths', 'Physics', 'Biology', 'Maths', 'Geography', 'English',
             'Biology', 'History', 'Maths', 'Music', 'English', 'Music', 'Art', 'Chemistry', 'Geography', 'PE', 'Biology',
               'PE', 'Physics', 'Art', 'Chemistry'],

    "9z3": ['Biology', 'Art', 'English', 'Maths', 'History', 'Maths', 'Music', 'English', 'Physics', 'Chemistry', 'Geography',
             'PE', 'Chemistry', 'History', 'Physics', 'Chemistry', 'Biology', 'Geography', 'Physics', 'Music', 'Maths', 'PE',
               'Biology', 'English', 'Art'],

    "9z4": ['Chemistry', 'Art', 'PE', 'Music', 'English', 'Music', 'Physics', 'Maths', 'History', 'Biology', 'Maths', 'Geography',
             'English', 'Physics', 'Art', 'PE', 'Biology', 'Maths', 'Geography', 'Chemistry', 'History', 'Chemistry', 'Biology',
               'Physics', 'English'],

    "9z5": ['Art', 'Physics', 'Music', 'English', 'Biology', 'Geography', 'Chemistry', 'Physics', 'History', 'PE', 'English', 'Maths',
             'Art', 'Geography', 'Chemistry', 'Biology', 'History', 'Maths', 'Music', 'PE', 'Maths', 'Biology', 'Physics', 'English',
               'Chemistry']
}


# # Function to assign teachers to subjects in the class timetable
# def assign_teachers_to_timetable(class_timetables, teacher_subjects):
#     assigned_teachers = {}
#     # Initialize teacher rotation counters
#     teacher_counters = {subject: 0 for subject in teacher_subjects}
#     # Initialize a dictionary to track assignments per period
#     period_assignments = defaultdict(lambda: defaultdict(list))

#     for class_name, timetable in class_timetables.items():
#         assigned_teachers[class_name] = []
#         for period, subject in enumerate(timetable):
#             # Get the list of available teachers for the subject
#             teachers = teacher_subjects.get(subject, [])
            
#             if teachers:
#                 # Find a teacher that is not already assigned for this period
#                 assigned_teacher = None
#                 for i in range(len(teachers)):
#                     teacher_index = (teacher_counters[subject] + i) % len(teachers)
#                     potential_teacher = teachers[teacher_index]
#                     if potential_teacher not in period_assignments[period][subject]:
#                         assigned_teacher = potential_teacher
#                         teacher_counters[subject] += i + 1
#                         break

#                 if not assigned_teacher:
#                     assigned_teacher = teachers[teacher_counters[subject] % len(teachers)]
#                     teacher_counters[subject] += 1

#                 # Add the teacher to the period assignment to prevent conflicts
#                 period_assignments[period][subject].append(assigned_teacher)
#             else:
#                 # No teacher available, just assign a placeholder
#                 assigned_teacher = 'No Teacher Available'
            
#             # Assign the teacher for the subject
#             assigned_teachers[class_name].append(assigned_teacher)

#     return assigned_teachers, period_assignments

# # Function to resolve conflicts by rescheduling
# def resolve_conflicts(assigned_teachers, period_assignments, teacher_subjects):
#     max_reschedule_attempts = 5
#     reschedule_attempts = defaultdict(int)
    
#     for class_name, teachers in assigned_teachers.items():
#         for period, teacher in enumerate(teachers):
#             if teacher != 'No Teacher Available':
#                 while period_assignments[period][teacher].count(teacher) > 1 and reschedule_attempts[(class_name, period, teacher)] < max_reschedule_attempts:
#                     # Find a replacement teacher
#                     subject = class_timetables[class_name][period]
#                     replacement_found = False
                    
#                     for new_teacher in teacher_subjects.get(subject, []):
#                         if new_teacher != teacher and new_teacher not in period_assignments[period][subject]:
#                             # Replace the teacher in the schedule
#                             assigned_teachers[class_name][period] = new_teacher
#                             period_assignments[period][subject].remove(teacher)
#                             period_assignments[period][subject].append(new_teacher)
#                             replacement_found = True
#                             break
                    
#                     reschedule_attempts[(class_name, period, teacher)] += 1
                    
#                     if replacement_found:
#                         break
                
#                 # If we can't find a replacement after max attempts, assign any free teacher
#                 if period_assignments[period][teacher].count(teacher) > 1:
#                     for new_teacher in teacher_subjects[subject]:
#                         if new_teacher not in period_assignments[period][subject]:
#                             assigned_teachers[class_name][period] = new_teacher
#                             period_assignments[period][subject].remove(teacher)
#                             period_assignments[period][subject].append(new_teacher)
#                             break

# # Function to assign any available free teacher if no subject teacher is found
# def assign_free_teacher(assigned_teachers, period_assignments):
#     for class_name, teachers in assigned_teachers.items():
#         for period, teacher in enumerate(teachers):
#             if teacher == 'No Teacher Available':
#                 # Find any teacher not teaching at this period
#                 for subject, subject_teachers in teacher_subjects.items():
#                     for free_teacher in subject_teachers:
#                         # Check if the teacher is not already assigned in this period
#                         if all(free_teacher not in period_assignments[period][subj] for subj in period_assignments[period]):
#                             # Assign this free teacher
#                             assigned_teachers[class_name][period] = free_teacher
#                             period_assignments[period][subject].append(free_teacher)
#                             break

# # Assign teachers based on the provided rules
# assigned_teachers, period_assignments = assign_teachers_to_timetable(class_timetables, teacher_subjects)

# # Function to verify and resolve scheduling conflicts
# def verify_and_resolve_conflicts(assigned_teachers):
#     period_teacher_assignment = defaultdict(lambda: defaultdict(set))
#     period_assignments = defaultdict(lambda: defaultdict(list))

#     for class_name, teachers in assigned_teachers.items():
#         for period, teacher in enumerate(teachers):
#             subject = class_timetables[class_name][period]
#             if teacher != 'No Teacher Available':
#                 if teacher in period_teacher_assignment[period][subject]:
#                     print(f"Conflict found: Teacher {teacher} is assigned to multiple classes in period {period}. Attempting to resolve...")
#                     period_assignments[period][subject].append(teacher)
#                     resolve_conflicts(assigned_teachers, period_assignments, teacher_subjects)
#                 else:
#                     period_teacher_assignment[period][subject].add(teacher)
#                     period_assignments[period][subject].append(teacher)

#     # Assign any available free teacher to slots with 'No Teacher Available'
#     assign_free_teacher(assigned_teachers, period_assignments)

# # Verify and resolve conflicts
# verify_and_resolve_conflicts(assigned_teachers)

# # Output for verification
# print("\nAssigned Teachers After Resolving Conflicts and Filling Gaps:")
# for class_name, teacher_list in assigned_teachers.items():
#     print(f"{class_name}: {teacher_list}")




connection = mysql.connector.connect(
    host="localhost",           # Replace with my MySQL host
    user="root",       # Replace with my MySQL username
    password="Libraries4Life!",   # Replace with my MySQL password
    database="test"    # Replace with my database name
    )

cursor = connection.cursor()


# # Define the teacher schedules
# schedules = {
#     '9z1': [
#         ('mcarter', 'janderson', 'ofoster', 'cyoung', 'cwhite'),  # Monday
#         ('jscott', 'lroberts', 'ofoster', 'ajackson', 'iking'),  # Tuesday
#         ('athompson', 'nwalker', 'madams', 'zedwards', 'dhill'),  # Wednesday
#         ('ofoster', 'wjohnson', 'ebrooks', 'gtaylor', 'edavis'),  # Thursday
#         ('ofoster', 'tlewis', 'rgreen', 'sbennett', 'sharris')   # Friday
#     ],
#     '9z2': [
#         ('nwalker', 'ofoster', 'ajackson', 'janderson', 'lroberts'),  # Monday
#         ('wjohnson', 'dhill', 'madams', 'ofoster', 'jscott'),          # Tuesday
#         ('gtaylor', 'ofoster', 'rgreen', 'cyoung', 'sharris'),         # Wednesday
#         ('zedwards', 'cwhite', 'athompson', 'ofoster', 'iking'),        # Thursday
#         ('sbennett', 'iking', 'mcarter', 'edavis', 'ebrooks')           # Friday
#     ],
#     '9z3': [
#         ('dhill', 'cwhite', 'janderson', 'lroberts', 'ofoster'),  # Monday
#         ('madams', 'cyoung', 'jscott', 'nwalker', 'ajackson'),    # Tuesday
#         ('ofoster', 'tlewis', 'athompson', 'ofoster', 'wjohnson'), # Wednesday
#         ('ebrooks', 'gtaylor', 'ofoster', 'mcarter', 'zedwards'),  # Thursday
#         ('rgreen', 'iking', 'sbennett', 'sharris', 'edavis')       # Friday
#     ],
#     '9z4': [
#         ('ajackson', 'edavis', 'tlewis', 'zedwards', 'janderson'),  # Monday
#         ('cyoung', 'nwalker', 'lroberts', 'vsanders', 'dhill'),     # Tuesday
#         ('madams', 'vsanders', 'jscott', 'wjohnson', 'cwhite'),     # Wednesday
#         ('iking', 'sbennett', 'rgreen', 'vsanders', 'athompson'),   # Thursday
#         ('vsanders', 'ebrooks', 'dhill', 'mcarter', 'janderson')    # Friday
#     ],
#     '9z5': [
#         ('edavis', 'nwalker', 'zedwards', 'jscott', 'gtaylor'),    # Monday
#         ('ofoster', 'ajackson', 'wjohnson', 'rgreen', 'tlewis'),   # Tuesday
#         ('sharris', 'lroberts', 'cwhite', 'vsanders', 'athompson'), # Wednesday
#         ('sbennett', 'ofoster', 'madams', 'cyoung', 'tlewis'),     # Thursday
#         ('lroberts', 'dhill', 'nwalker', 'janderson', 'ajackson')  # Friday
#     ]
# }

# # Define the days of the week
# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# # Update the records
# for student_class, periods in schedules.items():
#     for day, teachers in zip(days, periods):
#         query = (
#             "UPDATE student_timetables "
#             "SET period1_teach = %s, period2_teach = %s, period3_teach = %s, "
#             "period4_teach = %s, period5_teach = %s "
#             "WHERE student_class = %s AND day = %s"
#         )
#         data = (*teachers, student_class, day)
#         cursor.execute(query, data)

# # Commit the changes
# connection.commit()

# # Close the cursor and connection
# cursor.close()
# connection.close()
# print('Successfully committed!')






# #sql query to fetch the required columns for rooms
# select_query = "SELECT room, room_subj FROM rooms"

# #execute the SQL query
# cursor.execute(select_query)

# #fetch all rows from query
# rows = cursor.fetchall()

# #process and print the results using for loop
# for row in rows:
#     room, room_subj = row
#     print(f"room: {room}, Subject: {room_subj}")

# #close the cursor and connection
# cursor.close()
# connection.close()


# rooms = {
#     'Biology': ['BL1', 'BL2', 'BL3'],
#     'Chemistry': ['CL1', 'CL2', 'CL3'],
#     'Physics': ['PL1', 'PL2', 'PL3'],
#     'Maths': ['Room 1', 'Room 2', 'Room 3', 'Room 4', 'Room 5'],
#     'English': ['Room 6', 'Room 7', 'Room 8', 'Room 9', 'Room 10'],
#     'Geography': ['Room 11', 'Room 12', 'Room 13', 'Room 14', 'Room 15'],
#     'History': ['Room 16', 'Room 17', 'Room 18', 'Room 19', 'Room 20'],
#     'Music': ['Room 21', 'Room 22', 'Room 23'],
#     'Art': ['Room 24', 'Room 25', 'Room 26'],
#     'PE': ['sports field', 'sports hall'],
#     'spare': ['Room 27', 'Room 28', 'Room 29', 'Room 30']
# }



# # Function to assign rooms based on subject and resolve conflicts
# def assign_rooms_to_timetable(class_timetables, rooms):
#     assigned_rooms = {}
#     room_counters = {subject: 0 for subject in rooms}  # Initialize room rotation counters
#     period_assignments = defaultdict(lambda: defaultdict(list))

#     for class_name, timetable in class_timetables.items():
#         assigned_rooms[class_name] = []
#         for period, subject in enumerate(timetable):
#             # Get the list of available rooms for the subject
#             available_rooms = rooms.get(subject, [])

#             if available_rooms:
#                 # Find the next available room that is not already occupied in this period
#                 assigned_room = None
#                 for i in range(len(available_rooms)):
#                     room_index = (room_counters[subject] + i) % len(available_rooms)
#                     potential_room = available_rooms[room_index]
#                     if potential_room not in period_assignments[period][subject]:
#                         assigned_room = potential_room
#                         room_counters[subject] += i + 1
#                         break

#                 if not assigned_room:
#                     # If all subject-specific rooms are occupied, use a spare room
#                     for spare_room in rooms['spare']:
#                         if spare_room not in period_assignments[period]['spare']:
#                             assigned_room = spare_room
#                             break

#                 period_assignments[period][subject].append(assigned_room)
#             else:
#                 # No subject-specific room available, assign a 'spare' room or any free room
#                 assigned_room = 'No Room Available'
            
#             assigned_rooms[class_name].append(assigned_room)

#     return assigned_rooms, period_assignments

# # Function to resolve conflicts by rescheduling rooms
# def resolve_room_conflicts(assigned_rooms, period_assignments, rooms):
#     max_reschedule_attempts = 5
#     reschedule_attempts = defaultdict(int)
    
#     for class_name, room_schedule in assigned_rooms.items():
#         for period, room in enumerate(room_schedule):
#             if room != 'No Room Available':
#                 while period_assignments[period][room].count(room) > 1 and reschedule_attempts[(class_name, period, room)] < max_reschedule_attempts:
#                     # Find a replacement room
#                     subject = class_timetables[class_name][period]
#                     replacement_found = False
                    
#                     for new_room in rooms.get(subject, []):
#                         if new_room != room and new_room not in period_assignments[period][subject]:
#                             # Replace the room in the schedule
#                             assigned_rooms[class_name][period] = new_room
#                             period_assignments[period][subject].remove(room)
#                             period_assignments[period][subject].append(new_room)
#                             replacement_found = True
#                             break
                    
#                     reschedule_attempts[(class_name, period, room)] += 1
                    
#                     if replacement_found:
#                         break
                
#                 # If we can't find a replacement after max attempts, assign any free room
#                 if period_assignments[period][room].count(room) > 1:
#                     for spare_room in rooms['spare']:
#                         if spare_room not in period_assignments[period][subject]:
#                             assigned_rooms[class_name][period] = spare_room
#                             period_assignments[period][subject].remove(room)
#                             period_assignments[period][subject].append(spare_room)
#                             break

# # Function to assign any available free room if no specific room is found
# def assign_free_room(assigned_rooms, period_assignments):
#     for class_name, room_schedule in assigned_rooms.items():
#         for period, room in enumerate(room_schedule):
#             if room == 'No Room Available':
#                 # Find any room not occupied at this period
#                 for subject, subject_rooms in rooms.items():
#                     for free_room in subject_rooms:
#                         # Check if the room is not already assigned in this period
#                         if all(free_room not in period_assignments[period][subj] for subj in period_assignments[period]):
#                             # Assign this free room
#                             assigned_rooms[class_name][period] = free_room
#                             period_assignments[period][subject].append(free_room)
#                             break

# # Assign rooms based on the provided rules
# assigned_rooms, period_assignments = assign_rooms_to_timetable(class_timetables, rooms)

# # Function to verify and resolve scheduling conflicts
# def verify_and_resolve_room_conflicts(assigned_rooms):
#     period_room_assignment = defaultdict(lambda: defaultdict(set))
#     period_assignments = defaultdict(lambda: defaultdict(list))

#     for class_name, room_schedule in assigned_rooms.items():
#         for period, room in enumerate(room_schedule):
#             subject = class_timetables[class_name][period]
#             if room != 'No Room Available':
#                 if room in period_room_assignment[period][subject]:
#                     print(f"Conflict found: Room {room} is assigned to multiple classes in period {period}. Attempting to resolve...")
#                     period_assignments[period][subject].append(room)
#                     resolve_room_conflicts(assigned_rooms, period_assignments, rooms)
#                 else:
#                     period_room_assignment[period][subject].add(room)
#                     period_assignments[period][subject].append(room)

#     # Assign any available free room to slots with 'No Room Available'
#     assign_free_room(assigned_rooms, period_assignments)

# # Verify and resolve conflicts
# verify_and_resolve_room_conflicts(assigned_rooms)

# # Output for verification
# print("\nAssigned Rooms After Resolving Conflicts and Filling Gaps:")
# for class_name, room_list in assigned_rooms.items():
#     print(f"{class_name}: {room_list}")



# Define the room schedules
# room_schedules = {
#     '9z1': [
#         ('PL1', 'Room 6', 'Room 16', 'Room 21', 'Room 24'),  # Monday
#         ('Room 7', 'Room 1', 'Room 11', 'CL1', 'sports field'),  # Tuesday
#         ('CL2', 'PL2', 'Room 2', 'Room 22', 'BL1'),  # Wednesday
#         ('Room 12', 'PL3', 'CL3', 'BL2', 'Room 25'),  # Thursday
#         ('Room 17', 'sports hall', 'Room 3', 'BL3', 'Room 8')  # Friday
#     ],
#     '9z2': [
#         ('PL2', 'Room 18', 'CL1', 'Room 9', 'Room 4'),  # Monday
#         ('PL3', 'BL1', 'Room 5', 'Room 13', 'Room 10'),  # Tuesday
#         ('BL2', 'Room 19', 'Room 1', 'Room 23', 'Room 6'),  # Wednesday
#         ('Room 21', 'Room 26', 'CL2', 'Room 14', 'sports field'),  # Thursday
#         ('BL3', 'sports field', 'PL1', 'Room 24', 'CL3')  # Friday
#     ],
#     '9z3': [
#         ('BL1', 'Room 25', 'Room 7', 'Room 2', 'Room 20'),  # Monday
#         ('Room 3', 'Room 22', 'Room 8', 'PL2', 'CL1'),  # Tuesday
#         ('Room 15', 'sports hall', 'CL2', 'Room 16', 'PL3'),  # Wednesday
#         ('CL3', 'BL2', 'Room 11', 'PL1', 'Room 23'),  # Thursday
#         ('Room 4', 'Room 27', 'BL3', 'Room 9', 'Room 26')  # Friday
#     ],
#     '9z4': [
#         ('CL1', 'Room 24', 'sports field', 'Room 22', 'Room 10'),  # Monday
#         ('Room 23', 'PL2', 'Room 1', 'Room 17', 'BL1'),  # Tuesday
#         ('Room 2', 'Room 12', 'Room 6', 'PL3', 'Room 25'),  # Wednesday
#         ('sports hall', 'BL3', 'Room 3', 'Room 13', 'CL2'),  # Thursday
#         ('Room 18', 'CL3', 'BL1', 'PL1', 'Room 7')  # Friday
#     ],
#     '9z5': [
#         ('Room 26', 'PL2', 'Room 21', 'Room 8', 'BL2'),  # Monday
#         ('Room 14', 'CL1', 'PL3', 'Room 19', 'sports hall'),  # Tuesday
#         ('Room 9', 'Room 4', 'Room 24', 'Room 15', 'CL2'),  # Wednesday
#         ('BL3', 'Room 20', 'Room 5', 'Room 22', 'sports hall'),  # Thursday
#         ('Room 1', 'BL1', 'PL2', 'Room 10', 'CL1')  # Friday
#     ]
# }

# # Define the days of the week
# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# # Update the records
# for student_class, periods in room_schedules.items():
#     for day, rooms in zip(days, periods):
#         query = (
#             "UPDATE student_timetables "
#             "SET period1_room = %s, period2_room = %s, period3_room = %s, "
#             "period4_room = %s, period5_room = %s "
#             "WHERE student_class = %s AND day = %s"
#         )
#         data = (*rooms, student_class, day)
#         cursor.execute(query, data)

# # Commit the changes
# connection.commit()

# # Close the cursor and connection
# cursor.close()
# connection.close()





# # Step 1: Select all data from student_timetables
# cursor.execute("SELECT * FROM student_timetables")
# student_timetables = cursor.fetchall()

# # Get the column names for easier access
# columns = [col[0] for col in cursor.description]

# # Step 2: Create an empty dictionary to store teacher data
# teachers_dict = {}

# # Step 3 & 4: Iterate through each record and each period to populate teacher data
# for record in student_timetables:
#     day = record[columns.index('day')]
#     class_name = record[columns.index('student_class')]

#     # Loop through period1 to period5 to gather teacher data
#     for period_index in range(5):  # Periods 1 to 5
#         period_teach_column = f'period{period_index + 1}_teach'
#         period_teach = record[columns.index(period_teach_column)]
        
#         # Check if a teacher is assigned for this period
#         if period_teach:
#             # Initialize the teacher's entry in the dictionary if not already present
#             if period_teach not in teachers_dict:
#                 teachers_dict[period_teach] = []

#             # Get the lesson (subject) and room data for the current period
#             lesson_column = f'period{period_index + 1}'  # Period lesson (subject)
#             room_column = f'period{period_index + 1}_room'  # Period room

#             lesson = record[columns.index(lesson_column)]
#             room = record[columns.index(room_column)]

#             # Append the data for this period to the teacher's entry
#             teachers_dict[period_teach].append({
#                 'day': day,
#                 'period': f'period{period_index + 1}',
#                 'class': class_name,
#                 'subject': lesson,
#                 'room': room
#             })

# # Step 5: Insert the dictionary data back into the teacher_timetables table
# for teacher, periods in teachers_dict.items():
#     for period_data in periods:
#         day = period_data['day']
#         period = period_data['period']
#         subject = period_data['subject']
#         room = period_data['room']
#         class_name = period_data['class']

#         # Prepare the insert query for the current teacher and period data
#         insert_query = f"""
#             INSERT INTO teacher_timetables 
#             (day, teach_username, {period}_subj, {period}_class, {period}_room)
#             VALUES (%s, %s, %s, %s, %s)
#             ON DUPLICATE KEY UPDATE {period}_subj = VALUES({period}_subj), 
#             {period}_class = VALUES({period}_class), {period}_room = VALUES({period}_room)
#         """
        
#         # Execute the insert query with the appropriate values
#         cursor.execute(insert_query, (day, teacher, subject, class_name, room))

# # Commit the changes to the database
# connection.commit()

# # Close the cursor and connection
# cursor.close()
# connection.close()

# print("Data inserted into teacher_timetables successfully!")


#HASHING FUNCTION

def hash(password):
    hash_value = 0
    prime = 31  #prime to increase complexity and ensure it isnt reverse-engineerable

    #iterate through each character and its position in the password
    for i, char in enumerate(password):
        #Incorporate the character's ASCII value, its position, and prime number
        hash_value += (ord(char) * prime**(i + 1)) % 100000

    #mod the final hash value to so it's 5 digits
    hash_value = hash_value % 100000

    return hash_value


#select passwords from teachers timetable
cursor.execute("SELECT student_pass FROM students")
passwords = cursor.fetchall()

#create dictionary to store original and hashed passwords
password_dict = {}

#hash each password using hash function
for password_tuple in passwords:
    original_password = password_tuple[0]  # Extract the password from the tuple

    # Apply your custom hash function
    hashed_password = hash(original_password)

    # Store the original and hashed password in the dictionary
    password_dict[original_password] = hashed_password


#insert the original and hashed passwords into 'teacher_hashes' table
for original, hashed in password_dict.items():
    #query to put data back into table
    insert_query = """
        INSERT INTO pass_hashes (user_pass, pass_hash)
        VALUES (%s, %s)
    """
    #execute query
    cursor.execute(insert_query, (original, hashed))

connection.commit()
cursor.close()
connection.close()
print('Success')