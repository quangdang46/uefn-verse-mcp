## https://dev.epicgames.com/documentation/en-us/fortnite/ab-thumbnail-testing-in-fortnite-creative

# A/B Thumbnail Testing

A/B Test your thumbnails to find an image that increases your click-through rate.

![A/B Thumbnail Testing](https://dev.epicgames.com/community/api/documentation/image/c7cd6f2c-0a7b-467a-9ff0-098d542fe6e3?resizing_type=fill&width=1920&height=335)

The publishing and development process offers developers the opportunity to run an A/B test on island thumbnails to compare two different images to see which one drives more clicks and a higher click-through rate (CTR) — all backed by real player data to help you optimize engagement, reduce guesswork, and iterate faster.

Only a team member with publishing permission has the ability to create an A/B test and select which thumbnail to use after testing is complete.

## Start A/B Testing

A/B testing is part of the publishing process but it is not mandatory. To learn more about submitting a single thumbnail, see the **Cancel Testing** section below.

Under the **Promotional Materials** tab, submit your two thumbnails. To begin A/B testing:

The additional thumbnail will not get flagged as a duplicate.

### Thumbnail Moderation

If one thumbnail image fails moderation, the whole island will fail as well, and will need to go through the publishing and review process again after you correct the failed image.

### New Release

While the island is in mid-A/B testing, you cannot create a new release, but must wait until the A/B testing is complete and you've selected an image. Once you've done this, the **Create new release** button becomes available.

[![If you try to move forward before selecting an image, you'll be prompted to go back.](https://dev.epicgames.com/community/api/documentation/image/dba469d0-bb6b-4890-9305-b07a8cdc084e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dba469d0-bb6b-4890-9305-b07a8cdc084e?resizing_type=fit)

If you try to move forward before selecting an image, you'll be prompted to go back.

### Cancel Testing

You can cancel testing at any time by selecting either image being tested.

If you’re in the middle of creating a new release and don’t want to do A/B testing, you have the option to use a single thumbnail to continue moving forward.

Continue through the publishing process with a single thumbnail.

## Thumbnail Testing Metrics

Each thumbnail collects data after the island is published. An equal distribution of each thumbnail is sent to potential players. A/B-tested thumbnails are applied to the in-game **Discover** page, **browse** and **search**. Once a player sees a particular thumbnail for an island, they will only see that thumbnail moving forward.

Testing runs for a maximum of **90 days**. Results are found on the island's **Publishing** page under the **Release module**. The following A/B testing data will be available:

- **Impressions**
- **Clicks**
- **Click-Through Rate (CTR)**

[![Analytics collected during testing include: Impressions, Clicks, and Click-Through Rate.](https://dev.epicgames.com/community/api/documentation/image/a77e5e70-e721-49e6-8096-cf627b46af35?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a77e5e70-e721-49e6-8096-cf627b46af35?resizing_type=fit)

Analytics collected during testing.

## Testing Results

You can end the test by selecting a thumbnail anytime after the test starts. After 90 days, if you don’t end the test yourself, the system will select a default thumbnail on your behalf based on best results.

To select a thumbnail:

The selected thumbnail is marked as Selected and remains highlighted in the Release tab, while the thumbnail not chosen becomes unselectable. Collapse the A/B testing view to see a dated Completed test status under the release. This marks the date the selected thumbnail will appear as the image for the island for all players

[![Collapsed view of the A/B Testing on the project.](https://dev.epicgames.com/community/api/documentation/image/32acb90d-929b-4aa7-a3ff-6fc36d180694?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/32acb90d-929b-4aa7-a3ff-6fc36d180694?resizing_type=fit)

Collapsed view of the A/B Testing on the project.

If you do not choose a thumbnail after the 90-day testing period, the system automatically chooses the thumbnail. If a significant result is reached, it will assign the image with higher CTR as the chosen thumbnail. If no significant result is reached, it will assign thumbnail A — the first thumbnail uploaded.

### Insufficient Results

It’s possible that there will be no clear winner after the testing period is over. In this case, your A/B test result is flagged **Insufficient Results**.

[![If there is no clear winner, the A/B Test is labeled Insufficient Results.](https://dev.epicgames.com/community/api/documentation/image/669cc141-3842-4155-89d2-c716d0562f13?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/669cc141-3842-4155-89d2-c716d0562f13?resizing_type=fit)

Insufficient Results

You can still select a thumbnail at this point. Doing so opens a pop-up message informing you that there was no clear winner.

To conclude A/B testing:

[![](https://dev.epicgames.com/community/api/documentation/image/db9f340b-11f4-43c3-a614-b6931dfee9e0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/db9f340b-11f4-43c3-a614-b6931dfee9e0?resizing_type=fit)

Should you decide to create a new A/B test, you must go through the publish and moderation process again.

## A/B Testing FAQs

The following is a general overview of questions about the A/B testing process.

### What is A/B thumbnail testing?

A/B thumbnail testing provides a way to compare different thumbnails to determine which one performs best in terms of **Click-through rates (CTR)**. The feature provides data-driven insights to help you optimize your island’s engagement by using the most effective thumbnail.

### Who is this feature for?

It is designed for you to refine your thumbnails to improve **click-through rates**.

#### How does the A/B test work?

When you upload **two** thumbnail variants, the system distributes each variant evenly among viewers (a 50/50 split). The best-performing thumbnail is recommended based on the click-through rate (CTR) metric.

### How can I set up an A/B thumbnail test during publishing?

During the **Upload Promotional Media** step in the publishing flow, you can add an additional thumbnail for testing.

**Important:**

- The A/B test is only successfully created after the island passes moderation.
- If either thumbnail variant fails moderation, the entire submission (including the island) will be rejected.

  - In the rejection email, a clear explanation is provided about which thumbnail variant is rejected, or if both are rejected.
  - If one image variant is reported, both images are removed.

[![](https://dev.epicgames.com/community/api/documentation/image/1953eb91-0ec3-401f-87f3-9dc1724d9a85?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1953eb91-0ec3-401f-87f3-9dc1724d9a85?resizing_type=fit)

### How many thumbnails can I test at once?

You can upload **two** thumbnail variants per test. One test per release is allowed.

### Can Irun multiple A/B tests simultaneously?

At launch, you can only run one active test per release at a time. You’re asked to end the test if you want to create a new release.

### How long does an A/B test run?

The duration of the test depends on data collection speed, usually ranging from a few days to a couple of weeks, based on audience size and engagement levels. The maximum duration for an A/B test is 90 days. If you don’t intentionally select a thumbnail, a default thumbnail is selected on your behalf after 90 days. Prior to that, you will need to end the test manually.

### What metrics determine the winning thumbnail?

The system considers click-through rate (CTR) to determine the best-performing thumbnail.

### How does the system recommend a winning thumbnail?

The system analyzes the click-through rate (CTR) and impressions metrics to determine the top-performing variant. While we don’t visually declare a winner, we visually show youthat significant confidence is reached. You can then select the thumbnail based on your own judgement.

### Can I manually select a winning thumbnail?

Yes, you can override the system’s recommendation and select a thumbnail manually.

### What is significant confidence in A/B testing?

In A/B testing, significant confidence means there is a statistical certainty (set at 90% confidence) that the difference in performance (CTR) between two thumbnails isn’t due to random chance.

- Measured with a "p-value" (for example, p < 0.1 for 90% confidence).
- Requires enough data (impressions/clicks) to rule out flukes.
- If reached, the winning thumbnail is declared reliably better.
- If not reached, the test is inconclusive (no clear winner).

Example:

If thumbnail B’s CTR is 5% higher than A, with 90% confidence, you can trust that B genuinely performs better. This prevents you from making decisions based on misleading or noisy data.

### How is a default thumbnail selected for me after 90 days?

After 90 days, if you don’t select a thumbnail yourself, the system determines which thumbnail to default to based on the rules below:

- If a significant result is reached, assign the outperforming image to be the island thumbnail.
- If no significant result is reached, assign thumbnail A (the first thumbnail uploaded) to be the island thumbnail.

### Where can I view test results?

Results are displayed inside the release module on the Creator Portal Project Release page, showing Impressions, Clicks and CTR on each variant’s performance. You are also shown whether the test has reached sufficient results — in other words , whether the result shown is statistically trustworthy.

[![](https://dev.epicgames.com/community/api/documentation/image/d7407bdb-a244-453e-8e17-53cd6d732342?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d7407bdb-a244-453e-8e17-53cd6d732342?resizing_type=fit)

### Will players notice that thumbnails are changing?

No, players will be assigned a variant the first time they view the island’s thumbnail in Fortnite. This assignment happens on their player account level. Players will only see one thumbnail version, preventing any confusion.
