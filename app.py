import streamlit as st

# Title of the app
st.title("ABS - CLM Help Center")

# List of CLM tools and modules
clm_tools = ["Sirion", "Icertis", "Agiloft", "Ironclad"]
modules = ["Contract Types", "Obligations", "Security and Access", "Attributes and Properties"]

# Sample FAQs for each CLM tool and module
faqs = {
    "Icertis": {
        "Contract Types": [
            {"question": "What are the default contract types in Icertis?", "answer": "Icertis offers a variety of contract types like NDA, MSA, etc."},
            {"question": "How can I create a new contract type in Icertis?", "answer": "Navigate to the admin settings to add a new contract type."},
            {"question": "Can contract types be customized?", "answer": "Yes, contract types can be customized based on business needs."},
            {"question": "What is the role of templates in contract types?", "answer": "Templates help standardize contract types in Icertis."},
            {"question": "How to delete a contract type in Icertis?", "answer": "Go to settings and select the contract type to delete."},
        ],
        "Obligations": [
            {"question": "How does Icertis track contract obligations?", "answer": "Icertis tracks obligations using milestone tracking."},
            {"question": "Can I assign obligations to specific users?", "answer": "Yes, you can assign obligations to users within the platform."},
            {"question": "How are obligation deadlines managed?", "answer": "You can set reminders for obligation deadlines in Icertis."},
            {"question": "What happens if an obligation is missed?", "answer": "Missed obligations are flagged for review and escalation."},
            {"question": "Can I modify obligations after contract execution?", "answer": "Yes, obligations can be edited post-execution in Icertis."},
        ],
        "Security and Access": [
            {"question": "How is data secured in Icertis?", "answer": "Icertis uses encryption and role-based access to secure data."},
            {"question": "Can users have different access levels?", "answer": "Yes, access levels are customizable per user or role."},
            {"question": "What security certifications does Icertis have?", "answer": "Icertis is ISO 27001 certified for data security."},
            {"question": "How can I grant access to external users?", "answer": "You can create guest accounts with limited permissions."},
            {"question": "Is two-factor authentication available?", "answer": "Yes, Icertis supports two-factor authentication."},
        ],
        "Attributes and Properties": [
            {"question": "What are attributes in Icertis?", "answer": "Attributes are metadata fields that define contract details."},
            {"question": "Can I create custom attributes?", "answer": "Yes, custom attributes can be created in Icertis."},
            {"question": "How do properties differ from attributes?", "answer": "Properties define specific contract elements; attributes are metadata."},
            {"question": "Can I bulk update attributes?", "answer": "Yes, Icertis allows bulk updates of contract attributes."},
            {"question": "How are attributes used in reporting?", "answer": "Attributes can be used to filter and sort contract reports."},
        ],
    },
    # Similar data structure for other CLM tools...
    "Sirion": {
        "Contract Types": [
            {"question": "What contract types are available in Sirion?", "answer": "Sirion offers templates for various contract types like NDAs."},
            # Add 4 more questions for Sirion's "Contract Types"...
        ],
        "Obligations": [
            {"question": "How does Sirion track obligations?", "answer": "Sirion uses automated workflows to track obligations."},
            
        ],
        "Security and Access": [
            {"question": "How is data secured in Icertis?", "answer": "Icertis uses encryption and role-based access to secure data."},
            {"question": "Can users have different access levels?", "answer": "Yes, access levels are customizable per user or role."},
            {"question": "What security certifications does Icertis have?", "answer": "Icertis is ISO 27001 certified for data security."},
            {"question": "How can I grant access to external users?", "answer": "You can create guest accounts with limited permissions."},
            {"question": "Is two-factor authentication available?", "answer": "Yes, Icertis supports two-factor authentication."},
        ],
        "Attributes and Properties": [
            {"question": "What are attributes in Icertis?", "answer": "Attributes are metadata fields that define contract details."},
            {"question": "Can I create custom attributes?", "answer": "Yes, custom attributes can be created in Icertis."},
            {"question": "How do properties differ from attributes?", "answer": "Properties define specific contract elements; attributes are metadata."},
            {"question": "Can I bulk update attributes?", "answer": "Yes, Icertis allows bulk updates of contract attributes."},
            {"question": "How are attributes used in reporting?", "answer": "Attributes can be used to filter and sort contract reports."},
        ],
        # Add other modules for Sirion...
    },
    "Agiloft": {
        "Contract Types": [
            {"question": "How do I create a new contract type in Agiloft?", "answer": "Navigate to the contract templates to add a new type."},
            # Add 4 more questions for Agiloft's "Contract Types"...
        ],
        "Obligations": [
            {"question": "How does Agiloft manage contract obligations?", "answer": "Agiloft uses task assignments to manage obligations."},
            # Add 4 more questions for Agiloft's "Obligations"...
        ],
        "Security and Access": [
            {"question": "How is data secured in Icertis?", "answer": "Icertis uses encryption and role-based access to secure data."},
            {"question": "Can users have different access levels?", "answer": "Yes, access levels are customizable per user or role."},
            {"question": "What security certifications does Icertis have?", "answer": "Icertis is ISO 27001 certified for data security."},
            {"question": "How can I grant access to external users?", "answer": "You can create guest accounts with limited permissions."},
            {"question": "Is two-factor authentication available?", "answer": "Yes, Icertis supports two-factor authentication."},
        ],
        "Attributes and Properties": [
            {"question": "What are attributes in Icertis?", "answer": "Attributes are metadata fields that define contract details."},
            {"question": "Can I create custom attributes?", "answer": "Yes, custom attributes can be created in Icertis."},
            {"question": "How do properties differ from attributes?", "answer": "Properties define specific contract elements; attributes are metadata."},
            {"question": "Can I bulk update attributes?", "answer": "Yes, Icertis allows bulk updates of contract attributes."},
            {"question": "How are attributes used in reporting?", "answer": "Attributes can be used to filter and sort contract reports."},
        ],
        # Add other modules for Agiloft...
    },
    "Ironclad": {
        "Contract Types": [
            {"question": "How to add a new contract type in Ironclad?", "answer": "Go to settings to configure contract types in Ironclad."},
            # Add 4 more questions for Ironclad's "Contract Types"...
        ],
        "Obligations": [
            {"question": "What obligation management features does Ironclad offer?", "answer": "Ironclad has robust tools for obligation tracking."},
            # Add 4 more questions for Ironclad's "Obligations"...
        ],
        "Security and Access": [
            {"question": "How is data secured in Icertis?", "answer": "Icertis uses encryption and role-based access to secure data."},
            {"question": "Can users have different access levels?", "answer": "Yes, access levels are customizable per user or role."},
            {"question": "What security certifications does Icertis have?", "answer": "Icertis is ISO 27001 certified for data security."},
            {"question": "How can I grant access to external users?", "answer": "You can create guest accounts with limited permissions."},
            {"question": "Is two-factor authentication available?", "answer": "Yes, Icertis supports two-factor authentication."},
        ],
        "Attributes and Properties": [
            {"question": "What are attributes in Icertis?", "answer": "Attributes are metadata fields that define contract details."},
            {"question": "Can I create custom attributes?", "answer": "Yes, custom attributes can be created in Icertis."},
            {"question": "How do properties differ from attributes?", "answer": "Properties define specific contract elements; attributes are metadata."},
            {"question": "Can I bulk update attributes?", "answer": "Yes, Icertis allows bulk updates of contract attributes."},
            {"question": "How are attributes used in reporting?", "answer": "Attributes can be used to filter and sort contract reports."},
        ],
        # Add other modules for Ironclad...
    },
}

# Select CLM Tool
selected_clm = st.selectbox("Select your CLM tool", clm_tools)

# Select Module
selected_module = st.selectbox("Select the module", modules)

# Display FAQs based on selected CLM tool and module
if selected_clm and selected_module:
    st.subheader(f"FAQs for {selected_clm} - {selected_module}")
    for faq in faqs[selected_clm][selected_module]:
        if st.button(faq["question"]):
            st.write(f"**Answer:** {faq['answer']}")

# Global Search
st.subheader("Global Search")
search_query = st.text_input("Enter keyword")
selected_clm_search = st.selectbox("Select CLM tool for search", clm_tools)

if search_query:
    st.subheader(f"Search results for '{search_query}' in {selected_clm_search}")
    for module, questions in faqs[selected_clm_search].items():
        for faq in questions:
            if search_query.lower() in faq["question"].lower():
                if st.button(faq["question"]):
                    st.write(f"**Answer:** {faq['answer']}")

# "Have a Question?" field
st.subheader("Have a question?")
user_question = st.text_area("Ask your question here")
if st.button("Post"):
    st.success("Your question has been posted!")
    user_question = ""  # Clears the field
