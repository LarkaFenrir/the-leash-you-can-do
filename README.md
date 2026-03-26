# 🐶 The Leash You Can Do
**The Leash You Can Do** app is designed to help shelters and future adopters of furry babies connect more easily.\
Whether you'd like to know which sweet pups are looking for a forever home or which ones would love to be taken for a stroll, **The Leash You Can Do** makes the process simple and enjoyable. And who knows? Maybe after a walk together, you'll decide to take the next step and apply to become a furry parent.\
If you have questions or need support along the way, volunteers are always available to guide you and your future companion into the next chapter of your lives - together.

## The Idea
This project is inspired by the real challenges faced by animal shelters today, such as shortages of volunteers, adopters, and resources.\
**The Leash You Can Do** aims to:\
🌟 Help shelters showcase animals available for adoption\
🌟 Allow people to interact with animals before committing to adoption\
🌟 Encourage volunteering through walks, courses, and informational sessions\
🌟 Support shelters by simplifying basic organization and communication\
Even when users cannot adopt, they can still build meaningful bonds with animals by volunteering their time.

## Features
🐾 User registration for volunteers and potential adopters\
🐾 Shelter accounts to manage pets and activities\
🐾 Pet listings with adoption availability\
🐾 Booking system for walks, courses, and meetings with volunteers\
🐾 User profiles to track activities and adoption progress

## Technical Overview
**The Leash You Can Do** is built using Django and Python, following a simple REST API architecture.
### Main Models
#### Pet
* name
* sex
* age
* kind of pet
* breed
* description
* availability
#### User
* username
* email
* password
* role (volunteer or adopter)
#### Course
* title
* description
* category (obedience, first aid, responsible ownership)
#### Booking
* user
* pet (optional)
* course (optional)
* date
* type (walk, course, meeting)
