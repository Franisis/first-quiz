import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """


SELECT animals.name, animals.species, animals.age
FROM animals
where animals.animal_id not in (SELECT pet_id from people_animals)

"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """

SELECT COUNT(*)
FROM ANIMALS, PEOPLE_ANIMALS, PEOPLE
WHERE PEOPLE_ANIMALS.owner_id = PEOPLE.person_id
AND PEOPLE_ANIMALS.pet_id = ANIMALS.animal_id 
AND PEOPLE.age<animals.age


"""

# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """ 

SELECT p.name AS person_name, a.name AS pet_name, a.species
FROM people p
INNER JOIN people_animals pa ON p.person_id = pa.owner_id
INNER JOIN animals a ON pa.pet_id = a.animal_id
WHERE p.name = 'bessie'
AND a.animal_id not in (
        SELECT pet_id 
        FROM people_animals pa, people
        WHERE people.name != 'bessie'
        and people.person_id = pa.owner_id
        );
"""