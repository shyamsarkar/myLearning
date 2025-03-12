const fs = require('fs');
const ytdl = require('ytdl-core');

const url = 'https://www.youtube.com/watch?v=wZHtZ_VJGKI&list=PL8p2I9GklV47TMMnPzqnkCtSOS3ebr4O7&index=1&pp=iAQB';

// Function to download YouTube video
const downloadVideo = async (url) => {
    try {
        // Fetch video info
        const info = await ytdl.getInfo(url);
        const title = info.videoDetails.title;

        // Display available formats for debugging
        const formats = ytdl.filterFormats(info.formats, 'audioandvideo');
        console.log('Available formats:', formats.map(f => f.qualityLabel));

        // Choose the 'highestvideo' quality
        const format = ytdl.chooseFormat(formats, { quality: 'highestvideo' });
        
        // Set output file path
        const filePath = `${title}.mp4`;

        // Start the download
        console.log(`Downloading: ${title}`);
        ytdl(url, { format: format })
            .pipe(fs.createWriteStream(filePath))
            .on('finish', () => {
                console.log(`Download completed: ${filePath}`);
            })
            .on('error', (err) => {
                console.error('Error during download:', err);
            });
    } catch (error) {
        console.error('Error fetching video info:', error.message);
    }
};

downloadVideo(url);
