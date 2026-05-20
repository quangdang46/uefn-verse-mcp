## https://dev.epicgames.com/documentation/en-us/fortnite/text-localization-in-unreal-editor-for-fortnite

# Text Localization

Translate the text in your project to widen the audience of your island.

![Text Localization](https://dev.epicgames.com/community/api/documentation/image/916051d3-51af-4fbe-adf2-fcdaf50737f9?resizing_type=fill&width=1920&height=335)

Automatically translate your text files in Unreal Editor for Fortnite (UEFN) into the languages Fortnite supports. Localizing your files provides a way for all the text in your project to show in a local language when a player in another region plays on your island. This process has two phases (export and translation), and is designed to be run iteratively as the localizable text in your project changes over time.

Text **localization** is intended to adapt the content to feel more natural for the target language. For instance, replacing culture specific idioms, puns, jokes, and references with a suitable equivalent for the target language. **Translation** on the other hand is a literal translation of every word.

## Export

Export is the process of collecting the localizable text from your project’s content (assets and Verse), and converting it to per-language **Portable Object** (PO) files ready to be translated.

Export is triggered via **Build** > **Export Localization**. If you haven’t yet configured the localization settings for your project (**Projec**t > **Project Settings**), then you’ll be prompted to do so before moving on.

![Default Settings](https://dev.epicgames.com/community/api/documentation/image/6ce2647f-5b46-49a3-8810-809465a87ac9?resizing_type=fit&width=1920&height=1080)

![Custom Settings](https://dev.epicgames.com/community/api/documentation/image/4c271526-70a0-4b67-8b0e-c1a0d4d43f45?resizing_type=fit&width=1920&height=1080)

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

[![The export process runs synchronously in your local editor. You’ll see a progress notification while the export is running.](https://dev.epicgames.com/community/api/documentation/image/70a3f0a9-2f06-45a7-a17f-ff445bb9b9ec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/70a3f0a9-2f06-45a7-a17f-ff445bb9b9ec?resizing_type=fit)

When the export has finished you’ll find the per-language PO files under the **Localization** folder in your project’s content. These files are part of your projects’ content, and should be managed like any other content in your project.

Submit these files to source control or turn on [Unreal Revision Control](unreal-revision-control-in-unreal-editor-for-fortnite) in your projects.

[![When the export has finished you’ll find the per-language PO files under the **Localization** folder in your project’s content.](https://dev.epicgames.com/community/api/documentation/image/efedea5f-7198-4f12-87eb-f51b08ead97c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/efedea5f-7198-4f12-87eb-f51b08ead97c?resizing_type=fit)

*Click image to enlarge.*

These PO files are included when uploading your project, and are automatically converted to their runtime format by the cooking process.

## Translation

**Translation** is the process of adding per-language replacements for the localizable text that was exported to the per-language PO files (the localization data for your project).

### Auto Localization

**Auto Localization** is the process of running machine translation over the exported localization data for your project, and can be used as an alternative or complement to manually translating the exported PO files.

Auto Localization is triggered via **Build** > **Build Auto Localization**. If you haven’t yet configured the Auto Localization settings for your project (**Project** > **Project Settings**), then you’ll be prompted to do so before moving on.

![Default Settings](https://dev.epicgames.com/community/api/documentation/image/6e6e3e12-a72f-4170-8144-9cf8ddc2b9f7?resizing_type=fit&width=1920&height=1080)

![Custom Settings](https://dev.epicgames.com/community/api/documentation/image/46f07c4a-ade2-4eb6-b385-cbf37e487e5c?resizing_type=fit&width=1920&height=1080)

The settings relevant for Auto Localization are:

- **Languages to Translate**

  - This is the list of languages that Auto Localization will run machine translation for.
  - This may be a subset of the languages that your project is exporting localization data for, and may be changed at any time.
- **Translation Mode**

  - This controls whether Auto Localization is allowed to replace existing translation data with machine translations.
  - The default setting is that only untranslated text will be machine translated.

The translation process runs asynchronously via an online service, and you are not required to keep your project or UEFN open while it is running. You will see a notification while the translation process is running.

[![You will see a notification while the translation process is running.](https://dev.epicgames.com/community/api/documentation/image/e4521e00-bfc4-45af-92e9-d58fa0c58800?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e4521e00-bfc4-45af-92e9-d58fa0c58800?resizing_type=fit)

When the translation process has finished you will be prompted to import the result. This will update your PO files on disk with the new translation data.

[![When the translation process has finished you will be prompted to import the result.](https://dev.epicgames.com/community/api/documentation/image/9c666793-e453-4370-abb7-428773a4dfee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9c666793-e453-4370-abb7-428773a4dfee?resizing_type=fit)

### Manual Localization

You can directly edit the PO files exported for your project. This can be done to the files stored on your drive, or through the Content Browser in UEFN. The manual method allows you to provide custom translations or edit the translations provided by auto localization.

PO is a common format and can be edited locally by making changes in the file itself, or by using a translation tool like [Poedit](https://poedit.net/). For collaborative translations, you can try [Smartling](https://www.smartling.com/) or [Crowdin](https://crowdin.com/). If using Crowdin, verify your **PO Format** export setting.

## Automatic Export and Translation

When you create a **[Private Version](https://dev.epicgames.com/documentation/fortnite/visibility-screen-in-fortnite#private-version-code)** of your island, the text in your island project automatically goes through a localization process. You create a Private Version whether by selecting **Project** > **Upload to Private Version** in UEFN, or when publishing through the Creator Portal by selecting a **Project** > **Publish Project**.

The automatic export and translate option is enabled by default in UEFN. You can opt-out of the automatic translation process in one of two ways:

If you haven’t started to export the first version of your island, the first Private Version you generate requires you to specify the **Native Language** for the localization of your project. This option only appears when the Native Language hasn’t already been set, and mirrors the Native Language setting found in the **Project Setting**s.

[![Select the language for the Native Language option in the Project Settings.](https://dev.epicgames.com/community/api/documentation/image/8e6f9158-808d-4353-abd3-01e107da3007?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8e6f9158-808d-4353-abd3-01e107da3007?resizing_type=fit)

Click image to enlarge.

### Asset Localization

Asset localization allows you to completely replace one asset with another on a per-language basis. For example, you might want to replace a texture because it contains text that needs to be translated in the texture itself, or an asset may contain content and references that refer to local events that wouldn't make sense for another culture or region.

Localized assets exist in per-language folders under the "L10N" folder within your project’s content folder. So if you have an asset named /MyProject/MyFolder/MyAsset and you want to localize that asset for French ("fr"), then the localized asset would be /MyProject/L10N/fr/MyFolder/MyAsset.

The Content Browser has options to help you manage localized assets. These can be found under the **Asset Localization** sub-menu. Localized assets are hidden by default in the Content Browser. Click **Settings** > **Show Localized Content** to view them.
