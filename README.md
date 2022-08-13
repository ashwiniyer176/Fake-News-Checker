# Fake News Identification

The goal is to build a Machine Learning model that can classify a given news headline as real or fake. To achieve the task, we will be using a few popular news datasets as well as scraping data from sites for fake news(if the need arises). The first step to solving the problem is the creation of a dataset containing headlines and their respective class labels
## Datasets

1. **[Fake and real news dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset):** This is a collection of both fake and real news articles with features like **title**, **text**,**subject** and **date**. 
<br>

Files: `./data/sources/Fake (2).csv` and `./data/sources/True.csv`
<br>

2. **[Getting Real about Fake News](https://www.kaggle.com/mrisdal/fake-news):** This dataset is only a first step in understanding and tackling this problem. It contains text and metadata scraped from 244 websites tagged as "bullshit" by the BS Detector Chrome Extension by Daniel Sieradski. This is a combination of fake news and conspiracy theories (which by default are still fake).
<br>

Files: `./data/sources/fake.csv`
<br>

3. **[Fake News](https://www.kaggle.com/hassanamin/textdb3):** A binary classification dataset for both fake and real news articles. 
<br>

Files: `./data/sources/fake_or_real_news.csv`
<br>

4. **[Source based Fake News Classification](https://www.kaggle.com/ruchi798/source-based-news-classification):** A binary classification dataset for both fake and real news posts from social media. In an era where fake WhatsApp forwards and Tweets are capable of influencing naive minds, tools and knowledge have to be put to practical use in not only mitigating the spread of misinformation but also to inform people about the type of news they consume.  
<br>

Files: `./data/sources/news_articles.csv`
<br>

5. **[AG News Classification Dataset](https://www.kaggle.com/amananandrai/ag-news-classification-dataset):** AG is a collection of more than 1 million news articles. News articles have been gathered from more than 2000 news sources by ComeToMyHead in more than 1 year of activity. ComeToMyHead is an academic news search engine which has been running since July, 2004. The dataset is provided by the academic comunity for research purposes in data mining. The AG's news topic classification dataset is constructed by choosing 4 largest classes from the original corpus.
<br>

Files: `./data/sources/News Classification train.csv` and `./data/sources/News Classification test.csv`
<br>

The final dataset created for our prupose of News Classification is saved in `./data/TARP_Project_Final_Dataset.zip`. The dataset thus created was an approximately balanced one with very few null values.active



<!-- ## Model(s) Used

This needs to be a description of the model used and a brief overview of how it works in theory (e.g taken of a CNN Model): 

The network architecture used was a basic CNN model, with Max Pooling and ReLU Activation functions. Input images are resized to an optimal size and then fed into the **Convolutional layer**. These images are converted to their pixel values, which can be imagined as a three-dimensional matrix for the purpose of visualization. The **Convolutional layer** has a kernel. This kernel is generally a small matrix of specified kernel size mxnx3 (3 for RGB images). 
<br>

**Rectified Linear Unit (ReLU)** is the activation layer used in CNNs.The activation function is applied to increase non-linearity in the CNN. Images are made of different objects that are not linear to each other.


**Max Pooling:** A limitation of the feature map output of Convolutional Layers is that they record the precise position of features in the input. This means that small movements in the position of the feature in the input image will result in a different feature map. This can happen with re-cropping, rotation, shifting, and other minor changes to the input image. A common approach to addressing this problem from signal processing is called down sampling. This is where a lower resolution version of an input signal is created that still contains the large or important structural elements, without the fine detail that may not be as useful to the task.

## Future Work
Good ideas or strategies that you were not able to implement which you think can help  improve performance. -->


## Running The Application
As of now we do not have an application but an example flask application 

it is based on the modular structure to serve as an example of the same..

It can be launched by first init the VirtualEnv and then running the run.py in the home folder

for linux/mac
```
source ./env/bin/activate
```
For Windows with Python 3.7
```
pip install -r requirements.txt
set FLASK_APP=run.py
set FLAKS_DEBUG=1
flask run
```

The App folder contains all the information regarding the server
