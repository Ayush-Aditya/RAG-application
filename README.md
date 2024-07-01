# RAG-application
This repository contains code for a rag application that can be used for summarization and information retrieval from research papers.  

End User

Researchers and Academics: Individuals who need to quickly grasp the essence of numerous research papers without reading them in full.
Students: Those who need to understand and answer questions about specific topics in their studies.
Industry Professionals: Professionals who need to stay updated with the latest research and advancements in their field.
Librarians and Information Specialists: People responsible for managing and disseminating research information.
General Public: Individuals with a keen interest in specific research areas.


Industry Impact


Increased Efficiency: By summarizing research papers, your application can significantly reduce the time researchers and professionals spend on literature review, allowing them to focus more on their actual research and work.
Enhanced Knowledge Dissemination: It helps in spreading advanced research knowledge more widely and quickly, enabling faster implementation of new findings.
Educational Advancement: Supports educational institutions by providing a tool that helps students and educators easily access and understand complex research materials.
Innovation Acceleration: Facilitates quicker access to relevant information, which can accelerate innovation and development in various fields.
Interdisciplinary Collaboration: Makes it easier for experts from different fields to understand each other's work, fostering interdisciplinary research and collaboration.

Business Value


Cost Savings: Reduces the time and effort required for extensive literature reviews, leading to cost savings for research institutions and companies.
Competitive Advantage: Organizations can stay ahead of the competition by quickly accessing the latest research and developments in their field.
Improved Decision Making: Provides valuable insights and answers to specific questions, aiding in more informed decision-making processes.
Scalability: The application can handle a vast amount of research papers, making it scalable for large organizations and institutions.
Revenue Generation: Potential to monetize the application through subscription models, pay-per-use, or by offering it as a premium service.



Working:-
1. The data.py file is responsible for searching research papers by author name, title, and date in the arXiv archive. 

:arXiv by Cornell University
 is a free distribution service and an open-access archive for nearly 2.4 million scholarly articles in the fields of physics, mathematics, computer science, quantitative biology, quantitative finance, statistics, electrical engineering and systems science, and economics. Materials on this site are not peer-reviewed by arXiv.

- the provided code searches the archive and downloads the research paper in a specific location which serves as the data-source for the rag application to generate context.
![Screenshot 2024-07-01 193223](https://github.com/Ayush-Aditya/RAG-application/assets/162690292/25d19fab-c930-4497-b701-f323db75039b)


![Screenshot 2024-07-01 193237](https://github.com/Ayush-Aditya/RAG-application/assets/162690292/4381f547-82a3-4ad8-8815-fa3aeac63703)



  2. The rag application is built using pathway (Python ETL framework for stream processing, real-time analytics, RAG, and LLM pipelines).
   [(present in app.py)]
     It is capable of gathering context from a local data source and passing it to an LLM to generate responses. In our case, we can ask it to summarize the paper or retrieve some information  from the papers. The storage folder in the repo is to highlight this functionality, that the papers will be present in the storage for the application to function.  Please provide some logic to convert the pdf into the suitable file format and structure the code uses.
     


3. The final component of the system was  to build a Streamlit UI for running various scripts and apply some pre-built contexts and commands for summarization and question answering, integrating the whole logic of all the components. Unfortunately, due to time constraints and other reasons, I am unable to complete the UI for the application now but I will surely update the repo with the UI in the future.



Points to remember:-
-pathway is not available for Windows as of now you will have to use docker to run pathway and build the application.
-since I was unable to complete the UI as of now the rag application is static in nature.
-to use docker and pathway please refer to the official documentation

Here are some links that might help :-
-https://pathway.com/developers/user-guide/deployment/docker-deployment/#using-the-pathway-image

-https://pathway.com/

-https://docs.docker.com/manuals/

End Note:
I would like  to thank Pathway and the mentors there for giving us knowledge about RAG, LLM, word embeddings and prompt engineering through their various initiatives like live tutorials, learning resources and various other means, and for providing help in building this application.




Thank you 
