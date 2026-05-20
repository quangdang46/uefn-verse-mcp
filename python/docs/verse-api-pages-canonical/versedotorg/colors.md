## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/colors

# Colors module

Learn technical details about the Colors module.

Module import path: /Verse.org/Colors

- [`Verse.org`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg)
- **`Colors`**

  - [`NamedColors`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/namedcolors)

## Classes and Structs

| Name | Description |
| --- | --- |
| [`color`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/color) | Represents colors as RGB triples in the ACES 2065-1 color space. Component values are linear (i.e. `*gamma* = 1.0`). |
| [`color_alpha`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/color_alpha) | Represents colors as RGB triples in the ACES 2065-1 color space with an additional alpha channel A. This reasons about the `Color` and alpha (`A`) as separate concepts instead of as a single concept. All values are stored strictly as unopinionated floats but, when interpreted as a color with alpha, ranges for `A` are `0.0` (transparent) to `1.0` (opaque). Color values are not premultiplied. Component values are linear (i.e. `*gamma* = 1.0`). |

## Functions

| Name | Description |
| --- | --- |
| [`operator'+'`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/operatorplus) | Makes an ACES 2065-1 `color` from the component-wise sum of `c0` and `c1`. |
| [`operator'-'`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/operatorminus) | Makes an ACES 2065-1 `color` from the component-wise difference of `c0` and `c1`. |
| [`operator'*'`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/operatorstar) | Makes an ACES 2065-1 `color` from the component-wise product of `c0` and `c1`. |
| [`operator'*'`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/operatorstar-1) | Makes an ACES 2065-1 `color` from each component of `c` scaled by `factor`. |
| [`operator'*'`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/operatorstar-2) | Makes an ACES 2065-1 `color` from each component of `c` scaled by `factor`. |
| [`operator'*'`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/operatorstar-3) | Makes an ACES 2065-1 `color` from each component of `c` scaled by `factor`. |
| [`operator'*'`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/operatorstar-4) | Makes an ACES 2065-1 `color` from each component of `c` scaled by `factor`. |
| [`operator'/'`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/operatorslash) | Makes an ACES 2065-1 `color` from each component of `c` divided by `factor`. |
| [`operator'/'`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/operatorslash-1) | Makes an ACES 2065-1 `color` from each component of `c` divided by `factor`. |
| [`MakeColorFromSRGB`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/makecolorfromsrgb) | Makes an ACES 2065-1 `color` from sRGB components `Red`, `Green`, and `Blue`. Normal sRGB component values are between `0.0` and `1.0`, but this can handle larger values. |
| [`MakeSRGBFromColor`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/makesrgbfromcolor) | Makes an sRGB `tuple` by converting `InColor` from an ACES 2065-1 `color` to sRGB. |
| [`MakeColorFromSRGBValues`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/makecolorfromsrgbvalues) | Makes an ACES 2065-1 `color` from the integer sRGB components `Red`, `Green`, and `Blue`. Valid sRGB component values are between '0' and '255', inclusive. |
| [`MakeColorFromHex`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/makecolorfromhex) | Makes an ACES 2065-1 `color` from a CSS-style sRGB `hexString`. Supported formats are:   - RGB - RRGGBB - RRGGBBAA - RGB - RRGGBB - RRGGBBAA An invalid hex string will return `Black`. |
| [`MakeColorFromHSV`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/makecolorfromhsv) | Makes an ACES 2065-1 `color` from `Hue`, `Saturation`, and `Value` components. Components use the HSV color model in the sRGB color space. Expected ranges:   - `0.0 <= Hue <= 360.0` - `0.0 <= Saturation <= 1.0` - `0.0 <= Value <= 1.0`   Values out of expected ranges will undergo range reduction and conversion. |
| [`MakeHSVFromColor`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/makehsvfromcolor) | Makes an HSV `tuple` by converting `InColor` from an ACES 2065-1 `color` to sRGB and applying the HSV color model. |
| [`MakeColorFromTemperature`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/makecolorfromtemperature) | Makes an ACES 2065-1 `color` from the chromaticity of a blackbody radiator at `Temperature` Kelvin. `Temperature` is clamped such that `0 <= Temperature`. |
| [`MakeColorAlpha`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/makecoloralpha) | Makes a new `color_alpha` from individual `R`, `G`, `B`, `A` component values. |
| [`Over`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/colors/over) | Blend colors `CA1` and `CA2` with `CA1` over `CA2` using two non-premultiplied `color_alpha` values. Alpha components are clamped between `0.0` and `1.0`. Fails if the value of both clamped Alpha components are `0.0`. |
