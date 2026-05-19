## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ui/slider_regular

# slider_regular class
Learn technical details about the slider_regular class.
Slider with a text value. Displays a slider, its progress bar and value.
|
---|---
Verse `using` statement | `using { /Fortnite.com/UI }`
## Inheritance Hierarchy
This class is derived from `widget`.
Name | Description
---|---
[`widget`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/unrealenginedotcom/temporary/ui/widget) |  Base class for all UI elements drawn on the `player`'s screen.
## Members
This class has both data members and functions.
### Data
Data Member Name | Type | Description
---|---|---
`DefaultMaxValue` | `float` |  The maximum value that the slider can haver. Used only during initialization of the widget and not modified by SetMaxValue.
`DefaultMinValue` | `float` |  The minimum value that the slider can haver. Used only during initialization of the widget and not modified by SetMinValue.
`DefaultStepSize` | `float` |  The amount to adjust the value by, when using a controller or keyboard. Used only during initialization of the widget and not modified by SetStepSize.
`DefaultValue` | `float` |  The value to display to the user. Used only during initialization of the widget and not modified by SetValue.
### Functions
Function Name | Description
---|---
[`GetMaxValue`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ui/slider_regular/getmaxvalue) |  Gets the maximum value of the slider.
[`GetMinValue`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ui/slider_regular/getminvalue) |  Gets the minimum value of the slider.
[`GetParentWidget`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/unrealenginedotcom/temporary/ui/widget/getparentwidget) |  Returns the `widget`'s parent `widget`. Fails if no parent exists, such as if this `widget` is not in the `player_ui` or is itself the root `widget`.
[`GetRootWidget`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/unrealenginedotcom/temporary/ui/widget/getrootwidget) |  Returns the `widget` that added this `widget` to the `player_ui`. The root `widget` will return itself. Fails if this `widget` is not in the `player_ui`.
[`GetStepSize`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ui/slider_regular/getstepsize) |  Gets the amount to adjust the value by.
[`GetValue`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ui/slider_regular/getvalue) |  Gets the value of the slider.
[`GetVisibility`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/unrealenginedotcom/temporary/ui/widget/getvisibility) |  Returns the current `widget_visibility` state.
[`IsEnabled`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/unrealenginedotcom/temporary/ui/widget/isenabled) |  `true` if this `widget` can be modified interactively by the player.
[`OnValueChanged`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ui/slider_regular/onvaluechanged) |  Subscribable event that fires when the value of the slider has changed.
[`SetEnabled`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/unrealenginedotcom/temporary/ui/widget/setenabled) |  Enables or disables whether the `player` can interact with this `widget`.
[`SetMaxValue`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ui/slider_regular/setmaxvalue) |  Sets the maximum value of the slider, will enforce that the sliders maximum value is always larger than or equal to the minimum value.
[`SetMinValue`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ui/slider_regular/setminvalue) |  Sets the minimum value of the slider, will enforce that the sliders maximum value is always larger than or equal to the minimum value.
[`SetStepSize`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ui/slider_regular/setstepsize) |  Sets the amount to adjust the value by, when using a controller or keyboard.
[`SetValue`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/ui/slider_regular/setvalue) |  Sets the value of the slider, will clamp the value to be within the sliders minimum and maximum value.
[`SetVisibility`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/unrealenginedotcom/temporary/ui/widget/setvisibility) |  Shows or hides the `widget` without removing itself from the containing `player_ui`. See `widget_visibility` for details.
