#### Home page 
|User Type| User story|Completed|Test done|
|--------|-----------|----------|---------|
|User| As a user I expect a Nav bar shows links to the relevant pages such as products and accounts|[x]| Animania link takes you to home page, each category, series, sale and new link takes you to the respective page, the search link takes you to the search part of the all products, the profile link takes you to the account or login page, wishlist takes you to wishlist page, basket link takes you to the basket|
|User| As a user I expect to see a clear indication through images of what the page is about|[x]|Image displayed on the main page only exists when a product of that series exists, removed  a product series and the banner doesnt display as anticipated|
|User| As a user I expect to see products that could inspire me to buy|[x]| Sale and New products are displayed on the home page, they update accordingly when changed in the amend products|
|User| As a user I expect to see a link to take me to other sources that could be related to Animania e.g. a facebookpage|[x]|Facebook page link is present and connects to the correct url|
|User| As a user I expect to see a useful footer that gives me information and important links|[x]|Footer contains an about animania section, useful links that are dynamic to user status, no broken links, series link update as anticipated|
|Superuser & User| As a sitemanager/User I expect to see a promotional message to encourage purchase such as a promotion on delivery|[x]|Delivery message appears on the startup, users can easily dismiss this for a better overall view|

#### Accounts/Profile
|User Type| User story|Completed|Test done|
|--------|-----------|----------|---------|
|User| As a user I expect to be able to log in to the site|[x]|Log in is present and functional from the navbar and footer message returns when successful|
|User| As a user I expect to be able to log out of the site|[x]|Log out is present in the profile page and functional messages return when performed.
|User| As a user if i don't have an account I expect to be able to create an account|[x]|Create an account is located in an appropriate place by the login button, users can easily create a new account which redirects to the profile page with a message.|
|User| As a user I expect to be able to change my password for security|[x]|Change password is located in the profile app, the fucntionality of this works as expected|
|User| As a user I expect to be able to add some address details that are saved to my profile|[x]|Users can add new addresses from the profile page|
|User| As a user I expect to be able to update and remove my address details|[x]|Users can update and remove address details they have saved on the profile with messages on success or failure|
|User| As a user I expect to be able to see my personal details|[x]|Personal details for the user are present on the profile|
|User and Superuser| As a site manager/User I expect to be able to read a list of all the reviews I have posted|[x]|Reviews can be browsed through the button present in the profile page|
|User and Superuser| As a site manager/User I expect to be able to update any of the reviews I have posted|[x]|Reviews can be updated from the my reviews page with messages returned|
|User and Superuser| As a site manager/User I expect to be able to delete any of the reviews I have posted|[x]|Reviews can be deleted from the my reviews page with messages returned|
|Superuser| As a Site manager I expect to be able to add new products|[x]|New products can be added from the product overview button on the profile page taking you to the amend products page|
|Superuser| As a Site manager I expect to be able to make adjustments to products|[x]|Update functionality is present and working for each product|
|Superuser| As a Site manager I expect to be delete products|[x]|Delete functionality is working for the products, confirmation message is present asking a user if they are sure they wish to delete|
|Superuser| As a Site manager I expect to be able to create new home page banners|[x]|Banners can be created from the profile page using the amend banners button|
|Superuser| As a Site manager I expect to be able to update home page banners|[x]|Users can update banners from the amend banners page with returned messages|
|Superuser| As a Site manager I expect to be able to remove home page banners |[x]|Users can delete banners from the amend banners page with returned messages|
|Superuser| As a Site manager I expect to be able to track the total performance of the site|[x]|Users can see the sales data on the site using the sales data button popping up a modal displaying the data|

