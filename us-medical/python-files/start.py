import csv


"""
Some possible ideas for analysis are the following:

Find out the average age of the patients in the dataset.
Analyze where a majority of the individuals are from.
Look at the different costs between smokers vs. non-smokers.
Figure out what the average age is for someone who has at least one child in this dataset."""


class Pattients:
    def __init__(
        self, ages, sexes, bmis, num_children, is_smoker, regions, charges
    ) -> None:
        self.ages = ages
        self.sexes = sexes
        self.bmis = bmis
        self.num_children = num_children
        self.is_smoker = is_smoker
        self.regions = regions
        self.charges = charges

    def analise_ages(self):
        total_age = 0
        for age in self.ages:
            total_age += int(age)
        return (
            "Average Patient Age: "
            + str(round(total_age / len(self.ages), 2))
            + " years"
        )

    def unique_regions(self):
        d = {}
        for i in self.regions:
            d[i] = d.get(i, 0) + 1
        
        return "Majority of people are from: " + max(d,key=lambda x: d[x]) 
    
    def smoker_charges(self):
        d={'yes': [0,0],'no':[0,0]}
        for i in range(len(self.is_smoker)):
            d[self.is_smoker[i]][0]+=1
            d[self.is_smoker[i]][1]+=float(self.charges[i])
        return 'Average charges for smokers are: '+ str(round(d['yes'][1]/d["yes"][0],2)) + '\nAverage charges for non smokers are: ' + str(round(d['no'][1]/d["no"][0],2))

    def sex_charges(self):
        d={'male': [0,0],'female':[0,0]}
        for i in range(len(self.sexes)):
            d[self.sexes[i]][0]+=1
            d[self.sexes[i]][1]+=float(self.charges[i])
        return 'Average charges for male are: '+ str(round(d['male'][1]/d["male"][0],2)) + '\nAverage charges for female are: ' + str(round(d['female'][1]/d["female"][0],2))

    def children_charges(self):
        d={'0':[0,0],'more':[0,0]}
        for i in range(len(self.num_children)):
            number = int(self.num_children[i])
            if number>0:
                d['more'][0]+=1
                d['more'][1]+=float(self.charges[i])
            else:
                d['0'][0]+=1
                d['0'][1]+= float(self.charges[i])
        return 'Average charges without kids: '+ str(round(d['0'][1]/d["0"][0],2)) + '\nAverage charges with 1 kid or more: ' + str(round(d['more'][1]/d["more"][0],2))+' num of people with 1 or more  '+str(d["more"][0])

def load_list_data(lst, csv_file, column_name):
    with open("../python-portfolio-project-starter-files/" + csv_file) as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            lst.append(row[column_name])
        return lst


file_name = 'insurance.csv'
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

load_list_data(ages, file_name, "age")
load_list_data(sexes, file_name, "sex")
load_list_data(bmis, file_name, "bmi")
load_list_data(num_children, file_name, "children")
load_list_data(smoker_statuses, file_name, "smoker")
load_list_data(regions, file_name, "region")
load_list_data(insurance_charges, file_name, "charges")

p1 = Pattients(
    ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges
)
p1.analise_ages()
p1.unique_regions()
print(p1.smoker_charges())
print(p1.sex_charges())
print(p1.children_charges())