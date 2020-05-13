# Apache NiFi Project
Repository for the Apache NiFi project


<h3>Servers</h3>

<b>NiFi_Server IP</b>: 10.150.8.204<br/>
<b>NiFi Instance</b>: http://10.150.8.204:8080/nifi/<br/>

<b>NiFi_Registry IP</b>: 10.150.8.220<br/>

<h3>GIT Repository</h3>
Website: https://github.cs.adelaide.edu.au/<br/>
URL: https://github.cs.adelaide.edu.au/a1059233/nifi-project.git<br/>

<h3>Python for Scripts</h3>

Using version 3.7
Using pyhocon, HOCON parser. <br/>
<em>pip3 install pyhocon</em>

<h3>Useful scripts on server:</h3>

Creating new set of goal files<br/>
<em>sudo python3 /nifi_proj/config/full_config_generate.py </em><br/><br/>
Clearing the current log used to extract information from <br/>
<em>echo "" | sudo tee /opt/nifi/logs/nifi-status.log</em><br/><br/>
Check the current log size<br/>
<em>ls -l /opt/nifi/logs/nifi-status.log</em><br/>
