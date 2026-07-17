# Few-Shot Prompting: Tweet Classifier (Spam vs Not Spam)

## Objective
Create a few-shot prompt that teaches an AI model to classify tweets as either **"Spam"** or **"Not Spam"** by providing clear examples with reasoning.

---

## The Prompt

### Instructions
You are a tweet classification assistant. Your task is to classify each tweet as either **"Spam"** or **"Not Spam"**.

**Definition of Spam:**
- Contains suspicious links (e.g., bit.ly, short URLs)
- Promotes scams, fake giveaways, or "too good to be true" offers
- Uses excessive emojis, ALL CAPS, or repetitive characters to grab attention
- Asks for personal information (passwords, credit cards, etc.)
- Has no genuine human engagement value

**Definition of Not Spam:**
- Genuine opinions, questions, or personal updates
- Contains normal conversation or information sharing
- Links to reputable sources (news, blogs, educational content)
- Engages with others in a meaningful way

---

## Few-Shot Examples

### Example 1
**Tweet:** "🚨🚨 FREE iPhone 15 GIVEAWAY! 🚨🚨 Click here to claim now → bit.ly/free-iphone15 Only 5 left! 🔥🔥🔥"
**Classification:** Spam
**Reason:** Suspicious shortened link, too-good-to-be-true offer, excessive emojis and urgency tactics.

---

### Example 2
**Tweet:** "Just finished reading 'Atomic Habits' by James Clear. Honestly, it changed my perspective on productivity. Highly recommend! 📚"
**Classification:** Not Spam
**Reason:** Genuine personal opinion, no suspicious links, authentic book recommendation.

---

### Example 3
**Tweet:** "✅✅ EARN $10,000 IN 3 DAYS ✅✅ Work from home! No experience needed! DM me for details 💰💰💰"
**Classification:** Spam
**Reason:** Unrealistic income promise, excessive symbols/emojis, call-to-action via DM, no legitimate business details.

---

### Example 4
**Tweet:** "Anyone else experiencing login issues with Twitter/X today? I keep getting error codes and can't access my dashboard."
**Classification:** Not Spam
**Reason:** Real user reporting a technical problem, seeking community feedback, no promotional content.

---

### Example 5
**Tweet:** "🎉🎉 CONGRATULATIONS YOU'VE WON $500 AMAZON GIFT CARD! 🎉🎉 Verify your identity here → tinyurl.com/claim-now"
**Classification:** Spam
**Reason:** Fake prize notification, shortened suspicious link, asks for verification (potential personal data harvest).

---

### Example 6
**Tweet:** "Super excited to announce that our startup just raised $2M in seed funding! Full blog post here: techcrunch.com/startup-funding"
**Classification:** Not Spam
**Reason:** Legitimate professional announcement, credible news source link (TechCrunch), genuine company milestone.

---

## Now Classify These Tweets

### Tweet A
"🌸 Good morning everyone! Hope you all have a beautiful day filled with joy and positivity. Remember to be kind to yourself! ✨"

**Classification:** 
**Reason:** 

---

### Tweet B
"🔥🔥 LAST CHANCE! 90% OFF EVERYTHING 🔥🔥 Shop now before it's gone! 👉 https://shrtco.de/6fHk2"

**Classification:** 
**Reason:** 

---

### Tweet C
"Can someone recommend a good budget laptop for programming? I'm a computer science student and need something reliable under $800."

**Classification:** 
**Reason:** 

---

### Tweet D
"YOU'VE BEEN SELECTED! 🎰 Claim your $1,000 Walmart gift card HERE → cutt.ly/3xGmzPw Hurry, this expires in 24 hrs! ⏰"

**Classification:** 
**Reason:** 

---

### Tweet E
"Just adopted this adorable puppy from the local shelter! Meet Milo 🐕 He's already stolen my heart ❤️ #AdoptDontShop"

**Classification:** 
**Reason:** 
