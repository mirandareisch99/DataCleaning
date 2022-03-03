# DataCleaning
Used to extract data from postgres, transcribe audio, and clean data
I am unable to share the machine learning code, as it is private through the institution, however this is some of the datapreprocessing code that I used. 
The data was collected through an android mobile application which I helped format in Java (not included due to institution). 
The data was collected in a Postgres database which I conneted to through SQL. I extracted the encoded audio recordings and converted them to wav files. 
Then I extracted transcripts from the wav files, as we used both audio and transcripts in a combined audio/text machine learning algorithm. 
Next I cleaned the data and extracted the PHQ-9 (Depression) and GAD-7 (Anxiety) scores as recorded from the participants in the mobile application. 
Finally, I performed train/test splits with upsampling. 

This data was then transferred into the machine learning models. Results were inputted into a .db file which I extracted into a csv for analytics. 
