## https://dev.epicgames.com/documentation/en-us/fortnite/inisland-transactions-device-template-in-fortnite

# In-Island Transactions Device Template

Learn how to use the In-Island Transaction device template to get started quickly with your in-island transactions.

![In-Island Transactions Device Template](https://dev.epicgames.com/community/api/documentation/image/8a50e4b5-18d5-487a-a706-4b8693b7d667?resizing_type=fill&width=1920&height=335)

The In-Island Transactions Verse device contains a template for in-island transactions. It has all of the implementations for key aspects of the Marketplace module in the Verse API. This includes items, offers, bundle offers, and the handling of purchases by leveraging the default storefront UI. Use this code as a guide to quickly set up your storefront.

To access the device:

- Navigate to Verse Explorer.
- Right-click your project name.
- Select Add new Verse file to project.
- Select In-Island Transactions Device.

[![](https://dev.epicgames.com/community/api/documentation/image/29655ec4-8fae-4c75-9e34-cb84503fc165?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/29655ec4-8fae-4c75-9e34-cb84503fc165?resizing_type=fit)

## Creating Items

Items are defined in Verse as entitlements, and fall into one of two categories: consumable items, which are removed from the player inventory on use, and durable items, which the player can keep using without the item being removed from inventory.

### The EntitlementInfo Module

Modules are atomic units of code that can be redistributed for use in multiple files. Modules can be changed over time without breaking dependencies in a file in which the module is already used. You can separate lengthy or repetitive units of code, like entitlement definitions, into a different file, then import it with the using statement.

The `EntitlementInfo` module gathers the names, descriptions, and short descriptions of all entitlements in the template. Include this module in any file where you need to define entitlements without the need to redefine the name and other variables repeatedly for the same product, which makes alterations to the entitlement information simpler, and reduces the complexity of debugging your entitlements.

Verse

```
# Setup your entitlements and offers data, in this case that's your Names, Descriptions & Short Descriptions as well as any other data you want to be constant

EntitlementInfo<public> := module:

    Potion<public> := module:

        Name<public><localizes>:message = "Potion"

        Description<public><localizes>:message = "Adds +10 health when used. Green so you know its healthy!"
```

### Defining Entitlements

Every Verse entitlement has the following properties:

- **Name:** The entitlement name of up to 50 characters
- **Description:** The long description that displays with the entitlement, of up to 500 characters.
- **ShortDescription:** A short description that summarizes the entitlement with up to 100 characters.
- **Icon:** An image of the entitlement.

If your entitlement is a paid random item, you must include accurate numerical odds in the description of what the player might receive in. For more information, see Paid Random Items.

A Verse entitlement can also have the following optional properties:

- **MaxCount:** The maximum number of that entitlement that the player can own at any one time.
- **Consumable:** If set to **true**, the entitlement can be consumed with `ConsumeEntitlement` , which reduces the total number of the consumed entitlement the user has in Epic's systems. If set to **false**, the entitlement is a permanent item and will not be consumed on use.
- **PaidArea:** If set to **true**, the entitlement provides access to an area behind a paywall.
- **PaidRandomItem:** If set to **true**, these entitlements are purchased or redeemed with content to obtain a random reward.
- **ConsequentialToGameplay:** If set to **true**, the item provides a meaningful advantage in your island. See [Consequential to Gameplay](https://dev.epicgames.com/documentation/fortnite/creating-items-and-offers-in-fortnite#consequential-to-gameplay) for more details.

In the snippet below, you use the previously defined `EntitlementInfo` module to build the definitions for your entitlements. To define a consumable entitlement, **Consumable** must be set to **true**.

Before defining your entitlements, you need to create a base entitlement class that will be used for the entitlements in your experience 
—  in this case, `feature_example_entitlement`.

You also need to define a file path to an icon texture for each entitlement definition or your entitlement definition will fail validation.

Verse

```
Entitlements<public> := module:
    using {EntitlementInfo}

    # The base entitlement you should define for ALL your entitlements in your experience

    feature_example_entitlement<public> := class<abstract><castable>(entitlement){}

    basic_sword<public> := class<concrete>(feature_example_entitlement):

        var Name<override>:message = Sword.Name
```

By default, items are not Consumable, and have a `MaxCount` of 1. If the item is a Paid Area, a Paid Random Item, or provides a meaningful advantage that is consequential to gameplay, the relevant fields must be defined in your code.

## Entitlement Offers

An offer specifies a price in **V-Bucks** for an item or asset. Each offer has its own name, description, and icon, separate from the entitlement specifications. An offer is defined in Verse.

To sell the entitlement, you must have a corresponding offer for that entitlement.

Every offer has the following properties:

- **Name:** The offer name.
- **Description:** The long description displayed alongside the offer.
- **ShortDescription:** A short description to summarize the offer in smaller dialog boxes.
- **Icon:** An image of the offer.
- **EntitlementType:** A declaration of the entitlement included in the offer.
- **Price:** A price in V-Bucks. It must be no less than 50 V-Bucks and no greater than 5000 V-Bucks. The price must be set in multiples of 50.

This snippet demonstrates how to define entitlement offers, making use of your existing `EntitlementInfo` module for basic entitlement offer information. You also need to define an icon, the `EntitlementType` — 
which defines the entitlement the offer is for and the price in V-Bucks. You can also define an optional minimum purchase age for an offer, depending on a fixed value, a country code or restrict access to the offer by platform family or a combination of these factors. Some examples of this are demonstrated in the snippet below.

Subdivision codes are not currently supported and will be available in a future release.

Verse

```
ExampleOffers<public> := module:
    using {EntitlementInfo}

    basic_sword<public> := class(entitlement_offer):

        var Name<override>:message                = EntitlementInfo.Sword.Name

        var Description<override>:message         = EntitlementInfo.Sword.Description

        var ShortDescription<override>:message    = EntitlementInfo.Sword.ShortDescription
```

The price in V-Bucks must be a multiple of 50, and between 50 and 5000 V-Bucks.

For paid random items, you must ensure players can see accurate numerical odds of obtaining each paid random item in the offer details. Failure to do so will be considered a violation of the Fortnite Developer Rules, and subject you and your island to the appropriate sanctions.

For more information, see [In-Island Transactions Restrictions](https://dev.epicgames.com/documentation/fortnite/in-island-transactions-restrictions-in-fortnite).

## Bundle Offers

Bundles are defined in Verse and can contain a combination of different offers, stacks of the same offer, or a mix of the two. Like simple offers, bundle offers specify their own price, name, and description, and have an icon that is distinct from the entitlements and offers. You can also nest offers by including bundles within a bundle offer. An example would be a limited-time bundle that includes a shovel and a bundle of corn seed packets. This allows you to use smaller bundles as building blocks for larger, combined bundles.

The standard bundle types are:

- **Stacked bundle:** A bundle containing multiple offers of the same entitlement, usually for a discounted price.
- **Multi-offer bundle:** A bundle that combines offers for multiple entitlements, this can also include a mix of stacked offers and regular offers.

A bundle contains a tuple array of offers, which contains the defined offer and an int indicating the number of offers.

The depth of nested offers cannot exceed 5 or the attempted transaction will fail. Try to limit nesting of offers where possible.

The snippet below demonstrates the construction of a potion pack bundle. The offer information is defined within the `EntitlementInfo` module, and includes the `PotionCount` variable.

Verse

```
ExampleOffers<public> := module:

    using {EntitlementInfo}

<# --- other offer definitions above --- #>

    potion_pack<public> := class(bundle_offer) :

        var Name<override>:message                = EntitlementInfo.PotionPack.Name
```

## Purchase Restrictions

You can [restrict entitlement purchases](https://dev.epicgames.com/documentation/fortnite/in-island-transactions-restrictions-in-fortnite) to enable the creation of limited holiday items, promotional or seasonal offers, and create region-specific content.

### GetMinPurchaseAge

Use `GetMinPurchaseAge` to define a custom purchase restriction for a specific `entitlement_offer`. It is called automatically as part of purchase validation, and so only requires definition. You can define a specific integer value, a country code, or a platform family.

Subdivision codes are not currently supported and will be available in a future release.

Below are some examples of the `GetMinPurchaseAge` function.

Verse

```
# Optional overrideable function you can use to inform Epic systems what the minimum age a player needs to be to purchase this offer

        GetMinPurchaseAge<override>(CountryCode:string, SubdivisionCode:string, PlatformFamily:string)<decides><computes>:int =

            # A Hypothetical example where you only want to sell swords to people who don't live in Antarctica

            CountryCode <> CountryCodes.Antarctica

            return 0
```

## Player Entitlement Validation

Player entitlement validation is a necessary step to ensure entitlements purchased by players persist between sessions. Failure to properly validate entitlements can result in issues such as entitlement duplication or entitlement loss, for example.

### Validating previous purchases

The snippet below demonstrates a simple entitlement validation performed when a player joins a session. First, it checks to see if the incoming player is subscribed to the `OnPurchasesChanged` event. Next, if not already subscribed, the incoming player will be subscribed. Finally, a record is retrieved of all purchased entitlements for that player using `ValidatePreviousPurchases`.

It is good practice to also run validation checks of player entitlements at this stage, to ensure that any saved data in the experience matches what the Marketplace API says they own matches the player inventory.

Verse

```
OnPlayerJoin(InPlayer:player):void =

        Subscription := GetEntitlementsChangedEvent(InPlayer, Entitlements.feature_example_entitlement).Subscribe(OnPurchasesChanged)

        if (set EntitlementChangeSubscription[InPlayer] = option{Subscription}):

            Print("Adding entitlement Change Subscription player subscription")

        # On players joining you are likely going to want to run some validation checks to make sure that any data you save
```

## Handling Purchases

The two main functions used for handling purchases of entitlements are `BuyOffer` and `OnPurchasesChanged`. The first function handles the logic to present the player with an offer and validate the purchase. The second function handles the logic for a successful transaction or refund. The snippets below demonstrate these two functions.

Verse

```
# Base Implementation of how to present players with an offer to purchase in your experience

    TryBuyOffer(Player:player, Offer:entitlement_offer)<suspends>:void =

        Result := BuyOffer(Player, Offer)

        if (Result?):

            # do nothing it should respond in the purchase subscription, see OnPurchasesChanged for details
```

## Handling Consumables

To consume a consumable entitlement, you must use the ConsumeEntitlement function from the Marketplace Verse API. Once consumption is successful, you must handle the logic for the effect generated after consumption. The `Count` of the entitlement that the player owns will be decremented by the `Count` consumed in the function.

The snippet below demonstrates how a specific entitlement is consumed by a specified player.

Verse

```
# Base Implementation of how to flag a consumable in your experience as being consumed

    TryConsumeEntitlement(Player:player, Entitlement:concrete_subtype(entitlement), NumberConsuming:int)<suspends>:void =

        Result := ConsumeEntitlement(Player, Entitlement, ?Count := NumberConsuming)

        if (Result?):

            Print("Successfully consumed entitlement!")
```

You cannot consume a durable entitlement. If you attempt to do so, ConsumeEntitlement will fail.

## Granting Entitlements

Unlike purchasing an entitlement which requires V-Bucks, you can also grant entitlements to players with the `GrantEntitlement` method.

Potential use cases for granting an entitlement include promotional items, free samples of consumables, and restoring lost items due to bugs or glitches.

This snippet demonstrates a method for granting entitlements to your players.

Verse

```
# Base Implementation of how to give players a entitlement in your experience without them purchasing it

    TryGrantEntitlement(Player:player, Entitlement:concrete_subtype(entitlement), NumberToGrant:int)<suspends>:void =

        Result := GrantEntitlement(Player, Entitlement, ?Count := NumberToGrant)

        if (Result?):

            Print("Successfully granted a player your entitlement!")
```

Attempting to grant more than the Max Count of an entitlement or more than 1 of a durable entitlement will cause the entitlement grant to fail.

## Show Your Entitlement Offers to Players

The [Marketplace module](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/marketplace) provides a built-in storefront UI for use on your islands with the `ShowOffersDialog` function. The snippet below demonstrates a method to display a storefront that shows offers to a specific player.

Verse

```
# Base Implementation of how to show an array of offers to the player that are available for purchase

    ShowArrayOfOffers(Player:player)<suspends>:void =

        ShowOffersDialog(Player, array{ExampleOffers.basic_sword{}, ExampleOffers.potion{}, ExampleOffers.potion_pack{}, ExampleOffers.potion_thanksgiving{}, ExampleOffers.potion_gib{}})
```

# Base Implementation of how to show an array of offers to the player that are available for purchase
    ShowArrayOfOffers(Player:player)<suspends>:void =
        ShowOffersDialog(Player, array{ExampleOffers.basic_sword{}, ExampleOffers.potion{}, ExampleOffers.potion_pack{}, ExampleOffers.potion_thanksgiving{}, ExampleOffers.potion_gib{}})

## Complete Code

Verse

```
using { /Fortnite.com/Devices }

using { /Fortnite.com/Marketplace }

using { /UnrealEngine.com/Temporary/Diagnostics }

using { /Verse.org/Assets }

using { /Verse.org/Simulation }
```

---
