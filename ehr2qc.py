__author__ = 'Vitaliy'


import psycopg2
from sys import stdin

# Try to connect

def createQCSearchJsonRequest( term ):
    profile = """{"profileId":66, "queryFields":[
          {
             "id":223, "displayOrder":1, "displayName":"Patient/Problem", "searchField":"{0}"
          },
          {
             "id":252,
             "displayOrder":2,
             "displayName":"Intervention",
             "searchField":" "
          },
          {
             "id":253,
             "displayOrder":3,
             "displayName":"Compare to (leave blank if none)",
             "searchField":" "
          },
          {
             "id":254,
             "displayOrder":4,
             "displayName":"Outcome (optional)",
             "searchField":" "
          }
       ]
    }""" #.format(term)
    return profile


try:
    conn = psycopg2.connect("host='10.4.56.14' dbname='omop' user='postgres' password='5'")
except:
    print "I am unable to connect to the database."

cur = conn.cursor()
try:
    cur.execute("""select c.condition_start_date, cc.* from person p,
                                        public.visit_occurrence v,
                                        public.condition_occurrence c
                                        , public.concept cc
where p.person_id = v.person_id
        and v.visit_occurrence_id = c.visit_occurrence_id
        and c.condition_concept_id = cc.concept_id
        and p.person_id = 41530
order by c.condition_start_date desc""")
except:
    print "I can't SELECT from"

rows = cur.fetchone()
# print "\nRows: \n"
searchTerm = rows[2]
# print " row  ", rows[2]
# for i, row in enumerate(rows):
#     print " row  ",i, row[2]


print createQCSearchJsonRequest(searchTerm)




inputString = stdin.readline()
print