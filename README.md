# F1 Experiences

![Site Preview](static/images/site-preview.jpg)

---

## [Project Repository](https://github.com/filleben/F1Experiences)

## [Deployed Site](https://f1-experiences.herokuapp.com/)

---

The goal of this project is to make an application that allows users to view and purchase tickets/race packages to Formula 1 events.

## Table of Contents

- <a href="#ux">UX</a>
- <a href="#features">Features</a>
- <a href="#technologies">Technologies Used</a>
- <a href="#testing">Testing</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>

<span id="ux"></span>

## UX

### User Goals

I expect that the majority of the users will fall into the following criteria:

- A user looking to purchase event tickets.
- A user looking for information about upcoming events.
- A site manager adding/removing information and race packages.

### User Stories

- As a user, I want to be able to view a list of events.
- As a user, I want to be able to view a list of tickets for each event.
- As a user, I want to be able to view a running total of my puchases.
- As a user, I want to be able to create an account to view and manage my orders.
- As a user, I want to be able to edit and remove items from my cart while shopping.
- As a user, I want to be able to pay for tickets using card payment.
- As a user, I want to be able to search for events.
- As a site manager, I want to be able to add and remove race events.
- As a site manager, I want to be able to add and remove tickets for each race event.
- As a site manager, I want to be able to edit tickets and race events.

### Wireframes

[Here](https://github.com/filleben/F1Experiences/tree/master/wireframes) are the designs I made for the site.

The wireframes were made using [Balsamiq](https://balsamiq.cloud)

### Design Choices

- **Font**: I wanted the project to look as professional as possible so decided to use a copy of the official Formula One font sourced from [Here](https://www.ffonts.net/Formula1-Display-Regular.font.download).

- **Colours**: I wanted the project to look like a product from Formula One so with this in mind I used the same colour scheme used on the [Official Site](https://www.formula1.com/). I used white (Hex: '#ffffff' RGB: 'rgb(255, 255, 255)') as the background and navbar font colour, red (Hex: '#ff0000' RGB: 'rgb(255, 0, 0)') for the navbar and borders and then black (Hex: '#000000' RGB: 'rgb(0, 0, 0)') for the body text.

<span id="features"></span>

## Features

- **Navigation bar**: Allows the user to navigate to all the pages of the site, consistent throughout the site.
- **User Registration**: Users can create a account by providing a valid email address, username and password.
- **User Authentication**: Users can login to their accounts by providing the correct username and password combination.
- **Social Login**: Users can register and login to the site by using there Google account.
- **Password Reset**: Users can reset their password if forgotten.
- **Most Popular Events**: The 4 most popular events are featured on the home page.
- **Testimonials**: 4 different user testimonials are featured on the home page.
- **Contact Page**: User can get in touch using the contact form on the contact page.
- **Event Page**: A full list of race events, split into pages with 6 events per page.
- **Event Search**: Users can search for specfic events.
- **Event Details**: Each race event has a details page showing the avaiable tickets and circuit map for each event.
- **Cart**: Users can add, view and adjust tickets in their cart.
- **Checkout**: Users can purchase tickets in there cart using the checkout app. If users are logged in the checkout form will be prefilled with existing information when avaiable.
- **Add/Edit/Delete Events**: Site managers can edit or delete existing race events aswell as being able to add new events.
- **Add/Edit/Delete Tickets**: Site managers can edit or delete existing tickets for each race event aswell as being able to add new tickets.
- **404 Page**: Provides users with a message if they have entered an incorrect URL or clicked an incorrect link, gives the user the option to return to the home page.

### Features Left to Implement


<span id="technologies"></span>

## Technologies Used


<span id="testing"></span>

## Testing

### Testing Tools

#### I used the following tools and devices to test the website in several different scenarios. 

- [Firefox Developer Tools](https://developer.mozilla.org/en-US/docs/Tools)
  - The project used **Firefox Developer Tools** to test responsiveness, styles, and different layouts throughout development. This also allowed the site to be tested on several other [mobile devices](https://developer.mozilla.org/en-US/docs/Tools/Responsive_Design_Mode).

##### Devices I Physically Tested With. 

- [Samsung Note 10+](https://en.wikipedia.org/wiki/Samsung_Galaxy_Note_10)
  - The project used a **Samsung Note 10+** to test the site on a mobile device.

- [HP Envy x360 13](https://www.amazon.co.uk/HP-13-ar0001na-Touch-Screen-Convertible-Laptop/dp/B07V3J1H3V)
  - The project used an **HP Envy x360 13** to test the site on both a 13-inch laptop and a tablet.

##### Devices Simulated With In Firefox Dev Tools. 

- [Samsung Galaxy S9/S9+](https://en.wikipedia.org/wiki/Samsung_Galaxy_S9)

- [iPhone 6/7/8](https://en.wikipedia.org/wiki/IPhone_6)

- [iPhone X](https://en.wikipedia.org/wiki/IPhone_X)

- [iPad](https://en.wikipedia.org/wiki/IPad)

I used the following web browsers on both desktop (Windows) and mobile (Android) where available.

- [Mozilla Firefox](https://www.mozilla.org/en-GB/)
  - Desktop Version: 76.0.1 Mobile Version: 75.0.0-beta.6

- [Google Chrome](https://www.google.com/chrome/)
  - Desktop Version: 81.0.4044.138 Mobile Version: 81.0.4044.138

- [Opera](https://www.opera.com/)
  - Desktop Version: 68.0.3618.99

- [Microsoft Edge](https://www.microsoft.com/en-us/edge)
  - Desktop Version: 44.18362.449.0

### User Story Tests


### All tests performed with no errors found.

### Issues Found During Testing


<span id="deployment"></span>

## Deployment

<span id="credits"></span>

## Credits

### Content
  - I followed [this tutorial](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html) to intergrate pagination into the project.

### Media



### Acknowledgements

- **Gerard McBride** for helping me through the project with his advice and guidance.  