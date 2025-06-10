import streamlit as st
import os
import importlib.util
import inspect
from tasks.utils import capture_output
import traceback # For detailed error tracebacks

# --- Page Configuration (MUST BE THE FIRST STREAMLIT COMMAND) ---
APP_TITLE = "Python OOP Interactive Lab" # Concise Title
APP_ICON = "🔬" # Lab icon / Microscope
st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON, layout="wide", initial_sidebar_state="expanded")


# --- Helper Functions (Keep as before) ---
def load_tasks():
    tasks = {}
    if not os.path.exists(TASK_DIR):
        st.error(f"Task directory '{TASK_DIR}' not found. Please create it and add task files.")
        return tasks

    task_files_raw = [f for f in os.listdir(TASK_DIR) if f.startswith("task_") and f.endswith(".py")]

    def get_task_number(filename):
        try:
            # Extracts number after "task_" and before the next "_" or ".py"
            num_str = filename.split('_')[1]
            return int(num_str)
        except (IndexError, ValueError):
            return float('inf') # Put files with unparsable numbers at the end

    task_files_sorted = sorted(task_files_raw, key=get_task_number)

    for filename in task_files_sorted:
        module_name = filename[:-3] # Remove .py
        try:
            task_number_str = module_name.split('_')[1]
            task_number = int(task_number_str)
        except (IndexError, ValueError):
            st.warning(f"Could not parse task number from filename: '{filename}'. Skipping.")
            continue

        file_path = os.path.join(TASK_DIR, filename)
        spec = importlib.util.spec_from_file_location(module_name, file_path)

        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(module)
            except Exception as e:
                st.error(f"Error loading module {module_name}: {e}")
                st.code(traceback.format_exc())
                continue


            if hasattr(module, "run_task") and callable(module.run_task):
                docstring = inspect.getdoc(module) or "No description available."
                first_line_doc = docstring.split('\n', 1)[0] # Get only the first line
                task_title = first_line_doc
                # Clean up common prefixes if they exist
                task_title = task_title.replace(f"Task {task_number}: ", "").replace(f"Task {task_number_str}: ", "").strip()
                if "Concept:" in task_title: # Further cleanup
                    task_title = task_title.split("Concept:")[0].strip()
                if not task_title : # Fallback if parsing fails
                    task_title = module_name.replace("_", " ").title()


                tasks[f"Task {task_number:02d}: {task_title}"] = {
                    "module": module,
                    "docstring": docstring,
                    "source_code": inspect.getsource(module),
                    "run_function": module.run_task,
                    "get_input_params_function": getattr(module, "get_input_params", None)
                }
            else:
                st.warning(f"Module '{module_name}' does not have a callable 'run_task' function. Skipping.")
        else:
            st.warning(f"Could not load module specification for '{filename}'. Skipping.")
    return tasks

# --- Global Constants & Styling ---
TASK_DIR = "tasks" # Define TASK_DIR here to be accessible by load_tasks

# Custom CSS for minor styling (optional)
# You can add more specific CSS if needed, but keep it minimal for maintainability
st.markdown("""
<style>
    /* Main app background (Streamlit's default dark is usually good) */
    /* .stApp {
        background-color: #f0f2f6; /* Example: Light gray for light mode */
    } */

    /* Sidebar styling */
    .css-1d391kg { /* This selector might change with Streamlit updates, targets sidebar */
        /* background-color: #2E3139; /* Example: Slightly different dark for sidebar */
    }
    .sidebar-title {
        font-size: 28px;
        font-weight: bold;
        color: #A0D2DB; /* A light accent color */
        text-align: center;
        margin-bottom: 20px;
        padding-top: 10px;
    }
    .sidebar-footer {
        text-align: center;
        font-size: 0.9em;
        color: #E0E0E0; /* Lighter gray for footer text */
        padding: 10px;
        border-top: 1px solid #444; /* Subtle separator */
    }

    /* Section Headers in main content */
    h1, h2, h3 { /* Targeting Streamlit's generated headers */
        /* color: #A0D2DB; /* Example: Using the accent color for headers */
    }

    /* Input form container for better visual grouping */
    div[data-testid="stForm"] {
        border: 1px solid #4A4A4A; /* Subtle border for the form */
        border-radius: 8px;
        padding: 20px; /* More padding inside the form */
        background-color: #1E1E1E; /* Slightly different background for form if needed */
        margin-bottom: 20px; /* Space below the form */
    }
    div[data-testid="stForm"] > h3 { /* Targeting h3 inside the form */
        /* color: #FFFFFF; /* Ensure form title is visible */
        /* margin-top: -10px; /* Adjust if needed */
    }


</style>
""", unsafe_allow_html=True)


