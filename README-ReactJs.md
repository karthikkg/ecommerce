# Elikart 
#### An MVP formulated ReactJS app developed using Hasura BAAS powered with Python-Flask Backend.
##### Developed as a part of HPDF Internship offered by Hasura ( Team No. T43)
> The documentation is prepared in the view of *Hasura Hub Submission*

This is an **eCommerce** base like our _Flipkart_ and _Amazon_ .
Here the aim of the app is ~~fully featured~~ to have minimum and mandatory features of a regular *eCommerce* app Where the user can visit ,click on a product and buy 
> This is a T43PF submission
### Contents 
* [Developers](#developers)
* [Work Shared](#work-shared)
* [Sample Screenshots](#samples)

## Developers
> Frontend

    * Nanda Kishor Jeripothula  (j.kishor.bd@gmail.com)
    * Anusha Kalbande           (anushakalbande17@gmail.com)
    * Willson V                 (vermawillson@gmail.com)
> Backend (Python-Flask)
    
    * Gajula Karthik Kumar       (karthikg.myb@gmail.com)

## Work Done

### Frontend
> Nanda Kishor Jeripothula

* Login and Sign up handling for user
* Landing Page ( Slider + Products loading )
* Product Page **[Fully working]**
_Responsive Content_
> Anusha Kalbande 

* _[Assigned Part]_ **[Not yet finished]** Sellers Page

> Willson V

* _[Assingned Part]_ **[Not yet finished]** Cart Handling
*  **[Partially finished]** Product Page

### Backend
> Gajula Karthik Kumar 

 *   Entire APIs Developed 

 ## Sample Screenshots
 
[fullHome]:https://github.com/NandaKishorJeripothula/Elikart/blob/master/FullModeHome.png
[mobileHome]:[fullhome]:https://github.com/NandaKishorJeripothula/Elikart/blob/master/FullModeHome.png
[tabHome]:https://github.com/NandaKishorJeripothula/Elikart/blob/master/TabModeHome.png
[fullLogin]:https://github.com/NandaKishorJeripothula/Elikart/blob/master/Login.png
[mobileLogin]:https://github.com/NandaKishorJeripothula/Elikart/blob/master/LoginMobile.png
[productsHome]:https://github.com/NandaKishorJeripothula/Elikart/blob/master/ProductsHome.png
[productMobile]:https://github.com/NandaKishorJeripothula/Elikart/blob/master/ProductMobile.png
[productFull]:https://github.com/NandaKishorJeripothula/Elikart/blob/master/ProductFull.png
![Desktop Home][fullHome]
![MobileMode Home][mobileHome]
![Tab Home][tabHome]
![Desktop Login][fullLogin]
![Mobile Home][mobileLogin]
![Product Home][productsHome]
![Desktop view Products][productFull]
![Mobile view Products][productMobile]



## Backend APIs

-   Login/Sign up APIs
  > https://app.banner20.hasura-app.io/login
  
  > https://app.banner20.hasura-app.io/signup
  
  > https://app.banner20.hasura-app.io/seller_signup
 -  API to List products being sold and filter by category 
  > https://app.banner20.hasura-app.io/displaybycategory?category_id=2
 -   API to List products being sold and filter by sub category  
       > https://app.banner20.hasura-app.io/displaybysubcategory?sub_category_id=1
  
 -    API to List products by id 
      > https://app.banner20.hasura-app.io/product?product_id=10

-   API to List products by search using keywords in category, sub category, product name and description
      > https://app.banner20.hasura-app.io/search

-   API to add products by seller
      > https://app.banner20.hasura-app.io/add_product 

-   API to add multiple products to their shopping cart
     > https://app.banner20.hasura-app.io/add_to_cart

- API to place an order
     > https://app.banner20.hasura-app.io/place_order
