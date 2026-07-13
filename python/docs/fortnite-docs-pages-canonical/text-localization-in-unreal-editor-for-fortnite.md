## https://dev.epicgames.com/documentation/en-us/fortnite/text-localization-in-unreal-editor-for-fortnite

# Text Localization

Translate the text in your project to widen the audience of your island.

![Text Localization](https://dev.epicgames.com/community/api/documentation/image/916051d3-51af-4fbe-adf2-fcdaf50737f9?resizing_type=fill&width=1920&height=335)

Automatically translate your text files in Unreal Editor for Fortnite (UEFN) into the languages Fortnite supports. Localizing your files provides a way for all the text in your project to show in a local language when a player in another region plays on your island. This process has two phases (export and translation), and is designed to be run iteratively as the localizable text in your project changes over time.

Text **localization** is intended to adapt the content to feel more natural for the target language. For instance, replacing culture specific idioms, puns, jokes, and references with a suitable equivalent for the target language. **Translation** on the other hand is a literal translation of every word.

## Export

Export is the process of collecting the localizable text from your project’s content (assets and Verse), and converting it to per-language **Portable Object** (PO) files ready to be translated.

Export is triggered via **Build** > **Export Localization**. If you haven’t yet configured the localization settings for your project (**Projec**t > **Project Settings**), then you’ll be prompted to do so before moving on.

![Default Settings](https://dev.epicgames.com/community/api/documentation/image/986e34da-c570-45f9-a0fc-f37d0a842110?resizing_type=fit&width=1920&height=1080)

![Custom Settings](https://dev.epicgames.com/community/api/documentation/image/d168d1a1-2ff9-47ab-83a5-8507c733c1dc?resizing_type=fit&width=1920&height=1080)

The settings relevant for export are:

- **Native Language**

  - This is the language that the localizable text for your project is authored in..
  - You must author all of your localizable text in the same language, and should not change this setting once you’ve started to translate your project (otherwise you’ll lose your existing translations).
- **Languages to Generate**

  - This is the list of languages that will have localization data for your project.
  - This list is limited to the languages supported by Fortnite.
- **PO Format**

  - This controls the specific format of the exported PO files.
  - You may change this after you’ve started to translate your project, if you find that you need to switch to a different format for manual translation.

The export process runs synchronously in your local editor. You’ll see a progress notification while the export is running.

[![The export process runs synchronously in your local editor. You’ll see a progress notification while the export is running.](https://dev.epicgames.com/community/api/documentation/image/eaf9a71f-a0e6-4e20-abb6-774216ce004d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eaf9a71f-a0e6-4e20-abb6-774216ce004d?resizing_type=fit)

When the export has finished you’ll find the per-language PO files under the **Localization** folder in your project’s content. These files are part of your projects’ content, and should be managed like any other content in your project.

Submit these files to source control or turn on [Lore Version Control](https://dev.epicgames.com/documentation/fortnite/lore-version-control-viewport-status-highlighting-in-unreal-editor-for-fortnite) in your projects.

[![When the export has finished you’ll find the per-language PO files under the **Localization** folder in your project’s content.](https://dev.epicgames.com/community/api/documentation/image/106982ec-566d-4ce2-bed6-72a9a88312a6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/106982ec-566d-4ce2-bed6-72a9a88312a6?resizing_type=fit)

These PO files are included when uploading your project, and are automatically converted to their runtime format by the cooking process.

## Translation

**Translation** is the process of adding per-language replacements for the localizable text that was exported to the per-language PO files (the localization data for your project).

### Auto Localization

**Auto Localization** is the process of running machine translation over the exported localization data for your project, and can be used as an alternative or complement to manually translating the exported PO files.

Auto Localization is triggered via **Build** > **Build Auto Localization**. If you haven’t yet configured the Auto Localization settings for your project (**Project** > **Project Settings**), then you’ll be prompted to do so before moving on.

![Default Settings](https://dev.epicgames.com/community/api/documentation/image/8ad7314e-bbd7-453a-813e-ae34af2d5bb8?resizing_type=fit&width=1920&height=1080)

![Custom Settings](https://dev.epicgames.com/community/api/documentation/image/5a4d952b-7818-4e8c-9c99-b4ae78dabf9e?resizing_type=fit&width=1920&height=1080)

The settings relevant for Auto Localization are:

- **Languages to Translate**

  - This is the list of languages that Auto Localization will run machine translation for.
  - This may be a subset of the languages that your project is exporting localization data for, and may be changed at any time.
- **Translation Mode**

  - This controls whether Auto Localization is allowed to replace existing translation data with machine translations.
  - The default setting is that only untranslated text will be machine translated.

The translation process runs asynchronously via an online service, and you are not required to keep your project or UEFN open while it is running. You will see a notification while the translation process is running.

[![You will see a notification while the translation process is running.](https://dev.epicgames.com/community/api/documentation/image/0dd7b4f4-61cb-423a-b1b9-5a9b4c83190b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0dd7b4f4-61cb-423a-b1b9-5a9b4c83190b?resizing_type=fit)

When the translation process has finished you will be prompted to import the result. This will update your PO files on disk with the new translation data.

[![When the translation process has finished you will be prompted to import the result.](https://dev.epicgames.com/community/api/documentation/image/f712a936-9386-411e-9d0e-b854f426c6a2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f712a936-9386-411e-9d0e-b854f426c6a2?resizing_type=fit)

### Manual Localization

You can directly edit the PO files exported for your project. This can be done to the files stored on your drive, or through the Content Browser in UEFN. The manual method allows you to provide custom translations or edit the translations provided by auto localization.

PO is a common format and can be edited locally by making changes in the file itself, or by using a translation tool like [Poedit](https://poedit.net/). For collaborative translations, you can try [Smartling](https://www.smartling.com/) or [Crowdin](https://crowdin.com/). If using Crowdin, verify your **PO Format** export setting.

## Automatic Export and Translation

When you create a **[Private Version](https://dev.epicgames.com/documentation/fortnite/visibility-screen-in-fortnite#private-version-code)** of your island, the text in your island project automatically goes through a localization process. You create a Private Version whether by selecting **Project** > **Upload to Private Version** in UEFN, or when publishing through the Creator Portal by selecting a **Project** > **Publish Project**.

The automatic export and translate option is enabled by default in UEFN. You can opt-out of the automatic translation process in one of two ways:

If you haven’t started to export the first version of your island, the first Private Version you generate requires you to specify the **Native Language** for the localization of your project. This option only appears when the Native Language hasn’t already been set, and mirrors the Native Language setting found in the **Project Setting**s.

[![Select the language for the Native Language option in the Project Settings.](https://dev.epicgames.com/community/api/documentation/image/46e54f13-8fd8-409e-a333-ed019d0802fd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/46e54f13-8fd8-409e-a333-ed019d0802fd?resizing_type=fit)

Click image to enlarge.

### Asset Localization

Asset localization allows you to completely replace one asset with another on a per-language basis. For example, you might want to replace a texture because it contains text that needs to be translated in the texture itself, or an asset may contain content and references that refer to local events that wouldn't make sense for another culture or region.

Localized assets exist in per-language folders under the "L10N" folder within your project’s content folder. So if you have an asset named /MyProject/MyFolder/MyAsset and you want to localize that asset for French ("fr"), then the localized asset would be /MyProject/L10N/fr/MyFolder/MyAsset.

The Content Browser has options to help you manage localized assets. These can be found under the **Asset Localization** sub-menu. Localized assets are hidden by default in the Content Browser. Click **Settings** > **Show Localized Content** to view them.
