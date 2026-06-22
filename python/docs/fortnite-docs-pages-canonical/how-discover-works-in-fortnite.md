## https://dev.epicgames.com/documentation/en-us/fortnite/how-discover-works-in-fortnite

# How Discover Works

Learn how you can improve visibility and engagement for your islands by understanding how player metrics impact Fortnite Discover.

![How Discover Works](https://dev.epicgames.com/community/api/documentation/image/6645149f-2200-424b-9a76-aa25076de20f?resizing_type=fill&width=1920&height=335)

Fortnite Discover connects players to compelling islands and gives developers an opportunity to find and grow an audience.

This documentation provides a comprehensive overview for developers looking to maximize their island's visibility and success within Discover.

This document covers:

- **[How Discover works](https://dev.epicgames.com/documentation/fortnite/how-discover-works-in-fortnite#discover-overview)**: An end-to-end view of how players find and engage your island.
- **[How we evaluate islands for Discover](https://dev.epicgames.com/documentation/fortnite/how-discover-works-in-fortnite#how-we-evaluate-islands-for-discover)**: How we test, score, and rank islands in Discover.
- **[Metrics](https://dev.epicgames.com/documentation/fortnite/how-discover-works-in-fortnite#metrics)**: The signals that contribute to your island's exposure.
- **[Thumbnail best practices](https://dev.epicgames.com/documentation/fortnite/how-discover-works-in-fortnite#thumbnail-best-practices)**: Best practices — and pitfalls to avoid — for thumbnails.
- **[Tips](https://dev.epicgames.com/documentation/fortnite/how-discover-works-in-fortnite#helpful-links)**: Tools you can use to grow engagement on your island.
- **[Where your island can appear](https://dev.epicgames.com/documentation/fortnite/how-discover-works-in-fortnite#where-your-island-can-appear)**: The rows and surfaces that make up Discover, including For You.
- **[Search](https://dev.epicgames.com/documentation/fortnite/how-discover-works-in-fortnite#search)**: How players use Search to find specific islands.

## Discover Overview

Discover surfaces personalized recommendations, genre recommendations, Epic’s editorial selections, new and updated content, recently played and a Sponsored Row.

Three things to keep in mind as you read this guide:

- **Discover is dynamic**. Rows, ordering, and the algorithms behind them are continually tested and refined.
- **Engagement drives distribution**. The way players engage with your island is the primary signal we use to decide where it appears.
- **Quality is important**. Several core signals — Average Playtime, retention, Quality play-through rate (QPTR) — are evaluated on a per-player basis, so deep engagement can even outperform a large audience.

## How We Evaluate Islands for Discover

Every newly published island goes through an evaluation process before it earns broad distribution in Discover. The evaluation process looks for islands that players genuinely enjoy, are novel, and will bring players back. Islands are continuously evaluated as new player data comes in. High performance in any one metric may not secure high placement in a particular row. Evaluation is based on multiple metrics.

### Pre-Checks Before Publishing

Pre-publish checks run during the release process. If your island's metadata is highly similar to an existing experience, you'll receive a warning in Creator Portal and have the chance to make changes before submitting for content review.

Islands, including their metadata, that are highly similar to an existing experience, whether published by you or by another developer, are shown less frequently in Discover.

The original developer of a given title or thumbnail is determined using the following criteria:

- **Thumbnails**: The developer or team that first published the thumbnail in the Fortnite ecosystem.
- **Titles**: The developer or team who published an island that either had 100 unique users in the last 96 hours, or accumulated at least 150 minutes of editing time on the project in the last 30 days.

For more information, see **[Thumbnail Image Policies](https://dev.epicgames.com/documentation/fortnite/thumbnail-image-policies)** and **[Reporting Unoriginal Promotional Assets](https://dev.epicgames.com/documentation/fortnite/reporting-unoriginal-promotional-assets-in-fortnite-creative)**.

Re-using Verse code, devices, and systems from pre-existing islands is a standard and acceptable development practice, and will not trigger copycat detection.

If you or your team are the original developers of a title or thumbnail, those assets can only be used without restriction on a maximum of one live island at a time.

### The Testing Window for New Islands

When you publish a new island, Discover tests your content for up to 2 weeks. The testing window exists to gather enough real data to evaluate a new island’s quality before it earns broader distribution in Discover. During this window:

- The island appears to players primarily through the New row, which rotates new content across players to gather engagement signals quickly.

  - New islands also become eligible for genre rows and personalized surfaces from day one, and will become more likely to appear as impressions and engagement signals accumulate.
- We include historical context in scoring so your island isn't judged on a single bad day.

### Continuous Evaluation

Islands that perform well graduate from the testing pipeline and continue to  receive distribution across genre rows and personalized surfaces. Islands that underperform receive reduced algorithmic distribution but remain fully searchable and accessible via direct island code, Library, Favorites, and Profile Pages — and continue to be re-evaluated.

Two systems do the work:

- **Automated systems** continuously score islands against engagement, retention, social, and similarity signals. These systems re-score islands as fresh player data comes in.

  - Discover algorithms re-evaluate your island continuously.
  - Player engagement signals — including playtime, bounce rate, and quality play-through rate — are weighed against the historical performance distribution of other islands.

    - Updates to your island that improve its quality may increase your exposure on Discover surfaces.
- **Human review** does a secondary check across all rows for the best practices outlined in this document.

## Metrics

Below are some of the most important metrics that contribute to an island's exposure in Discover. These metrics are continually tested and refined.

|  |  |
| --- | --- |
| **Metric** | **Description** |
| **Average Playtime** | Average minutes per session over a period of time. For this metric, we cap at 120 minutes per session to prevent outlier sessions from distorting the playtime analytics we gather. |
| **Concurrent Users (CCU)** | The number of players playing on an island at the same time. |
| **Bounce Rate** | The fraction of sessions where a player stayed for less time than a row-specific threshold (often 5 minutes).NOTE: Metrics for this will be coming to Project Analytics in June 2026. |
| **Player Retention** | The percentage of players that return to your island over a period of time. |
| **Social Play** | Multiple social metrics are continuously evaluated including how often players invite others to play this island together, players returning to this island in a party, and the % of time the island is played in a party.  Metrics for this will be coming to [Project Analytics](https://dev.epicgames.com/documentation/fortnite/project-analytics-for-fortnite-games) soon. |
| **Qualified Play-Through Rate (QPTR)** | An engagement-weighted version of play-through that accounts for playtime. Players who go deep into your island are weighted more heavily than players who barely cross the threshold. |
| **Unique Users** | The number of players who have played on the island in the last seven days. |

## Thumbnail Best Practices

Thumbnails are important to the success of your island. Remember that all thumbnails must adhere to the [Fortnite Developer Rules](https://legal.epicgames.com/fortnite/developer-rules) to avoid moderation actions.

Follow the best practices below to improve the chances of your island appearing in Discover.  These will have an even greater impact on the visibility of your island in Discover starting **June 2026**.

|  |  |  |
| --- | --- | --- |
| **Best Practice** | **Description** | **Examples** |
| Represent Your Island Accurately | Use images that accurately represent your island and its gameplay. |  |
| Make it Unique | Consider using an image as a base that you intentionally composed with text, character art, or stylization that communicates what makes your island unique. |  |
| Show How Weapons Are Used In Gameplay | If you decide to show weapons, integrate them naturally into your thumbnail by showing them in action. |  |
| Make the Background Composition Meaningful | Use backgrounds that reflect what a player will actually see inside the experience, even if simplified or stylized. |  |

### Thumbnail Practices to Avoid

Avoid the following to increase your island's chances of appearing in Discover.

|  |  |  |
| --- | --- | --- |
| **What to Avoid** | **Description** | **Examples** |
| Plain Backgrounds | Avoid floating assets or plain text over a blank background, gradient, generic, or single-color backdrop. |  |
| Raw Screenshots | Avoid unedited or minimally edited screenshots from your game. |  |
| Floating Weapons Without Gameplay Context | Avoid overlaying 3D weapons, items and pickup icons onto your thumbnail. |  |

## Where Your Island Can Appear

The rows that players see in Discover, and the order they are listed, can change based on the player's cohort (age rating, platform, region, personalization opt-in). Discover frequently experiments with new rows and orderings to understand how it impacts overall player engagement. The names on the rows may vary.

### 🧑‍🎨 Editorial Rows

These rows showcase islands created by Epic and islands selected by Epic staff.

|  |  |
| --- | --- |
| **Row** | **Description** |
| **By Epic** | This row features islands developed or published by Epic Games. The content is editorially selected and not impacted by player metrics. No third-party content is included. |
| **Epic’s Picks** | This row features high novelty, innovative islands selected by Epic's editorial team. These selections highlight standout gameplay or creative use of mechanics. Islands in this row are manually curated and subject to quality reviews before being featured. For more information, see **[Epic's Picks](https://dev.epicgames.com/documentation/fortnite/epics-picks-in-fortnite)**. |

### ⏱Lifecycle and Personalized Rows

Lifecycle and personalized rows surface islands based on where they are in their publishing journey, what the player has recently played, and what we think the player wants to see next.

|  |  |
| --- | --- |
| **Row** | **Description** |
| **Recently Played** | This row displays a player's most recently played islands. It includes all island types without ranking or filtering, unless the island has become private or delisted. The list updates dynamically based on the player's session history. Islands in Recently Played last for 90 days before no longer being considered recent. |
| **New** | This row displays newly published islands that have entered Discover. |
| **Updated** | This row displays islands that were updated in the last 7 days. |
| **For You** | The For You row is a dynamic, personalized row that surfaces islands we think a specific player is most likely to want to play next, based on what they've engaged with historically. |
| **[Sponsored](https://dev.epicgames.com/documentation/fortnite/campaigns-in-fortnite)** | This row offers developers the choice to spend money to receive increased visibility for their islands. |

### 🎮 Genre / Play Style Rows

Discover categorizes islands by genre. When you publish your island, you'll need to select one of the following genres. The genre you select determines which row your island is eligible for. Island experiences that do not match their selected genre will not appear in those genre or play style rows. An island can only be featured in one genre row at a time, and you can change the genre of your island by republishing it and selecting a new genre.

Selecting a game tag is not the same as selecting a genre — game tags are used to give players and Epic more information about your island, but they don't determine row eligibility.

| Genre | Description |
| --- | --- |
| **Adventure & RPG** | World-driven islands where players are drawn into exploration, narrative, and discovery. The gameplay centers on character development, stats, and levelling up. Players select their character's skills through the choices they make. |
| **Battle Royale** | Last player or team standing experiences where players compete across a shrinking play space. Elimination and zone pressure are the defining mechanics. For example: zone wars, and Fortnite Battle Royale. |
| **Deathrun & Platformer** | Movement- and obstacle-based islands where navigating a course from beginning to end is the entire challenge. This type of gameplay prioritizes timing, precision, and overcoming obstacles by jumping, climbing, and navigating uneven terrain or traps. |
| **Horror** | Experiences designed primarily around fear, dread, and atmosphere. These types of islands rely on jump scares and psychological elements. |
| **Music & Rhythm** | Islands centered around music creation, performance, or rhythm-based gameplay. Players react to, perform with, or interact through music in a way that drives the core game loop. This is distinct from maps that simply have a good soundtrack. |
| **Party & Mini Games** | Islands designed for casual, short-session multiplayer fun with a reset loop. A round ends, someone wins, everyone plays again. |
| **Roguelike** | Islands built around run-based gameplay where players take on a series of levels or challenges, restarting from the beginning when defeated. Escalating difficulty, permanent elimination, and progression that carries between runs define the core loop. |
| **Roleplaying & Social** | Islands built around player-driven storytelling, social interaction, and creative expression rather than structured competitive gameplay. Players inhabit a role or an identity for a character in a shared world and space. |
| **Shooter** | Combat experiences where gunplay is the primary mechanic, but the format isn't Battle Royale. The goal is to rack up eliminations, not survival, like in free-for-alls, arenas, and training maps. |
| **Simulation & Tycoon** | Islands where players build, manage, grow, or optimize systems over time. Progress comes from accumulation and decision-making across sessions. |
| **Sport & Racing** | Islands structured around real-world athletic formats or vehicle competition. The rules, win conditions, and player roles mirror recognizable sport or racing conventions. Performance and skill within a defined format determine outcomes. |
| **Strategy** | Islands where planning, positioning, and decision making determine outcomes more than reflexes. For example tower defense or base-building games. |
| **Survival** | Islands where players manage resources and threats over sustained sessions in order to stay alive. For example, zombie attack, or wave-based defense games. |

### 🧩 Collections Row

The Game Collection row features islands built using collaborations like LEGO® and Fall Guys.

## Search

**Search** is an important way for players to find specific islands and genres within Fortnite. It uses a hybrid approach combining two algorithms: keyword matching and semantic search. **Keyword matching** returns islands that contain text that exactly matches the user’s query. **Semantic search** returns islands that are “semantically similar” to a user’s query.

This hybrid approach allows players to find content using generic terminology while also supporting very specific searches. For example:

| Search Algorithm Type | Search Term | Result |
| --- | --- | --- |
| **Semantic** | space | Islands set on the moon |
| **Semantic** | scary tycoons | Horror-themed tycoon islands, Zombie tycoons |
| **Keyword** | ffa | Free-for-all islands |
| **Keyword** | Reload | Reload |

Once results are compiled from a search, they are algorithmically sorted based on features like:

- Semantic similarity to the search term used
- Keyword match (if present)
- Concurrent users (CCU) at that moment, coupled with other variables
- Confirmed recent search count

Search ranking improves as players' query and selection patterns inform the algorithm.

## Helpful Links

- [About Project Analytics](https://dev.epicgames.com/documentation/fortnite/project-analytics-for-fortnite-games)
- [How to create a Sponsored campaign](https://dev.epicgames.com/documentation/fortnite/creating-and-editing-campaigns-in-fortnite)
- [How to use A/B Thumbnail Testing](https://dev.epicgames.com/documentation/fortnite/ab-thumbnail-testing-in-fortnite-creative)
- [Fortnite Developer Marketing Playbook](https://www.fortnite.com/developer/developer-marketing-playbook)
