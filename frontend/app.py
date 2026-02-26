import streamlit as st
import requests

try:
    API_URL = st.secrets["API_URL"]

except (FileNotFoundError, KeyError):
    API_URL = "http://127.0.0.1:8000"

with st.sidebar:
    st.header("🤖 Model Insights")
    st.info(
        "This model uses ***Your GOAL*** as an pivot and generates small-small tasks. You can check your progress by tracking your accomplishments step-by-step. "
    )
    # Capture the selection into a variable
    selected_model = st.selectbox(
        "Select Model:", ["Gemma3 12b", "Gemma3 27b", "Gemini 2.5 Flash"]
    )
    st.metric(label="Model Reliability (R²)", value="~98%")
    if st.button("🔄 Reset All Inputs"):
        pass

st.title("🚀 Execution Planner")

# ---------------------------------------------------------
# 1. CSS FOR RED DELETE BUTTONS (Wildcard Selector)
# ---------------------------------------------------------
st.markdown(
    """
<style>
    /* 1. EXISTING: Red Delete Buttons */
    div[class*="st-key-delete_goal"] button {
        color: #dc2626 !important;
        border: 1px solid #ef4444 !important;
        font-weight: bold;
    }
    div[class*="st-key-delete_goal"] button:hover {
        background-color: #dc2626 !important;
        color: white !important;
    }

    /* 2. NEW: Make Expander Headers BIG (Like Subheaders) */
    div[data-testid="stExpander"] summary p {
        font-size: 1.3rem !important;
        font-weight: 600 !important;
    }
    
    /* Optional: Add a slight border/background to the Goal Bar */
    div[data-testid="stExpander"] {
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        margin-bottom: 10px;
    }
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 2. CREATE GOAL
# ---------------------------------------------------------
st.header("Create Goal")
goal_input = st.text_input("Enter your goal")

if st.button("Generate Plan"):
    if not goal_input:
        st.warning("Please enter a goal first.")
    else:
        # 1. Construct the payload
        payload = {"title": goal_input, "model_name": selected_model}

        try:
            # 2. SEND THE DATA (POST request) - This was missing!
            response = requests.post(f"{API_URL}/goals", json=payload)

            # 3. Check success
            if response.status_code == 200:
                st.success(f"Plan generated using {selected_model}!")
                st.rerun()  # Refresh to show the new goal
            else:
                st.error(f"Server Error: {response.status_code} - {response.text}")

        except requests.exceptions.ConnectionError:
            st.error("❌ Could not connect to the backend. Is 'main.py' running?")

# ---------------------------------------------------------
# 3. VIEW & MANAGE GOALS
# ---------------------------------------------------------
st.header("Your Goals")
goals = requests.get(f"{API_URL}/goals").json()

# REVERSE THE LIST HERE
goals = goals[::-1]

for goal in goals:
    # Use Columns to put Title (Left) and Delete Button (Right)
    col1, col2 = st.columns([0.90, 0.10])

    # 1. Create a "One-Liner" preview (Truncate to 60 chars)
    full_text = goal["title"]
    short_preview = full_text[:50] + "..." if len(full_text) > 50 else full_text

    with col1:
        # 2. Use an Expander as the main container
        with st.expander(f"*🎯 {short_preview}*", expanded=False):
            st.markdown(f"**Full Goal:** {full_text}")

    with col2:
        # Unique Key: 'delete_goal_1', 'delete_goal_2', etc.
        # The CSS wildcard [class*="st-key-delete_goal"] catches this.
        if st.button("🗑️", key=f"delete_goal_{goal['id']}", help="Delete Goal"):
            requests.delete(f"{API_URL}/goals/{goal['id']}")
            st.rerun()

    # 2. Your updated loop
    for i, task in enumerate(goal["tasks"], start=1):
        # We assign a SIMPLE key based ONLY on status so the CSS can find it
        # Note: Streamlit keys must be unique, so we use the status as the class name
        status_class = "pending_box" if task["status"] == "pending" else "completed_box"

        # We use a unique ID for the container but keep the status_class as a way to target it
        with st.container(border=True, key=f"{status_class}_{task['id']}"):
            st.write(f"**{i}. {task['title']}**")

            if task["status"] == "pending":

                st.info("Status: Pending")
                # 1. Create two columns: small 'spacer' and the 'content' column
                spacer, content = st.columns([0.05, 0.95])

                # 2. Put the expander inside the 'content' column
                with content:
                    with st.expander("Complete:"):

                        # --- NEW SECTION: SUBTASKS ---
                        st.markdown("#### 🧩 Mini-Tasks")

                        # 1. If no subtasks exist, show Generate Button
                        if not task["subtasks"]:
                            if st.button(
                                "⚡ Break Down into Steps", key=f"break_{task['id']}"
                            ):
                                with st.spinner("Generating mini-steps..."):
                                    requests.post(
                                        f"{API_URL}/tasks/{task['id']}/generate_subtasks"
                                    )
                                    st.rerun()

                        # 2. If subtasks exist, show Checklist
                        else:
                            for sub in task["subtasks"]:
                                # Use a checkbox for instant toggle
                                is_checked = st.checkbox(
                                    sub["title"],
                                    value=sub["is_completed"],
                                    key=f"sub_{sub['id']}",
                                )

                                # If state changed, update backend
                                if is_checked != sub["is_completed"]:
                                    requests.put(
                                        f"{API_URL}/subtasks/{sub['id']}",
                                        params={"is_completed": is_checked},
                                    )
                                    st.rerun()

                        st.divider()

                        # --- EXISTING FORM (Time spent, etc) ---

                        time_spent = st.number_input(
                            "Time Spent (minutes)", min_value=0, key=f"time{task['id']}"
                        )
                        problems = st.text_area(
                            "Problems Faced", key=f"prob{task['id']}"
                        )
                        insights = st.text_area(
                            "Insights Gained", key=f"ins{task['id']}"
                        )

                        if st.button("Mark Complete", key=f"btn{task['id']}"):
                            requests.put(
                                f"{API_URL}/tasks/{task['id']}",
                                params={
                                    "time_spent": time_spent,
                                    "problems": problems,
                                    "insights": insights,
                                },
                            )
                            st.rerun()
            else:
                st.success("Status: Completed")

    st.divider()  # Visual separation between goals
