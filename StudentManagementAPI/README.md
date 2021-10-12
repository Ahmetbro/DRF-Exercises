# Student Management System

## This is a simple API for:

* creating a unified interface for keeping track of freeCodeSchool students
* accounts for students to login and see their own pages
* admins can login and see everyone via the Django admin interface
* it will be able to use Github OAuth


## Schema

* User
  * email
  * password
  * groups: student, admin, or volunteer (can only belong to one)

* StudentProfile
  * first_name
  * last_name
  * preferred_name
  * discord_name
  * github_username
  * codepen_username
  * fcc_profile_url
  * current_level
  * phone
  * timezone

* Volunteer
  * first_name
  * last_name
  * email
  * hours_available
  
* VolunteerHours
  * volunteer: FK
  * start: DateTime
  * end: DateTime
  
* Lecture
  * date
  * title
  * description
  * lecturer_name
  * slides_url
  * duration
  * level
  * required: BooleanField
  
* Attendance
  * lecture_id
  * student_id
  
* Project (labs)
  * title
  * description
  * url
  * level
  * required

* StudentSubmission
  * student_id
  * project_id
  * url: CharField
  * feedback: TextField (for comments from reviewers)
  * approved: BooleanField
  
* StudentCertificate 
  * student_id
  * certificate_id
  
* Certificate
  * name
  * description

* Waitlist
  * first_name
  * last_name
  * email
  * notes

## API

**Prefix:** /api/v1

**/users**

* get (temporary, only for testing)
* post

**/users/:id**

* get
* patch
* delete

**/users/:id/profile**

* get

*example response:*

```json
{
  "user": 6,
  "name": "Daneel Olivaw",
  "bio": "hello there...",
  "preferred_name": null,
  "avatar_url": "http://example.com",
  "discord_name": null,
  "github_username": "rdaneel",
  "codepen_username": null,
  "fcc_profile_url": null,
  "current_level": 1,
  "phone": null,
  "timezone": null
}
```

* post

**/users/:id/certificates**

* get

**/users/:id/assignments**

* get
* post

**/certificates**

* get

**/projects**

* get

## Roadmap

### Version 2

* Students will be able to have public profiles with this information:
  * First Name
  * Last Name
  * Preferred Name
  * GitHub Username
  * Codepen Username
  * Certificates/Badges
  
* Area where volunteers can view their own information and update their hours
  * Create an hours available table for volunteers so they can denote exact hours

* Set type of lecture (add type field to Lecture model)
