from nipyapi import config, canvas, nifi
pgs = canvas.list_all_process_groups()
cons = []
for pg in pgs:
    cons += nifi.ProcessGroupsApi().get_connections(pg.id).connections
for con in cons:
    #print (con.id)
    canvas.purge_connection(con.id)
