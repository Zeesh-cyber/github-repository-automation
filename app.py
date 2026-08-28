import csv
import io
import json
import zipfile
from datetime import datetime
from zoneinfo import ZoneInfo

import streamlit as st

from github_pipeline_functions import search_github


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
# Custom 3D / Professional Styling
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at 12% 5%,
                rgba(82, 112, 255, 0.20),
                transparent 28%
            ),
            radial-gradient(
                circle at 88% 10%,
                rgba(0, 214, 255, 0.13),
                transparent 25%
            ),
            radial-gradient(
                circle at 50% 92%,
                rgba(132, 82, 255, 0.09),
                transparent 28%
            ),
            linear-gradient(
                135deg,
                #05070d 0%,
                #0a0f1c 48%,
                #060912 100%
            );
    }


    .block-container {
        max-width: 1250px;
        padding-top: 1.8rem;
        padding-bottom: 4rem;
    }


    #MainMenu {
        visibility: hidden;
    }


    footer {
        visibility: hidden;
    }


    /* -----------------------------------------------------
       Hero
       ----------------------------------------------------- */

    .st-key-hero {
        padding: 2.5rem 2.2rem;
        margin-bottom: 2rem;

        border-radius: 28px;

        background:
            linear-gradient(
                145deg,
                rgba(255, 255, 255, 0.085),
                rgba(255, 255, 255, 0.025)
            );

        border: 1px solid rgba(255, 255, 255, 0.11);

        box-shadow:
            0 30px 70px rgba(0, 0, 0, 0.42),
            inset 0 1px 0 rgba(255, 255, 255, 0.09);

        backdrop-filter: blur(18px);

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }


    .st-key-hero:hover {
        transform: translateY(-2px);

        box-shadow:
            0 36px 80px rgba(0, 0, 0, 0.48),
            0 0 35px rgba(70, 120, 255, 0.08),
            inset 0 1px 0 rgba(255, 255, 255, 0.10);
    }


    /* -----------------------------------------------------
       Search panel
       ----------------------------------------------------- */

    .st-key-search_panel {
        padding: 1.5rem;

        border-radius: 22px;

        background:
            linear-gradient(
                145deg,
                rgba(255, 255, 255, 0.065),
                rgba(255, 255, 255, 0.02)
            );

        border: 1px solid rgba(255, 255, 255, 0.09);

        box-shadow:
            0 22px 48px rgba(0, 0, 0, 0.28),
            inset 0 1px 0 rgba(255, 255, 255, 0.06);
    }


    /* -----------------------------------------------------
       Inputs
       ----------------------------------------------------- */

    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {
        background: rgba(255, 255, 255, 0.045) !important;

        border: 1px solid rgba(255, 255, 255, 0.10) !important;

        border-radius: 12px !important;

        box-shadow:
            inset 0 1px 0 rgba(255, 255, 255, 0.035);
    }


    div[data-baseweb="input"] input {
        color: #ffffff !important;
    }


    /* -----------------------------------------------------
       Search button
       ----------------------------------------------------- */

    .st-key-search_button button {
        width: 100%;

        min-height: 3.25rem;

        border-radius: 14px;

        border: 1px solid rgba(126, 170, 255, 0.35);

        background:
            linear-gradient(
                135deg,
                #4b6fff,
                #00b7f4
            );

        color: #ffffff;

        font-weight: 800;

        box-shadow:
            0 14px 34px rgba(0, 120, 255, 0.25),
            inset 0 1px 0 rgba(255, 255, 255, 0.20);

        transition:
            transform 0.18s ease,
            box-shadow 0.18s ease;
    }


    .st-key-search_button button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 20px 42px rgba(0, 130, 255, 0.36),
            inset 0 1px 0 rgba(255, 255, 255, 0.25);
    }


    /* -----------------------------------------------------
       Metrics
       ----------------------------------------------------- */

    div[data-testid="stMetric"] {
        padding: 1.2rem;

        border-radius: 18px;

        background:
            linear-gradient(
                145deg,
                rgba(255, 255, 255, 0.07),
                rgba(255, 255, 255, 0.025)
            );

        border: 1px solid rgba(255, 255, 255, 0.09);

        box-shadow:
            0 16px 34px rgba(0, 0, 0, 0.25),
            inset 0 1px 0 rgba(255, 255, 255, 0.06);
    }


    div[data-testid="stMetricLabel"] {
        color: rgba(232, 239, 255, 0.58) !important;
    }


    div[data-testid="stMetricValue"] {
        font-weight: 800;
    }


    /* -----------------------------------------------------
       Repository cards
       ----------------------------------------------------- */

    [class*="st-key-repo_card_"] {
        margin-top: 1rem;
        padding: 1.1rem;

        border-radius: 20px;

        background:
            linear-gradient(
                145deg,
                rgba(255, 255, 255, 0.07),
                rgba(255, 255, 255, 0.025)
            );

        border: 1px solid rgba(255, 255, 255, 0.085);

        box-shadow:
            0 18px 42px rgba(0, 0, 0, 0.27),
            inset 0 1px 0 rgba(255, 255, 255, 0.055);

        transition:
            transform 0.20s ease,
            box-shadow 0.20s ease,
            border-color 0.20s ease;
    }


    [class*="st-key-repo_card_"]:hover {
        transform: translateY(-4px);

        border-color: rgba(110, 170, 255, 0.27);

        box-shadow:
            0 26px 52px rgba(0, 0, 0, 0.38),
            0 0 28px rgba(70, 130, 255, 0.07),
            inset 0 1px 0 rgba(255, 255, 255, 0.075);
    }


    /* -----------------------------------------------------
       Repository links
       ----------------------------------------------------- */

    [class*="st-key-repo_link_"] a {
        border-radius: 11px !important;

        border: 1px solid rgba(255, 255, 255, 0.09) !important;

        background:
            rgba(255, 255, 255, 0.04) !important;

        transition:
            transform 0.18s ease,
            background 0.18s ease;
    }


    [class*="st-key-repo_link_"] a:hover {
        transform: translateY(-1px);

        background:
            rgba(255, 255, 255, 0.075) !important;
    }


    /* -----------------------------------------------------
       Download panel
       ----------------------------------------------------- */

    .st-key-download_panel {
        margin-top: 1.2rem;
        padding: 1.3rem;

        border-radius: 21px;

        background:
            linear-gradient(
                145deg,
                rgba(255, 255, 255, 0.06),
                rgba(255, 255, 255, 0.022)
            );

        border: 1px solid rgba(255, 255, 255, 0.08);

        box-shadow:
            0 18px 40px rgba(0, 0, 0, 0.25),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
    }


    .stDownloadButton > button {
        min-height: 3rem;

        border-radius: 12px;

        border: 1px solid rgba(255, 255, 255, 0.10);

        background:
            linear-gradient(
                145deg,
                rgba(255, 255, 255, 0.07),
                rgba(255, 255, 255, 0.03)
            );

        box-shadow:
            0 12px 26px rgba(0, 0, 0, 0.18),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);

        transition:
            transform 0.18s ease,
            box-shadow 0.18s ease;
    }


    .stDownloadButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 17px 32px rgba(0, 0, 0, 0.28),
            inset 0 1px 0 rgba(255, 255, 255, 0.07);
    }


    /* -----------------------------------------------------
       About panel
       ----------------------------------------------------- */

    .st-key-about_panel {
        margin-top: 1.3rem;
        padding: 1.7rem;

        border-radius: 22px;

        background:
            linear-gradient(
                145deg,
                rgba(255, 255, 255, 0.055),
                rgba(255, 255, 255, 0.02)
            );

        border: 1px solid rgba(255, 255, 255, 0.075);

        box-shadow:
            0 18px 42px rgba(0, 0, 0, 0.24),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
    }


    /* -----------------------------------------------------
       Responsive
       ----------------------------------------------------- */

    @media (max-width: 800px) {

        .block-container {
            padding-top: 1rem;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Hero
# ---------------------------------------------------------

with st.container(
    border=True,
    key="hero",
):

    st.caption(
        "PYTHON • GITHUB REST API • AUTOMATION"
    )

    st.title(
        "🔎 GitHub Repository Automation"
    )

    st.write(
        "Discover, filter, sort, analyze, and export GitHub "
        "repositories through an automated Python-powered workflow."
    )

    st.markdown(
        "**Built by Zeeshan Hassan**"
    )


# ---------------------------------------------------------
# Search section
# ---------------------------------------------------------

st.markdown(
    "## Search GitHub"
)

st.caption(
    "Configure your repository search and let the automation pipeline do the work."
)


with st.container(
    border=True,
    key="search_panel",
):

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


    with st.container(
        key="search_button",
    ):

        search_clicked = st.button(
            "🚀 Search GitHub",
            use_container_width=True,
        )


# ---------------------------------------------------------
# Search workflow
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


        st.markdown(
            "## Results"
        )


        if not repositories:

            st.warning(
                "No repositories were found matching your criteria."
            )

        else:

            st.success(
                f"Found {len(repositories)} repositories."
            )


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
            # Generate fresh report data in memory
            # -------------------------------------------------

            generated_time = datetime.now(
                ZoneInfo("Asia/Kolkata")
            )


            # TXT report

            txt_buffer = io.StringIO()


            txt_buffer.write(
                "GITHUB AUTOMATION REPORT\n"
            )

            txt_buffer.write(
                "========================\n\n"
            )

            txt_buffer.write(
                "Generated on: "
                f"{generated_time.strftime('%Y-%m-%d %H:%M:%S IST')}\n"
            )

            txt_buffer.write(
                f"Total repositories: "
                f"{len(repositories)}\n\n"
            )


            for repo in repositories:

                txt_buffer.write(
                    f"Repository: "
                    f"{repo.get('full_name', 'Unknown repository')}\n"
                )

                txt_buffer.write(
                    f"Stars: "
                    f"{repo.get('stargazers_count', 0)}\n"
                )

                txt_buffer.write(
                    f"Language: "
                    f"{repo.get('language', 'Unknown')}\n"
                )

                txt_buffer.write(
                    f"URL: "
                    f"{repo.get('html_url', '#')}\n"
                )

                txt_buffer.write(
                    "------------------------\n"
                )


            txt_data = txt_buffer.getvalue().encode(
                "utf-8"
            )


            # CSV report

            csv_buffer = io.StringIO()


            csv_writer = csv.writer(
                csv_buffer
            )


            csv_writer.writerow(
                [
                    "Repository",
                    "Stars",
                    "Language",
                    "URL",
                ]
            )


            for repo in repositories:

                csv_writer.writerow(
                    [
                        repo.get(
                            "full_name",
                            "Unknown repository",
                        ),
                        repo.get(
                            "stargazers_count",
                            0,
                        ),
                        repo.get(
                            "language",
                            "Unknown",
                        ),
                        repo.get(
                            "html_url",
                            "#",
                        ),
                    ]
                )


            csv_data = csv_buffer.getvalue().encode(
                "utf-8"
            )


            # JSON report

            json_data = json.dumps(
                repositories,
                indent=4,
            ).encode(
                "utf-8"
            )


            # -------------------------------------------------
            # Repository results
            # -------------------------------------------------

            st.markdown(
                "### Repository Results"
            )


            for index, repo in enumerate(
                repositories
            ):

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


                with st.container(
                    border=True,
                    key=f"repo_card_{index}",
                ):

                    st.markdown(
                        f"### {name}"
                    )

                    st.write(
                        description
                    )

                    st.caption(
                        f"⭐ {stars:,}   |   "
                        f"🍴 {forks:,}   |   "
                        f"💻 {repo_language}"
                    )

                    with st.container(
                        key=f"repo_link_{index}",
                    ):

                        st.link_button(
                            "View Repository ↗",
                            html_url,
                        )


            # -------------------------------------------------
            # Download section
            # -------------------------------------------------

            st.markdown(
                "### Download Reports"
            )

            st.caption(
                "Download the current search results as TXT, CSV, JSON, or one combined ZIP archive."
            )


            with st.container(
                border=True,
                key="download_panel",
            ):

                download_col1, download_col2, download_col3 = (
                    st.columns(3)
                )


                if report_format in [
                    "TXT",
                    "All Reports",
                ]:

                    with download_col1:

                        st.download_button(
                            label="📄 Download TXT",
                            data=txt_data,
                            file_name="pipeline_report.txt",
                            mime="text/plain",
                            use_container_width=True,
                        )


                if report_format in [
                    "CSV",
                    "All Reports",
                ]:

                    with download_col2:

                        st.download_button(
                            label="📊 Download CSV",
                            data=csv_data,
                            file_name="pipeline_results.csv",
                            mime="text/csv",
                            use_container_width=True,
                        )


                if report_format in [
                    "JSON",
                    "All Reports",
                ]:

                    with download_col3:

                        st.download_button(
                            label="🗂️ Download JSON",
                            data=json_data,
                            file_name="pipeline_results.json",
                            mime="application/json",
                            use_container_width=True,
                        )


                if report_format == "All Reports":

                    st.markdown(
                        "<br>",
                        unsafe_allow_html=True,
                    )


                    zip_buffer = io.BytesIO()


                    with zipfile.ZipFile(
                        zip_buffer,
                        "w",
                        zipfile.ZIP_DEFLATED,
                    ) as zip_file:

                        zip_file.writestr(
                            "pipeline_report.txt",
                            txt_data,
                        )

                        zip_file.writestr(
                            "pipeline_results.csv",
                            csv_data,
                        )

                        zip_file.writestr(
                            "pipeline_results.json",
                            json_data,
                        )


                    zip_buffer.seek(0)


                    st.download_button(
                        label="📦 Download All Reports (.zip)",
                        data=zip_buffer.getvalue(),
                        file_name="github_repository_reports.zip",
                        mime="application/zip",
                        use_container_width=True,
                    )


# ---------------------------------------------------------
# About
# ---------------------------------------------------------

st.markdown(
    "## About This Project"
)


with st.container(
    border=True,
    key="about_panel",
):

    st.markdown(
        "**GitHub Repository Automation**"
    )

    st.write(
        "A Python automation tool that searches GitHub "
        "repositories using the GitHub REST API."
    )

    st.markdown(
        "**Core capabilities:**"
    )

    st.write(
        "🔎 Repository search • "
        "💻 Programming-language filtering • "
        "⭐ Minimum-star filtering"
    )

    st.write(
        "📊 Repository sorting • "
        "📄 API pagination • "
        "📋 JSON / CSV / TXT reports"
    )

    st.write(
        "📦 Combined ZIP downloads • "
        "🧪 Pytest testing • "
        "⚙️ GitHub Actions CI"
    )


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.divider()


st.caption(
    "GitHub Repository Automation"
)

st.caption(
    "Built by Zeeshan Hassan"
)

st.caption(
    "Python • Streamlit • GitHub REST API • Pytest"
)