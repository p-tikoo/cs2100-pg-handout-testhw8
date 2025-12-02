# SUMMARY

## Output from running the application

What is the target keyword that you used when running your program in Part 4?
effervescence

Please paste the final output of the sorted keywords here:
Carbonation, Carbon_dioxide, Champagne, Effervescence, Soft_drink, Sparkling_wine

## Stakeholder-value matrix

In this assignment, you scraped Wikipedia, and limited yourself to webpages in Wikipedia.
But, there exist many databases of webpages scraped from the internet at large, not 
limited to Wikipedia. Some of these webpages include personal information, harmful or 
unpleasant content, misinformation, etc.

### Question 1: robots.txt

Search online for a file called robots.txt. What is the intention of this file? Is it enforced?

The robots.txt file is a text file placed in the root directory of a website hat provides instructions to web crawlers and bots about which parts of the site they are allowed to access. robots.txt is NOT legally enforced. 
### Question 2: Stakeholder-value matrix

Please create a stakeholder-value matrix for a product which requires scraping the 
internet at large. Please include at least five stakeholders and at least five values.
Assume that the scraped data is being used for a product for users, such as a generative AI model.

It is recommended (but not required) that one of the stakeholders be bloggers from more
than ten years ago, and that one of the values is avoiding intellectual property theft.
It will help you with the next question.

stakeholder                   Avoiding IP Theft      Privacy Protection      Content Quality    Accessibility   Transparency
Bloggers from 10+ years ago - High, medium, medium, low, high 
content creators - very high, medium, high, medium, high
website owners - medium, high, medium, medium, medium
Marginalized Communities - medium, very high, high, medium, high
### Question 3: A conflict in the stakeholder-value matrix

Some people created online content a while ago, during a time when large generative
models were not a huge part of everyday life. What are some situations when the value of
avoiding intellectual property theft is de-prioritized for these stakeholders, in favor
of building the end product? For example, if the end product is a model that generates images,
what is a scenario in which these stakeholders' intellectual property rights are de-prioritized?

A scenario of this is when rather than asking permission (opt-in), companies scrape everything and offer opt-out mechanisms later. By the time creators learn their work was used, the model is already trained
For example, a writer discovers years later that their short stories from 2010 were used to train GPT, but the damage is done
### Question 4: Other conflicts in the stakeholder-value matrix

Identify at least two other conflicts that arise from the stakeholder-value matrix. For each
conflict, discuss possible mitigations.

Conflict 1: Privacy Protection vs. Accessibility
Possible mitigations:
Federated learning: Train models on user devices without centralizing data
Tiered access: Offer basic functionality with minimal data collection, premium features with explicit consent
Transparent trade-offs: Clearly explain to users what data is needed and why, giving informed choice

Conflict 2: Content Quality vs. Transparency
Possible mitigations:
Third-party audits: Allow independent researchers to audit training data under NDA
Open-source models: Make some models fully transparent as benchmarks for the industry
## Logistics

### How long did the assignment take?

_Rather than giving a range, if you are unsure, give the average of the range._
About 7 hours 
### What resources did you use?

_Please give specific URLs (not "Stack Overflow" or "Google") and state which
ones were particularly helpful._
https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy
Explained proper etiquette for scraping Wikipedia
https://realpython.com/python-hash-method/
Clarified how to properly implement equality and hashing

## Reflections

_Give **one or more paragraphs** reflecting on your experience with the
assignment, including answers to all of these questions:_

* What was the most difficult part of the assignment?
The most challenging aspect was implementing the webpages_so_far property with proper cycle detection. Initially, I struggled with the traversal logic because I needed to explore all pages that had been visited through the children relationships, but avoid infinite loops if a page was reached multiple times through different paths.
* What was the most rewarding part of the assignment?
The most rewarding part was seeing the interactive Wikipedia surfer come together and actually using it to discover interesting connections between pages.
* What did you learn doing the assignment?
I learned tools for making a wikepedia page
_Constructive and actionable suggestions for improving assignments, office
hours, and lecture are always welcome._
