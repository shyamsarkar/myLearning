const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const cors = require('cors');

const app = express();
const port = 9500;
const ip = '0.0.0.0';

app.use(cors());

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        const uploadDir = './uploads';
        if (!fs.existsSync(uploadDir)) {
            fs.mkdirSync(uploadDir);
        }
        cb(null, uploadDir);
    },
    filename: function (req, file, cb) {
        cb(null, file.originalname); // Keep the original filename
    }
});

const upload = multer({
    storage: storage,
    limits: { fileSize: 1024 * 1024 * 1024 * 5 } // 5GB limit per file
}).single('movie');  // Handle one file at a time

app.post('/upload', (req, res) => {
    console.log("-----------uploading File------------");
    upload(req, res, (err) => {
        if (err) {
            return res.status(500).send('File upload failed: ' + err.message);
        }
        console.log(`File uploaded: ${req.file.originalname}`);
        res.status(200).send('File uploaded successfully');
    });
});

app.listen(port, ip, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
