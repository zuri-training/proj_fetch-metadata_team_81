# **PROJECT NAME: METADRIX**
# **TEAM: 81**

## Project Brief
> >  <br>*Metadrix is a platform that extracts and displays the metadata of a particular file uploaded by a user. It allows the users to view the metadata, save it, download it, share it and convert it to any file format. Types of files that can be uploaded include images, csv, PDFs and JSON.* <br><Br>

<br>

## Goals

* To have a landing page that gives essential information about the web app. <br>
* To display the features the web application can perform which includes analyzing and converting data.<br>
* To generate metadata of files uploaded.<br>
* To export, download and share metadata recovered.<br>
* To ensure registered user can save data and resume download upon sign in<br><br>

## Background Context 

It is quite an unusual request to ask for the metadata of a file but the need arises every now and then. Although there are quite a number of platforms that derive and synthesize relevant information from files, they are riddled with poor management of all metadata information and a less interactive interface which is unfriendly to the average user.<br><Br>


>>>> <br>*“I need not to be bothered with more problems when I want my problems solved. A platform that offers all the basics and covers all the surfaces.<br>
It would also be great if I could recover and have access to my files upon sign up and sign in which in itself is a form of commitment to offer up my personal details in the first place because loss is bound to happen.”<br><br>*

<br><Br>
## Target Audience
* Law enforcement agencies in Investigative considerations. 
* File Analysts.<br><br>

## Features 

* Landing page: it allows site visitors to understand what the platform does <br>
* Sign in page: it allows existing users to have access to their account <br>
* Sign up page: it allows new users to create an account. <br>
* Dashboard: it gives users complete access to the platform (this is where files can be uploaded, metadata extracted, downloaded, shared and converted). Users can also track their activities here. <br>
* Contact us (where users can reach us) <br><br><br>

# <a name="contribute"></a> Contribution Guide

- Fork the project.

- Clone your own forked repository, run:
~~~
$ git clone "https://github.com/[your_github_username]/proj_fetch-metadata_team_81.git"
~~~
- Add remote upstream using the command:
~~~
$ git remote add upstream "https://github.com/zuri-training/proj_fetch-metadata_team_81.git"
~~~
- run:
~~~
$ git fetch upstream (You must fetch from the develop branch before or after checkout)
~~~
- run:
~~~
$ git merge upstream/develop (Merge updates from upstream)
$ git checkout -b ft-user-login (You are in the ft-user-login branch now)
~~~
  ## To push to github;<br/>
~~~
$ git add .
$ git commit -m "feat: implemented user login"
$ git pull origin ft-user-login (your forked version of the repository)
$ git push origin ft-user-login (note how it ends with a branch.) 
~~~


### Ensure your PR branch is titled in the following format<br/>
~~~
$ Ft-Feature (eg. "ft-user-login")
~~~
### Commit Message Format: `chore`, `feature`, `bug`

For a feature:
~~~
$ git commit -m "feat: implemented user log-in"
~~~
For a bug: 
~~~
$ git commit -m "bug: fixed inconsistency in log in screen"
~~~
For a chore:
~~~
$ git commit -m "chore: updated read me to include API endpoints"
~~~
<br>

## Create your PR to the `develop` branch of this repository.

 When making a PR, your PR is expected to have the following comments:<br/>

- What is the task completed ?
- What the PR actually does ?
- How can this PR be manually tested ?
- Screenshots (if applicable)
<br><br><br>

# USER RESEARCH
## Research Plan for METADRIX (A Metadata Platform)
### Idea brief: *Metadata platform to help improve customer experience when viewing and imputing metadata.*<br><br>
### **Client:** `Zuri`
### **Role:** `Product Designer` <br><Br>
## Research Background
From my secondary research, mostly conducted through google searches to further understand the meaning and usage of a metadata platform, it has been noticed that some challenges faced by users of metadata platforms include: poor management of all metadata, lack of access, less interactive interface and complexity of metadata presentation(this breaks Millers’ Law because it gives users too many things to keep in their working memory. e.g …working memory, and according to him this leads to lack of interest*)<br><Br>

