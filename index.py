import yaml

with open(r'C:\Users\kiran\Downloads\DataSet\Milestone1\Milestone1A.yaml') as file:
    documents = yaml.full_load(file)

    for item, doc in documents.items():
        print(item, ":", doc)

import datetime
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"),end="")
print("000000")

import yaml
import datetime,time
def carryOutSequentialTask(flowName,task):
    print("{}; {} Entry".format(datetime.datetime.now(),flowName))
    if(task["Function"] == "TimeFunction"):
        print("{}; {} Executing TimeFunction({})".format(datetime.datetime.now(),flowName,task["Inputs"]["ExecutionTime"]))
        time.sleep(int(task["Inputs"]["ExecutionTime"]))
    print("{}; {} Exit".format(datetime.datetime.now(),flowName))

def carryOutFlow(flowName,workFlow):
    print("{}; {} Entry".format(datetime.datetime.now(),flowName))

    if(workFlow["Execution"] == "Sequential"):
        activities = workFlow["Activities"]
        t = list(activities.keys())

        for j in t:
            if(activities[j]["Type"] == "Task"):
                carryOutSequentialTask(flowName+"."+j,activities[j])
            elif(activities[j]["Type"] == "Flow"):
                carryOutFlow(flowName+"."+j,activities[j])

    elif(workFlow["Execution"] == "Concurrent"):
        activities = workFlow["Activities"]
        t = list(activities.keys())

    elif(workFlow["Execution"] == "Nested"):
        activities = workFlow["Activities"]
        t = list(activities.keys())
    elif(workFlow["Execution"] == "Conditional"):
        activities = workFlow["Activities"]
        t = list(activities.keys())

    print("{}; {} Exit".format(datetime.datetime.now(),flowName))
with open("Milestone1/Milestone1A.yaml") as stream:
    dict = yaml.safe_load(stream)
    k = list(dict.keys())
    for i in k:
        if(dict[i]["Type"] == "Flow"):
            carryOutFlow(i,dict[i])
        elif(dict[i]["Type"] == "Task"):
            carryOutSequentialTask(i,dict[i])
