import streamlit as st
import json
from notebook_api import analyze_student_data, generate_feedback, generate_pdf

st.title("MathonGO Student Performance Analyzer")

uploaded_file = st.file_uploader("Upload Student JSON file", type=["json"])

if uploaded_file is not None:
    try:
        student_json = json.load(uploaded_file)
        # If the JSON is a list with one dict, extract the dict
        if isinstance(student_json, list) and len(student_json) == 1 and isinstance(student_json[0], dict):
            student_json = student_json[0]

        # Analyze student data
        summary, detailed_summary = analyze_student_data(student_json)

        st.subheader("Performance Summary")
        st.write(f"Correct Answers: {summary['correct']}")
        st.write(f"Incorrect Answers: {summary['incorrect']}")
        st.write(f"Accuracy: {summary['accuracy']:.2f}%")

        # Generate AI feedback
        student_id = student_json.get("test", {}).get("studentId", "Unknown Student")
        feedback = generate_feedback(student_id, detailed_summary)

        st.subheader("AI Feedback")
        st.markdown(feedback)

        # Generate PDF button
        if st.button("Generate PDF"):
            pdf_bytes = generate_pdf(student_id, feedback)
            st.success("PDF generated successfully!")
            st.download_button(
                label="Download PDF Report",
                data=pdf_bytes,
                file_name=f"{student_id}_report.pdf",
                mime="application/pdf"
            )
    except Exception as e:
        st.error(f"Error processing file: {e}")
