## https://dev.epicgames.com/documentation/en-us/fortnite/campaign-payments-in-fortnite

# Campaign Payments

Learn how payments are collected and how to deal with payment issues that might come up.

![Campaign Payments](https://dev.epicgames.com/community/api/documentation/image/b8a942a6-a268-428f-b3c5-02cb54c7478e?resizing_type=fill&width=1920&height=335)

The cost of a [Sponsored](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#sponsored-row) [Campaign](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#campaign) is determined by the number of **delivered impressions** at the [CPM](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#cpm) ([cost per mille](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#cost-per-mille)) that a campaign clears in an [auction](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#auction). This amount never exceeds your Max Daily Budget, or the maximum daily spend of $25,000.

Your payment method is charged the moment your campaign clears a **spending threshold** and at the end of each campaign day.

**Spending thresholds** are set billing milestones that trigger a charge as your campaign spend accumulates. Spending thresholds trigger at the following amounts:

- $50
- $250
- $1,000

If your account’s **lifetime Sponsored Row spend** is over $1,000, your payment method is only charged at the end of each campaign day. **Lifetime Sponsored Row spend** refers to the amount you’ve spent across all campaigns to date.

Below are breakdowns of how payments are made, priced, reported, and more.

See the **[Campaign FAQs](https://dev.epicgames.com/documentation/fortnite/campaign-faqs-in-fortnite)** page for more information on campaign payments.

## Campaign Payments

Credit cards and PayPal are supported payment methods. Receipts are emailed automatically at the time of billing for each payment per island. You are only billed for the impressions you actually received. If the campaign underdelivers, you pay less.

For additional information about making campaign payments see the **[Epic Games Store](https://store.epicgames.com/)** and the [**Epic Games Store End User License Agreemen**t](https://store.epicgames.com/eula/?lang=en-US).

Unless you have a [payment issue](https://dev.epicgames.com/documentation/fortnite/campaign-payments-in-fortnite#payment-issues), you will not make direct payments for your campaign. Your approved payment method will be billed automatically.

[![An example of Sponsored Row receipt.](https://dev.epicgames.com/community/api/documentation/image/9c24392b-c548-4ee7-a95f-4c7e83555c8e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9c24392b-c548-4ee7-a95f-4c7e83555c8e?resizing_type=fit)

Click image to enlarge.

Save your invoice emails for your records. They include campaign details and payment confirmation.

- Payments are charged in your **local currency** through Epic’s payment system.
- You only need to enter your payment method once during the campaign creation process.

If a payment fails, you have 7 days to update your payment method before the campaign is considered **Overdue**.

[![An example of an email for payment problems.](https://dev.epicgames.com/community/api/documentation/image/cb7d6191-c0ae-4f2c-a6f0-43b2d6a87401?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cb7d6191-c0ae-4f2c-a6f0-43b2d6a87401?resizing_type=fit)

Click image to enlarge.

**Overdue payments** result in:

- All active campaigns are canceled.
- Your Engagement Payout Award (EP) earnings for your island are used to pay the overdue balance.
- You are restricted from creating any new campaigns.

See **[Overdue Payments](https://dev.epicgames.com/documentation/fortnite/campaign-payments-in-fortnite#overdue-payment)** for more information.

To avoid payment issues:

- Use a primary card with a limit that can accommodate any charges you incur.
- Tell your bank you expect charges from Epic to avoid fraud blocks.
- Keep your email updated to receive the payment notices.
- After a campaign completes, check your Creator Portal for any **alert** banners.

## Campaign and Payment Status

Campaigns and their payments move through different statuses during the campaign lifecycle. Each stage is related to the delivery of a campaign and any issues that might arise.

### Campaign Status

- **In Review**: Indicates that a campaign is still in the **Campaign Moderation** process. This process ensures the island adheres to the terms and policies.
- **Scheduled**: Campaign has been approved and is waiting to start.

- **Planned**: Indicates that the campaign is set up and ready to launch, but has not yet been scheduled.
- **Canceled:** Indicates the campaign has been canceled before the anticipated end date, either automatically or manually by the developer.

- **Live**: Indicates that an island campaign is currently active and is eligible to receive impressions if the bid wins the auction. During this phase, the campaign spends its daily budget.
- **Active (not delivering)**: The campaign is active but is not currently delivering impressions. For example, if a published release is not eligible for campaign delivery due to Ad Policy review, if a Creator unpauses the campaign, or if there is a payment issue that is unresolved. Campaigns in this state will resume delivering once finalized.
- **Paused**: Indicates that the campaign has been temporarily stopped but can be resumed within seven days from the time of pause before the campaign is automatically changed to Canceled. When a campaign has been resumed, it will start on the next day universal coordinated time (UTC).

- **Completed**: Indicates that the campaign has reached its end date.

  Once a campaign is completed, it cannot be resumed but can be reviewed for performance [metrics and insights](https://dev.epicgames.com/documentation/fortnite/monetization-and-analytics-in-fortnite-creative).

### Payment Status

- **Removed**: Your campaign has been stopped from delivering impressions due to consistently low performance. This means that players are not clicking or engaging with your island enough to meet the minimum standards for Sponsored Row.

  - You can improve your island, then re-publish it to try again with a new campaign.
  - You cannot create new campaigns for this island version. All existing active campaigns will be canceled.

- **Payment Issue**: This status indicates that the Campaign has been temporarily stopped due to a payment issue on another campaign for the account. If the campaign is paid within seven days from the time of pause, the campaign will resume to Live.

  - The campaign status will change to Paused for six days. On the seventh day, it will change to Canceled
  - During this time, developers cannot edit or create new campaigns.
- **Overdue**: This status indicates that the Campaign has been auto-canceled due to an overdue payment. The developer will need to pay for all [completed-unpaid or canceled-overdue campaigns](https://legal.epicgames.com/en-US/fortnite/developer-rules).

See **[Campaign FAQs](https://dev.epicgames.com/documentation/fortnite/campaign-faqs-in-fortnite)** for a list of frequently asked questions about Sponsored Row campaigns.

## Payment Issues

Should a payment fail, or if you encounter other payment issues, you have seven days to update your payment method and pay the campaign. During this time, **all active campaigns are paused** to avoid additional charges and you **won’t be able to create new campaigns** until the outstanding balance is paid.

Payment issues are communicated clearly in the following ways:

- **Banners** at the top of your Sponsorships dashboard when action is required. For example: **Update card / Pay now.**

  [![An example of a payment issue banner on the Campaigns dashboard.](https://dev.epicgames.com/community/api/documentation/image/794c4dfa-1735-4a3b-ba06-d05345641e7c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/794c4dfa-1735-4a3b-ba06-d05345641e7c?resizing_type=fit)

  Click to enlarge image.
- **Headers** on the campaign row to clearly outline what needs to be done per campaign.

  [![An example of a payment issue header on a campaign in the Campaigns list.](https://dev.epicgames.com/community/api/documentation/image/d28452c0-0a78-442b-a3d2-92a899cf869a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d28452c0-0a78-442b-a3d2-92a899cf869a?resizing_type=fit)

  Click to enlarge image.
- **An Email** letting you know if there was an issue with your payment.

When there is a payment issue, Epic attempts to collect payment for several days.

All dates and times shown in the Creator Portal use Common Universal Time (UTC).

Fix a payment issue by updating your payment method:

- Open the **Creator Portal** and select **Sponsorships**.
- Select the affected campaign, **update your card**, then click **pay now**.

Once a payment is made, **restrictions are lifted** and your campaigns continue to run.

## Overdue Payment

An [overdue](https://dev.epicgames.com/documentation/fortnite/campaign-payments-in-fortnite#payment-status) payment refers to a balance that isn’t paid within the grace period shown in the [Sponsored Content Terms](https://dev.epicgames.com/documentation/fortnite/sponsored-campaigns-overview-in-fortnite):

[![An example of an email referring to an overdue payment.](https://dev.epicgames.com/community/api/documentation/image/a9b16820-f319-4621-a843-1a9021144eae?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a9b16820-f319-4621-a843-1a9021144eae?resizing_type=fit)

Click image to enlarge.

- **Access stays restricted**, active campaigns are canceled, and you can’t create new ones.
- Sponsored Content won’t appear in the Sponsored Row in Discover.
- Any islands tied to unpaid campaigns may have their engagement payouts (EP) withheld to be used toward the payment if you do not pay in time.
- You always have access to your payment method from within Creator Portal, unless you pay for your campaigns using Engagement Payout Award withdrawals.
- New campaigns cannot be created.
- Island ownership cannot be transferred.