#### Products
|User Type| User story|Completed|Test done|
|--------|-----------|----------|---------|
|User| As a user I expect to be able to browse a all the products available on the site|[x]|All products can be browsed in the all products page, this shows every product available on animanaia.|
|User| As a user I expect to be able to filter the products to narrow down the product I want|[x]|Filters are present and working for the products, each type of filter behaves as expected and clear filters returns the expected result| 
|User| As a user I expect to be able to search for a product that I want |[x]|Search bar functionality works as expected, takes keywords, description, name, series into account when returning results|
|User| As a user I expect to be able to see a number of search results |[x]|Correct number of returned results display on all products, filters and search results|
|User| As a user I expect to be able to see relevant details of the product|[x]|Each product as a quick overview of essential data such as name, series, new or sale, price, average review and a product details link|
|User| As a user I expect to be able to add a product to my wishlist|[x]|Each product has a heart icon that allows a user to add the product to the wishlist only appears for logged in users|
|User| As a user I expect to be able to find out more details about a product |[x]|Each product links to a product detail page that gives you the user more details to look through when considering a product|
|User| As a user I expect to be able to quickly see if it's on sale or if it's new |[x]|A small banner indiciates if the product is new or on sale, the sale amount is also present in the sale banner|
|User| As a user I expect to be able to quickly see a review score for the product|[x]|The review for each product is displayed in the product card if no reviews have been submit then a message stating so is displayed|
|User| As a user I expect to be able to be able to navigate the products without excessive page length (pagination) |[x]|pagination is present and functional on the page|
|User| As a user I expect to be able to choose a quantity of product I want and add it to my basket|[x]|In the product details users can add a quantity of an item to their basket|
|User| As a user I expect to be able to add a specific size of clothing to my basket |[x]|users can add specific sizes of clothing to their basket|
|SuperUser| As a site manager I expect to be able to see live changes as I update products e.g. price/sale/new/quantities|[x]|changes are present after a change is made and the style adjusts accordingly e.g. swapping a product from new to sale updates the banner style on the product and displays the discounted price with a slash through the normal price.

#### Basket
|User Type| User story|Completed|Test done|
|--------|-----------|----------|---------|
|User| As a user I expect to be able to be able to view the contents of my basket|[x]|On clicking the basket users can browse any and all goods they have added to it|
|User| As a user I expect to be able to adjust the quantity of items within my basket|[x]|Quantities can be adjusted within the bag|
|User| As a user I expect to be able to remove items from my basket|[x]|Items can be removed from the basket with messages returned|
|User| As a user I expect to be able to see a checkout amount before I proceed to the checkout |[x]|The total costs are displayed for the user so they know which costs to expect|
|User| As a user I expect to be able to see a breakdown of my costs before proceeding to the checkout |[x]| subtotal, delivery and grand total costs are all displayed before users get to the checkout page|
|User| As a user I expect to be able to have a quick way to rebrowse products in case I want to add more |[x]| a button is present to allow users to return to the products next to the checkout button|


#### Checkout
|User Type| User story|Completed|Test done|
|--------|-----------|----------|---------|
|User| As a user I expect to be able to see the contents of my basket again before I proceed forward for confirmation|[x]|Basket content is also displayed in the checkout page, allowing users to be completely sure they have the right products before proceeding to pay|
|User| As a user I expect to be able to fill out an easy to fill form that requires my personal details for delivery |[x]|details form is present with validation and placeholders|
|User| As a user I expect to be able to see this form prepopulated with my details I filled out previously |[x]|If i have exisiting address details they are prepopulated in this form if I am logged in.|
|User| As a guest user I expect to be able to still be able to complete checkouts.|[x]|Guest users can check out as normal, they just need to enter all the details required in the form|
|User| As a user I expect to be able to complete a payment option|[x]|Stripe payment is implemented on the page and is functional with validation|
|User| As a user I expect to be able to see a confirmation of my order once I have purchased it|[x]| users get directed to a checkout success page with a message displaying a successful transaction|
|User| As a user I expect to be able to see an invoice of the items I have purchased, the costs and the delivery address |[x]|the checkout success page displays, delivery and personal details, order number and order costs and also line by line the items the user has purchased|

#### News
|User Type| User story|Completed|Test done|
|--------|-----------|----------|---------|
|User| As a user I expect to be able to see up to date relevant news about the site or associated topics. |[x]|news page is present for logged in users, snippets of the articles are present on the main page|
|User| As a logged in user I expect to be able to see more details about an article. |[x]| each news article has a see details option that takes users to a more detailed page about the article|
|SuperUser| As a Site manager I expect to be able to add new articles to the page |[x]| new articles can be created from the news page, takes the user to a form with validation and returns messages on success or failure.
