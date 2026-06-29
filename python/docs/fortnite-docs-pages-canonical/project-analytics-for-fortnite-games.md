## https://dev.epicgames.com/documentation/en-us/fortnite/project-analytics-for-fortnite-games

# Project Analytics

Use these metrics to gain insight into how players respond to your thumbnails and descriptions, and how long they stick to your island.

![Project Analytics](https://dev.epicgames.com/community/api/documentation/image/6e982e3a-6078-4de0-8d69-d8057a547aa3?resizing_type=fill&width=1920&height=335)

The **Analytics** page for each project gives developers and their teams insight into the players their games attract, and the player levels of engagement. This helps you understand everything from how compelling a thumbnail is, to how players interact with your games themselves.

[![The project's Analytics page can give you various kinds of data about your published island.](https://dev.epicgames.com/community/api/documentation/image/a63419ce-a1c1-4c88-a22f-435cea752404?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a63419ce-a1c1-4c88-a22f-435cea752404?resizing_type=fit)

## Filters for Analytics Charts

The following filters are available on several charts within the analytics tab beginning with some of your audience metrics such as Impressions and Clicks. For some filters, if the filter causes the sample data to be too low, it will default to "Other Sources" or will not report data.

### Countries

The **Countries** filter allows developers to get more insight into where their players are from out of 150 countries globally. You can use this filter on the **Impressions** and **Clicks** charts on the **Audience** tab, and on the **Playtime**, **Players,**and **Links** charts on the **Engagement** tab.

### Party Size

The **Party Size** filter represents the number of players who were grouped together in a party in the Fortnite Lobby when they played on your island. For example, two players can be in a party of two in the Lobby, even if the game places them on a team of four during matchmaking.

Party size in the Creator Portal is determined by identifying the party configuration in which a player spent the most time during the selected time frame. Metrics for that player are then assigned to that predominant party size. For example, if a player spent five minutes playing solo and later spent sixty minutes playing with a friend, their activity for that period will be grouped under a party size of two.

This metric breakdown helps you understand how players prefer to experience your island, showing whether players prefer to play your island alone, with a friend, or as part of a larger social group.

There may be discrepancies between Party Size filter results and other metrics shown in various charts. We are using improved data for this filter, and will be improving existing data sources over time.

### Platforms

The **Platforms** filter shows you on what platforms players are seeing your thumbnails, and potentially clicking on those thumbnails. This filter can group data by **Next-gen Console**, **Handheld Console**, **PC**, **Console** and **Mobile**.

### Sources

Lastly, the **Sources** filter shows you where your players are seeing and clicking your thumbnail.  These sources include some initial Discover rows, and will include more detailed row data in the future.

- **Discover - General Rows**: Includes rows with New and Updated islands, Community momentum, Trending, Popular, Genre-based, and all remaining rows not listed distinctly as a source.
- **Discover - Homebar**: Islands that are trending and popular which rotates regularly.
- **Discover - Recommendations**: Islands recommended by play history and the play history of similar players in the ecosystem.
- **By Epic**: Collection of islands created by Epic Games.
- **Game Collections**: Islands featured in the subpages of Discover filtered by specific Category (such as Combat) or Game Collection (such as LEGO® or TMNT).
- **Search Results**: An Island code, name, or developer that is surfaced through search.
- **Sponsored Row**: Sponsored islands, paid for by developers.
- **Following**: Islands from islands or developers that a player is following.
- **Recents**: Islands that a player has recently played.
- **Libraries**: Islands in a players library such as a favorite or recently played island.
- **Browse Categories**: Islands found through the browse panel after browsing categories (such as Combat).
- **Profile Pages**: Islands surfaced on your dedicated profile page.
- **Other Sources**: A catch-all used when there isn't enough data to show the source while still respecting player privacy.

To submit your island for Discover, use the [Fortnite Discover Submission Form](https://creative.fortnite.com/).

## Analytics Categories

Metrics in a project's **Analytics** page are grouped thematically around the type of insight they provide, and are nested within several different tabs.

- Audience
- [Gameplay](https://dev.epicgames.com/documentation/fortnite/project-analytics-for-fortnite-games#gameplay-tab)
- Engagement
- Satisfaction
- Retention

The **Analytics** page is available to team members with an **Owner**, **Administrator** or **Publisher** role. Collaborators and Playtesters will not have access.

## Audience Tab

Use the **Audience** tab to understand how many potential players your island is attracting and converting to plays.

### Overview

The **Overview** chart shows an overview of all audience data, as well as your click-through rate (CTR).

**Click-through rate (CTR)** is the ratio of clicks over impressions, measured as a percentage for how many impressions resulted in a click. For example, if your project has 100 impressions, and 5 clicks, that is a 5% CTR.

CTR measures the effectiveness of your thumbnail and title at capturing player attention and getting players to click. For example, an increase in CTR could indicate that your thumbnail and title are generating more interest.

[![The Overview shows a snapshot of all your audience data in one chart.](https://dev.epicgames.com/community/api/documentation/image/b2996a69-f311-43c3-8c14-f83f400360c2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b2996a69-f311-43c3-8c14-f83f400360c2?resizing_type=fit)

### Impressions

This tab shows **Impressions**, or the number of times your island was displayed to players.

[![The Impressions chart shows how many times your island was displayed to players.](https://dev.epicgames.com/community/api/documentation/image/eee31ebd-6cb2-4275-a502-0b1013cfad7b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eee31ebd-6cb2-4275-a502-0b1013cfad7b?resizing_type=fit)

These impressions are from major sources in the game client such as Search, Browse, any Discover Rows your island is in, and players' individual libraries (the Fortnite.com website is currently not included in this data). To be counted, your island's thumbnail must be 100% visible on screen and viewable for 2 seconds or more.

If a player clicks your thumbnail, even if it's not fully visible or does not appear for the full two seconds, the impression will still count as an impression based on the click-through result.

Any in-game portals to your island, or players who visit your island as part of a party who have not seen the thumbnail, will not be measured.

### Clicks

Your island's **clicks** are the number of times a player clicked on your thumbnail within the Fortnite client.

[![The Clicks chart shows the number of times a player clicked on your thumbnail across the ecosystem.](https://dev.epicgames.com/community/api/documentation/image/cc4014d8-dfcd-45a3-94ab-13d1accf5c2c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cc4014d8-dfcd-45a3-94ab-13d1accf5c2c?resizing_type=fit)

Your island’s number of **plays** is how many times a player began a session on your island. This number is not unique, and you might see multiple plays resulting from a single click due to instances of players replaying your experiences or players entering as part of a party.

The impressions-to-clicks-to-plays funnel for an island involves generating awareness (impressions), capturing interest (clicks), and driving action (plays).

By optimizing each stage of the funnel through a compelling and attractive thumbnail, engaging tags and game description, and a clear onboarding, you can maximize your ability to attract and convert potential players.

## Gameplay Tab

The Gameplay tab shows how players are interacting with your island and how long they stay engaged with gameplay metrics.

### Session Length

The **Session Length** chart is a way for you to understand the amount of time players spend in your game on each visit.

[![The Session Length chart shows the average length of time players spent on your island.](https://dev.epicgames.com/community/api/documentation/image/8f21fbc8-ab67-4b65-bb51-6d34a03eef0a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8f21fbc8-ab67-4b65-bb51-6d34a03eef0a?resizing_type=fit)

A session starts when a player enters your island and ends when they exit for any reason. Time spent by players in the lobby, in a loading screen, or time spent in a failure to matchmake does not count toward the session length. Sessions that are over 99 minutes long are accessible using a dropdown in the upper right, but breakouts by bracketed minute will be available in the CSV download.

### Bounce Rate

The [Bounce Rate](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#bounce-rate) chart shows the percentage of sessions that ended within a given time threshold.

A bounce rate is calculated by dividing the number of sessions that ended before the time threshold by the total number of sessions. The chart below displays three thresholds: **2**, **5**, and **10 minutes**.

{Image placeholder}

Each threshold can surface different types of player drop-off:

- A high 2-minute bounce rate may indicate that your [thumbnail](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#thumbnail) or [promotional materials](https://dev.epicgames.com/documentation/fortnite/ab-thumbnail-testing-in-fortnite-creative) are [not representative of the in-island experience](https://dev.epicgames.com/documentation/fortnite/thumbnail-image-policies), or that players are encountering a technical issue on entry.
- A high 5-minute bounce rate may suggest that your island's initial experience is not engaging players enough to keep players playing.
- A high 10-minute bounce rate may indicate that players are interested in your island's concept but are not finding the engagement loop compelling enough to stay.

### Queue Time

The **Queue Time** chart shows the total time players spend in queue to join your island.

[![Queue Time shows the total time players waited in a queue to play your island.](https://dev.epicgames.com/community/api/documentation/image/04833191-825e-4b94-9c79-0715e07aa534?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/04833191-825e-4b94-9c79-0715e07aa534?resizing_type=fit)

This time includes both main and overtime queues. Players remain in queue until the targeted player count for the relevant phase is met. Queue times for private matches are not included. Learn more about matchmaking queue controls.

Queue time helps you understand the impact of changing your matchmaking settings. Matchmaking settings can be reset from the default 5 seconds, but if they are unchanged, this data will only show around the standard 5 second median without any percentile data. Queue time is inclusive of time spent by players in both main and overtime queues. To learn more about matchmaking settings, see [Matchmaking Queue Controls](https://dev.epicgames.com/documentation/fortnite/matchmaking-queue-controls-in-fortnite-creative).

### Game XP

The **Game XP** chart shows data on how much Battlepass XP players have earned, as granted by an Accolades device. If your island has no Accolades devices, this section will be empty with the following message: "This game has no Accolades devices implemented."

### Analytics Device

The **Analytics Device** chart shows the number of times each Analytics Device was triggered during a set time period. If your island has no Analytics devices, this section will be empty with the following message: "This game has no Analytics devices implemented."

## Engagement Tab

Use the **Engagement** tab to analyze engagement data related to island popularity, player acquisition, and ecosystem retention. Many of these metrics are used as part of calculating how this island is monetized as part of Fortnite’s engagement payout program. To learn more, see [Engagement Payout](https://dev.epicgames.com/documentation/fortnite/engagement-payout-in-fortnite-creative).

### Active Playtime

The **Active Playtime** metric is the total number of hours spent on your island.

[![Active Playtime is the total number of hours that players spent on your island.](https://dev.epicgames.com/community/api/documentation/image/769cb2fb-5726-4ab2-a539-f8996f6a3f89?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/769cb2fb-5726-4ab2-a539-f8996f6a3f89?resizing_type=fit)

### Active Players

The **Active Players** chart shows the number of unique users playing on your island within the time frame you specify.

Currently, this metric is included on a daily cadence. In the future, it will also be available in weekly and monthly cadences, allowing you to see the unique players in each. Be aware that manual calculations that add together your daily active users will result in duplicated players.

### New and Returning Fortnite Players

The **New and Returning Fortnite Players** chart shows how many new players are playing on your island, and how many returning players are playing.

[![The New and Returning Fortnite Players chart shows how many new and returning players are on your island.](https://dev.epicgames.com/community/api/documentation/image/16be074c-3bb8-412d-8374-f5e686bda9a5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16be074c-3bb8-412d-8374-f5e686bda9a5?resizing_type=fit)

**New Fortnite Players** shows players that have never played Fortnite before visiting your island. **Returning Fortnite Players** shows the number of players who returned to Fortnite (after a gap of 28 days or more) and visited your island.

### Links

The **Links** chart shows the number of Plays (unique gameplay sessions) and Active Players that played your island after reaching it through a link.

[![The Links chart shows you how many players and unique play sessions result from people clicking your shared links.](https://dev.epicgames.com/community/api/documentation/image/a5387e6b-f36f-47f1-8e55-0828f0d72f5c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a5387e6b-f36f-47f1-8e55-0828f0d72f5c?resizing_type=fit)

Both **Plays** and **Active Players** can be filtered by **Player type** (either **New** or **Returning Players**), **Country**, and **Platform**. You can view up to 10 links in the chart at a time. The links you create in Creator Portal will be listed here, and other deep links (such as your island’s URL on [Fortnite.com](http://fortnite.com)) will be labeled **Uncategorized**.

Players acquired through links are eligible to contribute to your [Engagement Payout](https://dev.epicgames.com/documentation/fortnite/engagement-payout-in-fortnite-creative) through User Acquisition Rewards.

## Satisfaction Tab

View any feedback your island may have received from post-game surveys.

[![](https://dev.epicgames.com/community/api/documentation/image/6cfa97ea-a7f8-4a57-a2be-b00dd84df295?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6cfa97ea-a7f8-4a57-a2be-b00dd84df295?resizing_type=fit)

Sometimes, after playing an island, players may be prompted to complete a brief survey about their experience. Currently, surveys appear at random – about 1 per every 500 plays.

The frequency the surveys appear will continue to be evaluated to ensure the best frequency for future surveys.

The tab aggregates survey responses so you can track player sentiment over time. Players may be asked one of the three questions:

- Did you have fun in the last game?
- On a scale of 1-10, how would you rate the last game?
- Overall, was your last game ‘Way Too Easy’, ‘Just Right’, or ‘Way Too Difficult’?

Each of the questions that you have responses for will be shown in both a summary and a trend over time. The summary of responses will also include comparison data to all other islands so you can understand where your responses stack up against the rest of the ecosystem.

[![](https://dev.epicgames.com/community/api/documentation/image/70a2ceb3-660c-4e7a-b72f-83c5933a4bb9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/70a2ceb3-660c-4e7a-b72f-83c5933a4bb9?resizing_type=fit)

Each question of the survey has a corresponding survey.

## Retention Tab

### Classic Retention

**Classic retention** tracks how many players return to your island on a given day after their first visit.

Sustained player engagement is a key pillar of successful game design and with Classic Retention (Day N Retention) metrics, developers can now track and understand longer-term player behavior, revealing new opportunities to improve experiences and boost engagement.

[![The Classic Retention chart shows how many players return to your island on a given day after their first visit.](https://dev.epicgames.com/community/api/documentation/image/43593ee7-2dab-417e-b9b4-55141e704617?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/43593ee7-2dab-417e-b9b4-55141e704617?resizing_type=fit)

For example, Day 7 retention measures how many players came back exactly seven days after their initial play session. Retention data is not available immediately, since it depends on players returning after a specific time period. Currently, only Day 1 and Day 7 metrics are displayed, but more metrics will be coming in future releases.
