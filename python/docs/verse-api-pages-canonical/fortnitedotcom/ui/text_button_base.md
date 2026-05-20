## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ui/text_button_base

# text_button_base class

Learn technical details about the text_button_base class.

Button with text message common base class. Displays a button with a custom message string.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Fortnite.com/UI }` |

## Inheritance Hierarchy

This class is derived from `widget`.

| Name | Description |
| --- | --- |
| [`widget`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/widget) | Base class for all UI elements drawn on the `player`'s screen. |

## Members

This class has both data members and functions.

### Data

| Data Member Name | Type | Description |
| --- | --- | --- |
| `DefaultText` | `message` | The text to display to the user. Used only during initialization of the widget and not modified by SetText. |
| `TriggeringInputAction` | `??input_action(t)` | The UI input action that will trigger the Click event of this button. |

### Functions

| Function Name | Description |
| --- | --- |
| [`GetParentWidget`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/widget/getparentwidget) | Returns the `widget`'s parent `widget`. Fails if no parent exists, such as if this `widget` is not in the `player_ui` or is itself the root `widget`. |
| [`GetRootWidget`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/widget/getrootwidget) | Returns the `widget` that added this `widget` to the `player_ui`. The root `widget` will return itself. Fails if this `widget` is not in the `player_ui`. |
| [`GetText`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ui/text_button_base/gettext) | Gets the text currently in the widget. |
| [`GetVisibility`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/widget/getvisibility) | Returns the current `widget_visibility` state. |
| [`IsEnabled`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/widget/isenabled) | `true` if this `widget` can be modified interactively by the player. |
| [`OnClick`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ui/text_button_base/onclick) | Subscribable event that fires when the button is clicked. |
| [`SetEnabled`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/widget/setenabled) | Enables or disables whether the `player` can interact with this `widget`. |
| [`SetText`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/ui/text_button_base/settext) | Sets the text displayed in the widget. |
| [`SetVisibility`](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/ui/widget/setvisibility) | Shows or hides the `widget` without removing itself from the containing `player_ui`. See `widget_visibility` for details. |
