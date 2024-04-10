# Feature Testing 

This content will outline all of the testing performed on the animania website.

## Index page testing 

| Description                                    | Expected Result | Actual Result  | Pass/Fail |
|------------------------------------------------|-----------------|----------------|-----------|
| Navbar is fixed to top with clear working dynamic filter links| Links should point to the specified path they have listed | Links all work | Pass|
|Profile page and wishlist links should only appear when logged in| Links dont appear when logged out|Links generate as expected on user status| Pass|
|Series links get automatically created when a new product is created in the navbar|Links should represent all of the product series that are available|Links generate with each new series created, also get deleted if a series gets deleted|Pass|
|On hovering over the basket the user gets a summary of the total of the basket|hovering the basket displays a grand total price| the cumulative price of the basket is displayed on hovering over the basket|Pass|
| Delivery bar can be close with x button | x button closes the bar| x button closes bar|pass|
| Main image has indicators that show the amount of images| circles inidicating the qty of images|indicators are present|Pass|
| Main image can be clicked to cycle             |Image changes on click      |Image changes on click    | Pass      |
| Main image has buttons to shop based on series|Button for the relevant series appears|button appears and works| Pass|
|Main image will only display images based on the series that are available to purchase| Images will only be present if that series has a product available for purchase| works as expected and dynamically changes based on the products available|Pass
| Category section has links that point to the correct filter| category links display products with that category| works as expected| Pass
|New section displays new products| Products that are new will display here| new products display as expected| Pass|
|New section will let you view the detail of the product| link points to the correct product and its details| works as expected|Pass|
|Sale section displays new products| Products that are discounted will display here| discounted ..lproducts display as expected| Pass|
|Sale section will let you view the detail of the product| link points to the correct product and its details| works as expected|Pass|
|Link to facebook sends you to the correct page|Takes you to the animania facebook page| works as expected|Pass|
|Footer has working links to profile, news and all product series| All links should take you to the pages specified| all links take you to the relevant pages|Pass|
|Footer is always at the bottom of all other content| You should see the footer last on every page| Footer is always on the bottom of the page| Pass|
|logout message should appear when logging out| message should appear at the top of the screen based on sign in status| message appears as expected|Pass|

## Accounts testing
This testing section covers the login/logout functionality and the profile page 

| Description                                    | Expected Result | Actual Result  | Pass/Fail |
|------------------------------------------------|-----------------|----------------|-----------|
|Non-users go to login page and users go to profile page from navbar|users and non-users go to different pages|Works as expected|Pass|
|User can login quickly with a feedback message|Message should appear on login| messages appears|Pass|
|User status changes the way the profile page looks e.g. a normal user has option to add address, superuser has product management| links should change based on status| Links appear as expected| Pass|
|all links on the profile page point to the correct urls| superusers can amend products, see sales data, change banners. normal users can add delivery addresses, change password, view the reviews they have submitted| All links work as expected| Pass|
| Details from signing up should appear on the profile page| Your details should be clearly visible on the profile page| Details are clearly visible|Pass|
|Validation feedback on signing up should be present|Validation in place that highlights required fields if not filled in| works as expected|Pass|

## Change password testing 
| Description                                    | Expected Result | Actual Result  | Pass/Fail |
|------------------------------------------------|-----------------|----------------|-----------|
|A button that takes you to a page to change your password| page displays a change password form| page displays change password form|Pass|
|Form allows you to update your password|Form allows the user to change their password|Works as expected|Pass|


## Amend products.html testing 
| Description                                    | Expected Result | Actual Result  | Pass/Fail |
|------------------------------------------------|-----------------|----------------|-----------|
|All products should be displayed on the amend products page|Products displayed in a table for good item management|Works as expected|Pass|
|All products should have the details associated with them e.g. price/name/saleitem?/newitem?|variables should give all the relevant data| works as expected| Pass|
|All products should have update and delete buttons associated to them|Buttons should appear for each product and should behave by letting you update or delete the particular records| Update button should take you to an update form that alters the details, delete button should remove the record| Buttons behave as intended and allows users to update and delete records|Pass|
|Confirmation of delete should be requested on delete|Pop up asking you to confirm should appear before deleting|Works as expected|Pass|
|Filtering products in the table should be functional and present|a-z, z-a, price, series, category, name and filtering should be functional and present|All functionality for filtering works as intended|Pass|
|Filtering should be able to be cleared completely|Clear button filter that removes all the filters|Button is present and functional for each filter category|Pass|
|Products that have sizes should have additional options to add sizes and quantities for each size|Button to add quantity to individual sizes| Button displaying for all products marked as clothing, in the size column a message requests you add the size and quantity|Pass|
|Users should be able to update size quantites|For products with sizes users should be able to update the sizes|User can update size quantites from the table|Pass|
|Pages are paginated so the table doesn't become too difficult to navigate|Pages should show links for paginataton to display multiple pages of products| Pagination appears for more than 30 products for easier product management|Pass|
|Feedback messages on successful CRUD operations| Delete and update and create new should have messages to the user| Messages display on deletion, updating and creating new records|Pass|
| Forms should guide users if they have missed a section that needs filling or give feedback if conditions havent been met|Displays the required fields if not filled in, gives message if duplicate objects are trying to be created, doesnt allow users to leave blank inputs for essential fields|Pass|

