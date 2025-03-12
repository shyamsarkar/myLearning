// npm install grunt-contrib-imagemin --save-dev

/* Use this if you need to copy images from one directory to another without modification */
//npm install grunt-contrib-copy --save-dev


module.exports = function (grunt) {
    //     grunt.initConfig({
    //         imagemin: {
    //             dynamic: {
    //                 files: [{
    //                     expand: true,
    //                     cwd: 'assets/images/',
    //                     src: ['**/*.{png,jpg,gif,svg}'],
    //                     dest: 'output/images/'
    //                 }]
    //             }
    //         }
    //     });

    //     grunt.loadNpmTasks('grunt-contrib-imagemin');

    //     grunt.registerTask('default', ['imagemin']);


    const mozjpeg = require('imagemin-mozjpeg');

    grunt.initConfig({
        imagemin: {
            static: {
                options: {
                    optimizationLevel: 3,
                    svgoPlugins: [{ removeViewBox: false }],
                    use: [mozjpeg()] // Example plugin usage
                },
                files: {
                    'output/img1.jpg': 'assets/images/image1.jpg',
                    'output/img2.jpg': 'assets/images/image2.jpg',
                }
            },
            dynamic: {
                files: [{
                    expand: true,
                    cwd: 'assets/images/',
                    src: ['assets/images/*.{png,jpg,gif}'],
                    dest: 'output/'
                }]
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-imagemin');
    grunt.registerTask('default', ['imagemin']);

};