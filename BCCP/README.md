# DL_Project >> ![image](https://github.com/Pratik-Salunkhe/DL_Project/assets/96179015/36a06a1a-e09f-4f90-84dd-66cb22c17a22)

![image](https://github.com/Pratik-Salunkhe/DL_Project/assets/96179015/71f93100-27a4-4345-9ec3-2c98bff01e75)

## PROBLEM STATEMENT :
  In hilly areas with curvy roads, going around sharp turns is a big safety challenge because these turns block the view, making it hard to see, and that raises the chance of accidents.

  ### Importance of Addressing Blind Corner Collisions

Timely intervention  (Acting quickly)  is really important to reduce the higher chance of accidents at spots where you can't see well around corners. This highlights the importance of creative solutions to make roads safer in hilly areas.

## OBJECTIVE :
  Our project aims to uses a CNN-based system to identify  the vehicles on the road, to prevent the collisions by classifying and alerting drivers about vehicles on-road in blind corners, thereby enhancing safety in challenging areas where we can’t see the vehicle ahead.

![image](https://github.com/Pratik-Salunkhe/DL_Project/assets/96179015/ff311954-6e37-4b70-bb2b-24adca6c3920)

![image](https://github.com/Pratik-Salunkhe/DL_Project/assets/96179015/c0b0ae05-de93-4cf1-8e11-16fe44705ef2)

### Data Collection 
      * Image Scraping : 
            Image scraping, a method of automatically extracting images from online sources, serves as a valuable technique for assembling such datasets.
      * Image Image Generator :
            An "image generator" in deep learning creates artificial images to expand and diversify training datasets, crucial for improving model performance in computer vision tasks like image classification and object detection. This tool enhances the dataset's variety, leading to better model generalization and effectiveness.
### Data Preprocessing
      * Image Resizing
      * Normalization
      * Data Augmentation
      * Label Encoding 
      * Splitting into Training and Validation Sets
      * Batch Processing
      * Data Shuffling
      * Handling Imbalanced Classes

### Model Training 
      * Training Process Description :
            The CNN undergoes a systematic training process where it learns to swiftly identify and classify vehicles based on the dataset. This ensures the model becomes adept at discerning on vehicles present on road and No vehicles Present on road, forming a crucial part of our collision prevention system.

### Model Evaluation & Tnning
      * Hyperparameter Tuning
      * Increasing Size of data

### Selecting Best Model 
![image](https://github.com/Pratik-Salunkhe/DL_Project/assets/96179015/ef0b153f-d006-426d-91c0-424eb0f07ee5)

### TESTING of Best 5 Model 
  Here similar to Ensemble Method i have used 5 best model and i am predicting the input from 5 models and depending on Majority of the class The prediction is done
![image](https://github.com/Pratik-Salunkhe/DL_Project/assets/96179015/d3ff5ea8-aab1-4ca8-a7d2-33453395ccee)

### Noise And Virtual Alerts

      * Methodology Description
            Imagine our system as a watchful guardian. When it spots a vehicle on-road nearing a blind corner, it quickly sends out a warning alert. It's like a digital lookout making sure drivers know about potential dangers ahead.
      * Noise and Visual Alerts Discussion
            To make sure drivers pay attention, our system uses two moves – loud noises and flashing lights. That the system will sounding an alarm and shining a light, ensuring drivers can't miss the warning even in the busiest and trickiest ghat areas.

### Benifits
      Our system acts as a digital guardian, reducing blind corner collisions and enhancing road safety in ghat areas by alerting drivers about hidden dangers.

### Challanges & Future work
      * Limitations Acknowledgment
            While our system is a powerful ally, we acknowledge the challenge of occasional false alerts and the need for continuous fine-tuning. Overcoming these limitations is crucial for ensuring the utmost reliability in blind corner collision prevention.

      * Future Enhancements Proposal
            Looking ahead, envision our system evolving into an even smarter protector. Future enhancements could include refining the classification accuracy, exploring advanced alert mechanisms, and integrating real-time traffic data for a more dynamic and effective blind corner collision prevention system.

### CONCLUSION

#### The innovative blind corner collision prevention system, driven by a Convolution Neural Network (CNN), stands as a formidable solution for ghat areas. By swiftly identifying and alerting drivers about on-road vehicles hidden in sharp turns, it significantly mitigates the risk of collisions. The combination of advanced technology and strategic deployment creates a promising avenue for reducing accidents and fostering secure journeys in ghat regions.







