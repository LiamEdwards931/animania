# Animania

## Animania Anime merchandise

Animania is an e-commerce merchandise store, the core behind animania is that it offers anime merchandise all in one place for anime lovers to buy. I decided to go for this particular genre as I know several anime fans, myself included and the market for being able to purchase and browse a selection of merchandise from different anime is quite scarce and difficult to find.

Even though this site is fictional and the products shown in this site are not available I do believe that there is a potential in the market for a store like this one, that could have little competition when browsing and purchasing goods for anime.

## Live deployment 

This project is deployed on Heroku 
the link for which is here: [live deployment](https://animania-175b65d61606.herokuapp.com/)

## Testing
The manual testing performed for animania is all document below:
[Animania-testing](TESTING.md)

## Bugs 
- Unfixed bugs
    - No bugs left unfixed within the website as far as the testing is concerened, features all seem to behave as expected.

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

## Credits 

- Code for adding products to the basket was taken from the boutique-ado walkthrough project.
- Used the project boutique-ado walkthrough for the creating order, order-lines code.