## Amend banners testing
| Description                                    | Expected Result | Actual Result  | Pass/Fail |
|------------------------------------------------|-----------------|----------------|-----------|
|All uploaded banners should be displayed on the page| Banners are clearly visible| All uploaded banners are shown on this page|Pass|
|Banners should have update and delete functionality| Buttons shown to process the CRUD operations| Buttons are shown for each banner to update and delete them|Pass
|feedback given to user on deletion or update| Message giving feedback to user| Messages appear at the time on deletion and update|Pass|


## Sales data testing 
| Description                                    | Expected Result | Actual Result  | Pass/Fail |
|------------------------------------------------|-----------------|----------------|-----------|
|Total of all order totals summed up should be displayed in this modal to give a total turnover of the business|All order totals are calculated and displayed when clicking the sales data button|Order totals are calculated and displayed to the user|Pass|
|The profit of the total of the orders calculated and displayed to the user| the profit made from the turnover should be displayed back to the user| The profit is calculated and displayed back to the user|Pass

## Address testing 
| Description                                    | Expected Result | Actual Result  | Pass/Fail |
|------------------------------------------------|-----------------|----------------|-----------|
|Uploaded addresses should be fedback to the specific user logged in| Only addresses uploaded by the logged in user should be able to see their address| Works as expected and users can view their specific address|Pass|
|Update and delete addresses|Button to update and delete addresses functional and present|Buttons exist and work as expected with feedback to the user.|Pass|

## Review testing 
| Description                                    | Expected Result | Actual Result  | Pass/Fail |
|------------------------------------------------|-----------------|----------------|-----------|
|Review button should take you to a page where you can see all of your uploaded reviews.|button takes you to review page|works as expected|Pass|
|Read, update and delete present for reviews|Update and delete buttons should be present for the Reviews|buttons work and are there as expected on operations performed feedback is given to the user|Pass|
|On update and delete the review should change on the product the review is for| the review should be updated or deleted in the overview of reviews and should also be updated on the product detail page where the reviews are|Pass|

## All products page testing 
| Description                                    | Expected Result | Actual Result  | Pass/Fail |
|------------------------------------------------|-----------------|----------------|-----------|
|Page that displays all of the product objects|Page displays all products available|Page displays all of the products|Pass|
|Page displays the correct information for product| Displays details like if its new on sale, price, series, name and image|all detail fields present and correct for the products|Pass|
|Each product has a link that takes you through to the details of the product|Link in obvious place that allows users to see more about the products on display|Links generated on the image and an anchor for each unique product|Pass|
|Filters functional available much like the amendproducts filters|different filters available and functional for users to be able to narrow down products they are looking for| tested a-z,z-a,price low-high, price high-low, series, category, sale and new all work as expected|Pass|
|Search bar on all products functional and in a prominent location|Functional search bar that uses keywords to find products|Search bar works as expected using search tags, product names, product categories, descriptions and keywords|Pass|
|Displays the amount of products found on all products, filtered products and searched products| displays an indication of how many products have been returned from no filters, with filters and search results|products have correct indication based on filter and search results|Pass|
|Wishlist icon displayed for logged in users on products|Icon to add products to a wishlist for logged in users|Icon appears for a logged in user adds the product to a wishlist and returns a message indicating it has been added|Pass|
|Pages are paginated so the table doesn't become too difficult to navigate|Pages should show links for paginataton to display multiple pages of products| Paginate exists and works for products on the page|Pass|

## Product details testing 
| Description                                    | Expected Result | Actual Result  | Pass/Fail |
|------------------------------------------------|-----------------|----------------|-----------|
|product details display correctly for the selected product from all products| The product selected in the all product matches the product shown in the product detail page| product is identical to all products selection, image is present, name, title, description and price, if item is a discounted item sale price is shown with the price striked out to show the savings|Pass|
|Product detail shows the user how many of that product is in stock| display of stock availability| the screen shows how much of that product is in stock, if the product has sizes shows the respective quantites for each size|Pass|
|Users cannot select more than what is available when adding to cart|max quantity in the input should be the same as the availability|max quantity is set for products without sizes, product with sizes returns an error message when trying to add more of a selected size than available|Pass|
|Message returned when a product is added to the basket| message appears when a product is added to the basket| message appears as excpected|Pass|
|Reviews for the product are displayed with star rating and usernames| Product reviews have the appropriate content displayed for the correct product| The reviews are displayed with an average star rating at the top calculated by adding the star rating and dividing by the amount it has, it has a review count, and content, for no reviews it states no reviews posted and allows user a link to submit a review|Pass|
|review form to submit a new review for an associated product| Users on clicking leave a review should be taken to a review page to submit a new review with validation| Users are taken to a leave a review page with according form validation on submitting the review the review appears under the product and also into that users my reviews page in their profile to edit and delete if they wish|Pass|

