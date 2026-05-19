## https://dev.epicgames.com/documentation/en-us/fortnite/cinematic-sequenceples-in-fortnite

# Reports
Download reports for multiple islands to analyze and compare island data.
![Reports](https://dev.epicgames.com/community/api/documentation/image/6a617423-43ee-4b8d-8c75-cad74b130d85?resizing_type=fill&width=1920&height=335)
Export and analyze island insights at scale. Use the **Reports** tab to download analytics data across all your islands at once in CSV format.
The **Reports** tab provides a centralized way to export analytics data for any islands where you are an **Owner** or **Administrator**. Instead of opening each island’s analytics individually, you can download data from multiple islands in one place.
Reports are exported as a **ZIP file** with folders for each island you select. Inside each folder is a CSV for each metric you selected under **Data Source**. You can use these CSVs for deeper analysis, external reporting, or visualization in the tools of your choice.
The Reports feature is currently in BETA and more functionality will be added over time.
You must have the [Owner or Admin role](https://dev.epicgames.com/documentation/fortnite/creating-teams-in-creator-portal-in-unreal-editor-for-fortnite) to use this feature.
##  Bulk Download
Select **Reports** from the [project navigation menu](https://dev.epicgames.com/documentation/fortnite/project-navigation-menu-in-fortnite).
[![An example of opening the Reports screen from the project navigation menu.](https://dev.epicgames.com/community/api/documentation/image/ad3e420c-335e-4ca3-8dfc-3741a2ff35ba?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ad3e420c-335e-4ca3-8dfc-3741a2ff35ba?resizing_type=fit) Reports
Once you’ve opened the **Reports** page you can select data points across multiple islands and download bulk reports for those islands. The bulk download tool allows you to export island analytics data by selecting:
  * A time range
  * One or more islands
  * One or more data sources (metrics)

All selections must be completed before you can generate your reports.
To begin a bulk download, follow these steps:
  1. Click the **time field** to open the **Time range** dropdown menu.
[![An example of the time range dropdown menu.](https://dev.epicgames.com/community/api/documentation/image/873a24d5-b143-4aec-bf0e-fcbd3b28a7ca?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/873a24d5-b143-4aec-bf0e-fcbd3b28a7ca?resizing_type=fit) Time range
  2. Select a range of time from the dropdown menu or select **Custom** to choose a custom date range from the calendar.
[![An example of selecting a custom time range.](https://dev.epicgames.com/community/api/documentation/image/5bdb5084-3668-4e98-9651-697017f12751?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5bdb5084-3668-4e98-9651-697017f12751?resizing_type=fit) Custom range
  3. Click **Apply**.
  4. Click **Select Island** to open the **Island** dropdown menu and select the islands you want data from.
[![An example of selecting islands from the island dropdown menu.](https://dev.epicgames.com/community/api/documentation/image/cf07fcac-b82d-4ac5-9e9b-4a90c12668b3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cf07fcac-b82d-4ac5-9e9b-4a90c12668b3?resizing_type=fit) Select islands
You have additional options:
     * **All** - Selects all islands in the list.
     * **Last Published** - Only selects data from the last published islands.
     * **My Islands** - Only selects islands created by you.
  5. Click **Apply**.
  6. Select the data points you want to appear on the reports from the **Data Source** list.
[![An example of selecting data points from the Data source section.](https://dev.epicgames.com/community/api/documentation/image/478a1c08-a4e5-4651-aa56-b2c33e7d369d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/478a1c08-a4e5-4651-aa56-b2c33e7d369d?resizing_type=fit) Data source
  7. Click **Generate** to begin downloading the report.

While the report is generating, a progress bar appears at the bottom of the Reports page.
[![An example of the Reports download progress bar.](https://dev.epicgames.com/community/api/documentation/image/9130b731-5cf0-4e08-b0b7-63e4f79e7a29?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9130b731-5cf0-4e08-b0b7-63e4f79e7a29?resizing_type=fit) Reports download progress bar
Once you see the success notification you can safely leave the Reports page.
[![An example of the success message that displays when a report has successfully downloaded.](https://dev.epicgames.com/community/api/documentation/image/2558afdd-5c48-481e-956a-e933fa9c7532?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2558afdd-5c48-481e-956a-e933fa9c7532?resizing_type=fit) Success message
###  Data Categories
Data sources correspond to the same analytics categories found in the Analytics page for the individual projects. Each category can be expanded to choose specific metrics, or you can select everything at once.
Available categories:
  * **Audience** - Impressions, clicks, plays, CTR, and related metrics
  * **Gameplay** - Session information, gameplay interactions, XP devices, and more.
  * **Engagement** - Minutes played, active players, returning players, and more.
  * **Satisfaction** - Player ratings and satisfaction signals
  * **Retention** - Return behavior across days

###  Download and File Format
The time required to prepare your download depends on:
  * Number of islands selected
  * Number of metrics selected
  * Length of the time range

Large exports (many islands + long time ranges + all metrics) may take several minutes. A warning message will appear if your export is expected to take longer than usual.
You must stay on the Reports page until generation completes.
Reports are downloaded and exported as a ZIP file containing one or more CSV files. Each CSV corresponds to a unique combination of metric and island.
You can open CSVs with most spreadsheet and analysis tools, including Excel, Google Sheets, and data tools such as Tableau, Looker, or Python notebooks.
##  Report Issues
There are a few reasons a report cannot generate or does not fully gather all data:
  * [Missing information](https://dev.epicgames.com/documentation/fortnite/reports-in-fortnite#missing-information)
  * [Download error](https://dev.epicgames.com/documentation/fortnite/reports-in-fortnite#download-error)
  * [An issue with the data](https://dev.epicgames.com/documentation/fortnite/reports-in-fortnite#data-issues)

###  Missing Information
If you forget to fill in one or more of the report fields, the field appears red and a prompt appears on the form. The **Generate** button will not be selectable at this time.
[![An example of the missing fields turning red.](https://dev.epicgames.com/community/api/documentation/image/722d006f-d777-42c6-a92f-b7fdc5e44c86?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/722d006f-d777-42c6-a92f-b7fdc5e44c86?resizing_type=fit) Missing information
###  Download Error
If an issue occurs while the download is in process, the report won’t generate. The progress bar goes into a failed state and stops downloading the report. A **download failed** message appears in the top-right corner of the screen.
[![An example of the download progress bar in a failed state.](https://dev.epicgames.com/community/api/documentation/image/e1b0a51a-0af6-4173-a7fe-b9bb0315d90e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e1b0a51a-0af6-4173-a7fe-b9bb0315d90e?resizing_type=fit) Fail download
[![An example of the download failed messaging.](https://dev.epicgames.com/community/api/documentation/image/454e43e5-bfc1-4e23-b059-ca807779f15d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/454e43e5-bfc1-4e23-b059-ca807779f15d?resizing_type=fit) Download fail message
###  Data Issues
If there’s an issue with any of the data selected, the report will continue generating.
[![An example of a download experiencing data issues.](https://dev.epicgames.com/community/api/documentation/image/7805346e-1950-4eaa-8580-59c5c015988b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7805346e-1950-4eaa-8580-59c5c015988b?resizing_type=fit) Data issues
However, once the report is generated a warning message appears to inform you that not all information could be pulled into the report.
[![An example of the data issue messaging.](https://dev.epicgames.com/community/api/documentation/image/c0ec72f4-adb2-44dd-8a7b-3b8a83feda58?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c0ec72f4-adb2-44dd-8a7b-3b8a83feda58?resizing_type=fit) Data issue message
##  Cancel Report
At any time while the report is generating you can cancel the bulk download. To cancel the report, follow these steps.
  1. Click **Cancel** on the progress bar. A confirmation pop-up message appears.
[![Click the Cancel button to cancel the report download.](https://dev.epicgames.com/community/api/documentation/image/4d1b3e2e-2789-4751-accf-7443fcadd49a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d1b3e2e-2789-4751-accf-7443fcadd49a?resizing_type=fit) Cancel report
  2. Click**Cancel report** on the pop-up. The report is canceled.
[![An example of the cancel confirmation pop-up message.](https://dev.epicgames.com/community/api/documentation/image/c09afe80-6117-418a-8842-f7b0cae028be?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c09afe80-6117-418a-8842-f7b0cae028be?resizing_type=fit) Cancel download confirmation

##  Best Practices
  * **Start with a narrow time range**. To speed the report generation, try 7 or 30 days before exporting larger files.
  * **Focus on key islands**. To speed up report generation and keep analysis efficient, select only the specific islands that you want to analyze.
  * **Export only the metrics you need**. Selecting fewer metrics reduces processing time.
  * **Group similar islands**. If you’re a developer with a large portfolio, grouping islands by theme or season makes report analytics more insightful and reduces download times.
