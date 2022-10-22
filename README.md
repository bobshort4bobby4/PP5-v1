# Portfolio Project 5 - CARSALES APP  
  
    
(CTRL + CLICK to open Links in new window)  

Deployed site can be found [here](https://pp5-carsales.herokuapp.com/)  
  
Github repository can be found [here](https://github.com/bobshort4bobby4/PP5-v1)  
  
  
  
![site mock-up](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/mock-up-pp5.png)  
  
  
  
# **Introduction**

This is the fifth project I have completed as part of the [Code Institute Full Stack Diploma Course](https://codeinstitute.net).  
  
This project sets out to create an ecommerce site for a fictitious car-sales business based in Dublin, Ireland.  
The site will display all available stock, allow a search of same.  Each item of stock should have a specific page giving more information on that vehicle.  
The site will have a shopping bag function where users can store items before purchasing them in the stripe enabled checkout.  
Users should be able to value a vehicle  for possible trade-in, accept this value if desired and apply it as a credit to their shopping bag total.
Staff members will need to be able to add, delete and edit stock items and also to change the trade-in base price for each manufacturer from the front-end.




# User Experience/User Interface (UX/UI)

<details>  
            
<summary>User Experience/User Interface (UX/UI)</summary>    
  
  
  
   
  
The AGILE methodology for project development will be used to produce this project, this method involves continual collaboration between all parties and improvements   at every stage. It helps to ensure good quality products are produced within time and financial constraints.
  
   ### User Stories    
     
   #### Casual Visitor Goals
   As a Casual Visitor I want:
   - [#1](https://github.com/bobshort4bobby4/PP5-v1/issues/1) to be easily able to ascertain information on the business and it's locality, to aid my purchasing decision.
   - [#2](https://github.com/bobshort4bobby4/PP5-v1/issues/2) to be able to easily browse and search stock and access data on each item of stock, to aid my purchasing decision.
   - [#3](https://github.com/bobshort4bobby4/PP5-v1/issues/3) to navigate easily around the site, to avoid frustration whilst using the site and to engender positive emotions towards the business.
   - [#4](https://github.com/bobshort4bobby4/PP5-v1/issues/4) to have any incorrect input rejected and the error explained clearly and quickly, so I do not have any frustrating emotions using the site. 
   - [#5](https://github.com/bobshort4bobby4/PP5-v1/issues/5) site to be responsive, to provide a positive user experience.
   - [#6](https://github.com/bobshort4bobby4/PP5-v1/issues/6) to be able to value any vehicle as a trade-in, to aid my purchasing decision.  
     
       
   #### Customer Goals
   As a Customer I want:
   - [#7](https://github.com/bobshort4bobby4/PP5-v1/issues/7) to easily add a vehicle to my order to make the purchasing process efficient.
   - [#8](https://github.com/bobshort4bobby4/PP5-v1/issues/8) to easily trade-in a vehicle, to make the purchasing process efficient.
   - [#9](https://github.com/bobshort4bobby4/PP5-v1/issues/9) to easily pay for my order, to make the purchasing process efficient.
   - [#10](https://github.com/bobshort4bobby4/PP5-v1/issues/10) to securely pay for my order, to engender trust in the site.
   - [#11](https://github.com/bobshort4bobby4/PP5-v1/issues/11) to be able to create a user account, to track my interaction with the site.
   - [#12](https://github.com/bobshort4bobby4/PP5-v1/issues/12) to be able to manage my user profile, to make site use easy.
   - [#13](https://github.com/bobshort4bobby4/PP5-v1/issues/13) to review my profile details and order details, to engender trust and provide as transparent process as possible.
   - [#14](https://github.com/bobshort4bobby4/PP5-v1/issues/14) to have all orders confirmed by email, to engender trust and provide as transparent process as possible.
   
   
   #### Site Owner Goals
   As a Site Owner I want:
   - [#15](https://github.com/bobshort4bobby4/PP5-v1/issues/15) to provide an easy to use website in order to drive sales and increase profits.
   - [#16](https://github.com/bobshort4bobby4/PP5-v1/issues/16) to engage potential customers and ensure they return to the site in the future, to drive sales and increase profits.
   - [#17](https://github.com/bobshort4bobby4/PP5-v1/issues/17) to use the site as a marketing tool, to drive sales and increase profits.
   - [#18](https://github.com/bobshort4bobby4/PP5-v1/issues/18) to enable staff members to perform certain admin tasks from the frontend, to efficiently run the site.
   
   ### EPICS
   
   Using the user stories as a frame of reference the following Epics were formulated;
  
  - Epic 01 implement basic html and django structure.
  - Epic 02 implement user registration and login.
  - Epic 03 implement stock display and search system.
  - Epic 04 implement order system.
  - Epic 05 implement purchase system using Stripe.
  - Epic 06 implement User profile system.
  - Epic 07 implement Seo and web-marketing.
  - Epic 08 implement staff admin functions.
  - Epic 09 implement trade-in function.
  
   
  The user stories were prioritised using the MoSCoW technique and the Kanban Board feature built-in to Github will be used as an information radiator.
  The user stories were broken down into tasks and these were listed under their respective issue in the initial Kanban Board.  
  The acceptance criteria for each user story are listed in each issue in the github project board.
  Care was taken to ensure should-have prioritised user stories are not greater than 60% of the total.  
    
  An image of the first issue is shown below for illustrative purposes.  
    
   ![issue 1 ](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/issue1-pp5.png)
    
      
  ### Table Showing User Story Allocation to Epics  
  
    
   |                                           User  story                                                                              | Epic     |
   |------------------------------------------------------------------------------------------------------------------------------------|----------|
   | to be easily able to ascertain information on the business                                                                         |  01      |
   | to be able to easily browse and search stock                                                                                       |  03      |
   | to navigate easily around the site                                                                                                 |  01      |
   | to have any incorrect input rejected and the error explained clearly                                                               |  01      |
   | site to be responsive                                                                                                              |  01      |
   | to be able to value any vehicle as a trade-in                                                                                      |  09      |
   | to easily add a vehicle to my order                                                                                                |  04      |
   | to easily trade-in a vehicle                                                                                                       |  09      |
   | to easily pay for my order                                                                                                         |  05      |
   | to securely pay for my order                                                                                                       |  05      |
   | to be able to create a user account                                                                                                |  02      |
   | to be able to manage my user profile                                                                                               |  06      |
   | to review my profile details and order details                                                                                     |  06      |
   | to have all orders confirmed by email                                                                                              |  05      |
   | to provide an easy to use website                                                                                                  |  01      |
   | to engage potential customers                                                                                                      |  07      |
   | to use the site as a marketing tool                                                                                                |  07      |
   | to enable staff members to perform certain admin tasks from the frontend                                                           |  08      |
   
   
   ### WireFrames  
   
     
    
(CTRL + Click to open in new window) [link to wireframes pdf](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/wireframes/pp5-wireframes-correct.pdf)

A full set of wire frames for this Project was produced and can be viewed at the above link, A sample of them are shown below.  
    
 #### Home Page Wireframe
![home page wireframe](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/wireframes/pp5-Home.png)  
#### All Vehicles Page Wireframe 
![all vehicles page wireframe](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/wireframes/pp5-All%20Vehicles.png)  
#### Vehicle Detail Page Wireframe
![vehicle detail page wireframe](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/wireframes/pp5-Vehicle%20Detail.png)  
#### Adjust Base Price Page Wireframe
![adjust base price page wireframe](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/wireframes/pp5-Adjust%20Base%20Price.png)
  
    
### Images
  Images used in this project were obtained from a number of sources but principaly the [Pexels Website](https://www.pexels.com/).  
  All images are free to use.  
  
### Colours  
    
![](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/colours/coloursblackink-pp5.png)
  
</details>    


# Features  

<details>
  
  <summary>Features</summary>
  
    
### Header  
    
![signed out header](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/features/headerfeature-pp5.png)
There are contact/location links at the top of each page. The telephone link initiates a voice call on suitable devices, the location opens a google map showing the business location.  
   
The business name is displayed top center on all pages, this title acts as a link to the home page to aid site navigation.  
    
There is a search facility which allows user to search the current stock.  The postgress text search is used to implement this search function. 
  
Login/Register links and links to stock page and trade in page are contained in the nav-bar.  This nav-bar is responsive and collaspes on smaller screen sizes, it is a standard bootstrap element.  
    
When a user logs in, a user icon is displayed, which is a drop-down menu with links relevant to the authorisation level of the user.  
  
![logged in nav-bar](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/features/signedin-navbar_featured-pp5.png)  
  
There is a link to the user's shopping cart and the value of goods in it.  
If there is a un-used trade-in credit amount, this is also displayed in the nav-bar.  
![trade-in credit amount](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/features/tradein-credit-pp5.png)
  
  
### User Authorisation  
  
The Django all-auth package is used to handle user registration, login and access levels.  
All all-auth templates are customised to match the appearance of the site.  
    
![all-auth register page](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/features/signup-pp5.png)  
    
    
### Footer  
   
The footer is displayed on all pages.  
There is a links section which links to the business's social media pages, to trade representative bodies and to the businesses privacy policy.  
The hours of business are shown on larger screens.  
There is a sign-up form for the business newsletter.  
In the bottom right corner there is a button which automatically scrolls the user to the top of the page.  
    
![Footer ](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/features/footer-large-pp5.png)  
    
### Home Page  
  
The Home page of the site features an image of a car with a prominent button linking to the stock page.  
There is also a carousel of featured vehicles.  
  ![home page](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/features/home-pp5.png)  
  

### Stock Page  
  
The stock page displays all available vehicles in a layout suitable for the viewing device, one per row on smaller screens, two on larger.  
  
![stock page](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/features/stock-pp5.png)
  
Each vehicle image when clicked links to a page giving more details on that particular vehicle. 
 The item can be added to the cart from this page.
 If the user is staff the item can be edited or deleted from this page.
![stockdetail](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/features/stockdetail-pp5.png)  
  
### Checkout  
    
  
![checkout](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/features/checkout-pp5.png)  
    
  
The checkout is stripe enabled with redundancies built in to accomodate unexpected user action and/or network errors.  
Logged in user's delivery details are automatically filled into form, if saved in user's profile.  
Upon completion of a successful order the item(s) are marked as sold in the Vehicles datatable and no longer displayed for sale.  
A confirmation email is sent to the user.  
A profile foregin key and a trade-in foregin key are attached to the order record if neccessary.  
 
  
    
  
### Profile  
  
The profile page for each user displays the user delivery information and lists that particular users order history.  
Each order is linked to the full details of that order.
The delivery information can be changed by the user from this page as can their password.  
![profile](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/features/profile-pp5.png)  
  
  
### Add Stock Item Page
This page is only available to staff members.  
It is used to add new vehicles to stock.  
The maker and fuel fields are drop down menus and form fields are validated.
![add stock page](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/features/addstock-pp5.png)
  
  
### Adjust Trade-in Base Price.  
 Only available to staff members.  It is used to change the price used to value vehicles for trade-in credit.  
 The Maker field is prepoulated with manufacturers listed in the Maker datatable.  
  Htmx is used to populate the price field on a change in the maker field.  
 ![adjust base price](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/features/adjust-price-pp5.png)
  
  
### Trade-In
 This page takes data from the user concerning a vehicle they wish to value as a tradein.  The site returns a value to the user who then decides if they want to accept this figure or not.  The user can clear the form and value another vehicle if needed. The form is validated.  
  
NB. The value returned from the site for each vehicle is calculated using the information input by the user and the base price for that particular manufacturer.  
  This function was based on several I found online and gives a very approximate value for each vehicle.  
  The Model type is not used in this calculation as the range of models for each maker is so large.  There are several API's which would have given accurate valuations for each vehicle but they were either a paid for service or subject to change so I decided not to use them for this project.  
    
  
![tradein page](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/features/trade-in-pp5.png)
  
    
  

  
  
  
  
  
</details>
  
 # Data Schema
 
 <details>
            
 <summary> Data Schema</summary>  
            
[link to erd pdf](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/erd_pp5.pdf)  
            
![erd](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/erd_pp5.png)  

Note: As I review this ERD, it seems to be redundant to have a separate relation for the fuel-type as there is only one field. It may prove useful in a hypothethical future version of the software if other features such as fuel efficency or environmental impact of each fuel needed to be calculated for each vechicle.  

              
</details>



# Search Engine Optimization

<details>

<summary> Search Engine Optimization</summary>
  
    
    

Ensuring the site ranks highly on search engines results is vital to the success of  most ecommerce businesses. Seo is a low cost method of marketing and is very effective at directing potential customers to the site.

#### Keyword Research
  
 I considered what topics our potential users most care about and using these created a list of potential keywords as follows;
    
 carsales, value cars, used cars, cheap cars, trade-in, second-hand vehicles, local garage, local car sales, Motordealers, cardealers, car finance, quality used cars, quality second hand vehicles, hybrid used cars, used electric vehicles, best garage near me, guaranteed used vehicles, guaranteed cars.  
   
The 10  best of these were selected based on relevance, authority and volume to the following short-tail and longtail phrases. the website wordtracker was used in this selection process

- used cars dublin
- used cars Ireland
- cars for sale
- second hand cars
- best place to buy used cars near me
- best place to buy new cars near me
- car dealers near me
- cheap used cars near me
- used hybrid cars
- used electric vehicles  
  
    
The next step in SEO optimisation was to include as many as possible of the keywords into the text of the website. This was done to ensure the language was still relevant and natural. Keywords placed in semantic elements were given higher priority as search engines give these elements greater weight.  

As resources allow it is planned to add articles and blog entries which will enhance the websites authority on our area of business, this should boost our ranking further.  A website that displays authority, expertise and trustworthiness will rank highly in search engine results, this metric is more important now that pure keyword matching. Relevant articles should also reduce bounce rate and increase session time.

The alt text for all the images on the stock page was changed to give each car a description of its make and model and a used or new classification.    

The social links were given the rel="noopener" attribute to ensure their content was ignored by search engines.    

A link to SIMI (Motor-Dealers representation body)  was provided to further boost rankings.  

The meta data tags were created in the html head.    

A sitemap.xml file was created using the xml-sitemaps.com website and placed in the root directory of the project.  The sitemap file helps search engines to access and analyse the website. It has not been registered with Google as per requirements for this project.  
  
A robots.txt file was created and saved in the root directory. This file specifies which search engines are allowed to crawl the site and which parts should be accessible.  
  
A link is provided to the websites privacy policy to aid transparency and build trust with users.  
The privacy policy was generated using [privacypolicygenerator.info](https://www.privacypolicygenerator.info/)
  




</details>


# Web Marketing

<details>

<summary>Web Marketing</summary>  
  
  
The site is a business to customer model. It will sell new and used vehicles directly to the end-user.  

It is planned that the main methods of marketing the business will be through SEO, via  organic social media marketing, principally Facebook and a weekly email newsletter.  

The reasons these methods were choosen was largely due to budget constraints.
Whilst there is plenty of scope for content marketing such as articles/guides to buying vehicles, maintainance tips,  weekly video's of new stock, a valuer for trade-in vehicles (api), there are insufficent resources available currently to implement all of these.    
  
Similar websites serving the same market will be looked at and features that are considered to work well will be implemented as a first step.  

Paid adds for social media sites and search engines were not considered at this stage due to the cost/value.  

The Facebook page is linked from the site and is also shown below. The Mailchimp app is used to facilitate the newsletter.


![facebookscreenshot top](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/images/facebook-top-pp5.png)
![facebookscreen shot middle](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/images/facebook-middle-pp5.png)
![facebookscreenshot bottom](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/images/facebook-bottom-pp5.png)



</details>


    
    

# Testing

<details>

<summary> Testing</summary>

 ### WAVE Acccessibility Tests  
 
  All pages of the app were tested using the WAVE Accessibility testing app.  
  ALL errors and contrast errors were resolved.  
  
  A sample of results is shown below.  
  
  Images of all page test can be found here  
  [https://github.com/bobshort4bobby4/PP5-v1/tree/main/media/readme_docs/wave_tests](https://github.com/bobshort4bobby4/PP5-v1/tree/main/media/readme_docs/wave_tests)  
  
    
   ![summary of WAVE results](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/wave_tests/wavesummary-pp5.png)
  
  
    
      
        
        
  ### HTML Validation.
  
  The Nu HTML checker was used to validate all project html.
  All errors were cleared
  
  Image of home page result is shown below along with links to other result images.  
    
   
 ![html checker result home page](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/html_tests/htmlhome_deployed-pp5.png)  
   
 (CLICK + CTRL to open in new tab)  
 [HTML Checker result stock page](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/html_tests/stockhtmlvalidation-pp5.png)  
 [HTML Checker result addstock page](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/html_tests/addstockhtmlvalid-pp5.png)  
 [HTML Checker result adjust price page](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/html_tests/adjustpricehtmlvalid-pp5.png)  
 [HTML Checker result bag page](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/html_tests/baghtmlvalidation-pp5.png)  
 [HTML Checker result checkout page](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/html_tests/checkouthtmlvalidation-pp5.png)  
 [HTML Checker result profile page](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/html_tests/profilevalidationhtml-pp5.png)  
 [HTML Checker result checkout success page](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/html_tests/checkoutsuccesshtmlvalidation-pp5.png)  
 [HTML Checker result tradein page](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/html_tests/profilevalidationhtml-pp5.png)  
 
   
   
 ### Lighthouse Testing  
   
     
All pages were tested using the Lighthouse app built into the Google Chrome web-browser.  

The result for the home page is shown and links to the results from the other pages are given below.  
  
![Lighthouse home page result](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/lighthouse_tests/lighthousehome-pp5.png)  
  
(CLICK + CTRL to open in new tab)   
 
[Lighthouse Stock page result](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/lighthouse_tests/lighthousestock-pp5.png)  
[Lighthouse AddStock page result](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/lighthouse_tests/lighthouseaddstock-pp5.png)  
[Lighthouse Adjustprice page result](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/lighthouse_tests/lighthouseadjustprice-pp5.png)  
[Lighthouse BAG page result](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/lighthouse_tests/lighthousebag-pp5.png)  
[Lighthouse Checkout page result](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/lighthouse_tests/lighthousecheckout-pp5.png)  
[Lighthouse Orderhistory page result](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/lighthouse_tests/lighthouseorderhistory-pp5.png)  
[Lighthouse Profile page result](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/lighthouse_tests/lighthouseprofile-pp5.png)  
[Lighthouse Stockdetail page result](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/lighthouse_tests/lighthousestockdetail-pp5.png)  
  
  
  
### CSS Testing  
  
    
The w3s app for validating (jigsaw) was used used to test the css files used in the application.  
Results are shown below.  All errors were cleared.  
  
 ![Main css test result](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/css_tests/prefixedcssvalidationmain-pp5.png) 
 ![Checkout test result](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/css_tests/prefixedcssvalidationcheckout-pp5.png)  
 
 
### Python Validation  
  The Flake 8 linter was used in the code editor to ensure the python code complied to standard. 
  A few images are shown below of python code syntax checks.  
    
  ![python checkout view check](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/checkoutviewspythonvalidation.png)  
  ![python profile view check](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/profileviewpythonvalidation.png)  
  ![python stock view check](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/stockapppythonvalidation.png)
  
  
  
### Javascript Validation

There was a small amount of Javascript used apart from the script supplied by Stripe.  
Both were validated by jshint, image of results are shown below.  
  
![jshint fragment test](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/jhintfragment-pp5.png)
![jshint stripe test](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/jshintstripe-pp5.png)   
  


 ### Responsive Testing
  
  The website was tested for responsiveness using the built-in tool in the Google Chrome browser. As I worked through each breakpoint I fixed any display issues I encountered.  
  A set of images of the homepage at each breakpoint is shown.  
   
  #### 320px home page
  ![320px-home](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/pp5-home-320px.png)
  
  #### 375px home page
  ![375px-home](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/pp5-home-375px.png)
  
  #### 425px home page
  ![425px-home](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/ppp5-home-425px.png)
  
  #### 768px home page
  ![768-home](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/pp5-home-768px.png)
  
  #### 1024px home page
  ![1024-home](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/pp5-home-1024px.png)
  
  #### 1440px home page
  ![1440-home](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/pp5-home-1440px.png)
  
  #### 2000px home page
  ![2000-home](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/pp5-home-2000px.png)
            
  #### Table showing responiveness testing.
    
  ![responsive test results](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/responsivetests-pp5.png)
  
  [link to responsive tests pdf](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/responsive-pp5.pdf)
              
  ### Manual Testing of User Inputs and Functions.  
         
  I systematically tested all user inputs and functionality in the website to compare feedback/results against expected results.
  Any unexpected output/outcomes were fixed.  
         
            
  (CTRL + Click to open in new tab) [Manual Testing pdf](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/manual_tests/Manual%20Testing%20pp5%20-%20Sheet1.pdf)
              
              
 ![manual test image](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/manual_tests/manual1-6.png)
 ![manual test image](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/manual_tests/manual7-14.png)
 ![manual test image](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/manual_tests/manual15-24.png)
 ![manual test image](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/manual_tests/manual25-29.png)
 ![manual test image](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/manual_tests/manual30-35.png)
 ![manual test image](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/manual_tests/manual36-46.png)
 ![manual test image](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/manual_tests/manual47-55.png)
 ![manual test image](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/manual_tests/manual56-62.png)
  
 ### Automated Tests
 I implemented those tests I had time resources for, the coverage rate for the app is 80%.  
 
    
 ![coverage result](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/coverageresult-pp5.png)  
   
      
 ### Testing Application For Achievement of User Goals.  
     
     
     
     
   |                                          User  story                      |                              Outcome                              |
   |---------------------------------------------------------------------------|-------------------------------------------------------------------|
   | to be easily able to ascertain information on the business                |  Social, telephone and location info provided                     |
   | to be able to easily browse and search stock                              |  Link to Stock page prominent, Search function provided           |
   | to navigate easily around the site                                        |  Forwards and backwards link on all pages                         |
   | to have any incorrect input rejected and the error explained clearly      |  All Inputs validated and message displayed                       |
   | site to be responsive                                                     |  Site responsive at all screen sizes                              |
   | to be able to value any vehicle as a trade-in                             |  Vehicle valuation facility provided                              |
   | to easily add a vehicle to my order                                       |  One ckick addition to bag, bag easily adjustable                 |
   | to easily trade-in a vehicle                                              |  Vehicle trade-in facility provided                               |
   | to easily pay for my order                                                |  Stripe enabled checkout                                          |
   | to securely pay for my order                                              |  Stripe enabled checkout                                          |
   | to be able to create a user account                                       |  All-auth  functionality implemented                              |
   | to be able to manage my user profile                                      |  Profile details editable from profile app                        |
   | to review my profile details and order details                            |  Profile and order history viewable from Profile app              |
   | to have all orders confirmed by email                                     |  Order and account actions confirmred by email                    |
   | to provide an easy to use website                                         |  All actions intuitive                                            |
   | to engage potential customers                                             |  Newsletter,social media links to engage users                    |
   | to use the site as a marketing tool                                       |  SEO used to promote the site to users                            |
   | to enable staff members to perform certain admin tasks from the frontend  |  Required admin tasks acccessible to staff from front-end.        |
     
 
          
  ### Security Issue
  
  In error I exposed a Stripe webhook signing secret to github.. Fortunately I had the GIT Guardian feature enabled which sent me an email immediately informing me of my error.  I was then immediately able to expire the signing secret via the Stripe dashboard thus minimising any security risk.  
   [Relevant Github commit](https://github.com/bobshort4bobby4/PP5-v1/commit/1ed667a6b7d1e6867baf1b762f1da6d4b4117ddb) 
   
  Email from Git Guardian 
  
  ![git guardian email]()
  
  
  ### Known Bugs Remaining 
  
</details>
  
      
        
        
 # Technologies Used
<details>
  <summary>Technologies Used</summary>
  
  #### Languages Used
  
  - Python
  - CSS  
  - HTML  
  - Javascript
  
  #### Development Environment
    
  I used the gitpod-full-template for gitpod provided by Code Institute.  
  The app was built using the Django framework.  
  I used the Django setup cheat sheet provided as course material to start and set basic settings for the application.
  
  
  #### Applications Used
  
  - [Balsamiq](https://www.balsamiq.com) was used to create wireframes for this project.
  - [LucidChart](https://www.lucidchart.com) used for the ERD in readme file.
  - [Git](https://git-scm.com/) Git was used for version control.
  - [GitHub](https://github.com/) GitHub is used to store the projects code.
  - [Heroku](http://www.heroku.com/) Heroku.com was used to deploy the site.
  - [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) used for layout and responsive testing.
  - [Wave](https://wave.webaim.org/) used for accessibility testing.
  - [W3 Validator](https://jigsaw.w3.org/css-validator/) used to test css code.
  - [w3 HTML Validator](https://validator.w3.org/) was used for html validation.
  - [extendsclass](https://extendsclass.com/python-tester.html) extendsclass python code checker used to validate python code
  - [Windows snip & sketch](https://www.microsoft.com/en-us/p/snip-sketch/9mz95kl8mr0l?activetab=pivot:overviewtab) used to capture screenshots for readme file.
  - [techsini.com](https://techsini.com/) used to create the mock-up used in the readme file.  
  - [autoprefixer.github.io](https://autoprefixer.github.io/) used to improve browser compatibility.  
  - [Cloudinary.com](https://cloudinary.com/) used to store media and to transform images on download.
  
  #### Django/Python Libaries Used
  I installed the following libraries.  
  
  - Django: The framework used to build the app.
  - Pillow:used to handle image files.
  - Cloudinary: used to serve/store media and css files.
  - Coverage: used in testing to determine how comphrensive testing is.
  - Gunicorn:WSGI application server (Web Server Gateway Interface)used to handle interaction between the web server and the app.
  - Django-allauth: Handles user verification and authorisation.
  - psycopg2:Library used to connect to database.
  - dj-database-url: Django utility which allows database URLs to be used to configure the app.
  - Django-crispy-forms: used to format forms within Django.
  - Stripe: enables secure payments.
  - Django-htmx: allows ajax calls without using javascript.
 
  
  
  </details>  
    
      
      
# Deployment and Version Control
<details>  
            
<summary>Deployment</summary>    
  
  
 ### Version Control
  
  Git is an open source version control system and was used for this project. Github was used to store the repository.   
  Git is run locally whereas Github is cloud based.
  
  ###### Forking
  Forking a Github repository is the process of making a copy of any repository that you can use without affecting the original, this original is known as the 
  "upstream repository".
  The process for forking a repository is set out below.
  1. Go to the Github page that hosts the repository you wish to fork.
  1. On the top-right of the page there is a button "Fork".
  1. Click this button.
  1. This creates a repository in your Github home page which is a copy of the original. You can submit and receive changes to the code by using pull requests 
  and/or syncing with the upstream repository.
    
  (Taken from the Github Docs guide "Forking Projects")
    
###### Cloning 
  Cloning a repository involves making a full copy of that repository on your local machine. This makes working on the code easier.  Changes can be pushed back up to the 
  GitHub site or changes from other sources pulled to your local copy. To make a clone follow the process below.
  1. Goto the repository page on GitHub.
  1. Above the file list click on the green button titled "Code".
  1. You can choose to download a zip file of the repository, unpack it on your local machine and open it in your IDE or,
  1. Clone using HTTPS by copying the URL under the HTTPS tab.
  1. Open a terminal window, set current directory to the one you want to contain the clone.
  1. Type `git clone `and paste the URL copied from the GitHub page.
  1. The repository clone will be created on your machine.
    
  (Taken from the Github Docs guide "Cloning a repository")
  
  ### Deployment
  
  ### Heroku

Heroku is a cloud based platform that allows the user to deploy and manage apps easily. The completed version of this project was deployed using Heroku.   
Heroku is fully managed meaning that all the hardware/server issues are taken care of.
Heroku apps can be deployed either through the website or via the terminal command line. 
  
To deploy my project I followed the steps below.
     
  - Create a new Heroku app using your chosen app name and choosing appropriate region  
  - Initialise Database.  
  - Initialise env variables in heroku including Cloudinary, Database, Email Settings and Stripe Keys
  - Link the Heroku app to the Github repository (automatic deploys can be enabled if desired)
  - Remove the collectstatic variable from Heroku settings  
  - Set debug to false in settings.py  
  - Set email settings in Django settings.py.
  - Set media and static paths in settings.py.
  - Create a runtime.py in the root file of the app specifying python and version.
  - Create a Profile file in the root file.  
  - Ensure all sensitive passwords/keys are included in the gitignore file.
  - Ensure requiremnets.txt file is updated.
  - Push to Github.
  - From the deploy tab in Heroku choose manual deploy.
    
      
   ![heroku manual deploy](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/herokumanualdeploy-pp5.png)
 
 </details>


  






https://docs.djangoproject.com/en/4.1/ref/contrib/postgres/search/
