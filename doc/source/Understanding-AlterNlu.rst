###############################
Understanding Alter NLU Console
###############################

=======
Intents
=======

Intents are what you expect users to say and what are their intentions. It depicts the gist of the expression that the user says or in simple terms what the user probably meant to say.

For Example :

		If the user types : 
		*I want to buy apple mobile worth 60k*
		
		Here the user intent to buy the specified product with the mentioned specifications. We can infer the intent of the user query as "search-product", which is a user-defined term.

There can be 2 varieties of intents:

	-	First, which do not contain any entities (explained below), but are simple and direct queries. For example “greet”, "exit" and other light conversational intents :: 
									
			“Hey there” or  “Hi”.
									
	-	Second, which can contain multiple or single entities in the training query which we want to extract from the user query as demonstrated in the image below:

		.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/intent-mapping.png   

========
Entities
========

Entities describe the piece of information you would want to extract from the expressions/messages of the user. 

Entities can consist of single or multiple words. For example "mobile" and "mobile cover" are 2 different entities.

Like in the image above, the "price", "product-type" and "brand" are the 3 entities in our Alter NLU console that will be tagged to their respective “Reference Value“ and “Synonyms“ values.

		.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/syn-1.png   

**Reference Value**

It is the convenient representation of the whole set of synonyms (explained below). It can be in the form of a ``unique_id``, ``abbreviations``, ``initials``, ``shortforms``, etc. according to the developers’ convenience.  

For example, in the last synonym set "Dolce & Gabbana" in the image above is conveniently referred as "D_G".

**Synonyms**

It is a set of words or phrases having similar meaning, mapped against each reference value.

**Selected Value**

It is the part of the sentence we highlight to tag against a particular entity. Each "Selected Value" in the Alter NLU console has a different color code based on the entity tagged.

=======
Reports
=======

Chatbot training is an ongoing process that should get better at every successive stage. With each improvement, the trainer/developer should have a clearer understanding of the changes made. 

	*The section provides NLP-based real-time ‘Reports’, where we list out the health of the training dataset created by the user, alert if there are issues and recommend ways to make it better.*

Here are the list of items that get covered under Reports:

	-	**Intent Distribution:**
		It represents that number of intents created and the numerical proportions for the number of relevant sentences present in each of the intents and their respective percentages.

		.. note::
		   The relevant sentences are those that contribute to building better a NLU model.

		
		.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/intent-distribution-1.png   


	-	**Figuring out the intents that require more training sentences:**
		It reports the specific intents that have less number of training sentences than the threshold set i.e 3 relevant sentence per intent. Also, it notifies the user with the name of the intents lacking enough training queries in comparison to the other intents in the bot.
		
			.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/report-1.png   

	-	**Examining the training dataset to extract the untagged entities:**
		Lists out keywords which have been tagged with an entity in intent but, the same keyword is untagged in the training sentence of another intent.
		It also notifies the user that they might have skipped tagging the keyword as an entity in the other intent mentioned.

			.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/untagged-entities.png   

	-	**Listing out the limitations in the entity section:**
		It reports about the name of the entities that have been defined but have not been used by the user to form training queries in the intent section. It also reports when the user might have mistakenly deleted the entity from the intent section but forgotten to delete the same from the entity section

	-	**Capturing repetition of training sentence:**
		It informs about the training sentence(s) that the user might have added in multiple intents by mistake. The console alerts this to the user with an error message at the top of the reports section.

			.. image:: https://s3-ap-southeast-1.amazonaws.com/kontikilabs.com/alter-nlu-readthedocs/report-2.png   

		.. note::
		   For good results, the console requires a minimum of 3 relevant training queries per intent. Also, Alter NLU console needs only a single synonym tagged for each entity reference value in training queries of the intent section.
		   So, all you need to do is add 1 training query in the intent section containing any one of the synonyms per reference value and your bot is good to go.

		   For instance, we need to train for 1 user query containing synonym for "D_G" reference value, like -
		   *I want a Dolce & Gabbana bag*
		   and rest will be handled automatically.	


