#!/usr/bin/env python
# coding: utf-8

# In[11]:


get_ipython().system('pip3 install textblob')


# # Sentiment Analysis Using Textblob Basic

# In[1]:


from textblob import TextBlob


# In[2]:


Feedback1 = "The food at Radison was awesome"
Feedback2 = "The food at Radison was very good"
Feedback3 = "The food at Radison was bad"
blob1 = TextBlob(Feedback1)
blob2 = TextBlob(Feedback2)
blob3 = TextBlob(Feedback3)
print(blob1.sentiment)
print(blob2.sentiment)
print(blob3.sentiment)


# # Spell Checker

# In[4]:


blob1.correct()


# In[6]:


argho = '''I hate wet and reiny days. It rainned a lot in 1816.... a lot - like everyday; the weaather in Europee was 
abnormally wet because it rained in Swiitzerland on 130 out of the 183 days from Appril to September. If I was Mary 
Shelley I might decide to write a book too. Afterall, it was the onnly thing you could do without TV or anything. She 
said that she "passed the summer of 1816 in the environs of Geneva...we occasionally amused ourselves with some German 
stories of ghosts... These tales excited in us a playful desire of imitation"  So, people were stuck inside and bored. 
Mary Shelley decided to write a book becuase it was so awful outside. I can totally see her point, you know? I guess I 
would write a novel if there was nothing else to do.'''


# In[7]:


blob = TextBlob(argho)


# In[9]:


blob.correct()


# # Upper Case and Lower Case

# In[10]:


correctedtext = blob.correct()
correctedtext


# In[15]:


correctedtext.upper()


# In[16]:


correctedtext.lower()


# # Polarity -- Range[-1, 1]
# ## Where 1 means positive statement and -1 means a negative statement

# In[18]:


correctedtext.polarity


# # Subjectivity refers that mostly it is a public opinion
# ## An explanatory article which must be analysed in context
# 

# In[19]:


correctedtext.subjectivity


# # Sentences from text seperated

# In[20]:


print(correctedtext.sentences)


# # Get the list of words 

# In[21]:


print(correctedtext.words)


# # Get the word count

# In[23]:


print(correctedtext.word_counts)


# # Get the Part of Speech tags for the text

# In[24]:


print(correctedtext.tags)


# 1. CC Coordinating conjunction
# 2. CD Cardinal number
# 3. DT Determiner
# 4. EX Existential there
# 5. FW Foreign word
# 6. IN Preposition or subordinating conjunction
# 7. JJ Adjective
# 8. JJR Adjective, comparative
# 9. JJS Adjective, superlative
# 10. LS List item marker
# 11. MD Modal
# 12. NN Noun, singular or mass
# 13. NNS Noun, plural
# 14. NNP Proper noun, singular
# 15. NNPS Proper noun, plural
# 16. PDT Predeterminer
# 17. POS Possessive ending
# 18. PRP Personal pronoun
# 19. PRPS Possessive pronoun
# 20. RB Adverb
# 21. RBR Adverb, comparative
# 22. RBS Adverb, superlative 
# 23. RP Particle
# 24. SYM Symbol
# 25. TO to
# 26. UH Interjection
# 27. VB Verb, base form
# 28. VBD Verb, past tense
# 29. VBG Verb, gerund or present participle
# 30. VBN Verb, past participle
# 31. VBP Verb, non3rd person singular present
# 32. VBZ Verb, 3rd person singular present
# 33. WDT Whdeterminer
# 34. WP Whpronoun
# 35. PS Possessive whpronoun
# 36. WRB Whadverb

# In[ ]:




