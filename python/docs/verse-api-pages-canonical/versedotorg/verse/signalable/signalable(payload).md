## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/signalable/signalable(payload)

# signalable(payload) interface
Learn technical details about the signalable(payload) interface.
A parametric interface implemented by events with a `payload` that can be signaled. Can be used with `awaitable`, `subscribable`, or both (see: `listenable`).
|
---|---
Verse `using` statement | `using { /Verse.org/Verse }`
## Members
This interface has functions, but no data members.
### Functions
Function Name | Description
---|---
[`Signal`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/signalable/signalable\(payload\)/signal) |  Concurrently resumes the tasks waiting for this event in `awaitable.Await` and synchronously invokes any callbacks added to this event by `subscribable.Subscribe`.
