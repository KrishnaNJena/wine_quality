Step 1: Created Environment : 

        conda create -n winequality python=3.7 -y


Step 2: Activate Environment : 


        activate winequality


Step 3: Created requirements.txt file


Step 4: Install requirements.txt file :

         pip install -r requirements.txt


Step 5: Download Wine Quality Check Dataset


Step 6: 

        git init 


Step 7: 

        dvc init


Step 8: 

        dvc add data_given/winequality.csv


Step 9: 
        
        git add .


Step 10: 

        git commit -m "first commit"


Step 11: push an existing repository from the command line

        git remote add origin https://github.com/krishna9753/simple-dvc-demo.git
        git branch -M main
        git push origin main


Step 12: tox command

        for rebuilding : tox -r 

Step 13: Pytest Command
        
        pytest -v 

Step 14: Setup commands: 

        pip install -e .

Step 15: Build your own package commands:

         python setup.py sdist bdist # Send distribution & build the distribution



