import io
import os
import zipfile

import streamlit as st

from github_pipeline_functions import (
    search_github,
    save_json,
    save_csv,
    create_report,
)


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="GitHub Repository Automation",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ---------------------------------------------------------
# Custom styling
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(88, 101, 242, 0.16),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(0, 210, 255, 0.10),
                transparent 28%
            ),
            linear-gradient(
                135deg,
                #080b14 0%,
                #0d1220 45%,
                #080b14 100%
            );
    }

    .block-container {
        max-width: 1200px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
    }

    .repository-card {
        padding: 1.3rem;
        margin-bottom: 1rem;
        border-radius: 18px;
        border: 1px solid rgba(255, 255, 255, 0.09);
        background: rgba(255, 255, 255, 0.04);
        box-shadow:
            0 15px 40px rgba(0, 0, 0, 0.20),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.caption(
    "PYTHON • GITHUB API • AUTOMATION"
)

st.title(
    "🔎 GitHub Repository Automation"
)

st.subheader(
    "Discover, filter, sort, and analyze GitHub repositories "
    "with an automated Python-powered workflow."
)

st.markdown(
    "**Built by Zeeshan Hassan**"
)

st.divider()


# ---------------------------------------------------------
# Search controls
# ---------------------------------------------------------

st.subheader(
    "Search GitHub"
)


query = st.text_input(
    "Search query",
    placeholder="Example: artificial intelligence",
)


col1, col2, col3 = st.columns(3)


with col1:

    repository_count = st.number_input(
        "Number of repositories",
        min_value=1,
        max_value=1000,
        value=10,
        step=1,
    )


with col2:

    minimum_stars = st.number_input(
        "Minimum stars",
        min_value=0,
        value=0,
        step=1,
    )


with col3:

    language = st.selectbox(
        "Programming language",
        [
            "Any",
            "Python",
            "JavaScript",
            "TypeScript",
            "Java",
            "C++",
            "C#",
            "Go",
            "Rust",
            "PHP",
            "Ruby",
            "Swift",
        ],
    )


col4, col5 = st.columns(2)


with col4:

    sort_option = st.selectbox(
        "Sort repositories by",
        [
            "Recently Updated",
            "Stars",
            "Forks",
        ],
    )


with col5:

    report_format = st.selectbox(
        "Report format",
        [
            "TXT",
            "JSON",
            "CSV",
            "All Reports",
        ],
    )


search_clicked = st.button(
    "🚀 Search GitHub",
    use_container_width=True,
)


# ---------------------------------------------------------
# Search GitHub
# ---------------------------------------------------------

if search_clicked:

    if not query.strip():

        st.warning(
            "Please enter a GitHub search query."
        )

    else:

        language_value = (
            None
            if language == "Any"
            else language
        )


        sort_mapping = {
            "Recently Updated": "updated",
            "Stars": "stars",
            "Forks": "forks",
        }


        sort_value = sort_mapping[
            sort_option
        ]


        with st.spinner(
            "Searching GitHub..."
        ):

            repositories = search_github(
                query=query.strip(),
                number=repository_count,
                language=language_value,
                sort_by=sort_value,
                minimum_stars=minimum_stars,
            )


        st.subheader(
            "Results"
        )


        if not repositories:

            st.warning(
                "No repositories were found "
                "matching your criteria."
            )

        else:

            st.success(
                f"Found {len(repositories)} repositories."
            )


            # -------------------------------------------------
            # Generate reports
            # -------------------------------------------------

            save_json(repositories)
            save_csv(repositories)
            create_report(repositories)


            # -------------------------------------------------
            # Result metrics
            # -------------------------------------------------

            metric1, metric2, metric3 = st.columns(3)


            with metric1:

                st.metric(
                    "Repositories",
                    len(repositories),
                )


            with metric2:

                st.metric(
                    "Minimum Stars",
                    minimum_stars,
                )


            with metric3:

                st.metric(
                    "Language",
                    language,
                )


            # -------------------------------------------------
            # Repository cards
            # -------------------------------------------------

            for repo in repositories:

                name = repo.get(
                    "full_name",
                    "Unknown repository",
                )


                description = repo.get(
                    "description",
                    "No description available.",
                )


                stars = repo.get(
                    "stargazers_count",
                    0,
                )


                forks = repo.get(
                    "forks_count",
                    0,
                )


                repo_language = repo.get(
                    "language",
                    "Unknown",
                )


                html_url = repo.get(
                    "html_url",
                    "#",
                )


                st.markdown(
                    '<div class="repository-card">',
                    unsafe_allow_html=True,
                )


                st.markdown(
                    f"**{name}**"
                )


                st.write(
                    description
                )


                st.caption(
                    f"⭐ {stars:,}   |   "
                    f"🍴 {forks:,}   |   "
                    f"💻 {repo_language}"
                )


                st.link_button(
                    "View Repository ↗",
                    html_url,
                )


                st.markdown(
                    "</div>",
                    unsafe_allow_html=True,
                )


            # -------------------------------------------------
            # Download reports
            # -------------------------------------------------

            st.subheader(
                "Download Reports"
            )


            base_dir = os.path.dirname(
                os.path.abspath(__file__)
            )


            json_path = os.path.join(
                base_dir,
                "pipeline_results.json"
            )


            csv_path = os.path.join(
                base_dir,
                "pipeline_results.csv"
            )


            txt_path = os.path.join(
                base_dir,
                "pipeline_report.txt"
            )


            download_col1, download_col2, download_col3 = (
                st.columns(3)
            )


            # -------------------------------------------------
            # TXT download
            # -------------------------------------------------

            if report_format in [
                "TXT",
                "All Reports",
            ]:

                with open(
                    txt_path,
                    "rb"
                ) as file:

                    txt_data = file.read()


                with download_col1:

                    st.download_button(
                        label="📄 Download TXT",
                        data=txt_data,
                        file_name="pipeline_report.txt",
                        mime="text/plain",
                        use_container_width=True,
                    )


            # -------------------------------------------------
            # CSV download
            # -------------------------------------------------

            if report_format in [
                "CSV",
                "All Reports",
            ]:

                with open(
                    csv_path,
                    "rb"
                ) as file:

                    csv_data = file.read()


                with download_col2:

                    st.download_button(
                        label="📊 Download CSV",
                        data=csv_data,
                        file_name="pipeline_results.csv",
                        mime="text/csv",
                        use_container_width=True,
                    )


            # -------------------------------------------------
            # JSON download
            # -------------------------------------------------

            if report_format in [
                "JSON",
                "All Reports",
            ]:

                with open(
                    json_path,
                    "rb"
                ) as file:

                    json_data = file.read()


                with download_col3:

                    st.download_button(
                        label="🗂️ Download JSON",
                        data=json_data,
                        file_name="pipeline_results.json",
                        mime="application/json",
                        use_container_width=True,
                    )


            # -------------------------------------------------
            # Download all reports as ZIP
            # -------------------------------------------------

            if report_format == "All Reports":

                zip_buffer = io.BytesIO()


                with zipfile.ZipFile(
                    zip_buffer,
                    "w",
                    zipfile.ZIP_DEFLATED
                ) as zip_file:

                    zip_file.write(
                        txt_path,
                        arcname="pipeline_report.txt",
                    )

                    zip_file.write(
                        csv_path,
                        arcname="pipeline_results.csv",
                    )

                    zip_file.write(
                        json_path,
                        arcname="pipeline_results.json",
                    )


                zip_buffer.seek(0)


                st.download_button(
                    label="📦 Download All Reports (.zip)",
                    data=zip_buffer,
                    file_name="github_repository_reports.zip",
                    mime="application/zip",
                    use_container_width=True,
                )


# ---------------------------------------------------------
# About
# ---------------------------------------------------------

st.subheader(
    "About This Project"
)


st.markdown(
    """
**GitHub Repository Automation**

A Python automation tool that searches GitHub repositories
using the GitHub REST API.

**Features**

- Repository search
- Programming-language filtering
- Minimum-star filtering
- Repository sorting
- API pagination
- JSON, CSV, and TXT report generation
- Individual report downloads
- Combined ZIP report download
- Pytest automated testing
- GitHub Actions continuous integration
"""
)


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()

st.caption(
    "Built by Zeeshan Hassan"
)

st.caption(
    "Python • Streamlit • GitHub REST API • Pytest"
)

st.caption(
    "GitHub Repository Automation"
)