# --- Main Application UI ---
# Sidebar Content
st.sidebar.markdown(f"<p class='sidebar-title'>{APP_ICON} {APP_TITLE}</p>", unsafe_allow_html=True)
st.sidebar.markdown("---") # Visual separator

st.sidebar.header("🎯 OOP Concepts") # "Choose OOP Concepts"
all_tasks = load_tasks() # Load tasks after defining TASK_DIR

if not all_tasks:
    st.error(f"No valid tasks found. Please check the '{TASK_DIR}' directory for Python files named 'task_XX_concept.py' each containing a 'run_task' function.")
else:
    sorted_task_names = sorted(all_tasks.keys())

    if 'selected_task_name' not in st.session_state or st.session_state.selected_task_name not in sorted_task_names:
        st.session_state.selected_task_name = sorted_task_names[0] if sorted_task_names else None

    selected_task_name = st.sidebar.selectbox(
        "Choose a task to explore:",
        sorted_task_names,
        index=sorted_task_names.index(st.session_state.selected_task_name) if st.session_state.selected_task_name in sorted_task_names else 0,
        key="task_selector_widget"
    )
    st.session_state.selected_task_name = selected_task_name # Update session state for persistence

    # Display total tasks
    st.sidebar.info(f"Total Tasks: {len(all_tasks)}")


    # Main Content Area
    if selected_task_name and selected_task_name in all_tasks:
        task_data = all_tasks[selected_task_name]
        task_short_name = selected_task_name.split(':')[0]
        form_key = f"{task_short_name}_input_form" # Unique key for the form

        st.header(f"🧑‍🏫 {selected_task_name}") # Task title with an icon

        # --- Explanation Section ---
        with st.container(): # Use container for better grouping
            st.subheader("📘 Concept & Explanation")
            st.markdown(task_data["docstring"], unsafe_allow_html=True)
            st.markdown("---")


        # --- Code Viewer ---
        with st.expander("🐍 View Python Code for this Task", expanded=False):
            st.code(task_data["source_code"], language="python")
        st.markdown("---")


        # --- Inputs Section ---
        st.subheader("⚙️ Provide Your Inputs (if any)")
        user_inputs = {} # This will hold the current values from widgets
        input_params_defined = False

        if task_data["get_input_params_function"]:
            params_to_get = task_data["get_input_params_function"]()
            if params_to_get:
                input_params_defined = True
                # The st.form helps group inputs and submit them together
                with st.form(key=form_key, clear_on_submit=False): # clear_on_submit=False to keep values
                    st.markdown("**Customize the example with your values:**")
                    for param_info in params_to_get:
                        param_widget_key = f"{form_key}_{param_info['name']}"
                        label = param_info["label"]
                        # Get previous value from session state if form was submitted before for this input
                        # This helps maintain input values if user navigates away and back, or if page reloads due to other interactions
                        # Default to param_info's default if not in session state
                        default_val_from_session = st.session_state.get(f'{form_key}_submitted_inputs', {}).get(param_info['name'], param_info.get("default"))


                        if param_info["type"] == "text_input":
                            user_inputs[param_info["name"]] = st.text_input(
                                label=label, value=default_val_from_session if default_val_from_session is not None else "", key=param_widget_key
                            )
                        elif param_info["type"] == "number_input":
                            user_inputs[param_info["name"]] = st.number_input(
                                label=label, value=default_val_from_session if default_val_from_session is not None else 0.0,
                                step=param_info.get("step", 1.0),
                                format=param_info.get("format", "%.2f"), # Default to float format
                                min_value=param_info.get("min_value"),
                                max_value=param_info.get("max_value"),
                                key=param_widget_key
                            )
                        elif param_info["type"] == "selectbox":
                            options = param_info.get("options", [])
                            idx = 0
                            if default_val_from_session in options: # Use value from session/default
                                idx = options.index(default_val_from_session)
                            elif param_info.get("default") in options: # Fallback to original default
                                idx = options.index(param_info.get("default"))

                            user_inputs[param_info["name"]] = st.selectbox(
                                label=label, options=options, index=idx, key=param_widget_key
                            )
                        elif param_info["type"] == "slider":
                            user_inputs[param_info["name"]] = st.slider(
                                label=label,
                                min_value=param_info.get("min_value", 0),
                                max_value=param_info.get("max_value", 100),
                                value=default_val_from_session if default_val_from_session is not None else param_info.get("min_value", 0),
                                step=param_info.get("step", 1),
                                key=param_widget_key
                            )
                        elif param_info["type"] == "checkbox":
                             user_inputs[param_info["name"]] = st.checkbox(
                                label=label,
                                value=default_val_from_session if isinstance(default_val_from_session, bool) else False,
                                key=param_widget_key
                            )
                        else:
                            st.warning(f"Unsupported input type '{param_info['type']}' for '{param_info['name']}'.")

                    # Form submission button
                    form_submit_button = st.form_submit_button(label=f"💾 Apply Inputs & Prepare to Run")
                    if form_submit_button:
                        st.session_state[f'{form_key}_submitted_inputs'] = user_inputs.copy()
                        st.success("Inputs applied! Click 'Run Task' below to see the results.")
            else:
                st.info("This task can accept inputs, but none are currently defined for customization.")
        else:
            st.info("This task runs with a predefined example and does not require user inputs.")
        st.markdown("---")


        # --- Execution Section ---
        st.subheader("🚀 Execution & Output")

        final_inputs_to_use = st.session_state.get(f'{form_key}_submitted_inputs', {}) # Get latest submitted inputs

        run_button_label = f"▶️ Run {task_short_name}"
        if input_params_defined and final_inputs_to_use : # If inputs were defined AND applied
             run_button_label += " with Your Inputs"

        output_text_key = f"output_text_{selected_task_name}"
        if output_text_key not in st.session_state:
            st.session_state[output_text_key] = "Click 'Run Task' to see the output."

        if st.button(run_button_label, key=f"run_button_{task_short_name}"):
            with st.spinner("🧠 Processing task..."):
                current_args_for_task = {}
                sig = inspect.signature(task_data["run_function"])
                default_args = {
                    k: v.default for k, v in sig.parameters.items()
                    if v.default is not inspect.Parameter.empty
                }
                current_args_for_task.update(default_args)
                current_args_for_task.update(final_inputs_to_use) # User inputs override defaults

                try:
                    # Filter current_args_for_task to only include actual parameters of run_function
                    valid_task_params = {k: v for k, v in current_args_for_task.items() if k in sig.parameters}
                    output = capture_output(task_data["run_function"], **valid_task_params)
                    st.session_state[output_text_key] = output if output else "✅ Task executed successfully with no print output."
                except Exception as e:
                    error_message = f"⚠️ An error occurred while running the task: {type(e).__name__} - {e}\n\n"
                    error_message += "Traceback:\n" + traceback.format_exc()
                    st.session_state[output_text_key] = error_message

        st.text_area("🖥️ Output Console:", value=st.session_state[output_text_key], height=350, key=f"output_display_{selected_task_name}")

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.markdown("<p class='sidebar-footer'>Created with Python & Streamlit by Taha ❤️ </p>", unsafe_allow_html=True)