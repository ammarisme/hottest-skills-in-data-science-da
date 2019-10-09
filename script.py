import csv
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import json
import os
    
lemmatizer = WordNetLemmatizer()

# function to convert nltk tag to wordnet tag
def nltk_tag_to_wordnet_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:          
        return None

def lemmatize_sentence(sentence):
    #tokenize the sentence and find the POS tag for each token
    nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))  
    #tuple of (token, wordnet_tag)
    wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        if tag is None:
            #if there is no available tag, append the token as is
            lemmatized_sentence.append(word)
        else:        
            #else use the tag to lemmatize the token
            lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
    return " ".join(lemmatized_sentence)


def load_resumes():
    resumeStores = []
    myResumes =[]
    for filename in os.listdir('./resumes'):
        with open('./resumes/'+filename, 'r') as f:
            resumeStores.append(json.load(f))
    for resumeStore in resumeStores:
        myResumes .extend(resumeStore["resumeModels"])    
    
    return myResumes;



def load_jobs():
    myJobs = []
    for filename in os.listdir('./jobs'):
        with open('./jobs/'+filename, 'r') as k:
            job = json.load(k)
            myJobs.extend(job.values())
    return myJobs
#for jobStore in jobStores:
 #   jobs.append(jobStore)    
 
jobs = load_jobs()
resumes =load_resumes()



skillsAvailable = []
def extract_skills_from_resumes(myResumes):
    mySkillSupply = []
    ignoreList = [];
    for resume in myResumes:
        for skill in resume["skills"]:
            skillName = lemmatize_sentence(str.lower(skill["skill"]))
            if( skillName not in skillsAvailable and (skillName  not in ignoreList )):
                skillsAvailable.append(skillName)
                mySkillSupply.append([skillName,1,0,0])
            elif (skillName in skillsAvailable) :
                mySkillSupply[skillsAvailable.index(skillName)][1] = mySkillSupply[skillsAvailable.index(skillName)][1] +1;

    return mySkillSupply

def add_skills_in_summaries(myResumes, mySkillSupply):    
    i = 0
    for resume in myResumes:
        i = i +1
        print(i)
        summaryText = lemmatize_sentence(str.lower(resume['summary']) );
        summaryArray= str.split(summaryText , ' ');
        for skill in resume["skills"]:
            skillName = lemmatize_sentence(str.lower(skill["skill"]))
            if(skillName in summaryArray and skillName  in skillsAvailable):
                mySkillSupply[skillsAvailable.index(skillName)][1] = mySkillSupply[skillsAvailable.index(skillName)][1] +1;

    return mySkillSupply

def save(skillSupply, fileName):
    with open(fileName, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(list(skillSupply))

#print('extracting skills : step 1')
#skillsSupply = extract_skills_from_resumes(resumes);
#print('extracting skills : step 2')
#skillsSupply = add_skills_in_summaries(resumes ,skillsSupply)
#print('skills supply')

def cleanhtml(raw_html):
  import re
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

keywords = []

skillDemand = [];

def generate_final_dataset(jobs,skillsAvailable, mySkillSupply):
    i = 0;
    for jobKey in jobs:    
        i = i + 1
        print(i)
        whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        #myStr = str.split(jobs[jobKey], ' ')
        jobDescription = cleanhtml(jobKey);
        jobDescription = str.replace('  ' ,' ', jobDescription)
        jobDescription= str.replace('   ' ,' ', jobDescription)
        jobDescription = str.replace('    ' ,' ', jobDescription)
        jobDescription = str.lower(jobDescription);
        
        answer = ''.join(filter(whitelist.__contains__, jobDescription))
        myStrArray  = str.split(answer, ' ');
        
        for word in list(myStrArray):  # iterating on a copy since removing will mess things up
            if word not in skillsAvailable:
                myStrArray.remove(word)
    
        jobSkills = set(myStrArray)
        for jobSkill in jobSkills:
                    mySkillSupply[skillsAvailable.index(str.lower(jobSkill))][2] = mySkillSupply[skillsAvailable.index(str.lower(jobSkill))][2] +1;
        
        keywords.extend(jobSkills)
    
    for skill in mySkillSupply:
        if(skill[1] > 0 and skill[2] > 0):
            skill[3]  = skill[2] / skill[1]

    return mySkillSupply

#skillsSupply = generate_final_dataset(jobs, skillsAvailable, skillsSupply)
#print(skillsSupply);
#save(skillsSupply , 'skills_data.csv')


def hotness(elem):
    return elem[3]

# random list
import csv
    
def final_cleaning():    
    
    file=open( "./skills_data.csv", "r")
    reader = csv.reader(file)
    # hottest # ignoreList = ['testing' ,'jenkins','training' , "dynamics", 'javascript' , "marketing", 'recruitment' , 'publishing' , 'quantitative' ];
    ignoreList = ['analytics' , 'quantitative'];
    
    final_array = [];
    for line in reader:
        t=line[0]
        whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,')
        #myStr = str.split(jobs[jobKey], ' ')
        
        answer = ''.join(filter(whitelist.__contains__, t))
        myStrArray  = str.split(answer, ','); 
        if(len(myStrArray) == 4 and not(myStrArray[0] in ignoreList)):
                myStrArray[1] = float(myStrArray[1])
                myStrArray[2] = float(myStrArray[2])
                myStrArray[3] = (float(myStrArray[2])); #hottest skills
                final_array.append(myStrArray);
                
    return final_array
    
def draw_chart(xlabel, ylabel , title, data):
    from collections import Counter
    
    Counter = Counter(keywords)
    most_occur = data[:10];
    
    from collections import Counter
    import numpy as np
    import matplotlib.pyplot as plt
    
    
    labels = []
    values = []
    
    for index in most_occur:
        labels.append(index[0])
        values.append(index[3])
    
    indexes = np.arange(len(labels))
    width = 1
    
    
    plt.xlabel(xlabel, fontsize=5)
    plt.ylabel(ylabel, fontsize=5)
    #plt.xticks(index, labels, fontsize=5, rotation=30)
    plt.title(title)
    
    plt.bar(indexes, values, width=0.5)
    plt.xticks(indexes, labels, rotation= 45)
    plt.show()

skillSupply = final_cleaning()
        
# sort list with key
skillSupply.sort(key=hotness ,reverse = True)
#draw_chart('Skills' , '% of CVS with the skill / Total CVs' , 'Most available skills in Data Science' , skillSupply)
#draw_chart('Skills' , 'No. of Jobs / No. of CVs' , 'Hottest skills in Data Science' , skillSupply)
draw_chart('Skills' , 'No. of Jobs' , 'Most sought out skills in Data Science' , skillSupply)

