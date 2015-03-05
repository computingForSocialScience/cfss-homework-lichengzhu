import MySQLdb
import unicodecsv
import datetime

db = MySQLdb.connect(host='mcmahan.zapto.org', user='cfss15', passwd='computers', db='cfss', port=9999)
c = db.cursor()
f= open('countires.csv')
mycsv = unicodecsv.reader(f)

header = True
for l in mycsv:
    print l
    if header:
        header=False
        continue
    print l
    country = l[0]
    google_country_code= l[1]
    country_group = l[2]
    name_en = l[3]
    name_fr= l[4]
    name_de = l[5]
    latitude = l[6]
    longitude = l[7]
    sql = "INSERT INTO countries (country, google_country_code, country_group, name_en, name_fr, name_de, latitude, longitude) VALUES ('%s','%s','%s', '%s' ,'%s','%s', '%s','%s')" % (country, google_country_code, country_group, name_en, name_fr, name_de, latitude, longitude)
    print sql
    c.execute(sql)
db.commit()
c.close()