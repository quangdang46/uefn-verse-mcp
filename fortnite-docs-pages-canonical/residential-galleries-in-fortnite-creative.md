## https://dev.epicgames.com/documentation/en-us/fortnite/residential-galleries-in-fortnite-creative

# Guidelines for In-Island Monetization
Find out more about what to do and what to avoid when monetizing your island experiences.
![Guidelines for In-Island Monetization](https://dev.epicgames.com/community/api/documentation/image/cd0f43e6-e1cd-4d17-aab8-3656d5c3082c?resizing_type=fill&width=1920&height=335)
This page contains sections that relate to policies in the [Fortnite Developer Rules](https://legal.epicgames.com/fortnite/developer-rules). Make sure you take time to review the rules and guidelines before you submit your island. If a violation of these rules is found during moderation, your island will be rejected.
##  What Is and Is Not Allowed
Players expect certain categories of items to work across all of Fortnite, and the following guidelines maintain this expectation.
###  Outfits
####  ❌ Do not offer character outfits.
Do not offer outfits or items that individually or in combination alter a character’s overall appearance along the lines of outfits, either in exchange for V-Bucks or entitlements purchased with V-Bucks.
###  Emotes
####  ❌ Do not offer emotes.
Do not offer animations or dances for the character that are initiated by the player, either in exchange for V-Bucks or entitlements purchased with V-Bucks.
###  Vehicles
####  ❌ Do not offer cars, trucks or buses.
Do not offer cars, trucks, or buses, either in exchange for V-Bucks or entitlements purchased with V-Bucks.
##  Other Items
####  ✅ You are allowed to offer items in categories similar to those sold in the Fortnite Item Shop – aside from Outfits, Emotes, Cars, Trucks and Buses as noted above – as long as they affect gameplay and are not purely cosmetic.
This applies when offered in exchange for V-Bucks and when offered in exchange for entitlements purchased with V-Bucks.
Here are some examples that are OK:
  * Tires that allow players to drive off-road
  * A jetpack that allows players to fly
  * Spring boots that allow players to land a jump without fall damage

####  ✅ You are allowed to offer cosmetic items in categories that are not sold in the Fortnite Item Shop.
You can have items of entirely new types that aren't in the Fortnite Item Shop, such as:
  * Hats or scarves
  * Decor for a house
  * Airplanes
  * A "Supporter badge" that a player can display in the island

####  ❌ Do not offer in-island transactions that grant nothing in return.
Here is an example of what is not allowed:
  * Requesting a V-Bucks tip with nothing granted to the player in return.

####  ❌ Do not offer any in-island transactions that directly or indirectly influence prize wheels.
The examples below are NOT allowed:
  * A luck boost that can improve the outcomes on a prize wheel
  * In-game content that can be used to purchase a spin on a prize wheel
  * Any spin on a prize wheel, such as a single spin, extra spin, or bundle of spins.

###  Correctly Set Up Entitlements
####  ✅ Do correctly label entitlements that give players a meaningful advantage in your island.
If the item you are selling gives players a meaningful advantage in your island, you must set the `ConsequentialToGameplay` field to `true`. Check out the [Consequential to Gameplay](https://dev.epicgames.com/documentation/fortnite/creating-items-and-offers-in-fortnite#consequential-to-gameplay) section for more information.
Here are some examples that should be labeled as `ConsequentialToGameplay`:
  * A fertilizer that boosts flower growth 2x
  * Access to an area behind a paywall containing weapons that do extra damage

####  ✅ Do correctly label entitlements that can be used or consumed.
If the entitlement can be used or consumed by a player, you must set the `Consumable` field to `true`. Check out the [Creating a Consumable Entitlement](https://dev.epicgames.com/documentation/fortnite/creating-items-and-offers-in-fortnite#creating-a-consumable-entitlement-in-verse) section for more information.
Here are some examples:
  * A potion to give the player extra health
  * A seed the player can plant to grow a corn plant
  * A ticket to experience an event

If you have consumable items, you must call `ConsumeEntitlement` to cause them to be consumed. This ensures Epic's systems have proper records of them in case a player seeks support.
####  ✅ Do correctly label entitlements that grant access to areas behind a paywall.
For entitlements that grant access to areas or gameplay, you must set the `PaidArea` field to `true`.
Examples of paid areas include:
  * Rusty Key that unlocks the heavy machine shed permanently
  * Maintenance Override Card that unlocks the underground service tunnels for a single use
  * Master Harbor Seal that gives unrestricted access to the dockyard’s precious cargo bay

####  ✅ Do correctly label entitlements that grant random items.
If you offer paid random items, you must use the appropriate APIs to ensure that they are only offered to eligible players. Check out the [Paid Random Items](https://dev.epicgames.com/documentation/fortnite/creating-items-and-offers-in-fortnite#paid-random-items-nbsp) section for more information.
See below for some examples:
  * If you offer a “mystery item box” for purchase with V-Bucks, you must set the `PaidRandomItem` function in the entitlement to `true` and disclose the accurate numerical odds of obtaining each possible item.
  * If you offer a “luck boost” for purchase with V-Bucks that provides the player with a greater probability of receiving a random item in gameplay, you must set the `PaidRandomItem` function in the entitlement to `true` and disclose the accurate numerical odds of obtaining each possible item.
  * If you offer “tokens” for purchase with V-Bucks that can only be redeemed for a random item, you must use the `RestrictPaidRandomItems` function to prevent players without access from acquiring the random reward.
  * If you offer “tokens” for purchase with V-Bucks that can be redeemed for various items including a random item, you must use the `RestrictPaidRandomItems` function to prevent players without access from acquiring the random reward.

####  ✅ Do clearly disclose if offers have time-limited perks.
You can offer players time-limited benefits, so long as you are clear in the offer about how long the benefits last.
For example:
  * A 30-day Turbo Bonus (+25% speed boost that lasts 30 days)
  * A 10-day Machine Overclock License (boosts machine productivity by +100% for 10 days)

###  Terms and Naming
####  ❌ Do not use Fortnite Item Shop terms.
Players should never be confused about whether they are purchasing cosmetic items that can be used across all of Fortnite or only within your island. All entitlements that you offer are for use in your island only.
Here is a list of terms that should never appear in your in-island transactions:
  * Aura
  * Backbling
  * Contrail
  * Drift Trail
  * Emoticon
  * Glider
  * Harvesting Tool
  * Pickaxe
  * Jam Track
  * Kicks
  * Sidekick
  * Spray
  * Wrap
  * Outfit
  * Emote

####  ❌ Do not use the terms “XP”, “Experience” or “Battle Pass”.
You can never say or imply that a purchase made on your island can give players additional Fortnite XP that contributes to a player’s pass or quest progression across all of Fortnite.
This applies when offered in exchange for V-Bucks and when offered in exchange for entitlements purchased with V-Bucks.
The examples below are not OK:
  * “Buy 5000 XP for 50 V-Bucks.”
  * “Buy the [Island Name] Battle Pass.”
  * “Buy this Farm Pass to progress your Battle Pass faster!”

####  ✅Use terms specific to your Island’s progression.
You can offer custom passes and progression systems, but you must make clear the progression only pertains to the island in which it is offered.
Here are some examples of clear progression terms:
  * “Buy the [Island Name] Farm Pass to gain X Seed Points!”
  * “Increase your Farm Prestige by two levels!”
  * Name your farming island’s custom progression “Harvest Skill”.
