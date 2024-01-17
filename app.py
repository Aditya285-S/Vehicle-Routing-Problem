# streamlit_app.py
import streamlit as st
from algorithm import calculate_optimal_route

def main():
    st.set_page_config(page_title="Vehicle Routing Problem")

    html_temp = """
    <div style="background-color:lightblue;padding:20px;margin-bottom:30px">
    <h2 style="color:black;text-align:center;font-weight:bold;font-size:45px">Vehicle Routing Problem</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    # Input for the number of customers
    num_customers = st.number_input("Number of Customers:", min_value=1, max_value=10, value=5)

    # Input for depot
    st.header("Depot Location:")
    depot_x = st.number_input("Depot X", value=25)
    depot_y = st.number_input("Depot Y", value=25)
    depot = (depot_x, depot_y)

    # Input for customer and vehicle information
    st.header("Customer and Vehicle Information:")
    customers = {}
    for i in range(1, num_customers + 1):
        st.subheader(f"**Customer {i}:**")
        x = st.number_input(f"X co-ordinate", key=f"cx_{i}", value=0)
        y = st.number_input(f"Y co-ordinate", key=f"cy_{i}", value=0)
        demand = st.number_input(f"Customer Demand", key=f"cd_{i}", value=0)
        customers[i] = (x, y, demand)

    st.write("")
    vehicle_capacity = st.number_input("Vehicle Capacity:", value=30)

    # Calculate optimal route
    if st.button("Calculate Optimal Route"):
        best_route, best_distance = calculate_optimal_route(customers, depot, vehicle_capacity)

        # Display the result
        if best_route:
            st.success("Optimal Solution Found")
            route_with_depot = [0] + best_route[1:]  # Add depot at the beginning and end of the route
            st.write(f"Route: {', '.join(map(str, route_with_depot))}")
            st.write(f"Total Distance: {best_distance:.2f}")
        else:
            st.error("No valid route found.")

if __name__ == "__main__":
    main()
