# Blog API

This is an api for the personel blog built with the Django REST Framework.

## Schema

**Post**

* user_: ForeinKey
* title: required
* content: nullable
* draft: def = True
* slug: required
* created_at
* updated_at
* image


**Favourite**

* user : ForeignKey
* post : ForeignKey
* content 


**Comment**

* User : ForeignKey
* post : ForeignKey
* content
* parent : ForeignKey to 'self' (replies to the comments)
* created_at

**Profile**

(autocreate user profile when new user created)
* user : OneToOneField
* note : nullable
* twitter : nullable


## API

**/post**

* GET
* POST

**/post/:slug**

* GET
* PATCH
* DELETE

**/favourite/fav**

* GET
* POST

**/favourite/fav/:id**

* GET
* PATCH
* DELETE

**/comment/create**

* POST

**/comment/list**

* GET

**/comment/list/:id**

* GET
* PATCH
* DELETE


**/account/me**

* GET
* PATCH

**/account/change-pw**

* PATCH

**/account/register**

* POST
