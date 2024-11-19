# Majoras Music-Box House 

This repository contains custom music files for the Majora's Mask Randomizer, as well as the tools necessary to create a Majora's Mask audiobin file so Majora's Mask Randomizer custom music files can be used with the Ocarina of Time Randomizer.

## Table of Contents
1. [Majora's Mask Audiobin](#--majoras-mask-audiobin-)
2. [Requests](#--requests-)
3. [Issues With Music Files](#--issues-with-music-files-)
4. [Submissions](#--submissions-)
   - [Submission Steps](#submission-steps)
   - [Creating a Fork](#creating-a-fork)
   - [Creating a New Branch](#creating-a-new-branch)
   - [Uploading Your Music Files](#uploading-your-music-files)
   - [Creating a Pull Request](#creating-a-pull-request)
5. [DMCA Critical Sequences](#--dmca-critical-sequences-)
6. [Credits](#--credits-)

<h2>
  Majora's Mask Audiobin <a href="#table-of-contents" title="Return to Table of Contents">🔝</a>
</h2>

To learn how to create a Majora's Mask audiobin file so that music files can be used with Ocarina of Time Randomize version 8.3 and above, please read the guide in the "Majora's Mask Audiobin" folder of this repository.

<h2>
  Requests <a href="#table-of-contents" title="Return to Table of Contents">🔝</a>
</h2>

If there is a song you would like to be converted to a Majora's Mask binary sequence file (`.seq`), then packed into a Majora's Mask custom music file (`.mmrs`), and added to the repository, feel free to request it by opening an issue with "`[Request]`" in the title.

<h2>
  Issues with Music Files <a href="#table-of-contents" title="Return to Table of Contents">🔝</a>
</h2>

Should you find — while playing yourself or watching a stream — that a music file has volume issues or other in-game issues, please feel free to either open an issue, or contact us in [Discord](https://discord.gg/EVpd499gkS) in the `#songs-with-issues` channel.

<h2>
  Submissions <a href="#table-of-contents" title="Return to Table of Contents">🔝</a>
</h2>

If you wish to submit your custom music to this repository, the process to submit is detailed below. While you may host music on your own, having a single resource where users can contribute and download music is better for the community.

> [!NOTE]
> As long as the custom music works — and does not have any objectively bad audio issues — it will be merged into the main branch.

If you believe a sequence can be better adapted, you can either contact the original author and collaborate on improving it to replace the current one, or submit it as a second custom music file with an identifier in the filename to distinguish it from other files.

You can also submit a true remix or original creation if you do not wish to recreate a piece of music entirely.

### Submission Steps

> [!IMPORTANT]
> This process requires a GitHub account, so please [create one](https://github.com/signup?user_email=&source=form-home-signup) if you have not already and wish to submit your custom music.

#### Creating a Fork
To create a fork of this repository to submit music, please follow the steps below:

<details>
  <summary><em>Click to View Steps</em></summary>
  <blockquote>
    <ol>
      <li>
        In the top right corner of this repository's page, click "Fork".
        <br>
        <img src="https://i.ibb.co/xMqdS5M/fork.png" width=50%>
      </li>
      <hr>
      <li>
        Under "Owner", select the dropdown menu and select and owner for the forked repository.
        <br>
        <img src="https://i.ibb.co/xX4pzJW/owner.png" width=50%>
      </li>
      <hr>
      <li>
        By default, the repositories name will be the same as the original repository. Optionally, you may change this by typing a new name in the "Repository name" field in order to distinguish your forked repository from the original repository.
        <br>
        <img src="https://i.ibb.co/hVgphYq/reponame.png" width=50%>
      </li>
      <hr>
      <li>
        Select "Copy the DEFAULT branch only". This will create a fork with only the "main" repository branch. If you do not select the "Copy the DEFAULT branch only" option, then all branches from the main repository will be copied into your forked repository.
        <br>
        <img src="https://i.ibb.co/TTKDkYs/copymain.png" width=50%>
      </li>
      <hr>
      <li>
        Click "Create fork".
      </li>
    </ol>
  </blockquote>
</details>

#### Creating a New Branch

> [!IMPORTANT]
> You can only create branches in a repository in which you have push access.

> [!TIP]
> While creating a new branch is not required, it is best practice to create and make changes on branches separated from the main branch just in case — in the event something does happen where you have made changes to the main branch but need the branch synced with the original repository, then you will need to create a new branch with the original repositories main branch as the source.

To create a new branch in your forked repository, please follow the steps below:

<details>
  <summary><em>Click to View Steps</em></summary>
  <blockquote>
    <ol>
      <li>
        On GitHub, navigate to the main page of your forked repository.
      </li>
      <hr>
      <li>
        From the file tree view on the left, select the branch dropdown menu.
        <br>
        <img src="https://i.ibb.co/p4SB3m9/branch.png" width=50%>
      </li>
      <hr>
      <li>
        click "View all branches".
        <br>
        <img src="https://i.ibb.co/njkKfb5/viewall.png" width=50%>
      </li>
      <hr>
      <li>
        On the branches page, click "New branch".
      </li>
      <hr>
      <li>
        Under "Branch name", type a name for your new branch — you can name this branch anything, there are no special requirements for the branch name.
        <br>
        <img src="https://i.ibb.co/NTJ1L03/branchname.png" width=50%>
      </li>
      <hr>
      <li>
        Under "Branch source", choose the source your branch will copy its data from.
        <ul>
          <li>
            If your repository is a fork, select the repository dropdown menu and click your fork or the original repository.
          </li>
          <li>
            Click the branch dropdown menu and select a branch to copy data from.
          </li>
        </ul>
        <br>
        <img src="https://i.ibb.co/bb2VGYK/sourcebranch.png" width=50%>
      </li>
      <hr>
      <li>
        Click "Create branch".
      </li>
    </ol>
  </blockquote>
</details>

#### Uploading Your Music Files

> [!IMPORTANT]
> To help keep things organized, you should upload your files into the proper game folder your custom music originates from. If a folder for the game doesn't already exist, you will need to create one before or after uploading your files.

To upload files to your newly created fork — and branch if you've created a new branch — please follow the steps below:

<details>
  <summary><em>Click to View Steps</em></summary>
  <blockquote>
    <ol>
      <li>
        On GitHub, navigate to the main page of your forked repository. If you have created a new branch to upload files to, then you will need to change the branch before uploading.
      </li>
      <hr>
      <li>
        In the top right of your forked repository's page, click "Add file".
        <br>
        <img src="https://i.ibb.co/rFsk3t8/addfile.png" width=50%>
      </li>
      <hr>
      <li>
        In the file dropdown menu, click "Upload files".
        <br>
        <img src="https://i.ibb.co/8MJ7Jzf/uploadfiles.png" width=50%>
      </li>
      <hr>
      <li>
        This will bring you to the upload page where you can upload files. Choose the files you wish to upload to your forked repository.
      </li>
      <hr>
      <li>
        Once you are done uploading your files, ensure "Commit directly to the BRANCHNAME branch" is the selected option, then click "Commit changes".
      </li>
    </ol>
  </blockquote>
</details>

#### Creating a Pull Request
The final step in submissions is creating a pull request to the original repository. Creating a pull request will allow the changes you have made to your forked respository to be merged with the original repository.

To create a pull request to the original repository, please follow the steps below:

<details>
  <summary><em>Click to View Steps</em></summary>
  <blockquote>
    <ol>
      <li>
        On GitHub, navigate to the main page of your forked repository. If you have created a new branch and uploaded your files there, then you will need to change the branch before continuing.
      </li>
      <hr>
      <li>
        Click "Contribute", then click "Open pull request".
        <br>
        <img src="https://i.ibb.co/87MxbWB/contribute.png" width=50%>
      </li>
      <hr>
      <li>
        This will bring you to the pull request page where you will add the details of your pull request. Create a title for you pull request in the "Add a title" field.
      </li>
      <hr>
      <li>
        After adding a title, you may submit your pull request by clicking "Create pull request". Optionally, you may add details on what your changes are in the "Add a description" field of the pull request page.
      </li>
    </ol>
  </blockquote>
</details>

<h2>
  DMCA-Critical Sequences <a href="#table-of-contents" title="Return to Table of Contents">🔝</a>
</h2>

> [!CAUTION]
> Some music files may trigger a DMCA takedown request. Music files that trigger a DMCA takedown request cannot be used in any race hosted by ZeldaSpeedRuns on Twitch or YouTube — these files should be reported by submitting an issue with "`[DMCA Issue]`" in the title. Music files that trigger DMCA takedown requests will not be hosted on this repository in any capacity.

> [!IMPORTANT]
> Copyright is a hard legal subject, but it is important to remember that "Content ID claims" and "copyright claims" are *not* the same as a copyright strike and/or DMCA takedown request. The latter is far more severe in urgency and action taken than the former is — the former may be abused by randoms, so please be careful and *do not* falsely report songs that are not triggering severe copyright issues.

<h2>
  Credits <a href="#table-of-contents" title="Return to Table of Contents">🔝</a>
</h2>

- [Spreadsheet](https://docs.google.com/spreadsheets/d/1Yvgjex502cB_dVvvZm0a88aGL4WNFOm-5XvEbZLkWqI/edit)
- Ainurmusician64
- Amalgorithmic
- Crimsonae
- Darkychao
- DetectiveSky612
- Fish
- Isghj
- Philos_kun
- Professor Stupid
- TheRealPixelShake
- WEEMS
- Yaruzu
- Zeraphyr
- ZoeyZolotova
