import pandas as pd

# Step 1: CSV file read karo
data = pd.read_csv("data.csv")

# Step 2: Data print karo
print("📊 Full Data:\n")
print(data)

# Step 3: Sirf feedback column print karo
print("\n📝 Feedback List:\n")
for i, feedback in enumerate(data["feedback"], 1):
    print(f"{i}. {feedback}")
    print("\n📌 Total Feedback Count:", len(data))
    import pandas as pd

print("🚀 Feedback AI Project Started")

# CSV read
data = pd.read_csv("data.csv")

print("\n📊 Full Data:\n")
print(data)

print("\n📝 Feedback List:\n")

for i, feedback in enumerate(data["feedback"], 1):
    print(f"{i}. {feedback}")

print("\n📌 Total Feedback Count:", len(data))


# ✅ बिना API वाला smart analysis function
def analyze_feedback(feedback):
    feedback = feedback.lower()

    if "slow" in feedback or "crash" in feedback:
        return "Category: Performance | Sentiment: Negative"
    
    elif "love" in feedback:
        return "Category: UI Issue | Sentiment: Positive"
    
    elif "feature" in feedback:
        return "Category: Feature Request | Sentiment: Neutral"
    
    elif "dark mode" in feedback:
        return "Category: Feature Request | Sentiment: Neutral"
    
    else:
        return "Category: Other | Sentiment: Neutral"


print("\n🔍 Analysis Result:\n")

results = []

for fb in data["feedback"]:
    result = analyze_feedback(fb)
    print(f"{fb} → {result}")
    results.append(result)

# Save output
data["analysis"] = results
data.to_csv("output.csv", index=False)

print("\n✅ Done! Check output.csv file")
import pandas as pd
from collections import Counter

print("🚀 Feedback AI Project Started")

# CSV read
data = pd.read_csv("data.csv")

# ---------- Step 1: Analysis Function ----------
def analyze_feedback(feedback):
    feedback = feedback.lower()

    if "slow" in feedback or "crash" in feedback:
        return "Performance", "Negative"
    
    elif "love" in feedback:
        return "UI Issue", "Positive"
    
    elif "feature" in feedback or "dark mode" in feedback:
        return "Feature Request", "Neutral"
    
    else:
        return "Other", "Neutral"


# ---------- Step 2: Apply Analysis ----------
categories = []
sentiments = []

for fb in data["feedback"]:
    cat, sent = analyze_feedback(fb)
    categories.append(cat)
    sentiments.append(sent)

data["Category"] = categories
data["Sentiment"] = sentiments


# ---------- Step 3: Grouping ----------
print("\n📊 Category Count:\n")
category_count = Counter(categories)

for cat, count in category_count.items():
    print(f"{cat}: {count}")


# ---------- Step 4: Top 3 Issues ----------
top_issues = category_count.most_common(3)

print("\n🔥 Top 3 Issues:\n")
for issue, count in top_issues:
    print(f"{issue} ({count} times)")


# ---------- Step 5: Weekly Report ----------
report = "\n📅 Weekly Product Feedback Report\n"
report += "----------------------------------\n"

report += "\n🔝 Top Issues:\n"
for issue, count in top_issues:
    report += f"- {issue}: {count} feedbacks\n"

report += "\n💬 Sentiment Summary:\n"
sentiment_count = Counter(sentiments)

for sent, count in sentiment_count.items():
    report += f"- {sent}: {count}\n"

report += "\n💡 Suggestions:\n"
report += "- Improve app performance (speed & crashes)\n"
report += "- Work on UI improvements\n"
report += "- Consider adding requested features\n"


print(report)


# ---------- Step 6: Save ----------
data.to_csv("final_output.csv", index=False)

with open("weekly_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("\n✅ Final files created:")
print("📁 final_output.csv")
print("📄 weekly_report.txt")