import streamlit as st
import pandas as pd
from collections import Counter

st.set_page_config(page_title="Feedback AI Tool", layout="wide")

st.title("🚀 Feedback Analysis AI Tool")

# Upload file
uploaded_file = st.file_uploader("📂 Upload your feedback CSV", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("📊 Raw Data")
    st.dataframe(data)

    # Analysis function
    def analyze_feedback(feedback):
        feedback = str(feedback).lower()

        if "slow" in feedback or "crash" in feedback:
            return "Performance", "Negative"
        elif "love" in feedback:
            return "UI Issue", "Positive"
        elif "feature" in feedback or "dark mode" in feedback:
            return "Feature Request", "Neutral"
        else:
            return "Other", "Neutral"

    # Apply analysis
    categories = []
    sentiments = []

    for fb in data["feedback"]:
        cat, sent = analyze_feedback(fb)
        categories.append(cat)
        sentiments.append(sent)

    data["Category"] = categories
    data["Sentiment"] = sentiments

    st.subheader("🔍 Analyzed Data")
    st.dataframe(data)

    # Counts
    category_count = Counter(categories)
    sentiment_count = Counter(sentiments)

    st.subheader("📊 Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.write("### Category Distribution")
        st.bar_chart(pd.DataFrame(category_count.values(), index=category_count.keys()))

    with col2:
        st.write("### Sentiment Distribution")
        st.bar_chart(pd.DataFrame(sentiment_count.values(), index=sentiment_count.keys()))

    # Top Issues
    st.subheader("🔥 Top Issues")
    top_issues = category_count.most_common(3)

    for issue, count in top_issues:
        st.write(f"👉 {issue} ({count} times)")

    # ================= REPORT =================
    st.subheader("📄 Weekly Report")

    report = "Weekly Product Feedback Report\n\n"

    report += "Top Issues:\n"
    for issue, count in top_issues:
        report += f"- {issue}: {count}\n"

    report += "\nSentiment Summary:\n"
    for sent, count in sentiment_count.items():
        report += f"- {sent}: {count}\n"

    report += "\nSuggestions:\n"
    report += "- Improve app performance\n"
    report += "- Work on UI improvements\n"
    report += "- Add requested features\n"

    # Show report
    st.text(report)

    # Download button (IMPORTANT: same block ke andar)
    st.download_button(
        "⬇️ Download Report",
        report,
        file_name="report.txt"
    )