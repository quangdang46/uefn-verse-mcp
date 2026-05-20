## https://dev.epicgames.com/documentation/en-us/fortnite/unreal-revision-control-command-line-interface-in-unreal-editor-for-fortnite

# Unreal Revision Control Command Line Interface

Use text-based command lines to efficiently search for assets, projects, and revisions in Unreal Revision Control.

![Unreal Revision Control Command Line Interface](https://dev.epicgames.com/community/api/documentation/image/65795433-6e41-42d6-9f8e-f422110614e7?resizing_type=fill&width=1920&height=335)

The **Unreal Revision Control (URC) Command Line Interface (CLI)** gives you a way to perform revision control actions on your project. Although these actions can often be performed with the user interface, some allow you to go beyond what the interface currently supports.

Do not use the CLI while your project is also open in the editor, as commands coming from both at once can result in confused states.

To use the CLI with URC2:

## Before You Start

To use command lines you need to know where the URC files are located in Windows Explorer and set up an environment variable to create and use command lines with URC.

[![URC files location](https://dev.epicgames.com/community/api/documentation/image/6337033c-1af6-44b3-918a-2dcfccbb2606?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6337033c-1af6-44b3-918a-2dcfccbb2606?resizing_type=fit)

Before setting the environment variable, make sure to set your folder where the **urc2.exe** exists within your path variable.

You’ve successfully edited an environment variable.

## Launching PowerShell

Open the Unreal Editor for Fortnite (UEFN) project you’re working on with Windows Explorer.

[![Opening your project in Windows Explorer](https://dev.epicgames.com/community/api/documentation/image/2ae27969-92f6-4010-9049-17a426443ff4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2ae27969-92f6-4010-9049-17a426443ff4?resizing_type=fit)

## URC CLI Reference

### URC2

Command Line

```
Usage: urc2 [OPTIONS] [COMMAND]

Commands:
  repository    Repository commands
  branch        Branch commands
  revision      Revision commands
  file          File commands
  logfile       Logfile commands
  status        Show current repository status
  clone         Clone a remote repository into the given path
```

### Branch

Command Line

```
Branch commands

Usage: urc2 branch [OPTIONS] <COMMAND>

Commands:
  list       List available branches
  info       Get info about the given branch
  create     Create a new branch
  switch     Switch to a different branch
  push       Push commits to remote
```

#### Create (Branch)

Command Line

```
Create a new branch

Usage: urc2 branch create [OPTIONS] <branch>

Arguments:
  <branch>  Name of the branch

Options:
      --repository <path>
          Use given path as repository path
```

#### Delete (Branch)

Command Line

```
Delete an existing branch

Usage: urc2 branch delete [OPTIONS] <branch>

Arguments:
  <branch>  Name of the branch to delete

Options:
      --repository <path>
          Use given path as repository path
```

#### Diff (Branch)

Command Line

```
Diff two branches using the common ancestor base revision. Will calculate the set of changes between source branch latest revision and the base revision that is not in the set of changes between the target branch latest revision and the base revision.

Usage: urc2 branch diff [OPTIONS] <target>

Arguments:
  <target>  Name of the target branch

Options:
      --source <source>
          Name of the source branch
```

#### Info (Branch)

Command Line

```
Get info about the given branch

Usage: urc2 branch info [OPTIONS] [branch]

Arguments:
  [branch]  Name of the branch

Options:
      --repository <path>
          Use given path as repository path
```

#### Latest

Command Line

```
Branch latest related commands

Usage: urc2 branch latest [OPTIONS] <COMMAND>

Commands:
  list  
  help  Print this message or the help of the given subcommand(s)

Options:
      --repository <path>
```

##### List (Branch Latest)

Command Line

```
Usage: urc2 branch latest list [OPTIONS] [LIMIT]

Arguments:
  [LIMIT]  Max number of history entries to show

Options:
      --branch <branch>
          Branch to query
      --repository <path>
          Use given path as repository path
```

#### List (Branch)

Command Line

```
List available branches

Usage: urc2 branch list [OPTIONS]

Options:
      --repository <path>
          Use given path as repository path
      --log-level <level>
          Set the logging level
  -d, --debug
```

#### Merge (Branch)

Command Line

```
Merge two branches

Usage: urc2 branch merge [OPTIONS] <branch|--id <branch-id>>
       urc2 branch merge [OPTIONS] <COMMAND>

Commands:
  unresolve  Marks the merge unresolved
  into       Merge into branch
  start      Start a merge process
  restart    Restart the merge, resetting the current merge state
```

##### Abort (Branch Merge)

Command Line

```
Abort a merge process

Usage: urc2 branch merge abort [OPTIONS]

Options:
      --repository <path>
          Use given path as repository path
      --log-level <level>
          Set the logging level
  -d, --debug
```

##### Into

Command Line

```
Merge into branch

Usage: urc2 branch merge into [OPTIONS] <branch|--id <branch-id>> <MESSAGE>

Arguments:
  <branch>   Name of the target branch to merge the current branch into
  <MESSAGE>  Commit message

Options:
      --id <branch-id>
```

##### Resolve (Branch Merge)

Command Line

```
Resolves the merge

Usage: urc2 branch merge resolve [OPTIONS] [paths]...
       urc2 branch merge resolve <COMMAND>

Commands:
  mine    Resolve using my changes
  theirs  Resolve using their changes
  help    Print this message or the help of the given subcommand(s)
```

###### Mine (Branch Merge Resolve)

Command Line

```
Resolve using my changes

Usage: urc2 branch merge resolve mine [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files to stage

Options:
      --targets <file>
          Path to a targets file
```

###### Theirs (Branch Merge Resolve)

Command Line

```
Resolve using their changes

Usage: urc2 branch merge resolve theirs [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files to stage

Options:
      --targets <file>
          Path to a targets file
```

##### Restart (Branch Merge)

Command Line

```
Restart the merge, resetting the current merge state

Usage: urc2 branch merge restart [OPTIONS] <paths|--targets <file>|--keep-conflict-files>

Arguments:
  [paths]...  Any number of paths or files to restart

Options:
      --targets <file>
          Path to a targets file
```

##### Start (Branch Merge)

Command Line

```
Start a merge process

Usage: urc2 branch merge start [OPTIONS] <branch|--id <branch-id>>

Arguments:
  [branch]  Name of the source branch to merge into the current branch

Options:
      --id <branch-id>
          ID of the source branch to merge into the current branch
```

##### Unresolve (Branch Merge)

Command Line

```
Marks the merge unresolved

Usage: urc2 branch merge unresolve [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files to unresolve

Options:
      --targets <file>
          Path to a targets file
```

#### Protect

Command Line

```
Protect a branch from direct pushes

Usage: urc2 branch protect [OPTIONS] <branch>

Arguments:
  <branch>  Name of the branch to protect

Options:
      --repository <path>
          Use given path as repository path
```

#### Push

Command Line

```
Push commits to remote

Usage: urc2 branch push [OPTIONS] [branch]

Arguments:
  [branch]  Optional name or identifier of the branch, push current branch if not specified

Options:
      --repository <path>
          Use given path as repository path
```

#### Reset (Branch)

Command Line

```
Reset local latest pointer for a branch

Usage: urc2 branch reset [OPTIONS] <revision>

Arguments:
  <revision>  Revision to reset the local latest pointer to

Options:
      --branch <branch>
          Branch to reset, or the current branch if not set
```

#### Switch

Command Line

```
Switch to a different branch

Usage: urc2 branch switch [OPTIONS] <branch> [revision]

Arguments:
  <branch>    Name of the branch
  [revision]  Revision to switch to

Options:
      --dry-run
```

#### Unprotect

Command Line

```
Remove push protection from a branch

Usage: urc2 branch unprotect [OPTIONS] <branch>

Arguments:
  <branch>  Name of the branch to unprotect

Options:
      --repository <path>
          Use given path as repository path
```

### Clone

Command Line

```
Clone a remote repository into the given path

Usage: urc2 clone [OPTIONS] <url> [path]

Arguments:
  <url>   URL of repository
  [path]  Path to clone into

Options:
      --view <view>
```

### Commit

Command Line

```
Commit the staged revision

Usage: urc2 commit [OPTIONS] <MESSAGE>

Arguments:
  <MESSAGE>  Commit message

Options:
      --stats
          Print stats
```

### Completions

Command Line

```
Generate terminal autocompletions

Usage: urc2 completions [OPTIONS] <shell> [path]

Arguments:
  <shell>  Shell to generate autocompletions for [possible values: bash, elvish, fish, powershell, zsh]
  [path]   Directory path to write the autocompletion script to

Options:
      --repository <path>
```

### Diff

Command Line

```
Show differences between two revisions of a file

Usage: urc2 diff [OPTIONS] [paths]...

Arguments:
  [paths]...  Any number of paths or files

Options:
      --source <revision_source>
          Optional signature of the source revision to diff from, by default the current revision
```

### File

Command Line

```
File commands

Usage: urc2 file [OPTIONS] <COMMAND>

Commands:
  info        Get info about the given file or directory
  metadata    Manage metadata of a given file or directory
  dependency  Manage file dependencies
  stage       Stage changes to a file or directory to be tracked in the repository
  unstage     Unstage changes to a file or directory
```

#### Dependency

Command Line

```
Manage file dependencies

Usage: urc2 file dependency [OPTIONS] <COMMAND>

Commands:
  add     Add dependency edges from a source file to one or more dependency files
  remove  Remove dependency edges from a source file to one or more dependency files
  list    List dependencies or dependents for files
  help    Print this message or the help of the given subcommand(s)
```

##### Add (File Dependency)

Command Line

```
Add dependency edges from a source file to one or more dependency files

Usage: urc2 file dependency add [OPTIONS] <SOURCE> [dependencies]...

Arguments:
  <SOURCE>           Source file that depends on the listed dependencies
  [dependencies]...  One or more dependency file paths

Options:
      --tag <tag>...
```

##### List (File Dependency)

Command Line

```
List dependencies or dependents for files

Usage: urc2 file dependency list [OPTIONS] [paths]...

Arguments:
  [paths]...  Paths to list dependencies for (all files if omitted)

Options:
      --reverse
          List dependents instead of dependencies
```

##### Remove (File Dependency)

Command Line

```
Remove dependency edges from a source file to one or more dependency files

Usage: urc2 file dependency remove [OPTIONS] <SOURCE> [dependencies]...

Arguments:
  <SOURCE>           Source file to remove dependencies from
  [dependencies]...  One or more dependency file paths to remove

Options:
      --tag <tag>...
```

#### Diff (File)

Command Line

```
Show differences between two revisions of a file

Usage: urc2 file diff [OPTIONS] [paths]...

Arguments:
  [paths]...  Any number of paths or files

Options:
      --source <revision_source>
          Optional signature of the source revision to diff from, by default the current revision
```

#### Hash

Command Line

```
Hash a local file

Usage: urc2 file hash [OPTIONS] [paths]...

Arguments:
  [paths]...  Any number of paths or files to unstage

Options:
      --targets <file>
          Path to a targets file
```

#### History (File)

Command Line

```
List revisions of a file

Usage: urc2 file history [OPTIONS] <PATH> [LENGTH]

Arguments:
  <PATH>    File path to get revisions for
  [LENGTH]  Number of revisions to show

Options:
      --revision <revision>
```

#### Info (File)

Command Line

```
Get info about the given file or directory

Usage: urc2 file info [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files

Options:
      --targets <file>
          Path to a targets file containing all the paths to all files
```

#### Metadata (File)

Command Line

```
Manage metadata of a given file or directory

Usage: urc2 file metadata [OPTIONS] <COMMAND>

Commands:
  clear  Clear metadata for a staged file
  get    Get metadata from a file
  set    Set metadata on for a staged file
  help   Print this message or the help of the given subcommand(s)
```

##### Clear (File Metadata)

Command Line

```
Clear metadata for a staged file

Usage: urc2 file metadata clear [OPTIONS] <PATH>

Arguments:
  <PATH>  File path to clear metadata for

Options:
      --repository <path>
          Use given path as repository path
```

##### Get (File Metadata)

Command Line

```
Get metadata from a file

Usage: urc2 file metadata get [OPTIONS] <PATH> [key]

Arguments:
  <PATH>  File to get metadata for
  [key]   Attribute to get metadata for

Options:
      --revision <revision>
```

##### Set (File Metadata)

Command Line

```
Set metadata on for a staged file

Usage: urc2 file metadata set [OPTIONS] <PATH> [pairs]...

Arguments:
  <PATH>      File path to set metadata on
  [pairs]...  Metadata key/value pairs

Options:
      --binary
```

#### Obliterate

Command Line

```
Obliterate a file or fragment

Usage: urc2 file obliterate [OPTIONS] <--address <ADDRESS>|--path <PATH>>

Options:
      --address <ADDRESS>
          Address of a blob
      --path <PATH>
          Path to a file
      --repository <path>
```

#### Reset (File)

Command Line

```
Reset changes to a path or file to the current revision, discarding your local changes

Usage: urc2 file reset [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files

Options:
      --purge
          Delete untracked files
```

#### Stage (File)

Command Line

```
Stage changes to a file or directory to be tracked in the repository

Usage: urc2 file stage [OPTIONS] <paths|--targets <file>>
       urc2 file stage [OPTIONS] <COMMAND>

Commands:
  move   Move or rename a file or directory
  merge  Stage as a merge
  help   Print this message or the help of the given subcommand(s)
```

##### Merge (File Stage)

Command Line

```
Stage as a merge

Usage: urc2 file stage merge [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files

Options:
      --targets <file>
          Path to a targets file containing all the paths to all files
```

##### Move (File Stage)

Command Line

```
Move or rename a file or directory

Usage: urc2 file stage move [OPTIONS] <from> <to>

Arguments:
  <from>  Original path of file
  <to>    New path of file

Options:
      --repository <path>
```

#### Unstage (File)

Command Line

```
Unstage changes to a file or directory

Usage: urc2 file unstage [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files to unstage

Options:
      --targets <file>
          Path to a targets file
```

#### Write

Command Line

```
Write data to a specific location

Usage: urc2 file write [OPTIONS] --output <OUTPUT>

Options:
      --address <ADDRESS>
          Address of a blob
      --path <PATH>
          Path to a file
      --revision <REVISION>
```

### Global-Store

Command Line

```
Manage the global store

Usage: urc2 global-store [OPTIONS] <COMMAND>

Commands:
  create  
  info    
  help    Print this message or the help of the given subcommand(s)

Options:
```

#### Create (Global-Store)

Command Line

```
Usage: urc2 global-store create [OPTIONS] <remote-url>

Arguments:
  <remote-url>  Remote URL that will back the store

Options:
      --path <path>
          Where to create the global store
      --make-default <MAKE_DEFAULT>
          Set this as the default global store in the global config file, defaults to true [possible values: true, false]
```

#### Info (Global-Store)

Command Line

```
Usage: urc2 global-store info [OPTIONS]

Options:
      --repository <path>
          Use given path as repository path
      --log-level <level>
          Set the logging level
  -d, --debug
          Enable debug output
  -f, --force
```

### History

Command Line

```
List revisions of a repository

Usage: urc2 history [OPTIONS] [LENGTH]

Arguments:
  [LENGTH]  Number of revisions to show

Options:
      --revision <revision>
          Start listing from the specified revision. If not specified, start listing from the current branch latest revision
```

### Lock

Command Line

```
Lock file

Usage: urc2 lock [OPTIONS] <COMMAND>

Commands:
  acquire  Acquire lock on file(s)
  status   Get lock status on file(s)
  query    Query the lock status given a branch, owner or path
  release  Release lock on file(s)
  help     Print this message or the help of the given subcommand(s)
```

#### Acquire

Command Line

```
Acquire lock on file(s)

Usage: urc2 lock acquire [OPTIONS] <paths|--branch <branch>>

Arguments:
  [paths]...  Any number of file paths to lock

Options:
      --branch <branch>
          Branch where lock is to be acquired
```

#### Query (Lock)

Command Line

```
Query the lock status given a branch, owner or path

Usage: urc2 lock query [OPTIONS]

Options:
      --branch <branch-name>
          Branch to query locks on
      --owner <owner-id>
          Owner to query locks belonging to them
      --path <path>
```

#### Release

Command Line

```
Release lock on file(s)

Usage: urc2 lock release [OPTIONS] [paths]...

Arguments:
  [paths]...  Any number of file paths to release the lock

Options:
      --branch <branch>
          Branch where lock was acquired
```

#### Status (Lock)

Command Line

```
Get lock status on file(s)

Usage: urc2 lock status [OPTIONS] [paths]...

Arguments:
  [paths]...  Any number of file paths to get the lock status

Options:
      --branch <branch>
          Branch where lock was acquired
```

### Logfile

Command Line

```
Logfile commands

Usage: urc2 logfile [OPTIONS] <COMMAND>

Commands:
  info  Info
  help  Print this message or the help of the given subcommand(s)

Options:
      --repository <path>
```

#### Info (Logfile)

Command Line

```
Info

Usage: urc2 logfile info [OPTIONS]

Options:
      --repository <path>
          Use given path as repository path
      --log-level <level>
          Set the logging level
  -d, --debug
```

### Notification

Command Line

```
Notifications

Usage: urc2 notification [OPTIONS] <COMMAND>

Commands:
  subscribe  Subscribe to events on the given repository
  help       Print this message or the help of the given subcommand(s)

Options:
      --repository <path>
```

#### Subscribe

Command Line

```
Subscribe to events on the given repository

Usage: urc2 notification subscribe [OPTIONS] [seconds]

Arguments:
  [seconds]  Time to be subscribed in seconds

Options:
      --repository <path>
          Use given path as repository path
```

### Push

Command Line

```
Push commits to remote

Usage: urc2 push [OPTIONS] [branch]

Arguments:
  [branch]  Optional name or identifier of the branch, push current branch if not specified

Options:
      --repository <path>
          Use given path as repository path
```

### Repository

Command Line

```
Repository commands

Usage: urc2 repository [OPTIONS] <COMMAND>

Commands:
  status  Show current repository status
  info    Get info about a repository
  list    List repositories
  create  Create a repository in the given directory
  clone   Clone a remote repository into the given path
```

#### Clone (Repository)

Command Line

```
Clone a remote repository into the given path

Usage: urc2 repository clone [OPTIONS] <url> [path]

Arguments:
  <url>   URL of repository
  [path]  Path to clone into

Options:
      --view <view>
```

#### Dump

Command Line

```
Dump repository state information

Usage: urc2 repository dump [OPTIONS]

Options:
      --path <path>
          Optional path in the repository to start dumping from
      --revision <revision>
          Optional revision to dump
      --max-depth <max-depth>
```

#### GC

Command Line

```
Run a full garbage collection pass on the local repository store

Usage: urc2 repository gc [OPTIONS]

Options:
      --repository <path>
          Use given path as repository path
      --log-level <level>
          Set the logging level
  -d, --debug
```

#### Info (Repository)

Command Line

```
Get info about a repository

Usage: urc2 repository info [OPTIONS] [url]

Arguments:
  [url]  URL of repository

Options:
      --repository <path>
          Use given path as repository path
```

#### Status (Repository)

Command Line

```
Show current repository status

Usage: urc2 repository status [OPTIONS] [PATH]...

Arguments:
  [PATH]...  Optional paths in repository

Options:
      --unstaged
          Show unstaged files
```

#### Store

Command Line

```
Access the repository data store

Usage: urc2 repository store [OPTIONS] <COMMAND>

Commands:
  immutable  Operations on the immutable store
  help       Print this message or the help of the given subcommand(s)

Options:
      --repository <path>
```

##### Immutable

Command Line

```
Operations on the immutable store

Usage: urc2 repository store immutable [OPTIONS] <COMMAND>

Commands:
  query  Query the store
  help   Print this message or the help of the given subcommand(s)

Options:
      --repository <path>
```

###### Query (Repository Store Immutable)

Command Line

```
Query the store

Usage: urc2 repository store immutable query [OPTIONS] <ADDRESS>

Arguments:
  <ADDRESS>  Fragment address to query

Options:
      --recurse
          Recurse into subfragments
```

#### Verify

Command Line

```
Verify repository state consistency

Usage: urc2 repository verify [OPTIONS] [COMMAND]

Commands:
  state     Verify repository state consistency (default)
  fragment  Verify a specific fragment in the local store
  help      Print this message or the help of the given subcommand(s)

Options:
```

##### Fragment

Command Line

```
Verify a specific fragment in the local store

Usage: urc2 repository verify fragment [OPTIONS] <HASH>

Arguments:
  <HASH>  Fragment hash to verify

Options:
      --context <CONTEXT>
          Context part of the address to verify
```

##### State

Command Line

```
Verify repository state consistency (default)

Usage: urc2 repository verify state [OPTIONS]

Options:
      --path <path>
          Optional path in the repository to start verification from
      --heal
          Attempt to heal discrepancies found in a new staged state
      --repository <path>
```

### Reset

Command Line

```
Reset changes to a file or directory

Usage: urc2 reset [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files

Options:
      --purge
          Delete untracked files
```

### Revision

Command Line

```
Revision commands

Usage: urc2 revision [OPTIONS] <COMMAND>

Commands:
  history      List revisions of a repository
  info         Get info about a revision
  commit       Commit the staged state
  amend        Amend the latest commit's message
  sync         Synchronize to a given state of a repository [aliases: synchronize]
```

#### Amend

Command Line

```
Amend the latest commit's message

Usage: urc2 revision amend [OPTIONS] <MESSAGE>

Arguments:
  <MESSAGE>  Commit message

Options:
      --stats
          Print stats
```

#### Bisect

Command Line

```
Binary search for a change introduced between start (exclusive) and end (inclusive.)

Usage: urc2 revision bisect [OPTIONS] --start <start_revision> --end <end_revision>

Options:
      --start <start_revision>
          The latest revision known to not have the change
      --end <end_revision>
          The earliest revision known to have the change
      --repository <path>
```

### Cherry-Pick

Command Line

```
Cherry-pick a revision onto the currently synced revision

Usage: urc2 revision cherry-pick [OPTIONS] <revision>
       urc2 revision cherry-pick [OPTIONS] [revision] <COMMAND>

Commands:
  unresolve  Marks the cherry-pick unresolved
  restart    Restart the cherry-pick, resetting the current cherry-pick state
  resolve    Resolve conflicts
  abort      Abort a cherry-pick
```

##### Abort (Revision Cherry-Pick)

Command Line

```
Abort a cherry-pick

Usage: urc2 revision cherry-pick abort [OPTIONS]

Options:
      --repository <path>
          Use given path as repository path
      --log-level <level>
          Set the logging level
  -d, --debug
```

##### Resolve (Revision Cherry-Pick)

Command Line

```
Resolve conflicts

Usage: urc2 revision cherry-pick resolve [OPTIONS] <paths|--targets <file>>
       urc2 revision cherry-pick resolve <COMMAND>

Commands:
  mine    Resolve using my changes
  theirs  Resolve using the incoming changes
  help    Print this message or the help of the given subcommand(s)
```

###### Mine (Revision Cherry-Pick Resolve)

C++

```
Resolve using my changes

Usage: urc2 revision cherry-pick resolve mine [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files to target

Options:
      --targets <file>
          Path to a targets file
```

###### Theirs (Revision Cherry-Pick Resolve)

C++

```
Resolve using the incoming changes

Usage: urc2 revision cherry-pick resolve theirs [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files to target

Options:
      --targets <file>
          Path to a targets file
```

##### Restart (Revision Cherry-Pick)

Command Line

```
Restart the cherry-pick, resetting the current cherry-pick state

Usage: urc2 revision cherry-pick restart [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files to target

Options:
      --keep-conflict-files
          Keep mine/theirs/base files for conflicted files merged with conflict markers
```

##### Unresolve (Revision Cherry-Pick)

Command Line

```
Marks the cherry-pick unresolved

Usage: urc2 revision cherry-pick unresolve [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files to target

Options:
      --targets <file>
          Path to a targets file
```

#### Commit (Revision)

Command Line

```
Commit the staged state

Usage: urc2 revision commit [OPTIONS] <MESSAGE>

Arguments:
  <MESSAGE>  Commit message

Options:
      --stats
          Print stats
```

#### Diff (Revision)

Command Line

```
Diff two revisions

Usage: urc2 revision diff [OPTIONS] <revision_source>

Arguments:
  <revision_source>  Source revision to compare

Options:
      --target <revision_target>
          Target revision to compare, by default the current revision
```

#### Find

Command Line

```
Find revision

Usage: urc2 revision find [OPTIONS] <COMMAND>

Commands:
  metadata  Find revision by metadata
  number    Find revision by number
  help      Print this message or the help of the given subcommand(s)

Options:
```

##### Metadata (Revision Find)

Command Line

```
Find revision by metadata

Usage: urc2 revision find metadata [OPTIONS] <key> [value]

Arguments:
  <key>    Metadata key to search for
  [value]  Metadata value to match with

Options:
      --repository <path>
```

##### Number

Command Line

```
Find revision by number

Usage: urc2 revision find number [OPTIONS] <NUMBER>

Arguments:
  <NUMBER>  Revision number to search for

Options:
      --repository <path>
          Use given path as repository path
```

#### History (Revision)

Command Line

```
List revisions of a repository

Usage: urc2 revision history [OPTIONS] [LENGTH]

Arguments:
  [LENGTH]  Number of revisions to show

Options:
      --revision <revision>
          Start listing from the specified revision. If not specified, start listing from the current branch latest revision
```

#### Info (Revision)

Command Line

```
Get info about a revision

Usage: urc2 revision info [OPTIONS] [revision]

Arguments:
  [revision]  Revision to get info for

Options:
      --delta
          Show delta information
```

#### Metadata (Revision)

Command Line

```
Manage metadata of a given revision

Usage: urc2 revision metadata [OPTIONS] <COMMAND>

Commands:
  clear  Clear metadata for a staged revision
  get    Get metadata from a revision
  set    Set metadata on for a staged revision
  help   Print this message or the help of the given subcommand(s)
```

##### Clear (Revision Metadata)

Command Line

```
Clear metadata for a staged revision

Usage: urc2 revision metadata clear [OPTIONS]

Options:
      --repository <path>
          Use given path as repository path
      --log-level <level>
          Set the logging level
  -d, --debug
```

##### Get (Revision Metadata)

Command Line

```
Get metadata from a revision

Usage: urc2 revision metadata get [OPTIONS] [key]

Arguments:
  [key]  Attribute to get metadata for

Options:
      --revision <revision>
          Revision to get metadata for
```

##### Set (Revision Metadata)

Command Line

```
Set metadata on for a staged revision

Usage: urc2 revision metadata set [OPTIONS] [pairs]...

Arguments:
  [pairs]...  Metadata key/value pairs

Options:
      --binary
          Indicator that values are paths to files
```

#### Restore

Command Line

```
Restore current revision as latest revision

Usage: urc2 revision restore [OPTIONS] [MESSAGE]

Arguments:
  [MESSAGE]  Commit message

Options:
      --repository <path>
          Use given path as repository path
```

#### Revert

Command Line

```
Revert a revision from the currently synced revision

Usage: urc2 revision revert [OPTIONS] <revision>
       urc2 revision revert [OPTIONS] [revision] <COMMAND>

Commands:
  unresolve  Marks the revert unresolved
  restart    Restart the revert, resetting the current revert state
  resolve    Resolve conflicts
  abort      Abort a revert
```

##### Abort (Revision Revert)

Command Line

```
Abort a revert

Usage: urc2 revision revert abort [OPTIONS]

Options:
      --repository <path>
          Use given path as repository path
      --log-level <level>
          Set the logging level
  -d, --debug
```

##### Resolve (Revision Revert)

Command Line

```
Resolve conflicts

Usage: urc2 revision revert resolve [OPTIONS] <paths|--targets <file>>
       urc2 revision revert resolve <COMMAND>

Commands:
  mine    Resolve using my changes
  theirs  Resolve using the incoming changes
  help    Print this message or the help of the given subcommand(s)
```

###### Mine (Resolve Revision Revert)

Command Line

```
Resolve using my changes

Usage: urc2 revision revert resolve mine [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files to target

Options:
      --targets <file>
          Path to a targets file
```

###### Theirs (Resolve Revision Revert)

Command Line

```
Resolve using the incoming changes

Usage: urc2 revision revert resolve theirs [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files to target

Options:
      --targets <file>
          Path to a targets file
```

##### Restart (Revision Revert)

Command Line

```
Restart the revert, resetting the current revert state

Usage: urc2 revision revert restart [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files to target

Options:
      --keep-conflict-files
          Keep mine/theirs/base files for conflicted files merged with conflict markers
```

##### Unresolve (Revision Revert)

Command Line

```
Marks the revert unresolved

Usage: urc2 revision revert unresolve [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files to target

Options:
      --targets <file>
          Path to a targets file
```

#### Sync (Revision)

Command Line

```
Synchronize to a given state of a repository

Usage: urc2 revision sync [OPTIONS] [revision]

Arguments:
  [revision]  Revision hash signature to synchronize to. If detach option is given this can be an arbitrary signature, otherwise it has to be a signature on the current branch. Can be a partial hash signature

Options:
      --detach
          Sync to a detached revision and clear branch
```

### Stage

Command Line

```
Stage changes to a file or directory

Usage: urc2 stage [OPTIONS] <paths|--targets <file>>
       urc2 stage [OPTIONS] <COMMAND>

Commands:
  move   Move or rename a file or directory
  merge  Stage as a merge
  help   Print this message or the help of the given subcommand(s)
```

#### Merge (Stage)

Command Line

```
Stage as a merge

Usage: urc2 stage merge [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files

Options:
      --targets <file>
          Path to a targets file containing all the paths to all files
```

#### Move (Stage)

Command Line

```
Move or rename a file or directory

Usage: urc2 stage move [OPTIONS] <from> <to>

Arguments:
  <from>  Original path of file
  <to>    New path of file

Options:
      --repository <path>
```

### Status

Command Line

```
Show current repository status

Usage: urc2 status [OPTIONS] [PATH]...

Arguments:
  [PATH]...  Optional paths in repository

Options:
      --unstaged
          Show unstaged files
```

### Sync

Command Line

```
Synchronize to a repository state

Usage: urc2 sync [OPTIONS] [revision]

Arguments:
  [revision]  Revision hash signature to synchronize to. If detach option is given this can be an arbitrary signature, otherwise it has to be a signature on the current branch. Can be a partial hash signature

Options:
      --detach
          Sync to a detached revision and clear branch
```

### Unstage

Command Line

```
Unstage changes to a file or directory

Usage: urc2 unstage [OPTIONS] <paths|--targets <file>>

Arguments:
  [paths]...  Any number of paths or files to unstage

Options:
      --targets <file>
          Path to a targets file
```
