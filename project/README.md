# CS50 Project

# Medical portal

**description**:a medical portal which allow user to do multiple things:

- add pre-description and be able to edit them also has a no.of time a day with and wether it is af - bf - na

## data base demo

### user

- id
- Username
- Password

### posts

- id
- Symptoms
- Medications
- Diagnoses
- Notes/description

### med

- Id
- User_id
- Time
- No

## Routing

- “/” get the home page
- “/posts“ go to the community page
- “/addpost”go to the form to add post
- “/Med“  list all medications in a table
- “/searchmed”  **experimental**  using the api above to have the diagnose by the medications
