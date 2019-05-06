##############################
Building an E-commerce Chatbot
##############################

The console is developed to handle multiple chatbot datasets within a single user login i.e you can add training data for any number of chatbots.

Start by creating your account from our `Alter NLU console <https://console.kontikilabs.com>`_

	.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/main-page.png   

Upon clicking the ‘Sign Up’ button, an e-mail is sent to the ID you provide above. You can log in on the console once you verify your identity via the e-mail.

You can also register and login using social sites credentials of your Facebook or Google account.

Below in the documnet are the steps that will guide you in building your training dataset.

================
Creating Dataset
================

Upon successful login, you will be redirected to the "Create Dataset" page.

	.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/create-dataset.png   

Get started by creating a new dataset, which requires a ``bot name`` and the ``industry/vertical`` that your bot belongs to. Here, we are going to name our bot as - "ecomm-bot" and the domain will be "E-commerce".
Once you click on the "Add" button, the dataset gets created and you will be redirected to "Intent Page".

=======================================================
Building no Keyword Intents (Intents with no Entities):
=======================================================

The intents like “greet” and “exit” are the generic intents every bot should handle. Besides these intents, build other intents you plan to include in your chatbot. Like, I have included “ongoing_offers”. Follow the steps below to create the “ongoing_offers” intent :

-	Create an intent using the “ADD INTENT” option.
-	Next, in "Add New Training Phrase" text area write simple user queries asking about the current sales, vouchers in our e-commerce chatbot. Example - ‘any offers?’, ‘do you have any voucher’, etc.
-	Save the “ongoing_offers” intent using the “SAVE” button on the top right corner. 

This intent will hold all the user queries asking about the current sales, vouchers in our e-commerce chatbot.

	.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/ongoing-offers.png   

Remember to train the dataset with expressions that contain words like sales, vouchers, etc. This is because words will keep the “ongoing_offers” intent unique from other non-keyword intents.

=================
Building Entities
=================

The e-commerce chatbot should be trained to handle queries like:

User says : I want to buy **apple** **mobile** worth **60K**.

So, I plan to create 3 entities that will extract the:
	-	brand
	-	product-type and
	-	price

from the user query.

-	Create an entity "brand" by using the “ADD ENTITY” option.
-	The "brand" entity will contain "Reference Value” as the main brand name (like apple) as well as synonyms that the user may refer to a particular brand that your chatbot endorses.

	.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/brand-entity.png   

-	Similarly create other entities, add the ‘Reference Value’ and its synonyms. Like a user can write ‘loui vuitton’ (our Reference Value) as ‘lv’ or ‘Louis Vuitton’ (the synonymns for ‘loui vuitton').

	.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/lv.png   

-	Similarly, create values and synonyms for the other fields and finally, save your dataset.

==============================
Building Intents with Entities
==============================

For queries as stated in the above section, dataset should have an intent that stores all possible user queries from which the bot should be extracting the entities.

Create an intent with the name "search-product" and go to the training phrase section of the intent and start writing the expected user queries. 

For instance, “I want to buy **apple** **mobile** worth **60K**”. From this text, tag the information you want to extract and work upon.

	.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/intent-with-entities.png   


For the ease of developers, we have built the console in a manner that each ‘Selected Value’ in the intent section can be linked to a ‘Reference Value’ of your choice.

Like in the images below, you can see in the intent section:

*Selected Value : 60k, 2k both have same ‘Reference Value’ i.e price-range*

	.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/ref-value-example.png   

*In the entity section, every price-range example is defined in the same “Reference Value”*

	.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/price-range.png   

.. note::
	If you change the ‘Reference Value’ in the entity section, the same will be reflected dynamically in the intent section and vice versa.

======================================================
Analysing Loopholes in the dataset: The Report Section
======================================================

Once you are done building the dataset, move to the Report Section which will analyse your dataset for all intents and entities in real-time and notify the errors and warnings that need to be addressed for the accuracy of the chatbot’s response.

Click on the tool tip icon next to each of the section title for recommendations. Below listed are the key functions that form the Report:

-  Illustrating Intent Distribution in the form of a pie chart.
-  Analysing the Training Data Required by intents and entities to achieve accuracy.
-  Pointing out Possibly Untagged Entities to inform about keywords that have been tagged as an entity in the intent, but the same keyword occurs untagged in the training sentence of another intent.
-  Intent - Sentence conflicts table alerts about the training sentence(s) you may have added in multiple intents by mistake.
-  Handling training bias by highlighting the name of intents lacking enough training expressions when compared with other intents.

Once you have rectified all the errors, you will be able to download the dataset JSON in both — the Alter NLU or the RASA format.

.. note::
	If you are using RASA NLU, you can quickly create the dataset using Alter NLU Console and Download it in RASA NLU format. We have updated our console for hassle-free data creation that is less prone to mistakes.

==============
Build Your Bot
==============
Go to Git Repository from the link below:

`https://github.com/Kontikilabs/alter-nlu/tree/v1.0.0-beta <https://github.com/Kontikilabs/alter-nlu/tree/v1.0.0-beta>`_

Next, go through the README.MD file and start executing the steps as mentioned.










