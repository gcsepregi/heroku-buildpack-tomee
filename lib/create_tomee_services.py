import json
import os

service_descriptor = json.loads(os.environ['VCAP_SERVICES'])

tomee_xml = open('tomee.xml', 'w')

tomee_xml.write('''
<?xml version="1.0" encoding="UTF-8"?>
<tomee>
  <!-- see http://tomee.apache.org/containers-and-resources.html -->

  <!-- activate next line to be able to deploy applications in apps -->
  <!-- <Deployments dir="apps" /> -->
''')

# parsing mysql datasources
mysql_datasources = service_descriptor['mysql']

for datasource in mysql_datasources:
    tomee_xml.write('<Resource id="' + datasource['name'] + '" type="javax.sql.DataSource">')
    tomee_xml.write('    JtaManaged    true')
    tomee_xml.write('    JdbcDriver    com.mysql.jdbc.Driver')
    tomee_xml.write('    JdbcUrl       ' + datasource['credentials']['jdbcUrl'])
    tomee_xml.write('    UserName      ' + datasource['credentials']['username'])
    tomee_xml.write('    Password      ' + datasource['credentials']['password'])
    tomee_xml.write('</Resource>')

tomee_xml.write('</tomee>') 