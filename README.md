# Portfolio Project 5 - CARSALES APP  
  
    
(CTRL + CLICK to open Links in new window)  

Deployed site can be found [here](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/css_tests/prefixedcssvalidationcheckout-pp5.png)  
  
Github repository can be found [here](https://github.com/bobshort4bobby4/PP5-v1)  
  
  
  
![site mock-up](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/mock-up-pp5.png)  
  
  
  
# **Introduction**

This is the fifth project I have completed as part of the[Code Institute Full Stack Diploma Course](https://codeinstitute.net).  
  
This project sets out to create an ecommerce site for a fictitious car-sales business based in Dublin, Ireland.  
The site will display all available stock, allow a search of same.  Each item of stock should have a specific page giving more information on that vehicle.  
The site will have a shopping bag function where users can store items before purchasing them in the stripe enabled checkout.  
Users should be able to value a vehicle  for possible trade-in, accept this value if desrired and apply it as a credit to their shopping bag total.
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
   
     
    
(CTRL + Click to open in new window) [link to wireframes pdf](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/pp5-wireframes-correct.pdf)

A full set of wire frames for this Project was produced and can be viewed at the above link, A sample of them are shown below.  
    
 #### Home Page Wireframe
![home page wireframe](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/pp5-Home.png)  
#### All Vehicles Page Wireframe 
![all vehicles page wireframe](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/pp5-All%20Vehicles.png)  
#### Vehicle Detail Page Wireframe
![vehicle detail page wireframe](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/pp5-Vehicle%20Detail.png)  
#### Adjust Base Price Page Wireframe
![adjust base price page wireframe](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/pp5-Adjust%20Base%20Price.png)
  
    
### Images
  Images used in this project were obtained from a number of sources but principaly the [Pexels Website](https://www.pexels.com/).  
  All images are free to use.  
  
### Colours
  
</details>    
  
 # Data Schema
 
 <details>
            
 <summary> Data Schema</summary>  
            
[link to erd pdf](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/erd_pp5.pdf)  
            
![erd](https://github.com/bobshort4bobby4/PP5-v1/blob/main/media/readme_docs/erd_pp5.png)  

Note: As I review this erd, it seems to be redundant to have a separate relation for the fuel-type as there is only one field. It may prove uesful in a hypothethical future version of the software if other features such as fuel efficency or environmental impact of each fuel needed to be calculated for each vechicle.  

              
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
            
  
</details>






https://docs.djangoproject.com/en/4.1/ref/contrib/postgres/search/
