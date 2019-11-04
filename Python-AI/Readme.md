# Python + AI
This repo contains how to run image classification example using Microsoft cognitive services  and Python. 


## Prerequiste
- Python 3.7
- Microsoft Azure Subscription
- pip install azure-cognitiveservices-vision-customvision

## Hands on

1. If you don't have Azure subscription then create [Azure trial account](https://azure.microsoft.com/en-us/free/?wt.mc_id=AID2463800_QSG_SCL_361865&ocid=AID2463800_QSG_SCL_361865&utm_medium=Owned%20%26%20Operated&utm_campaign=FY20_APAC_Dev%20Community_CFT_Internal%20Social)

2. Clone a repo using below command on your disk

  ```
  git clone https://github.com/apacdevpmmresources/NewZealand.git
  ```

3. Open [Custom Vision](https://www.customvision.ai/) in a browser
 ![SignIn](/Python-AI/HandsOnImages/0.png)


4. Sign in with the account you used for seeting up Azure Subscription


5. Click **NEW PROJECT**

![NewProject](/Python-AI/HandsOnImages/1.png)

6. On the screen **Ceate new project** provide Name, Description (optional) 
![CreateNewProject](/Python-AI/HandsOnImages/2.png)

7. On **Resource** drop down menu, if no value is there then click **create new**

8. On **Create New Resource** provide Name, Subscription, Resource Group (create new resource group if you want), Kind, Location, Pricing Tier
![CreateNewResource](/Python-AI/HandsOnImages/3-0.png)

9.  For creating a new Resource Group (click new for Resource Group as mentioned above), provide Name and Location 
![CreateNewResourceGroup](/Python-AI/HandsOnImages/3-1.png)

10. Once all the information provided click **Create resource**
![CreateNewResourceGroup](/Python-AI/HandsOnImages/4.png)

11. Once resources got created, select **Project Types**, **Classification Types**, **Domains** and click **Create Project**
![CreateProject](/Python-AI/HandsOnImages/5.png)

12. Once project creation done, Click **Add images**
![AddImages](/Python-AI/HandsOnImages/6.png)

13. In open window, navigate to the folder where all the images were stored (let's upload images from axes folder). Select All images and click **Open**
![uploadImages](/Python-AI/HandsOnImages/7.png)

14. Provide **My Tags** and click **Upload 79 files**
![TagImages](/Python-AI/HandsOnImages/8.png)

![TagImages1](/Python-AI/HandsOnImages/8-1.png)


15. Click **Done** once all files were uploaded
![TagImages1](/Python-AI/HandsOnImages/8-2.png)

16. Now you can see the images and it's tag
![TagImages2](/Python-AI/HandsOnImages/9.png)

17. Repeat step 12-16 for other images. Once images taged and uploaded is done it will show all the tags and associated picture
![AllTags](/Python-AI/HandsOnImages/10.png)

18. Click **Train** 
![Training](/Python-AI/HandsOnImages/11.png)

19. On **Choose Training Type** select **Quick Training** and click **Train**
![Training](/Python-AI/HandsOnImages/12.png)

20. Wait while training is in process
![Training1](/Python-AI/HandsOnImages/13.png)

21. Once training is completed, click **Publish**
![Publish](/Python-AI/HandsOnImages/14.png)

22. On **Publish Model** screen, provide **Model name** and **Prediction resource** and click **Publish**
![Publish1](/Python-AI/HandsOnImages/15.png)

23. Let's do a quick test. Click **Predictions** 
![Publish2](/Python-AI/HandsOnImages/16.png)

24. Click **Quick Test**
![Publish2](/Python-AI/HandsOnImages/17.png)

25. Provide [this link](https://www.sportforaction.com/wp-content/uploads/2017/08/Ski-Helmet-Ultralight-Sking-Helmet-CE-Certification-Snow-Ski-Skateboard-Snowboard-Helmet-55-61CM.jpg) in **Image URL** and click -> 
![QuickTest](/Python-AI/HandsOnImages/18.png)

26. Let's copy values for the following variables
    Endpoint
    projectid
    publishiterationname
    prediction_key
    
27. Click settings and copy **Project Id** and **Endpoint**
![CopyValue](/Python-AI/HandsOnImages/19.png)

28. Click **Performance** copy **Published as** 
 ![CopyValue1](/Python-AI/HandsOnImages/20.png)

29. Click **Prediction URL** and copy **Prediction-Key**
![CopyValue2](/Python-AI/HandsOnImages/21.png) 

30. Open **pythonAI.py** file

31. Paste values we copied in previous steps and change the location of test image. 
![PasteValue](/Python-AI/HandsOnImages/22.png)

32. Run python code and watch output
![Output](/Python-AI/HandsOnImages/23.png)


# End of Hands on Lab !!!