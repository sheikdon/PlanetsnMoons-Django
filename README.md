# PlanetsnMoons-Django API
An application for creating and viewing information about the solar systems planets and biggest moons!

# Routes

## /planets

| URL                  | HTTP Verb | Action                                   |
|----------------------|-----------|------------------------------------------|
| /planets          | GET       | index all planets                           |
| /planets/:id      | GET       | show character details                      |
| /planets/:id      | PATCH     | update character details                    |
| /planets/:id      | DELETE    | delete character                            |
| /planets          | POST      | create a new character                      |


## /moons

| URL                  | HTTP Verb | Action                                   |
|----------------------|-----------|------------------------------------------|
| /moons             | GET       | index all moonss                           |
| /moons             | POST      | create moonss                              |
| /moons/:id         | GET       | show character details                     |
| /moons/:id         | PATCH     | update character details                   |
| /moons/:id         | DELETE    | delete character                           |