## Problem Statement
As mentioned above, the problems noticed about metadata platforms are mainly related to the management and presentation of the metadata on the platforms. Research has shown that a huge problem users encounter is the inability to filter through the metadata as it is not presented in a concise manner for ease of accessibility. The interfaces are not  appealing to use and have  only basic features.<br><Br>
## Research Objectives
1. With this research we aim to examine the full scope of the problems discussed and to see any other problems that might have been missed.
2. Look into the ways it has affected users and what they see as huge issues so features can be implemented to fix these issues.
3. Examine the solutions that could be implemented and also get a wishlist of features users would like to see that would aid their use of the platform .<br><Br>
## Research Questions
* How often do they use metadata platforms? (Behaviors)
* Do they use metadata for viewing purposes or for inputting too? (Behaviors)
* Have they been able to view metadata easily? (Pain points)
* Have they had accessibility issues with viewing the metadata ? (Pain points)
* How organized are the metadata on these platforms ? ( Pain points)<br><Br>

## Method & Recruiting
The recruitment will be done in two phases, the first is a Google forms questionnaire constructed by Ajibola Omoyayi, a team members that would then funnel willing participants to an online interview for about 3 to 5 minutes where they would provide their insights into the metadata platforms and their experiences using  them. 
## Timeline
> * Milestone 1: Research and break down of data
>> * Milestone 2: User journey and wireframes
>>> * Milestone 3: Hi-Fi Designs
>>>> * Milestone 4: Prototype and Presentation of case study

<br>

## Interview Script
### Introduction
Hello and thank you for participating in this research study. I am Babajide Oluwaferanmi. I am working on a project that involves metadata platforms and some problems people face while using them. I would love to hear about your experience(s), so I will be asking you a series of questions.
This interview will last a maximum of 10 minutes. However, if you wish to take a break or leave, you are absolutely free to do so. Also, this interview is not a test of knowledge on any subject matter. There are no wrong answers so please feel free to express yourself.<br><Br>
### Do you have any questions before we start?
#### Section 1: *Creating rapport*
>* How old are you?
>* What state are you from ?
>* What is your favorite method of dealing with metadata?
#### Section 2: *Finding out behaviors and motivations*
>* Why do you use metadata platforms ?
>* Why not some other ways of dealing with metadata?
>* Have you ever tried another option other than a metadata platform?Why not?
>* Would you still use a platform if it was less organized than other means? Why?
>* How many times a month do you use metadata platforms?
#### NoSection 3: *Finding out pain points*
>* What is your biggest problem with metadata platforms?
>* Do metadata platforms often frustrate you ?
>* Would you say metadata platforms are effective? If not why.
>* Would you say metadata platforms should make access easier?
>* Would well organized metadata platforms make access ofto your imputed metadata easier?

Section 4: Wishlist of Features
>* What features would aid your use of metadata platforms
>* What are some features about metadata platforms that you dislike?
>* Are there any features you think they should have which they don’t?
I really appreciate this opportunity. Thank you for giving your time to helping me build a better product.

<br><br>

# Design Documentation 
[Team](https://docs.google.com/spreadsheets/d/1XTySY9v9Um3r1PXwa9b3JnNb4IIwOWa_h4ZVisebvFY/edit#gid=0)

[Figjam board](https://www.figma.com/file/WVx8Ffc1Ay9X1n5COCeI9F/TEAM-81-USER-RESEARCH?node-id=0%3A1)

[Figma Board](https://www.figma.com/file/G0uwfELRR8TT7hzV6NvJbQ/Team81_proj-fetch-metadata?node-id=730%3A32459)

[User Research plan](https://docs.google.com/document/d/1ldFvCMjYGGkGMnb8vzSOZgfVgUHv4qxOx1Ptkd38e1A/edit?usp=drivesdk)

[Project Database Schema](https://www.figma.com/file/cgAhnz0QCtI7Yp25tnUW7Q/Database-Schema?fuid=1079883776695949775)
