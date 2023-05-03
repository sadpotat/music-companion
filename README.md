# music-companion

This project is a webapp where the user can search songs to view their lyrics. The app is planned to support search by query and audio recognition.

</br>
<img src="https://github.com/sadpotat/music-companion/blob/main/for_readme/screenshot.JPG?raw=true" width="90%">
</br>

You will need a [Genius API](https://docs.genius.com/#/getting-started-h1) access key to run this project. The webapp uses Genius's [Search API](https://docs.genius.com/#search-h2) to fetch song information, as well as the URL to the song's lyrics. The lyrics are then scraped from this URL. If you don't have an access key, you can use `json_data.json`. It contains sample data of the song that's shown in the screenshot attached above.

### Features I haven't implemented yet :
Audio recognition has not been added yet. I'm thinking of using either [AudD API](https://audd.io/) or [ShazamKit](https://developer.apple.com/shazamkit/).

I'll also probably add a section for displaying song info, like artist information, release date and highest ranking on the Billboard 200.
