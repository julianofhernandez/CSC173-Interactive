# CSC173-Interactive
Interactive design for CSC 173 with Dr Baynes

# Requirements
- [x] Preprocessing script @julian
  - Read the businesses.json file, parse it for all the businesses in Santa Barbara then output to a new JSON file. yelp_filtered_to_santa_barbara.json is (3840/150346) = 0.03% of the lines that were in yelp_academic_dataset_business.json. If you need the input file parsed better or changed let me know or if you are comfortable with python feel free to update ./yelpDatasetParser.py
- [ ] Currently locations are plotted using a static list, we need to load the data from yelp_filtered_to_santa_barbara.json so that everyone else can start their tasks. @Kenta

- [ ] 4 interactives ( include panning, zooming, brushing, details-on-demand (e.g., tooltips), dynamic query filters, and selecting different measures to display.)
  - [ ] Slider: Filter by stars (give the user a slider between 0 and 5 for stars) @Abdallah
  - [ ] Slider: Filter by total reviews (give the user a slider between 0 and the most reviewed restaurant) @Abdallah
  - [ ] Search: Add a text input box that is used to filter by name (for example let me compare all "Starbucks" locations) @Sam
  - [x] Zoom: Add zooming functionality @Julian
  
- [ ] Your chart must have at least 3 attributes. Attributes: 
  - [ ] Size will be number of reviews @Kenta
  - [ ] Color will be average rating @Sam
  - [x] Latitude and longitude for x and y and basemap coordinates @Julian

 - [ ] Write up @Julian
  - A rationale for your design decisions. How did you choose your particular visual encodings and interaction techniques? What alternatives did you consider and how did you arrive at your ultimate choices?
  
  
  
  - An overview of your development process. Describe how the work was split among the team members. Include a commentary on the development process, including answers to the following questions: Roughly how much time did you spend developing your application (in people-hours)? What aspects took the most time?

Julian 6h for setting up base layer and coordinate translation.


# Setup

We will be using VSCode for running this project. First install Live Server using the extensions menu.

![image](https://user-images.githubusercontent.com/39971693/199818995-d84bfa44-e474-4a0e-a5e8-15cd93e22698.png)

Then right click test-map.html and Open With Live Server.

![image](https://user-images.githubusercontent.com/39971693/199819047-b473269a-d26f-4428-8123-84c70a8fb964.png)
 
 This will then open your browser and should be running the visualization.
 
![image](https://user-images.githubusercontent.com/39971693/200206211-94389134-208c-4e0f-954d-0b129a074a7d.png)

