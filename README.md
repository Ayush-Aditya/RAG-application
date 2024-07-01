# RAG-application
This repository contains code for a rag application that can be used for summarization and information retrieval from research papers.  

Working:-
1. The data.py file is responsible for searching research papers by author name, title, and date in the arXiv archive. 

:arXiv by Cornell University
 is a free distribution service and an open-access archive for nearly 2.4 million scholarly articles in the fields of physics, mathematics, computer science, quantitative biology, quantitative finance, statistics, electrical engineering and systems science, and economics. Materials on this site are not peer-reviewed by arXiv.

- the provided code searches the archive and downloads the research paper in a specific location which serves as the data-source for the rag application to generate context.
![Screenshot 2024-07-01 193223](https://github.com/Ayush-Aditya/RAG-application/assets/162690292/25d19fab-c930-4497-b701-f323db75039b)
![Screenshot 2024-07-01 193237](https://github.com/Ayush-Aditya/RAG-application/assets/162690292/4381f547-82a3-4ad8-8815-fa3aeac63703)



  2. The rag application is built using pathway (Python ETL framework for stream processing, real-time analytics, RAG, and LLM pipelines)[(present in app.py)]
     It is capable of gathering context from a local data source and passing it to an LLM to generate responses. In our case, we can ask it to summarize the paper or retrieve some 
      from the papers.


3. The final component of the system was  to build a Streamlit UI for running various scripts and apply some pre-built contexts and commands to summarization and question answering, integrating the whole logic of all the components. Unfortunately, due to time constraints and other reasons, I am unable to complete the UI for the application now but I will surely update the repo with the UI in the future.



Points to remember:-
-pathway is not available for Windows as of now you will have to use docker to run pathway and build the application.
-since I was unable to complete the UI as of now the rag application is static in nature.
-to use docker and pathway please refer to the official documentation

Here are some links that might help :-
https://pathway.com/developers/user-guide/deployment/docker-deployment/#using-the-pathway-image
https://pathway.com/
https://docs.docker.com/manuals/

End Note:
I would like  to thank Pathway and the mentors there for giving us knowledge about RAG, LLM, word embeddings and prompt engineering through their various initiatives like live tutorials, learning resources and various other means, and for providing help in building this application.




Thank you 