## Wishlist testing 
| Description                                    | Expected Result | Actual Result  | Pass/Fail |
|------------------------------------------------|-----------------|----------------|-----------|
|Items added to the wishlist should display on the wishlist page| wishlist items all displayed on the page| Items added to the wishlist are displayed correctly on the wishlist page| Pass|
|Wishlist items should have an option to go to the product detail of that product so users can add it to the basket| items should link to the relevant detail page for that product| items link to the relevant page of product details|Pass|
|Wishlist items should have a remove button to delete items from the wishlist| The remove button is present and functional in removing items from the wishlist| the remove button is present and gives a confirmation box on delete attempt, if confirms user gets a feedback message, if canceled keeps the item in the basket|Pass|

## Basket testing
| Description                                    | Expected Result | Actual Result  | Pass/Fail |
|------------------------------------------------|-----------------|----------------|-----------|
| Items added to the basket should have a message stating the action has been done| Message should return what Item and the quantity has been added to the basket| Message returns product name and quantity and if size states which size has been added|Pass|
|The basket should have line by line each product added with its subtotal| basket items will have a line for each product added showing the quantity, the size and the subtotal amount| The products in the basket display an image, quantity, size(if clothing) and subtotal price along with the price per item, the user can adjust the quantity here that will update the values of quantity and price.|Pass|
|The basket should have an option to remove the product from the basket| a button to remove the product from the basket| A link exists and functions properly to removed basket items|Pass|
|The basket should display all of the charges the users will have such as product costs, delivery costs and the combined costs of product and delivery| The page displays all of the expected results and recalculates when quantities of products changes.|Pass|
|basket should have an option to go back to keep shopping|The cart should have a clear option to allow users to change there minds to add more products to the basket|button exists and is functional to take users back to the all products page to add more items to the cart|Pass|
|Basket should have an option to let users checkout|A button to take users to the checkout page with the items in their basket should be present and functional| The button takes the user to the checkout page with their current basket contents|Pass|

## Checkout testing
| Description                                    | Expected Result | Actual Result  | Pass/Fail |
|------------------------------------------------|-----------------|----------------|-----------|
|The checkout should display all of the products from the basket| The items in the basket should also be present in the checkout| The checkout displays all of the basket contents and the associated costs, giving users a clear overview of what they are purchasing with complete transparency|Pass|
| The checkout should have a form for guest users and logged in users to fill out their information for the delivery| The form should be intuitive to fill out for new users, should be prepopulated for logged in users who have already filled an address out in their profile| New users have an intuitive detail form to fill out, logged in users have a prepopulated form with the details from the profile app.|Pass|
|Back to basket button present| A button to go back to the basket present for last minute adjustments| Button is present and takes the user back to the basket with the items they have added to make last minute changes|Pass|
|The checkout should have an option for users to add their credit card details| Payment form should be present on the page for users to make a purchase that functions properly with stripe| Payments can be made using the form at the bottom of the details form, validation is in place and errors are returned on card details that do not exist.|Pass|


## Checkout success testing 
| Description                                    | Expected Result | Actual Result  | Pass/Fail |
|------------------------------------------------|-----------------|----------------|-----------|
|Order confirmation should appear on a successful purchase|User should have confirmation the order has been processed| User is redirected to checkout success, with a message displaying the success of the purchase|Pass|
|Unique order number should generate for every new order| Order numbers should be unique for each order| Order number is generated randomly and is always unique| Pass|
|Order summary should be present with correct details| An overview of the prices and order details should be displayed| Users details of address and product purchases are all present and consistent with the basket and the purchase|Pass|

## News
| Description                                    | Expected Result | Actual Result  | Pass/Fail |
|------------------------------------------------|-----------------|----------------|-----------|
|Only logged in users should be able to view the news content, non logged in users should be pushed to create an account or log in| Page displays differently based on user status| Page displays differently base on the log in status of the user|Pass
| A page displaying the news for the site should be present| A page displaying relevant topics that could improve marketing should be present on the page| The news items are present on the page displaying relevant content|Pass|
| Video urls should work on the news detail page without any errors| The video link url links to a video relevant to the product or series| The link successfully navigates to the youtube video based on the url submitted in the form and in a new tab|Pass|
|Superusers should be able to add new news content through a form| An intuitive functional button should be available to navigate to the form to create news articles| button is at the top of the screen on pressing it user navigates to the create news article page| Pass|
|News form validation messages| Message should guide the user if the form has been submitted wrong| Messages appear for required items on creating an article, gives the user an indication of what they did wrong| Pass|


## Final note on testing 
I have tested these features thoroughly and to the best of my ability, I used testing with Precious my mentor and testing through friends and family to try and find and work out kinks within Animania all testing documented in this readme were as a result of my own personal testing throughout the site.
