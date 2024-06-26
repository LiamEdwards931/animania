# Animania

## Animania Anime merchandise

Animania is an e-commerce merchandise store, the core behind animania is that it offers anime merchandise all in one place for anime lovers to buy. I decided to go for this particular genre as I know several anime fans, myself included and the market for being able to purchase and browse a selection of merchandise from different anime is quite scarce and difficult to find.

Even though this site is fictional and the products shown in this site are not available I do believe that there is a potential in the market for a store like this one, that could have little competition when browsing and purchasing goods for anime.

This project was created for the portfolio project 5 - with code institute

## Live deployment 

This project is deployed on Heroku 
the link for which is here: [live deployment](https://animania-175b65d61606.herokuapp.com/)

## Contents
- [Project outline](#project-outline)
    - [Purpose](#purpose)
    - [User goals](#user-goals)
    - [Site manager goals](#site-manager-goals)
    - [Business model](#business-model)
        - [Marketing strategies](#marketing-strategies)
        - [SEO](#search-engine-optimisation)
- [Agile method](#agile-method-for-project-management)
- [Database Models](#database-models)
    - [Models](#models)
    - [Relationships](#relationships)
- [UX](#ux-user-experience)
    - [Wireframes](#wireframes)
    - [User Stories](#user-stories)
    - [Site Perspective](#site-perspectives)
    - [Design choices](#design-choices)
- [Features](#features)
    - [Home](#homepage)
    - [Profile](#profile)
    - [Amend Products](#amend-products)
    - [All products](#all-products)
    - [Product-detail](#product-detail)
    - [basket](#checkout-basket)
    - [checkout](#checkout-features)
    - [Checkout success](#checkout-success)
    - [News](#news-features)
    - [News detail](#news-detail-page)
    - [Forms](#forms)
- [Future features](#future-features)
- [Technology used](#technology-used)
- [Testing](#testing)
    - [User story testing](#user-story-testing)
    - [Manual testing](#manual-testing)
    - [Lighthouse testing](#lighthouse-score)
    - [Automated testing](#automated-testing)
    - [Responsive testing](#responsive-testing)
    - [code validation](#code-validation)
- [Bugs](#bugs)
- [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Cloning a repository](#cloning-a-repository)
- [Credits](#credits)
- [Achknowledgments](#achknowledgements)


## Project outline 

### Purpose
The purpose of this website is to get users and site owners excited about buying or selling anime merchandise, using colourful visuals and an intuitive layout, I have tried to design this site as seamlessly as I can using html, css, javascript, python and the django framework.

### User goals 
The goals for a user are simple, easy navigation to products for quick impulse or well thought out purchases, they should be able to navigate to whichever product they wish to buy and easily be able to purchase it!

### Site manager goals
Full control over quantity, price, costprice, product statuses such as new or discounted products, which banners to display on the front page for promotional pushing. Ability to track the turnover and profit returned from the online store via the profile.
To give users a feeling of satisfaction when shopping the site so that repeat custom is almost guaranteed.

### Business Model 
 - The core of animania is a B2C (business to consumer), we want to invoke an emotional response with the user that really gives them that feeling of a good shopping experience, in turn driving repeat visitation and marketing by word of mouth.
 The core point of animania is to sell anime related goods to an end-point user giving transparancy of costs along the way, and relevant guidance in purchasing where necessary, We consider the impulse purchases and the considered purchases and implement a style that hopefully has something for everyone.

#### Marketing Strategies
 - Competetion tracking is essential when it comes to merchandise and the only main competitor I could find on the market was Atsuko, that offered a similar style of merchandising the way Animania would.
 - Trending series is essential when deciding on products to sell with animania and market research to keep up to date with new series and new season releases should be shown in the news page for users to get to grasps with upcoming and trending animes
 - The page highlights sale products and also emphasises what products are new to the store potentially driving an impulse purchase with the customer
 - Changes to products can be amended swiftly, changes to banners can be adjusted swiftly giving the user a more dynamic approach and hopefully they see something new when they do decide to revisit the store.
 - Customer engagement and feedback is also imperative when it comes to marketing and a new user is much more likely to purchase from the site if the level of positive feedback is high, this is shown in the all products page as an average review score, and all reviews are displayed within the product detail page to let customers persuade other customers about the quality.
 - Animania is responsive on all devices allowing users to be able to shop on a multitude of devices. according to google 
 'Nearly three-quarters of British shoppers prefer mobile devices when making online purchases, with 48% of them using their phones for purchases at least once a week.' - dontdisappoint
 - Social media presence is a huge factor in todays success of a business, sometimes though it is difficult to filter through the authenticity of a business. Animania uses a facebook page as a source of marketing
 ![animania-facebook-page](readmeimages/facebookpage.png)
 
#### Search engine optimisation
SEO (search engine optimisation) is Important for authenticity of a website, important for ranking in a search engines search queries, the higher you score the more likely it is that your site is going to be shopped and viewed by customers. 

Animania SEO implementation:
- Meta description: "Discover a wide range of anime merchandise including apparel, figures, accessories, and more at our online store. Shop now for the latest anime products!
- Meta keywords: 
I used [Wordstream](https://tools.wordstream.com/fkt?website=animania&cid=&camplink=&campname=&geoflow=1) to check my keywords against competition, the link only includes the result for the animania keyword.
"animania, anime merchandise, anime store, anime apparel, anime figures, anime accessories, anime merch, pop-vinyl, clothing, sale-items"
- Inclusions
    - Inclusion of a robots.txt file: As I am aware this only improves performance based on the site being a custom domain that needs card details.
    - Inclusion of a sitemap.xml file.
- Suitable rel tags for external links: the tags used in this project are noopeners as they do not have direct content linked to animania, they are standalone webpages that do not need to be crawled to learn about the animania site. 
- Lighthouse SEO score
![SEO_score](readmeimages/animaniaSEOscore.png)

[Back to top](#animania)

## Agile method for project management

- I used github issues, milestones and the project board to implement a MosCow approach to the development of Animania
The issues outline the general criteria I need to fulfill and within the milestones I have the explored deeper into what may be expected from each feature and the acceptance criteria needed to pass the project through to it's next phase. 
[Animania Project Board](https://github.com/users/LiamEdwards931/projects/6/views/1)

[Back to top](#animania)

## Database Models

### Models
There are multiple models with the animania project:
- Product app
    - Product - This model handles creating the details for the product
        | Model property        | Property value       |
        |-----------------------|----------------------|
        | image                 | CloudinaryField      |
        | alternative_images    | CloudinaryField      |
        | name                  | TextField            |
        | description           | TextField            |
        | series                | TextField            |
        | price                 | DecimalField         |
        | category              | CharField            |
        | sub_category          | CharField            |
        | cost_price            | DecimalField         |
        | search_tags           | CharField            |
        | related_products      | ManyToManyField      |
        | quantity_available    | PositiveIntegerField |
        | new                   | BooleanField         |
        | discounted            | BooleanField         |
        | discount_amount       | PositiveIntegerField |
        | created_on            | DateField            |
        | updated_on            | DateField            |
        
        The product model has properites also such as:
        - Discounted price
            - Gets the discount amount and turns it into a percentage e.g value 10 = 10%, then that value gets worked out from the product price and subtracted to get the discount with the correct % value.
        - Profit margin 
            - Gets worked out by subtracting the cost price from the sale price in a variable called margin, the margin is then divided by the cost price and multiplied by 100 to work out the profit margin % of a product.
        - Profit amount
            - Works in a similar way to the profit margin except it's price - cost price / cost price

    - Size - This model handles adding quantites to individual sizes as opposed to having one generic quantity that covers all of the sizes. 
        | Model property         | Property value       |
        |------------------------|----------------------|
        | product                | ForeignKey("Product")|
        | alternate_size         | CharField            |
        | Size_quantity_available|PositiveIntegerField |
    
    - Banners - This model handles creating new banners for the home screen
        | Model property        | Property value       |
        |-----------------------|----------------------|
        | image                 | CloudinaryField      |
        | Series                | Textfield            |
        - The banner is a standalone model, I did add validation check in the form to upload this to check if a product series exists before uploading the image which returns validation errors if the product series does not exist.

    - Product Review - This model handles the reviews submitted to products. 
        | Model property   | Property value         |
        |------------------|------------------------|
        | title            | CharField              |
        | product          | ForeignKey("Product")  |
        | rating           | PositiveIntegerField   |
        | content          | CharField              |
        | created_by       | ForeignKey(User)       |
        | created_on       | DateField              |
        | updated_on       | DateField              |
        - As you can see the review model has a foreign key to both the User and The product, this allows review association with products and users.

    - Wishlist - This model handles wishlisted products.
        | Model property   | Property value         |
        |------------------|------------------------|
        | product          | ForeignKey("Product")  |
        | created_by       | ForeignKey(User)       |
            - The wishlist has 2 properties user and product, it's a simple model that allows users to keep track of items that they wish to purchase in the future. 

- Accounts app
    - Address 
    | Model property | Property value        |
    |----------------|-----------------------|
    | user           | ForeignKey User       |
    | door_number    | IntegerField          |
    | street         | CharField             |
    | city           | CharField             |
    | state          | CharField             |
    | country        | CharField             |
    | postal_code    | CharField             |
        - The accounts app has a singular model not inclusive of the User, extra fields are submitted to user data in the form to create a new user such as email address and first and last names.

- Checkout app
    - Order: this model handles all of the orders processed through animania.
        | Model property | Property value                                 |
        |----------------|------------------------------------------------|
        | order_number   | CharField                                      |
        | first_name     | CharField                                      |
        | last_name      | CharField                                      |
        | email          | EmailField                                     |
        | door_number    | IntegerField                                   |
        | street         | CharField                                      |
        | city           | CharField                                      |
        | county         | CharField                                      |
        | country        | CharField                                      |
        | postal_code    | CharField                                      |
        | date           | DateField                                      |
        | delivery_cost  | DecimalField                                   |
        | total_cost     | DecimalField                                   |
        | grand_total    | DecimalField                                   |
        - This model has associated properites such as generating an order number and calculating total costs.

    - Order-line - this creates product lines for each order, for order tracking and item tracking.
        | Model Property | Property Value                        |
        |----------------|---------------------------------------|
        | order          | ForeignKey to Order model             |
        | product        | ForeignKey to Product model           |
        | quantity       | IntegerField                          |
        | product_size   | ForeignKey to Size model (nullable)   |
        | subtotal       | DecimalField                          |
        - Has a calculated subtototal within the save method of this model.

- News app
    - News this model handles news article creation
    | Model Property      | Property Value          |
    |---------------------|-------------------------|
    | title               | CharField               |
    | news_image          | CloudinaryField         |
    | short_description   | CharField               |
    | description         | CharField               |
    | video_url           | URLField                |
    | author              | ForeignKey to User      |
    | date                | DateField               |
    
### Relationships
The image below outlines the relationships of the models

![Model-relationships](readmeimages/Model-relationships.png)

[Back to top](#animania)

## UX (User experience)
This section shows the design progress and choices for animania, it outlines the user stories

### Wireframes

- Home page 

![homepage](readmeimages/Wireframe1Homepage.png)

- All products

![All Products](readmeimages/Wireframe2allProducts.png)

- Product Detail

![All products](readmeimages/wireframe3productdetail.png)

- Basket

![Basket](readmeimages/wireframe4basket.png)

- Checkout

![Checkout](readmeimages/wireframe5checkout.png)

- Checkout success

![Checkout Success](readmeimages/wireframe6checkoutsuccess.png)

- Profile

![Profile](readmeimages/wireframe7profile.png)

- Amend Products

![Amend products](readmeimages/wireframe8amendproducts.png)

### User stories

#### Home page 
|User Type| User story|Completed|
|--------|-----------|----------|
|User| As a user I expect a Nav bar shows links to the relevant pages such as products and accounts|[x]|
|User| As a user I expect to see a clear indication through images of what the page is about|[x]|
|User| As a user I expect to see products that could inspire me to buy|[x]|
|User| As a user I expect to see a link to take me to other sources that could be related to Animania e.g. a facebookpage|[x]|
|User| As a user I expect to see a useful footer that gives me information and important links|[x]|
|Superuser & User| As a sitemanager/User I expect to see a promotional message to encourage purchase such as a promotion on delivery|[x]|

#### Accounts/Profile
|User Type| User story|Completed|
|--------|-----------|----------|
|User| As a user I expect to be able to log in to the site|[x]|
|User| As a user I expect to be able to log out of the site|[x]|
|User| As a user if i don't have an account I expect to be able to create an account|[x]|
|User| As a user I expect to be able to change my password for security|[x]|
|User| As a user I expect to be able to add some address details that are saved to my profile|[x]|
|User| As a user I expect to be able to update and remove my address details|[x]|
|User| As a user I expect to be able to see my personal details|[x]|
|User and Superuser| As a site manager/User I expect to be able to read a list of all the reviews I have posted|[x]|
|User and Superuser| As a site manager/User I expect to be able to update any of the reviews I have posted|[x]|
|User and Superuser| As a site manager/User I expect to be able to delete any of the reviews I have posted|[x]|
|Superuser| As a Site manager I expect to be able to add new products|[x]|
|Superuser| As a Site manager I expect to be able to make adjustments to products|[x]|
|Superuser| As a Site manager I expect to be delete products|[x]|
|Superuser| As a Site manager I expect to be able to create new home page banners|[x]|
|Superuser| As a Site manager I expect to be able to update home page banners|[x]|
|Superuser| As a Site manager I expect to be able to remove home page banners |[x]|
|Superuser| As a Site manager I expect to be able to track the total performance of the site|[x]|

#### Products
|User Type| User story|Completed|
|--------|-----------|----------|
|User| As a user I expect to be able to browse a all the products available on the site|[x]|
|User| As a user I expect to be able to filter the products to narrow down the product I want|[x]|
|User| As a user I expect to be able to search for a product that I want |[x]|
|User| As a user I expect to be able to see a number of search results |[x]|
|User| As a user I expect to be able to see relevant details of the product|[x]|
|User| As a user I expect to be able to add a product to my wishlist|[x]|
|User| As a user I expect to be able to find out more details about a product |[x]|
|User| As a user I expect to be able to quickly see if it's on sale or if it's new |[x]|
|User| As a user I expect to be able to quickly see a review score for the product|[x]|
|User| As a user I expect to be able to be able to navigate the products without excessive page length (pagination) |[x]|
|User| As a user I expect to be able to choose a quantity of product I want and add it to my basket|[x]|
|User| As a user I expect to be able to add a specific size of clothing to my basket |[x]|
|SuperUser| As a site manager I expect to be able to see live changes as I update products e.g. price/sale/new/quantities|[x]|

#### Basket
|User Type| User story|Completed|
|--------|-----------|----------|
|User| As a user I expect to be able to be able to view the contents of my basket|[x]|
|User| As a user I expect to be able to adjust the quantity of items within my basket|[x]|
|User| As a user I expect to be able to remove items from my basket|[x]|
|User| As a user I expect to be able to see a checkout amount before I proceed to the checkout |[x]|
|User| As a user I expect to be able to see a breakdown of my costs before proceeding to the checkout |[x]|
|User| As a user I expect to be able to have a quick way to rebrowse products in case I want to add more |[x]|


#### Checkout
|User Type| User story|Completed|
|--------|-----------|----------|
|User| As a user I expect to be able to see the contents of my basket again before I proceed forward for confirmation|[x]|
|User| As a user I expect to be able to fill out an easy to fill form that requires my personal details for delivery |[x]|
|User| As a user I expect to be able to see this form prepopulated with my details I filled out previously |[x]|
|User| As a guest user I expect to be able to still be able to complete checkouts.|[x]|
|User| As a user I expect to be able to complete a payment option|[x]|
|User| As a user I expect to be able to see a confirmation of my order once I have purchased it|[x]|
|User| As a user I expect to be able to see an invoice of the items I have purchased, the costs and the delivery address |[x]|

#### News
|User Type| User story|Completed|
|--------|-----------|----------|
|User| As a user I expect to be able to see up to date relevant news about the site or associated topics. |[x]|
|User| As a logged in user I expect to be able to see more details about an article. |[x]|
|SuperUser| As a Site manager I expect to be able to add new articles to the page |[x]|

#### Site perspectives 
A user logged in, a user not logged in and a superuser have different experiences in animania.

- Logged out differences to logged in users
Guest users(non logged in) these users do not have access to wishlists, they do not have access to browse news articles and forms in the checkout are not prepopulated with details. The profile button in the navbar points to a log in page rather than a profile page and the footer has the same effect indirectily meaning that address details for non logged in users cannot be accessed or added.
A non logged in user cannot submit a product a review. 
The reverse is all true for the logged in user and they have access to all of the mentioned features

- Superusers 
Superusers have access to everything on the site, the main difference lies within the profile a superuser has no need to add an address so in it's stead the product management buttons exist, where a superuser can add products and banners and perform CRUD operations on them and also can see the sales data for the performance of the website.

#### Design choices

- Typography
    - Headers in animania are in custom google font: "Luckiest Guy" with a backup of "cursive"; 
    - All other text is standard sans-serif;

- Colour scheme
    - The colours chosen were intential to provoke a nostalgia like feeling when shopping animania in matching colours up with the massive platform for anime crunchyroll; 
    - I didn't want to overbear the user with colour and only really used it where I felt it would be effective colours
        - Orange
            ![color-image](readmeimages/colorimage.png)

        - Black
            ![black-image](readmeimages/black-color-image.png)

        - White
            ![White-image](readmeimages/color-image-white.png)

    - Some of the headers are complemented with a text-shadow just make them have more of a cartoon characteristic. 

### Features
#### Homepage
- Navbar
    The navbar is fixed to the top of the screen and responsive on mobile devices, it contains links to the relevant sections that users need to make purchases. category and series links are automatically generated when a product with a new series or category are created.
    
    Large screen
    ![Navbar](readmeimages/feature-images/Home/navbar.png)

    Small screens.
    ![Navbar](readmeimages/feature-images/Home/responsivenavbar1.png)

    ![Navbar](readmeimages/feature-images/Home/responsivenavbar2.png)

- Main banner image 
    The main banner displays the image of a series as long as a product of that series exists for it, it also generates a button that takes the user to browse products by that specific series.

    ![Main image](readmeimages/feature-images/Home/mainimage.png)

- Delivery banner
    A banner appears on loading the page that displays a threshold a user needs to spend to be entitled to free delivery.
    the banner can be closed off if the user wishes to do so.

    ![Delivery banner](readmeimages/feature-images/Home/delivery-pop-up.png)

- Category sections 
    There is a section on the home page for categories that allow users to filter the products by the 3 main categories that exist for animanaia. 

    ![Category](readmeimages/feature-images/Home/home-category.png)

- New section 
    There is a section that displays 4 new products, this was designed intentionally so that the products didn't clutter the home page and allows user to access the details of the appended products or they can shop all sale items with the top link

    ![New section](readmeimages/feature-images/Home/home-new.png)

- Sale section 
    There is a section that displays 4 sale products, works the same as news and allows user to access the details of the appended products or they can shop all sale items with the top link

    ![Sale section](readmeimages/feature-images/Home/home-sale.png)

- Facebook banner 
    There is a banner suggesting users to follow the site on facebook the icon is a link that will take the user to the animania facebook page

    ![facebook](readmeimages/feature-images/Home/social-media-banner.png)

- Footer 
    The footer is positioned at the bottom of the screen, it has a section about animania, it has useful links for site navigation and it has links for series that generate the same way they do in the navbar 

    ![Footer](readmeimages/feature-images/Home/footer.png)

#### Profile

- User view
    The users on coming to the profile page have a selection of options:
    - logout - redirects to the home page with a message 
    - change password - redirects to a form to change password
    - address - brings up a modal that shows all of the address details and the option to add a new address
    if an address exists there are options for a user to update or delete them too. 
    - my reviews - redirects to a page that displays all of the logged in users reviews and allows users to update or delete them.
    - Breadcrumb links to allow backtracking of urls so users know their path back.
    
    ![User-profile](readmeimages/feature-images/Profile/userprofile.png)

- Superuser view
    - Similar page layout to the User except
     - address becomes product overview 
     - product overview button redirects to the amend products page where superusers can add update and delete products.
     - banner overview button redirects to banner page where superuses can add update and delete banners. 
     - sales data - opens a modal that shows total turnover, total profit and amount of orders processed.

     ![Superuser Profile](readmeimages/feature-images/Profile/superuserprofile.png)

#### Amend products
Super users can navigate to the amend products page from the profile this is the hub for all product creation, updating and deletion.
- The amend product features:
    - search bar to navigate to specific products in the amend products table 
    - Filter options to pinpoint items, a-z, z-a, price, category, series - the filter box appears as a modal 
    - Displays all of the products in a table, updates along with the products 
    - buttons to update and delete products 
    - button to display all product details in a modal for an easier overview
    - button to add size quantities for products that are clothing.
    - paginated pages. 
    - This page IS NOT designed for mobile due to the size of the columns.

    ![Amend products page](readmeimages/feature-images/Amend_products/amendproducts.png)

#### All products
- The all products features:
    - it has a search bar that allows user to search for the products that they wish to purchase
    - it has a filter button that pops up a modal and allows users to filter through different options such as a-z, z-a, price, series, category
    - Returns a number of search results
    - displays all products displayed on the animania page.
    - Shows the page number you are on for the products.

    Page for all products
    ![all products main page](readmeimages/feature-images/All_products/allproducts1.png)

    Each product container
    ![Products in all products](readmeimages/feature-images/All_products/allproducts2.png)

    Pagination display
    ![pagination](readmeimages/feature-images/All_products/pagination.png)

#### Product detail
- Product detail features:
    - main image displaying the product
    - details about the product such as if its new or on sale, price, series and name also gives the user the quantity available.
    - If product is clothing has 3 different values of quantity for the sizes and also has a size selector box. 
    - a quantity to add the product to the basket 
    - won't let users add more than the available amount to the basket.

    ![product-details](readmeimages/feature-images/Product_detail/productdetailpage.png)

#### Checkout Basket
- Basket features:
    - products that have been added to the basket will all be displayed here 
    - the quantities selected from the product detail will mirror what has been selected
    - the size will also display if a clothing item is being purchased
    - calculates a subtotal for each product in the basket based on quantity and price status e.g discounted or not
    - calculates a delivery total if it's below the threshold and tells users how much more they need to spend 
    - calculates a grand total which is the product subtotals combined + delivery

    ![basket](readmeimages/feature-images/Basket/Basket.png)

#### Checkout features
- The features in the checkout are:
    - A summary of all the products that are being processed in the checkout app 
    - a form for a user to fill out with name, email, delivery details 
    - a stripe payment form
    - Multiple messages displaying how much the card is going to be charged
    - Messages if form for details or card isn't filled out correctly 
    - Return to basket button to allow users to change their minds.

    ![checkout](readmeimages/feature-images/Checkout/checkoutpage.png)

#### Checkout success
- The features of the checkout success page are:
    - A success message on successful transaction 
    - A summary of the order including order number, subtotals, delivery and grand total
    - A summary of the delivery address filled in by the user
    - A breakdown of all of the products that have been purchased by the user.
    - After a successful checkout the quantites purchased are removed and recalculated in the quantities available for the product, e.g. if I had 8 x small clothing, if i buy one in small the quantity would update to 7, this allows easier inventory tracking for a site manager. 

    ![Checkout success](readmeimages/feature-images/Checkout%20success/checkoutsuccess.png)

#### News features
- The features of the news page are:
    - Superusers have the option to upload a new article from the top of the page 
    - Normal users can look through and see the available articles and choose to see more of them if they choose too
    - Non-logged in users see a message suggesting to the user to either log in or signup so they can browse the content.

    Logged in as superuser:
    ![News logged in](readmeimages/feature-images/news/newspage.png)

    Not logged in:
    ![Not logged in news page](readmeimages/feature-images/news/nonloggedinnews.png)

    I have added the addition of a news signup page, accessible from the profile page and from the news page when you are not logged in. 
    ![news signup](readmeimages/newssignup.png)

#### News detail page
- The features of the news detail page are:
    - An image is displayed the same as the news page except larger
    - Content for the article is displayed on the right hand side
    - The url link requested in the form has a link that takes you to the video uploaded. 
    - Each news article has a link to crunchyroll to allow users to browse more animes and hopefully increase visitation.

#### Forms
- All forms with the exception of the checkout form follow the following style:

    ![form](readmeimages/feature-images/form.png)

    - Forms have validation messages if form data is missing or the screen automatically focuses on the content that is missing suggesting to the user it needs filling in.

#### how the available quantities work
I decided to use multiple variables for availble quantity and quantity_size I did this as I wanted to streamline what was shown to the user and not have to create multiple instances of the same product for the different sizes, to be able to track the quantity available of each size of a clothing article, the only way I could think to do this was to track the
quantities in a seperate model so I only have the one instance of the clothing item but multiple instances of the size e.g. S,M,L each with their own individual inventory.

### Future features
In the future some more features that could be included in the animania project are:
- Delivery times and live tracking
- Advertisements through social media, partners (youtube)
- Order confirmation (email, on profile)
- Routing addresses for quick transport
- Calculation of shipping costs from the business end
- More in depth sales tracking 
- Automated quantity updates based on resupply 
- Gift cards
- Coupons

[Back to top](#animania)

### Technology used
- The main technology used in this project are:
    - Code editor
        - Code editor - [VS Code](https://code.visualstudio.com/Download)
    - Languages
        - Html
        - CSS
        - Javascript
        - Python
    - Hosting sites
        - [Github](https://github.com/) - Holds the repository for the site
        - [Heroku](https://www.heroku.com/) - Hosts the finished site
        - [Cloudinary](https://cloudinary.com/) - Stores the media files
        - [elephant SQL](https://www.elephantsql.com/) - stores the database models
    - Design sites
        - [Balsamiq](https://balsamiq.com/) - Used to design the site via wireframes
        - [Markdown live preview ](https://markdownlivepreview.com/)- Keep my README file consistent
        - [LucidChart](https://lucid.co/) - Created the model relationship diagram
    - Google chrome dev tools
        - Built in responsive tester 
        - Lighthouse - SEO testing
        - Applications - Clear the session data for basket testing
        - Console - Check for logs reported from Javascript/Python
        - Network - Used in debugging 500 errors on the live site.
- VS code extensions used in this project are:
    - Python debugger 
    - Pylance
    - GitHub Codepaces
    - Git history
    - Dev containers
    - Github Copilot
    - Close HTML/XML tag
    - Github actions
    - Github Pull Requests
    - Github repositories
    - Gitignore
    - Remote Repositories
- Libraries used in this project are:
    - [Bootstrap](https://getbootstrap.com/)
    - Django(https://www.djangoproject.com/) 
    - [cloudinary]((https://cloudinary.com/))
    - dj3-cloudinary-storage
    - [Stripe](https://stripe.com/gb)
    - psycopg2
    - gunicorn
    - dj-database-url
    
[Back to top](#animania)

## Testing
 Testing performed is performed by myself, I did get my partner with no context to navigate through the site as a normal user to test the intuitiveness and she found a couple of the bugs I have fixed in the [fixed bugs](#bugs) section. 

### User story testing
User story testing performed for animania is all documented below:
[User story testing](USER_STORY_TESTING.md)

### Manual testing
The manual features testing performed for animania is all documented below:
[Animania-testing](TESTING.md)

### Lighthouse score

![Lighthouse score](readmeimages/lighthouseindex.png)

- Performance
    Negative performance drivers:
    - Google chrome extensions negatively impact performance
    - Images are jpeg and not webp
    - Image sizing was a little off.
    - Cloudinary has a large network payload
- Accessibility
    Negative accesability 
    - Button-id name has name of shop-btn.
    - wishlist links generated in for loop have ids.
- Best practives
    Negative practices
    - Uses 3rd party cookies from stripe + cloudinary
    - Console shows issues (cookies from cloudinary)
- SEO 
    Perfect score of 100 no problems at all.

### Automated testing
No automated testing has been done for the Animania project.

### Responsive testing
All responsive testing has been performed in the developer tools using microsoft edge and also google chrome.
- Responsive on laptops 1550px - 1024px, consistent for each page within the site for condensed purposes images will represent the home page 
    - Links all render, images render, content is visible 

    ![Home-page-laptop-responsive](readmeimages/laptop-responsive.png)

- Responsive on ipads 1024px - 890px
    - Responsive works fine as intended, with all links images and text rendering correctly

    ![Ipad responsive](readmeimages/ipad-responsive.png)

- 890px - 573px 
    Microsoft edge bug:
    The strange thing with this bug is that in the dev tools it works perfectly and responds the way it should behave when clicking through different device types but not consistently, and sometimes in dev tools it gives me the blank side as mentioned below, so i'm finding it very difficult to confirm if the error lies within the dev tools responsiveness or within the application itself. 
    
    - A bug appears where a white column appears down the side of the html page pushing the navbar to exceed the width of the html page, the content, links and images all still render correctly and work as intended.
    - On deleting the elements in the dev tools and putting them back in, the issue goes away but comes back again when reloading the page. 
    - There is no apparent reason for the navbar to respond in this way as the elements in the document all stay within the width of the body and html and none of them push the navbar out. 
    - No margin or padding exists on the navbar causing it to exceed the width.

    - Google chrome testing for this size works as expected as is causing no issues at all.

- 573px - 320px 
    - All responsiveness works for mobile devices, all links render correctly, all images scale, content can be viewed. 

    ![Mobile responsive](readmeimages/mobile-responsive.png)


### Code validation
Tested the code validation through various different linters: 
- HTML
    - [W3C Validator](https://validator.w3.org/nu/?showsource=yes&useragent=Validator.nu%2FLV+https%3A%2F%2Fvalidator.w3.org%2Fservices&acceptlanguage=&doc=https%3A%2F%2Fanimania-175b65d61606.herokuapp.com%2F)

    - Returned a couple of bad value errors from URLS dynamically generated by django for having spaces in between them 

    ![html validation](readmeimages/Htmlvalidation.png)

    each html file individually passed through the validation, only errors returning are those due to django syntax and have returned as parse errors.

- CSS
    - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/validator)
    
    - Returned 17 errors all connected to bootstrap
    - On passing my CSS files through individually the CSS passed

    - Style.css
        ![Style.css](readmeimages/styleCSSvalidation.png)

    - News.css
        ![News.css](readmeimages/newsCSSvalidation.png)

- Javscript
    - [JS hint](https://jshint.com/)

    - Index.js 
        - There are 5 functions in this file.
        - One warning: 56 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
        - One unused variable 55 removeDelivery - Used as an OnClick
    - Messages.js
        - There is only one function in this file
        - Two warnings 
            - 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
            - 'arrow function syntax (=>)' is only available in ES6 (use 'esversion: 6').
    - Product.js
        - There are 11 functions in this file.
        - No warnings returned.
    - Qty-button.js
        - There are 5 functions in this file.
        - 11 warnings all related to the 'const' and 'arrow function syntax'
    - Script.js
        - There are 8 functions in this file.
        - Three warnings about 'let' being available in ES6
    - stripe_elements.js
        - There are 3 functions in this file.
        - Two warnings of 'template literal syntax' is only available in ES6 (use 'esversion: 6').

- Python
    - [ Code insititute python linter](https://pep8ci.herokuapp.com/#)
    - Product app
        - Models.py - No errors reported
        - Views.py - No errors reported
        - Urls.py - No errors reported
        - Admin.py - No errors reported
        - Forms.py - No errors reported
    - Accounts app
        - Models.py - No errors reported
        - Views.py - No errors reported
        - Urls.py- No errors reported
        - Admin.py - No errors reported
        - Forms.py - No errors reported
    - Basket app
        - Models.py - No models
        - Views.py - No errors reported
        - Urls.py - No errors reported
        - Admin.py - No admin
    - Checkout App
        - Models.py - No errors reported
        - Signals.py - No errors reported
        - Urls.py - No errors reported
        - Views.py - 1 error returned as a for loop exceeded line length.
        - forms.py - No errors returned
        - Admin.py - No errors returned
    - News App
        - Models.py - No errors reported
        - Views.py - No errors reported
        - Urls.py - No errors reported
        - forms.py - No errors reported

     re ran each of the animania apps through validation and encountered a few errors in settings.py and some in the checkout app, all files are now responding as clear of errors throughout the entire python files.

[Back to top](#animania)

## Bugs 
- Unfixed bugs
    - Microsoft edge: There is a bug that on some ipad mini screen sizes the navbar exceeds the length of the html page, I have looked into margin/padding on navbar and the entire page and I cannot figure the cause of the issue as within the code there should be no reason the navbar performs like this only for that screen size, the responsiveness works on all other screens. This isn't a consistent problem and it does not happen in google chrome dev tools suggesting the issue is lying in the dev tools and not within my code.

- Fixed bugs 
    - Issue rendering the dynamic links in the navbar when a filter was in, this was due to a conflict in variable names in the context processor for the site and the variable in the view for the all products page.
    
    - Issue with button on the banner image on index.html not submitting a filter query when pressed, button was not inside a form and therefore had nowehere to navigate too.

    - Footer wasn't generating the extra text when clicking the 'readmore...' drilled into it further with the script and adjusted the code to remove syntax errors. 

    - Amend products table wasn't showing the boolean results of if a product was 'new', fixed by amending the if statement i had used to get the correct results.

    - Couldn't upload a banner for attack on titan this was due to two seperate values of Attack on Titan being available in series choices representing two different values

    - Sizes were being delete when updating quantities in the shopping bag, fixed by adding a name to the size hidden input form in basket.html

    - search bar was disappearing from base.html on click, made the search function only available in all products as it seemed more logical for it to live in there

    - 404 returned when non-users tried to submit a review, fixed by using an if statement to only display leaving a review if you are logged in. 

    - 404 on submitting a new product, fixed by assigning making sure the order number after generation was being passed back into itself. 

    - Calculations for delivery were not being recognised, had some wrong variable names in the model that were causing the issue of not calculating properly.

    - Bug where the size was not being processed in the checkout, changed the way that size was being fetched in the context processor and made sure that the size was correctly matching the values specified in the Size model.

    - Used a wrong variable in the model that was causing the order total, grand total and delivery not to to update in the admin for new orders. 

    - bug where only the first product was allowed to have a size, amended the view for new products and removed the init method of the form to make sure that it now works correctly, added extra validation in the view to prevent mulitple sizes being submitted.

    - bug where a non size item was being prevented from being added to the basket fixed by adding the a variable for the product in the add to basket app so that it could correctly calculate a validation for the quantity available and not let a user buy more than available

    - 500 error code returning for 404, the issue was I missed a path name in urls.py on products so when a user typed in http://127.0.0.1:8000/b for example it was looking for a product and not a faulty url returning the 500 code and not the 404.
    
    - Readmore function wasn't working on the index page, added the script inline on this page to ensure it works across the entire site.

    - Address button wasn't displaying for new users - the add new address was indented in the for loop for addresses meaning it only ever existed if an address object was present, moved the add new address outside the loop.

    - 500 error when a logged in user tried to checkout without having an attached address, fixed by adding an else statement in the checkout app that prepopulates the form based on name and email if no address exists fixing the 500 issue.

## Deplyment
### Heroku

This project is deployed with Heroku - the steps to deploy are as follows:
- Sign in and click "Create new app"

![Step1](readmeimages/deployment-1.png)

- Name your project and select you region:

![Step2](readmeimages/deployment-2.png)

- In the settings tab Add your config vars in this case:
  - Cloudinary
  - database
  - secret_key
  - stripe_public_key
  - stripe_secret_key
  - stripe web hook

![step3](readmeimages/config-vars-step.png)

- Go to deploy and connect your repository for your project using the GitHub Option

![step4](readmeimages/deployment-4.png)

- Once you have connected deploy from main branch - choose "automatic updates if you want to update as you work on your project" if not press deploy at the bottom

![step5](readmeimages/deployment-5.png)

- The Animania live site is deployed through Heroku the live deployment is here: 
[Animania](https://animania-175b65d61606.herokuapp.com/)

### Cloning a repository

1. On your GitHub repository navigate to your repository page.
2. Click on the green button with "CODE" written in it.
3. Go to the HTTPS and copy the URL by pressing the overlapping squares.
4. Open Git Bash. in your IDE
5. Enter git clone followed by the copied URL.
6. Enter where you would like your repository to be saved too for your local file.
7. Press Enter to finalise the clone.
8. within the local file in your IDE add the the requirements.txt file: pip3 install -r requirements.txt
this allows you to have the necessary requirements to run the project.
9. set up the necessary env.py file: 
  - import os
  - os.envrion["CLOUDINARY_URL"]= "Your cloudinary URL"
  - os.environ["DATABASE_URL"] ="Your database URL"
  - os.environ["SECRET_KEY"] =" Your made up secret key"
  - os.environ["STRIPE_PUBLIC_KEY] = "your stripe public key"
  - os.environ["STRIPE_SECRET_KEY] = "your stripe secret key"
  - os.environ["STRIPE_WH_SECRET] = "your stripe webhook"
10. Once this is set up run migrations
    - python3 manage.py makemigrations --dry-run (check all is okay)
    - python3 manage.py makemigrations
    - python3 manage.py migrate --plan (double check all is okay)
    - python3 manage.py migrate
11. Create a superuser for admin management
    - python3 manage.py createsuperuser
    - set up a username and password and an optional email.

[home](#animania)

## Credits 

- Code for adding products to the basket was taken from the boutique-ado walkthrough project.
- Used the project boutique-ado walkthrough for the creating order, order-lines code.
- I did add to the parts used from the walkthrough and tried to create an original version in parts of my own.
- Used [Stack overflow](https://stackoverflow.com/) for help with size association guidance, inspiration for better ways in structuring some of the python   views
- Used this site for some help with setting users up:
[account setup](https://gghantiwala.medium.com/django-sign-in-and-logout-tutorial-for-beginners-1a5612933434)
- Used [W3 schools](https://www.w3schools.com/) for help creating the amend products table, amend banners table
- Referenced [Amazon](https://www.amazon.co.uk/) for any ideas I may have missed with products. (didn't add any of the ideas just brainstormed)

[Back to top](#animania)

## Acknowledgments

This is my 5th and final project I will be submitting for My full stack development course, I would like to thank the student care team for swiftly answering the queries that I had and thanks to my mentor [Precious ljge ](https://www.linkedin.com/in/precious-ijege-908a00168/) for the constructive feedback of this project.

Liam Edwards 2024.
[Home](#introduction)