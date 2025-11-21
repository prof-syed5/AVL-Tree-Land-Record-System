import streamlit as st
from land_Record_Management import PlotRecord, LandRecordsManager

st.set_page_config(page_title="Land Records Management", layout="wide")
st.title("Land Records Management System")
st.subheader("AVL Tree Based")

if "manager" not in st.session_state:
    st.session_state.manager = LandRecordsManager(index_by='plot')

manager = st.session_state.manager

st.header("Add New Land Record")
col1, col2 = st.columns(2)

with col1:
    plot = st.number_input("Plot Number", step=1)
    owner = st.text_input("Owner Name")

with col2:
    area = st.number_input("Area Size (sq ft)", step=0.1)
    location = st.text_input("Location")

if st.button("Add Record"):
    if plot and owner and area and location:
        try:
            rec = PlotRecord(plot, owner, area, location)
            manager.add_record(rec)
            st.success(f"Record added successfully: Plot# {plot}")
        except ValueError as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please fill all fields correctly.")

st.header("Search Record By Plot Number")
plot_search = st.number_input("Enter Plot Number to Search", step=1, key="search_plot")

if st.button("Search Plot"):
    result = manager.search_by_plot(plot_search)
    if result:
        st.success("Record Found:")
        st.write(str(result))
    else:
        st.warning("No record found.")

st.header("Search Records By Area")
area_search = st.number_input("Enter Area Size to Search", step=0.1, key="search_area")

if st.button("Search Area"):
    results = manager.search_by_area(area_search)
    if results:
        st.success(f"{len(results)} Record(s) Found:")
        for r in results:
            st.write(str(r))
    else:
        st.warning("No records found.")

st.header("Delete Record")
plot_delete = st.number_input("Enter Plot Number to Delete", step=1, key="delete_plot")

if st.button("Delete Record"):
    try:
        manager.delete_by_plot(plot_delete)
        st.success(f"Record Deleted (if existed): Plot# {plot_delete}")
    except KeyError:
        st.warning("No record found to delete.")

st.header("View All Records (Sorted by Plot Number)")
records = manager.list_all()
if records:
    st.table([r.__dict__ for r in records])
else:
    st.info("No records found.")
