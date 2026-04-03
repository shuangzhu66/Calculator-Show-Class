# Import the Streamlit library for creating web apps
import streamlit as st

# Set the title of the web app
st.title("📊 Average Calculator")

# Add a description to help users understand the app
st.write("This app calculates the average of numbers you enter.")
st.write("---")  # This creates a horizontal line for visual separation

# Create instructions section
st.subheader("📝 Instructions:")
st.write("1. Enter numbers in the text box below (separated by commas)")
st.write("2. Click the 'Calculate Average' button")
st.write("3. View your result!")
st.write("---")

# Create a text input box where users can enter their numbers
# The user should separate numbers with commas (e.g., 5, 10, 15, 20)
user_input = st.text_input(
    "Enter your numbers (separated by commas):",
    placeholder="Example: 5, 10, 15, 20"
)

# Create a button that triggers the calculation
if st.button("Calculate Average"):
    
    # Check if the user actually entered something
    if user_input:
        try:
            # Split the input string by commas and convert each part to a number
            # strip() removes any extra spaces around the numbers
            numbers = [float(num.strip()) for num in user_input.split(",")]
            
            # Calculate the average by dividing the sum by the count of numbers
            average = sum(numbers) / len(numbers)
            
            # Display the results in a nice format
            st.success("✅ Calculation Complete!")
            
            # Create two columns for organized display
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(label="Numbers Entered", value=len(numbers))
            
            with col2:
                st.metric(label="Average", value=f"{average:.2f}")
            
            # Show all the numbers that were entered
            st.write("**Your numbers:**", numbers)
            
        except ValueError:
            # If the user enters something that's not a number, show an error
            st.error("❌ Please enter valid numbers separated by commas!")
    
    else:
        # If the input box is empty, remind the user to enter numbers
        st.warning("⚠️ Please enter some numbers first!")

# Add a footer with additional information
st.write("---")
st.caption("💡 Tip: You can enter decimals too! (e.g., 5.5, 10.2, 15.8)")
