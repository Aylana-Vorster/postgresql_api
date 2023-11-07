# postgresql_api
PostgreSQL API/Requests Implementation using postgresql as an alternative to SQLAlchemy

Here's an example of an insert function with many local variables that need to be passed:
```
query = """INSERT INTO public."Cams_from_nx" (guid, cam_name, serverid,url,tag) VALUES ('"""+ str(i["id"][1:-1]) + """','""" + i["name"] + """','""" + i["serverId"][1:-1] + """','""" + i["url"] + """','""" + str(i["name"].rsplit('-', 1)[-1]) +"""') """
```

Here's an example of the paramaters needed:
```
host= "localhost" #or the ip
port= "5432"
database= "my_first_db"
user= "postgres"
password= "12345"
```

