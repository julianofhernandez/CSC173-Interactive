# CSC173-Interactive
Interactive design for CSC 173 with Dr Baynes

# Requirements
- [x] Preprocessing DONE
  - Read the businesses.json file, parse it for all the businesses in Santa Barbara then output to a new JSON file. yelp_filtered_to_santa_barbara.json is (3840/150346) = 0.03% of the lines that were in yelp_academic_dataset_business.json
 
- [ ] 4 interactives ( include panning, zooming, brushing, details-on-demand (e.g., tooltips), dynamic query filters, and selecting different measures to display.)
  - [ ] Filter by business type (category)
  - [ ] Select an item and see more details (show all underlying JSON)
  - [ ] Group by - I'm not sure how to implement this but we could combine chains, for example show all 'starbucks' locations as one item, the problem here is which coordinates do you use if you are combining say 10 locations.
  - [ ] Interaction technique???
  
- [ ] Your chart must have at least 3 attributes. Attributes: size will be number of reviews, color will be average rating, and latitude and longitude for x and y.

 - [ ] Write up
  - A rationale for your design decisions. How did you choose your particular visual encodings and interaction techniques? What alternatives did you consider and how did you arrive at your ultimate choices?
  - An overview of your development process. Describe how the work was split among the team members. Include a commentary on the development process, including answers to the following questions: Roughly how much time did you spend developing your application (in people-hours)? What aspects took the most time?

# Setup

We will be using VSCode for running this project. First install Live Server using the extensions menu.

![image](https://user-images.githubusercontent.com/39971693/199818995-d84bfa44-e474-4a0e-a5e8-15cd93e22698.png)

Then right click index.html and Open With Live Server.

![image](https://user-images.githubusercontent.com/39971693/199819047-b473269a-d26f-4428-8123-84c70a8fb964.png)
 
 This will then open your browser and should be running the visualization.
 
 ![image](https://user-images.githubusercontent.com/39971693/199819201-58fd420c-65b3-46e4-bf13-2c29f0f961e2.png)
