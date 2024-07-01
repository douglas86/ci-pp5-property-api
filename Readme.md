# Property UK

---

![Code Institute Logo](https://camo.githubusercontent.com/654be5a252cf75ac9ac6ea453f7bfe3b2d437f3e6789ed91924bfe501b0df142/68747470733a2f2f636f6465696e737469747574652e73332e616d617a6f6e6177732e636f6d2f66756c6c737461636b2f63695f6c6f676f5f736d616c6c2e706e67)

---

## Description

This forms part of my fifth project with code institute.

This API is used to store and retrieve data from the database, as well as Register, login or logout users.
This app is designed to help solve the Property Market problem.
You can buy, rent, submit complaints or report maintenance issues.
You will also be able to see what maintenance contractor has been assigned to your maintenance issue.

---

[//]: # (Badges)

![Pop OS](https://img.shields.io/badge/Pop!_OS-48B9C7?style=for-the-badge&logo=Pop!_OS&logoColor=white)
![Pycharm](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)
![Google Chrome](https://img.shields.io/badge/Google_chrome-4285F4?style=for-the-badge&logo=Google-chrome&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Django Rest Framework](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Daphne](https://img.shields.io/badge/daphne-092E20?style=for-the-badge&logo=django&logoColor=green)
![Sqlite](https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![postgres](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)

---

## Table of content

- [Planning](#planning)
    - [ERD diagrams for mapping out my models](#erd-diagrams-for-mapping-out-my-models)
    - [User Stories using MOSCOW Prioritization techniques](#user-stories-using-moscow-prioritization-techniques)
    - [A Proper Description of the Technologies used in this API](#a-proper-description-of-the-technologies-used-in-the-api)
    - [Description of how the code is organized](#description-of-how-the-code-is-organized)
- [Features](#features)
  - [async/await](#asyncawait) 
- [Testing](#testing)
- [Bugs](#bugs)
  - [Does not want to display data on heroku app](#does-not-want-to-display-data-on-heroku-app)
  - [Cant create superuser the normal way](#cant-create-superuser-the-normal-way)
- [Credits](#credits)

___

### [Planning](#planning)

#### [ERD diagrams for mapping out my models](#erd-diagrams-for-mapping-out-my-models)

#### [User Stories using MOSCOW Prioritization techniques](#user-stories-using-moscow-prioritization-techniques)

#### [A Proper Description of the Technologies used in the API](#a-proper-description-of-the-technologies-used-in-the-api)

- Pop Os is a Linux distribution from System76 that I use for development
- Pycharm was used as my IDE as it gives me better features to be more productive
- Django was used as my Backend framework
- Django Rest Framework was used in conjunction with Django to write this API
- Daphne was used to add async/await to my API design
- Sqlite was used as my local database when I was developing locally
- Postgres was used in conjunction with heroku for an online database
- Figma was used to design my ERD diagram
- Heroku was used as my cloud provider

#### [Description of how the code is organized](#table-of-content)

---

### [Features](#table-of-content)

#### [async/await](#features)

- I was able to get async / await right in this project
- With the help of a Package called [daphne](https://pypi.org/project/daphne/)
- I also needed to use a Package called [adrf](https://pypi.org/project/adrf/) for async/await views
- If you want to find out how I set up django for async / await, click [here](https://docs.google.com/document/d/1f-XpQLNI51lp_32UEDDWBoK9GzG8L_m7pP11FSGgwPs/edit#heading=h.cbds7u507bkn)

---

### [Testing](#table-of-content)

---

### [Bugs](#table-of-content)

#### [Does not want to display data on heroku app](#table-of-content)

#### Problem?

- when I go to the heroku live link it doesn't want to display
- data as JSON data

![problem1.png](assets/docs/heroku_app/problem1.png)

#### Solution?

- Adding a key value pair to REST_FRAMEWORK dictionary did the trick

![solution.png](assets/docs/heroku_app/solution.png)

#### [Cant create superuser the normal way](#table-of-content)

##### Problem?

- I cant seem to create superuser from the terminal
- Then register through postman

##### Solution?

- I had to create the user through Postman first
- then run python shell to create the superuser the long way

![first.png](assets/docs/superuser/first.png)

---

### [Credits](#table-of-content)

---