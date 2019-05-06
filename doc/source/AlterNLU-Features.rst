################################################
Alter NLU Console Features and Data Manipulation  
################################################

================================================
Interactive UI to Build and Manage Training Data
================================================

	.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/alter-nlu-ui.gif   
	   :align: center

**Intent : Create, Modify, Delete intent and intent queries.**

We give filter functionalities for intent names and intent-specific training sentences to help the user modify the data quickly. We also have a search functionality that enables users to filter out the list.

For user convenience, we allow drop down search for both "Selected Value" and "Reference Value".

	.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/search-1.png   


**Entity : Create, Modify, Delete entity and entity-specific reference value and synonyms.**

We give filter functionalities for entity name, reference value and entity-specific synonyms to help the user modify the data quickly.

	.. note::
		Whenever an entity is tagged in the sentence, it is automatically mapped in the synonyms of the corresponding reference value.

		Also, if you change the ‘Reference Value’ in the entity section the same will be reflected dynamically in the intent section, and vice versa.

==========================================================
Get Real-Time Report of Training Data if There’s Any Issue
==========================================================

A dedicated reports page which gives you the insights of all the warnings and errors that might affect the training of the bot or make it perform less efficiently.

-	Presenting Intent Distribution in the form of a pie chart
-	Figuring out the intents that require more training sentences
-	Listing out the limitations in the entity section
-	Examining the training dataset to extract untagged entities
-	Capturing repetition of training sentence

=================================================================
Download the Training Dataset in 2 Formats - Alter NLU & RASA NLU
=================================================================

The download button will get activated only when user meets the below threshold requirements -

1. Each intent must contain at least 3 relevant training sentences.
2. Each entity reference value must have at least one of the synonyms tagged in any one of the intents' training sentences.
3. There should never be multiple intents containing same training sentence(s).
4. The number of total intents must be at least 2 to allow downloading of training data.

Once you have rectified all the errors, you will be able to download the dataset JSON in both — the Alter NLU and the RASA format.

	.. note::
		If you are using RASA NLU, you can quickly create the dataset using Alter NLU Console and Download it in RASA NLU format. We have updated our console for hassle free data creation which is less prone to mistakes.

	.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/download-format.png   

=================
Data Manipulation
=================

To maintain the dataset standards, we apply dynamic algorithms to perform data manipulation efficiently. Below is an example that illustrates how we are manipulating your training data for better accuracy.

	.. note::
		Any modification made in the entity section is altered dynamically in the sentences of the intent section and vice versa.

Let us suppose - an entity "brand" which has the below data:

	.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/brand-synonyms.png   

From the image above we can make out that Reference Value i.e "lenovo" has synonyms - ``["inspiron", "thinkpad"]`` etc, while the other entry is "dell" which holds ``["vostro", "chromebook"]`` etc as synonyms.

Now, in the intent section, I train for the phrase - "I want an Inspiron". And for other similar phrases, I tag the word "Inspiron" with "lenovo" reference value. 

	.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/example-1.png   


Later, while examining my created entities, I realize that I have added "Inspiron", which is a variant of "dell" to "lenovo". Therefore, from the entity section I delete the synonym "Inspiron" from "lenovo" and add it to "dell" reference value. 
Now, our code dynamically judges the modification made and update the "Reference Value" to "dell" in all the sentences present in the intent section.



