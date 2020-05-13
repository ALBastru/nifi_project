import sys
import json
import csv
from collections import defaultdict

#Open the Apache NiFi custom logger that will be parsed
#f = open("/opt/nifi/logs/nifi-status.log","r")

f = open("nifi-status_nlb.log","r")


Lines = f.readlines() 
linesCount = len(Lines)-1
count = 0
index = -1
# Strips the newline character 
currentFlowInfo = []
currentFlowName = ""
keyName = ""
keyValue = ""
currentFlowData = {}
finalFlowData = defaultdict(dict)
filteredFlowData = defaultdict(dict)
filteredAllData = defaultdict(dict)
currentFlowDataKey = 0
goalCounter = 1
taskCounter = 0
foundNewFlowName = False
for line in Lines:
    index += 1 
    #Variable names are after "Key:" in the current line    
    if(line.find("Key:") != -1):
        splitText = line.split("'")
        keyName = splitText[1]
        keyValue  = ''    
        continue
    #Variable value are after "Key:" in the current line
    if(line.find('Value:') != -1):
        splitText = line.split("'")
        keyValue = splitText[1]
        currentFlowData[keyName] = keyValue
    #Current Goal Name/Goal Name that will be used to group results on    
    if (keyName =="flow_name"):
        currentFlowName = keyValue
        taskCounter = 0
    if (keyName =="uuid"):
        currentFlowDataKey = keyValue        
    #A line that starts with "Standard FlowFile Attributes" denotes the end of an entry and the beginning of a new one
    if (line.strip() == "Standard FlowFile Attributes" or index==linesCount ):
        if (currentFlowName != ''):
            goalCounter += 1
            # From the gathered data use just a couple of KPI's
            if ('flow_duration_millisecond' in currentFlowData and 'type_a_count' in currentFlowData):
                mykeys = ['flow_name', 'log', 'flow_duration_human','flow_duration_millisecond',  'flow_control_update_time', 'type_a_count', 'type_b_count','type_c_count', "info_experiment_code", "info_run_number", "flow_control_update_time"]
                
                newList =  {key: currentFlowData[key] for key in mykeys if key in currentFlowData}
                charsToRemove = ['[', ']']
                currentLog = newList["log"].translate({ord(x): '' for x in charsToRemove})
                currentLogArray =  currentLog.split(":")
                counter = 0
                currentTask = defaultdict(dict)
                for logElement in currentLogArray:
                    if logElement != '':
                        taskCounter += 1
                        logElementArray = logElement.split(",")
                        counter += 1
                        currentTask[counter]['fire_team'] = logElementArray[0]
                        currentTask[counter]['state'] = logElementArray[1]
                        currentTask[counter]['radio_silence'] = logElementArray[2]
                        currentTask[counter]['node'] = logElementArray[3]
                        currentTask[counter]['process_type'] = logElementArray[4]
                        currentTask[counter]['resource_qty'] = logElementArray[5]
                        currentTask[counter]['duration'] = logElementArray[6]
                        currentTask[counter]['ignored_node'] = logElementArray[7]                        
                        currentTask[counter]['time_since_start'] = logElementArray[8]                        
                        newIndex = int(max(filteredAllData.keys(), default=0)) + 1
                        filteredAllData[newIndex]['goal'] =  currentFlowName
                        filteredAllData[newIndex]['task'] = "T #"+ str(taskCounter)
                        filteredAllData[newIndex]['fire_team'] = logElementArray[0]
                        filteredAllData[newIndex]['state'] =  logElementArray[1]
                        filteredAllData[newIndex]['radio_silence'] =  logElementArray[2]
                        filteredAllData[newIndex]['node'] =  logElementArray[3]
                        filteredAllData[newIndex]['process_type'] =  logElementArray[4]
                        filteredAllData[newIndex]['resource_qty'] =  logElementArray[5]
                        filteredAllData[newIndex]['duration'] =  logElementArray[6]
                        filteredAllData[newIndex]['ignored_node'] =  logElementArray[7]
                        filteredAllData[newIndex]['time_since_start'] =  logElementArray[8]
                        filteredAllData[newIndex]['goal_duration'] = newList['flow_duration_millisecond']
                        filteredAllData[newIndex]['type_a_count'] = newList['type_a_count']
                        filteredAllData[newIndex]['type_b_count'] = newList['type_b_count']
                        filteredAllData[newIndex]['type_c_count'] = newList['type_c_count']
                        filteredAllData[newIndex]['info_experiment_code'] = newList['info_experiment_code']
                        filteredAllData[newIndex]['info_run_number'] = newList['info_run_number']
                        if (not 'flow_control_update_time' in newList):
                            newList['flow_control_update_time'] = "n_a"
                        filteredAllData[newIndex]['flow_control_update_time'] = newList['flow_control_update_time']
                        filteredFlowData[currentFlowName] = newList
                        filteredFlowData[currentFlowName]["tasks"] = currentTask                
            if (currentFlowName in finalFlowData):
                if(currentFlowDataKey in finalFlowData[currentFlowName]):                
                    for k in currentFlowData:
                        finalFlowData[currentFlowName][currentFlowDataKey][k] = currentFlowData[k]                        
                else:
                    finalFlowData[currentFlowName][currentFlowDataKey] = currentFlowData         
            else: 
                finalFlowData[currentFlowName][currentFlowDataKey] = currentFlowData                
            currentFlowData = {}
            currentFlowDataKey = 0


# For debugging purposes can output part of the logs to some files

# with open('data_dump.json', 'w', encoding='utf-8') as f:
#     json.dump(finalFlowData, f, ensure_ascii=False, indent=4)
# with open('all_filtered_data.json', 'w', encoding='utf-8') as f:
#     json.dump(filteredAllData, f, ensure_ascii=False, indent=4)
# with open('filtered_data.json', 'w', encoding='utf-8') as ff:
#     json.dump(filteredFlowData, ff, ensure_ascii=False, indent=4)


#Output the result to a CSV file

with open('all_results_nlb.csv', 'w') as output:
    writer = csv.writer(output, delimiter=',')
    writer.writerow(["goal","task", "fire_team", "state", "radio_silence", "node","ignored_node", "process_type", "resource_qty", "duration", "time_since_start", "goal_duration","type_a_count","type_b_count", "type_c_count", "info_experiment_code", "info_run_number", "flow_control_update_time" ])
    for flowName  in filteredAllData:
        info  = filteredAllData[flowName]        
        if not "info_run_number" in info:
            info["info_run_number"] = 1
        if not "info_experiment_code" in info:
            info["info_experiment_code"] = "DEFAULT"

        if not "duration" in info:
            info["duration"] = -1
        else:            
            info["duration"] = info["duration"]
        if not "time_since_start" in info:
            info["time_since_start"] = -1
        else:            
            info["time_since_start"] = info["time_since_start"]
        if not "type_a_count" in info:
            info["type_a_count"] = -1
        if not "type_b_count" in info:
            info["type_b_count"] = -1
        if not "type_c_count" in info:
            info["type_c_count"] = -1
        writer.writerow([str(info['goal']),str(info['task']),str(info['fire_team']), str(info["state"]), str(info['radio_silence']), str(info['node']), str(info['ignored_node']), str(info['process_type']), str(info['resource_qty']), str(info['duration']), str(info['time_since_start']), str(info['goal_duration']), str(info["type_a_count"]), str(info["type_b_count"]), str(info["type_c_count"]), str(info["info_experiment_code"]), str(info["info_run_number"]),str(info["flow_control_update_time"])])