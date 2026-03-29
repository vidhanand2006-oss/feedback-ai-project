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
# app.py

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO

st.set_page_config(page_title="Feedback AI Project", layout="wide")

st.title("🤖 Feedback AI Analyzer - Day 2")
st.write("Upload feedback data to get insights with sentiment & top issues.")

# --- CSV Upload ---
uploaded_file = st.file_uploader("📁 Upload your feedback CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Full Data")
    st.dataframe(df)

    # --- Prepare Feedback List ---
    feedbacks = df['feedback'].tolist()
    st.subheader("📝 Feedback List")
    for i, fb in enumerate(feedbacks, start=1):
        st.write(f"{i}. {fb}")

    # --- Analysis (Dummy Logic / Replace with AI calls if needed) ---
    categories = []
    sentiments = []

    for fb in feedbacks:
        fb_lower = fb.lower()
        if "crash" in fb_lower or "slow" in fb_lower:
            categories.append("Performance")
            sentiments.append("Negative")
        elif "love" in fb_lower or "nice" in fb_lower:
            categories.append("UI Issue")
            sentiments.append("Positive")
        else:
            categories.append("Feature Request")
            sentiments.append("Neutral")

    df['Category'] = categories
    df['Sentiment'] = sentiments

    st.subheader("🔍 Analysis Result")
    for fb, cat, sent in zip(feedbacks, categories, sentiments):
        st.write(f"{fb} → Category: {cat} | Sentiment: {sent}")

    # --- Category Distribution Pie Chart ---
    st.subheader("📊 Category Distribution")
    category_counts = df['Category'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
    st.pyplot(fig)

    # --- Top Issues ---
    st.subheader("🔥 Top Issues")
    for cat, count in category_counts.items():
        st.write(f"- {cat}: {count} feedbacks")

    # --- Sentiment Summary ---
    st.subheader("💬 Sentiment Summary")
    sentiment_counts = df['Sentiment'].value_counts()
    for sent, count in sentiment_counts.items():
        st.write(f"- {sent}: {count}")

    # --- Suggestions ---
    st.subheader("💡 Suggestions")
    st.write("- Improve app performance (speed & crashes)")
    st.write("- Work on UI improvements")
    st.write("- Consider adding requested features")

    # --- Download CSV ---
    st.subheader("📥 Download Files")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Final CSV",
        data=csv,
        file_name='final_output.csv',
        mime='text/csv'
    )

    # --- Weekly Report ---
    report = f"""
Weekly Product Feedback Report
----------------------------------
Top Issues:
{''.join([f"- {cat}: {count} feedbacks\n" for cat, count in category_counts.items()])}

Sentiment Summary:
{''.join([f"- {sent}: {count}\n" for sent, count in sentiment_counts.items()])}

Suggestions:
- Improve app performance (speed & crashes)
- Work on UI improvements
- Consider adding requested features
"""
    st.download_button(
        label="Download Weekly Report",
        data=report,
        file_name='weekly_report.txt',
        mime='text/plain'
    )

else:
    st.info("Please upload a CSV file to see analysis.")